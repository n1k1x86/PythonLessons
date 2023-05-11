import asyncio

import aiohttp
import requests
import re
from bs4 import BeautifulSoup
from collections import OrderedDict
import itertools
import json


def get_target_urls():
    url = 'https://markets.businessinsider.com/index/components/s&p_500'
    main_url = 'https://markets.businessinsider.com'
    urls = []

    for page_num in range(1, 11):
        resp = requests.get(url + f'?p={page_num}')
        soup = BeautifulSoup(resp.text, 'lxml')

        data = soup.tbody.find_all('tr')

        for i in data:
            up_down_year_raw = i.find('td').find_next_siblings('td')[-1]
            urls.append((main_url + i.td.a.get('href'), re.findall(r'[-+]?[0-9]+\.?[0-9]+', str(up_down_year_raw))))

    return urls


class WebScraper(object):
    def __init__(self, urls):
        self.urls = urls
        self.all_data = []
        self.main_data = {}
        self.usd_course = self.get_usd_course()
        asyncio.run(self.main())

    async def fetch(self, session, url):
        try:
            async with session.get(url[0]) as response:
                text = await response.text()
                up_year = url[1][0]
                down_year = url[1][1]
                code = await self.extract_code(text)
                name = await self.extract_name(text)
                price = await self.extract_price(text)
                [profit_week_low, profit_week_high] = await self.extract_profit_week_low_high(text)
                pe_ratio = await self.extract_pe_ratio(text)
                try:
                    assets_profit = round(profit_week_high - profit_week_low, 2)
                except TypeError:
                    assets_profit = 0
                return url, code, name, price, profit_week_low, profit_week_high, pe_ratio, up_year, down_year, \
                    assets_profit
        except Exception as e:
            print(e)

    @staticmethod
    async def extract_code(text):
        try:
            soup = BeautifulSoup(text, 'html.parser')
            return soup.find('span', {'class': 'price-section__category'}).span.text[2:]
        except Exception as e:
            print(str(e))

    @staticmethod
    async def extract_name(text):
        try:
            soup = BeautifulSoup(text, 'html.parser')
            return soup.find('span', {'class': 'price-section__label'}).text[:-1]
        except Exception as e:
            print(str(e))

    async def extract_price(self, text):
        try:
            soup = BeautifulSoup(text, 'html.parser')
            price_usd = float(soup.find('span', {'class': 'price-section__current-value'}).text.replace(',', ''))
            return round(self.usd_course * price_usd, 2)
        except Exception as e:
            print(str(e))

    async def extract_profit_week_low_high(self, text):
        try:
            soup = BeautifulSoup(text, 'html.parser')
            try:
                raw_result_low = soup.findAll('div', {'class': 'snapshot__highlow'})[1].find('div', {
                    'class': 'snapshot__data-item snapshot__data-item--small'}).text
                raw_result_high = soup.findAll('div', {'class': 'snapshot__highlow'})[1].find('div', {
                    'class': 'snapshot__data-item snapshot__data-item--small snapshot__data-item--right'}).text
            except IndexError:
                try:
                    raw_result_low = soup.findAll('div', {'class': 'snapshot__highlow'})[0].find('div', {
                        'class': 'snapshot__data-item snapshot__data-item--small'}).text
                    raw_result_high = soup.findAll('div', {'class': 'snapshot__highlow'})[0].find('div', {
                        'class': 'snapshot__data-item snapshot__data-item--small snapshot__data-item--right'}).text
                except IndexError:
                    return 0, 0
            low = re.findall(r'\d+\.\d+', raw_result_low)[0]
            high = re.findall(r'\d+\.\d+', raw_result_high)[0]
            return round(float(low) * self.usd_course, 2), round(float(high) * self.usd_course, 2)
        except Exception as e:
            print(str(e))

    async def extract_pe_ratio(self, text):
        try:
            soup = BeautifulSoup(text, 'lxml')
            try:
                target = soup.find('div', string="P/E Ratio").parent
                pe_ratio = float(re.findall(r'\d+\.\d+', str(target))[0])
                return round(float(pe_ratio) * self.usd_course, 2)
            except AttributeError:
                target = soup.find('td', string="P/E Ratio").find_next_sibling('td')
                pe_ratio = float(re.findall(r'\d+\.\d+', str(target))[0])
                return round(float(pe_ratio) * self.usd_course, 2)
        except Exception as e:
            print(e)

    async def main(self):
        tasks = []
        async with aiohttp.ClientSession(trust_env=True) as session:
            for url in self.urls:
                tasks.append(self.fetch(session, url))

            htmls = await asyncio.gather(*tasks)
            self.all_data.extend(htmls)

            for html in htmls:
                if html is not None:
                    self.main_data[html[0][0]] = {"code": html[1], "name": html[2], "price": html[3],
                                                  "profit_week_low": html[4], "profit_week_high": html[5],
                                                  "pe_ratio": html[6], "up_year": html[7], "down_year": html[8],
                                                  "assets_profit": html[9]}
                else:
                    continue

    @staticmethod
    def get_usd_course():
        resp_bank = None
        while resp_bank is None:
            try:
                resp_bank = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
                soup_bank = BeautifulSoup(resp_bank.content, 'xml')
                usd = float(soup_bank.find(ID='R01235').Value.string.replace(',', '.'))
            except requests.exceptions.ConnectionError:
                continue
        return usd


app = WebScraper(get_target_urls())
all_data = app.main_data

ordered_top_10_assets_price = dict(
    itertools.islice(OrderedDict(sorted(all_data.items(), key=lambda i: i[1]['price'], reverse=True)).items(), 10))

ordered_top_10_low_pe_ratio = dict(
    itertools.islice(OrderedDict(sorted(all_data.items(), key=lambda i: i[1]['pe_ratio'])).items(), 10))

ordered_top_10_up_year = dict(
    itertools.islice(OrderedDict(sorted(all_data.items(), key=lambda i: i[1]['up_year'], reverse=True)).items(), 10))

ordered_top_10_assets_profit = dict(
    itertools.islice(OrderedDict(sorted(all_data.items(), key=lambda i: i[1]['assets_profit'], reverse=True)).items(),
                     10))

with open("json_data/ordered_top_10_assets_price.json", "w") as j:
    json.dump(ordered_top_10_assets_price, j)

with open("json_data/ordered_top_10_low_pe_ratio.json", "w") as j:
    json.dump(ordered_top_10_low_pe_ratio, j)

with open("json_data/ordered_top_10_up_year.json", "w") as j:
    json.dump(ordered_top_10_up_year, j)

with open("json_data/ordered_top_10_assets_profit.json", "w") as j:
    json.dump(ordered_top_10_assets_profit, j)

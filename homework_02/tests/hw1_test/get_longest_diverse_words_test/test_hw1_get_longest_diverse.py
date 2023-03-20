from tasks import hw1
import pytest


@pytest.mark.parametrize('file_name, expected', [('tests/hw1_test/get_longest_diverse_words_test/test_data.txt',
                                                  ['Souveränitätsansprüche', 'symbolischsakramentale',
                                                   'Kollektivschuldiger', 'Bevölkerungsabschub', 'unmißverständliche',
                                                   'politisch-strategischen', 'Werkstättenlandschaft',
                                                   'résistance-Bewegungen', 'Verwaltungsmaßnahme', 'Selbstverständlich']
                                                  )])
def test_get_longest_diverse_words(file_name, expected):
    test_result = hw1.get_longest_diverse_words(file_name)
    for i in test_result:
        assert i in expected


@pytest.mark.parametrize('exception, wrong_file_name',
                         [(FileNotFoundError, 'tests/hw1_test/get_longest_diverse_words_test/some_data'),
                          (FileNotFoundError, 'tests/hw1_test/get_longest_diverse_words_test/database.txt'),
                          (FileNotFoundError, 'tests/hw1_test/get_longest_diverse_words_test/text.txt'),
                          (OSError, 123),
                          (OSError, 234512),
                          (OSError, 9091234)])
def test_get_longest_diverse_words_exceptions(exception, wrong_file_name):
    with pytest.raises(exception):
        hw1.get_longest_diverse_words(wrong_file_name)

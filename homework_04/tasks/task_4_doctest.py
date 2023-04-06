"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


#>>> fizzbuzz(5)
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Return a fizzbuzz sequence
    How to run doctests via pytest:
    1) Input in the command line:

        pytest --doctest-glob=*.rst

    2) And then you can use it for testing:

        pytest .\task_4_doctest.rst

    """

    return ["fizzbuzz" if i % 15 == 0
            else "fizz" if i % 3 == 0
            else "buzz" if i % 5 == 0
            else str(i)
            for i in range(1, n + 1)]

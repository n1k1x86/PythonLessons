from tasks.hw1 import ColorsEnum, SizesEnum


def test_hw1_colors_positive():
    assert ColorsEnum.storage == {'RED': 'RED', 'BLUE': 'BLUE', 'ORANGE': 'ORANGE', 'BLACK': 'BLACK'}


def test_hw1_sizes_positive():
    assert SizesEnum.storage == {'XL': 'XL', 'L': 'L', 'M': 'M', 'S': 'S', 'XS': 'XS'}


def test_hw1_colors_negative():
    assert ColorsEnum.storage != {'GG': 'GG', 'WP': 'BLUE', 'MM': 'ORANGE', 'BLACK': 'BLACK'}


def test_hw1_sizes_negative():
    assert SizesEnum.storage != {'XXL': 'XL', 'LL': 'L', 'M': 'M', 'S': 'SS', 'XS': 'XSS)'}

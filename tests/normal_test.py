from tests.settings import *

# create tests for normal items here...

def test_normal_general():
    item = Item("name item", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 19

def test_normal_datePassed():
    item = Item("name item", 0, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == -1
    assert item.quality == 18

def test_normal_negativeQuality():
    item = Item("name item", 10, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 9
    assert item.quality == 0
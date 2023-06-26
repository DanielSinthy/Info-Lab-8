from tests.settings import *


def test_passes_10days():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 9
    assert item.quality == 22

def test_passes_5days():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 23

def test_passes_general():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == -1
    assert item.quality == 0
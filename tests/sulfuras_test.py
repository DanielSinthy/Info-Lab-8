from tests.settings import *

@pytest.mark.xfail(xfail_bug_in_original, reason = "Sulfuras' sell date is always -1")
def test_sulfuras_sell_in():
    item = Item("Sulfuras, Hand of Ragnaros", 10, 80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == -1
    assert item.quality == 80

@pytest.mark.xfail(xfail_bug_in_original, reason = "Sulfuras' quality is always 80")
def test_sulfuras_quality():
    item = Item("Sulfuras, Hand of Ragnaros", 23, 70)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == -1
    assert item.quality == 80

# -*- coding: utf-8 -*-


class GildedRose(object):

  


    def __init__(self, items):
        self.items = items
        self.strategy_mapping = {
            "Aged Brie": AgedBrieItemStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassItemStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasItemStrategy()
        }


    def update_quality(self):
        for item in self.items:
            strategy = self.strategy_mapping.get(item.name, RegularItemStrategy())
            strategy.update_quality(item)

class RegularItemStrategy:
    def update_quality(self, item):
        if item.quality > 50:
            item.quality = 50
        else:
            if item.quality > 0:
                item.quality -= 1
            item.sell_in -= 1
            if item.sell_in < 0 and item.quality > 0:
                item.quality -= 1

class AgedBrieItemStrategy:
    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class BackstagePassItemStrategy:
    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0

class SulfurasItemStrategy:
    def update_quality(self, item):
        if item.quality != 80:
            item.quality = 80
        if item.sell_in != -1:
            item.sell_in != -1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
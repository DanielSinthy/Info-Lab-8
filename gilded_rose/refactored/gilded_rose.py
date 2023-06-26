# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_passes(item)
            elif item.name != "Sulfuras, Hand of Ragnaros":
                self.update_normal_item(item)

        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1

        if item.sell_in < 0:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                self.decrease_quality(item)
            else:
                item.quality = 0


    def update_aged_brie(self, item):
        if item.quality < 50:
            item.quality += 1

    def update_backstage_passes(self, item):
        if item.quality < 50:
         item.quality += 1
        if item.sell_in < 11:
            self.increase_quality(item)
        if item.sell_in < 6:
            self.increase_quality(item)

    def update_normal_item(self, item):
        if item.quality > 0:
            item.quality -= 1

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def decrease_quality(self, item):
        if item.quality > 0:
         item.quality -= 1
            


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
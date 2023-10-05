# -*- coding: utf-8 -*-

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


#-------------------- Classes for update items (applied strategy design pattern) --------------------#
class ItemUpdater:
    def update(self, item):
        pass


class DefaultUpdater(ItemUpdater):
    def update(self, item):
        if item.quality > 0:
            if item.sell_in >= 0:
                item.quality -= 1
            if item.sell_in < 0 and item.quality > 1:
                item.quality -= 2
        item.sell_in -= 1


class AgedBrieUpdater(ItemUpdater):
    def update(self, item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1


class BackstagePassesUpdater(ItemUpdater):
    def update(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0


class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        pass


class ConjuredUpdater(ItemUpdater):
    def update(self, item):
        if item.quality > 0:
            if item.sell_in >= 0 and item.quality > 1:
                item.quality -= 2
            if item.sell_in < 0 and item.quality > 3:
                item.quality -= 4
        item.sell_in -= 1


#-------------------- Updated GildedRose (treat class as first class citizens) --------------------#
class GildedRose(object):
    ITEM_UPDATERS = {
        "Aged Brie": AgedBrieUpdater(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassesUpdater(),
        "Sulfuras, Hand of Ragnaros": SulfurasUpdater(),
        "Conjured Mana Cake": ConjuredUpdater(),
    }

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items


    def update_quality(self):
        for item in self.items:
            if item.name in self.ITEM_UPDATERS:
                self.ITEM_UPDATERS[item.name].update(item)
            else:
                DefaultUpdater().update(item)

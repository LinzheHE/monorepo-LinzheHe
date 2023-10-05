# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    #-------------------- Tests for default items --------------------#
    def test_default_item_general(self):
        # Arrange
        test_item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertGreater(original_sell_in, new_sell_in)
        self.assertEqual(new_sell_in, original_sell_in - 1)

        self.assertGreaterEqual(new_quality, 0)
        self.assertLessEqual(new_quality, 50)
        self.assertGreater(original_quality, new_quality)
        self.assertEqual(new_quality, original_quality - 1)


    def test_default_item_double_decrease(self):
        # Arrange
        test_item = Item(name="+5 Dexterity Vest", sell_in=-1, quality=20)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertGreater(original_quality, new_quality)
        self.assertEqual(new_quality, original_quality - 2)

    
    def test_default_item_stop_decrease(self):
        # Arrange
        test_item = Item(name="+5 Dexterity Vest", sell_in=10, quality=0)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertEqual(new_quality, original_quality)
    

    #-------------------- Tests for aged brie items --------------------#
    def test_aged_brie_item_general(self):
        # Arrange
        test_item = Item(name="Aged Brie", sell_in=2, quality=0)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertGreater(original_sell_in, new_sell_in)
        self.assertEqual(new_sell_in, original_sell_in - 1)

        self.assertGreaterEqual(new_quality, 0)
        self.assertLessEqual(new_quality, 50)
        self.assertGreater(new_quality, original_quality)
        self.assertEqual(new_quality, original_quality + 1)
    

    def test_aged_brie_stop_increase(self):
        # Arrange
        test_item = Item(name="Aged Brie", sell_in=2, quality=50)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertGreater(original_sell_in, new_sell_in)
        self.assertEqual(new_sell_in, original_sell_in - 1)

        self.assertLessEqual(new_quality, 50)
        self.assertEqual(new_quality, original_quality)
    

    #-------------------- Tests for backstage items --------------------#
    def test_backstage_item_increase_one(self):
        # Arrange
        test_item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertGreater(original_sell_in, new_sell_in)
        self.assertEqual(new_sell_in, original_sell_in - 1)

        self.assertGreaterEqual(new_quality, 0)
        self.assertLessEqual(new_quality, 50)
        self.assertGreater(new_quality, original_quality)
        self.assertEqual(new_quality, original_quality + 1)
    

    def test_backstage_item_increase_two(self):
        # Arrange
        test_item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertGreater(original_sell_in, new_sell_in)
        self.assertEqual(new_sell_in, original_sell_in - 1)

        self.assertGreaterEqual(new_quality, 0)
        self.assertLessEqual(new_quality, 50)
        self.assertGreater(new_quality, original_quality)
        self.assertEqual(new_quality, original_quality + 2)
    

    def test_backstage_item_increase_two_stop(self):
        # Arrange
        test_item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertGreater(original_sell_in, new_sell_in)
        self.assertEqual(new_sell_in, original_sell_in - 1)

        self.assertGreaterEqual(new_quality, 0)
        self.assertLessEqual(new_quality, 50)
        self.assertGreater(new_quality, original_quality)
        self.assertEqual(new_quality, 50)
    

    def test_backstage_item_increase_three(self):
        # Arrange
        test_item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertGreater(original_sell_in, new_sell_in)
        self.assertEqual(new_sell_in, original_sell_in - 1)

        self.assertGreaterEqual(new_quality, 0)
        self.assertLessEqual(new_quality, 50)
        self.assertGreater(new_quality, original_quality)
        self.assertEqual(new_quality, original_quality + 3)
    

    def test_backstage_item_drop_zero(self):
        # Arrange
        test_item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=20)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertGreater(original_sell_in, new_sell_in)
        self.assertEqual(new_sell_in, original_sell_in - 1)

        self.assertEqual(new_quality, 0)

    #-------------------- Tests for sulfuras items --------------------#
    def test_sulfuras_item(self):
        # Arrange
        test_item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertEqual(new_sell_in, original_sell_in)

        self.assertEqual(new_quality, original_quality)
    

    #-------------------- Tests for conjured items --------------------#
    def test_conjured_item_general(self):
        # Arrange
        test_item = Item(name="Conjured Mana Cake", sell_in=3, quality=6)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertGreater(original_sell_in, new_sell_in)
        self.assertEqual(new_sell_in, original_sell_in - 1)

        self.assertGreaterEqual(new_quality, 0)
        self.assertLessEqual(new_quality, 50)
        self.assertGreater(original_quality, new_quality)
        self.assertEqual(new_quality, original_quality - 2)


    def test_conjured_item_double_decrease(self):
        # Arrange
        test_item = Item(name="Conjured Mana Cake", sell_in=-1, quality=6)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertGreater(original_quality, new_quality)
        self.assertEqual(new_quality, original_quality - 4)

    
    def test_conjured_item_stop_decrease(self):
        # Arrange
        test_item = Item(name="Conjured Mana Cake", sell_in=5, quality=0)
        gr = GildedRose([test_item])

        original_sell_in = test_item.sell_in
        original_quality = test_item.quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = test_item.sell_in
        new_quality = test_item.quality

        self.assertEqual(new_quality, original_quality)    


if __name__ == '__main__':
    unittest.main()

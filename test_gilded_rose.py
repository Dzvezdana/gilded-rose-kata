import unittest

from gilded_rose import Item, GildedRoseUpdater


class GildedRoseUpdaterTest(unittest.TestCase):
    # Normal
    def test_normal_item_before_sell_date(self):
        items = [Item(name="foo", sell_in=10, quality=4)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

    def test_normal_item_on_sell_date(self):
        items = [Item(name="foo", sell_in=0, quality=9)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_normal_item_after_sell_date(self):
        items = [Item(name="foo", sell_in=-10, quality=10)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(-11, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_normal_with_zero_quality(self):
        items = [Item(name="foo", sell_in=2, quality=0)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    # Brie
    def test_brie_before_sell_date(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=0)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_brie_on_sell_date(self):
        items = [Item(name="Aged Brie", sell_in=0, quality=0)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_brie_after_sell_date(self):
        items = [Item(name="Aged Brie", sell_in=-10, quality=0)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(-11, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_brie_max_quality(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=50)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_brie_over_max_quality(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=52)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_brie_negative_quality(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=-5)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    # Sulfuras
    def test_sulfuras_on_sell_date(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_before_sell_date(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_after_sell_date(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_max_quality(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=82)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    # BackStage
    def test_backstage_sell_in_15(self):
        items = [Item(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_sell_in_10(self):
        items = [Item(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_sell_in_5(self):
        items = [Item(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=5, quality=20)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_sell_in_0(self):
        items = [Item(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=0, quality=49)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_after_concert(self):
        items = [Item(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=-1, quality=49)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_quality_change_50(self):
        items = [Item(name="BackStage Passes to a TAFKAL80ETC concert", sell_in=10, quality=50)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    # Conjured
    def test_conjured_before_sell_date(self):
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_conjured_on_sell_date(self):
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=6)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_conjured_after_sell_date(self):
        items = [Item(name="Conjured Mana Cake", sell_in=-2, quality=6)]
        gilded_rose = GildedRoseUpdater(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    # Other
    def test_other_products(self):
        dexterity_item = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
        elixir_item = [Item(name="Elixir of the Mongoose", sell_in=5, quality=7)]

        gilded_rose_dexterity = GildedRoseUpdater(dexterity_item)
        gilded_rose_dexterity.update_quality()

        gilded_rose_elixir = GildedRoseUpdater(elixir_item)
        gilded_rose_elixir.update_quality()
        self.assertEqual(19, dexterity_item[0].quality)
        self.assertEqual(6, elixir_item[0].quality)


if __name__ == '__main__':
    unittest.main()

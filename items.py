from products import Products

MIN_QUALITY = 0
MAX_QUALITY = 50
LEGENDARY_MAX_QUALITY = 80
MIN_SELL_IN_VALUE = 0


class ItemFactory:
    """ Used for creating product object. """

    @staticmethod
    def create(name, sell_in, quality):
        """
        Checks if the product is a specific (Aged Brie, BackStage Passes, Conjured or
        Sulfuras) or a normal product and creates a product instance.

        Args:
            name (str): item name.
            sell_in (int): number of days we have left to sell the item.
            quality (int): item quality value.

        Returns:
            product object: Calls a specific product updater.

        """
        if name == Products.AGED_BRIE.value:
            return AgedBrie(name, sell_in, quality)

        elif name == Products.BACKSTAGE_PASSES.value:
            return BackstagePasses(name, sell_in, quality)

        elif name == Products.CONJURED.value:
            return Conjured(name, sell_in, quality)

        elif name == Products.SULFURAS.value:
            return Sulfuras(name, sell_in, quality)

        else:
            return Item(name, sell_in, quality)


class Item:
    """ Used to describe item properties. """

    def __init__(self, name, sell_in, quality):
        """
        Args:
            name (str): item name.
            sell_in (int): number of days we have to sell the item.
            quality (int): item quality value.
        """
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update(self) -> None:
        """ Calls the quality and the sell in updaters. """
        self._update_sell_in()
        self.quality = self._update_quality(self.sell_in)

    def _update_quality(self, sell_in: int) -> int:
        """
        Updates regular product quality. Regular product's quality:
        - decreases by 1 before sell by date
        - by 2 after sell by date passes.

        Args:
            sell_in (int): number of days we have to sell the item.

        Returns:
            int: updated product quality.
        """
        if sell_in >= 0:
            return max(self.quality - 1, MIN_QUALITY)
        else:
            return max(self.quality - 2, MIN_QUALITY)

    def _update_sell_in(self) -> None:
        """ Decreases sell in date. """
        self.sell_in -= 1


class AgedBrie(Item):
    """
    Used to increase the quality by day for Brie (whose value increases
    over time).
    """
    def _update_quality(self, sell_in: int) -> int:
        if self.quality < 0:
            return MIN_QUALITY

        if sell_in >= 0 and self.quality > 0:
            return min(self.quality + 1, MAX_QUALITY)
        else:
            return min(self.quality + 2, MAX_QUALITY)


class BackstagePasses(Item):
    """
    Backstage passes, increases in quality as its sell_in value approaches;
    Quality increases by:
        - 2 when there are 10 days or less,
        - 3 when there are 5 days or less,
        - drops to 0 after the concert.
    """
    def _update_quality(self, sell_in: int) -> int:
        if sell_in > 10:
            return min(self.quality + 1, MAX_QUALITY)
        elif sell_in > 5:
            return min(self.quality + 2, MAX_QUALITY)
        elif sell_in >= 0:
            return min(self.quality + 3, MAX_QUALITY)
        else:
            return MIN_QUALITY


class Conjured(Item):
    """
    Conjured items degrade in quality twice as fast as normal items:
        - by 2 before and on the sell in date,
        - by 4 after the sell in date.
    """
    def _update_quality(self, sell_in: int) -> int:
        if self.quality < 0:
            return MIN_QUALITY

        if sell_in >= 0:
            return max(self.quality - 2, MIN_QUALITY)
        else:
            return max(self.quality - 4, MIN_QUALITY)


class Sulfuras(Item):
    """
    Sulfuras is a legendary item that never has to be sold or decreases in quality.
    """
    def _update_quality(self, sell_in: int) -> int:
        if self.quality > LEGENDARY_MAX_QUALITY:
            return LEGENDARY_MAX_QUALITY
        else:
            return LEGENDARY_MAX_QUALITY

    def _update_sell_in(self) -> None:
        pass

MIN_QUALITY = 0
MAX_QUALITY = 50
LEGENDARY_MAX_QUALITY = 80
MIN_SELL_IN_VALUE = 0


class Item:
    """
    Used to describe item properties.
    """
    def __init__(self, name, sell_in, quality):
        """
        Args:
            name: item name.
            sell_in: number of days we have to sell the item.
            quality: item value.
        """
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRoseUpdater(object):
    """
    Used to update items properties.
    """
    def __init__(self, items):
        """
        Args:
            items (list): List of items.
        """
        self.items = items

    def update_quality(self):
        """
        Iterates through and updates items.
        """
        for item in self.items:
            get_product_updater(item)


def get_product_updater(item):
    """
    Checks if the product is a specific (Aged Brie, BackStage Passes, Conjured or
    Sulfuras) or a normal product.

    Args:
        item (list): Product item.

    Returns:
        function call: Calls a specific updater.

    """
    if "Aged Brie" in item.name:
        return increase_quality_by_day(item)

    elif "BackStage Passes" in item.name:
        return update_backstage_passes(item)

    elif "Conjured" in item.name:
        return update_conjured(item)

    elif "Sulfuras" in item.name:
        return update_legendary(item)

    else:
        return decrease_quality_by_day(item)


def increase_quality_by_day(item):
    """
    Used to increase the quality by day for products (like Brie) whose value increases
    over time.

    Args:
        item (list): Product item.
    """
    quality = item.quality

    if quality < MAX_QUALITY and quality == MIN_QUALITY:
        quality += 1

    # Product quality cannot be negative.
    elif quality < MIN_QUALITY:
        quality = MIN_QUALITY

    # Product quality cannot be greater than 50.
    elif quality >= MAX_QUALITY:
        quality = MAX_QUALITY

    item.quality = quality
    item.sell_in = get_updated_sell_in_value(item.sell_in)


def decrease_quality_by_day(item):
    """
    Used to decrease the quality of products by day.

    Args:
        item (list): Product item.
    """
    quality = item.quality
    sell_in_value = item.sell_in

    if quality <= MIN_QUALITY:
        quality = MIN_QUALITY

    # Once the sell by date has passed, quality degrades twice as fast.
    elif sell_in_value < MIN_SELL_IN_VALUE and quality >= MIN_QUALITY + 2:
        quality -= 2

    else:
        quality -= 1

    item.quality = quality
    item.sell_in = get_updated_sell_in_value(item.sell_in)


def update_backstage_passes(item):
    """
    Backstage passes, increases in quality as its sell_in value approaches;
    Quality increases by:
        - 2 when there are 10 days or less,
        - 3 when there are 5 days or less,
        - drops to 0 after the concert.

    Args:
        item (list): Product item.
    """
    quality = item.quality
    sell_in_value = item.sell_in

    if quality == MAX_QUALITY and sell_in_value != MIN_SELL_IN_VALUE:
        quality = MAX_QUALITY

    # Quality becomes 0 after the concert.
    elif sell_in_value < MIN_SELL_IN_VALUE:
        quality = 0

    # Quality grows by 3, 5 days or less before the concert.
    elif sell_in_value <= 5:
        quality += 3

    # Quality grows by 2, 10 days or less before the concert.
    elif sell_in_value <= 10:
        quality += 2

    # Quality can't be negative.
    elif quality < MIN_QUALITY:
        quality = MIN_QUALITY

    else:
        quality += 1

    if quality > MAX_QUALITY:
        quality = MAX_QUALITY

    item.quality = quality
    item.sell_in = get_updated_sell_in_value(item.sell_in)


def update_conjured(item):
    """
    Conjured items degrade in quality twice as fast as normal items:
        - by 2 before and on the sell in date,
        - by 4 after the sell in date.

    Args:
        item (list): Product item.
    """
    quality = item.quality
    sell_in_value = item.sell_in

    if quality <= MIN_QUALITY:
        quality = MIN_QUALITY

    elif sell_in_value < MIN_SELL_IN_VALUE and quality >= MIN_QUALITY + 2:
        quality -= 4

    else:
        quality -= 2

    item.quality = quality
    item.sell_in = get_updated_sell_in_value(item.sell_in)


def update_legendary(item):
    """
    Sulfuras is a legendary item that never has to be sold or decreases in Quality.

    Args:
        item (list): Product item.
    """
    quality = item.quality
    if quality > LEGENDARY_MAX_QUALITY:
        item.quality = LEGENDARY_MAX_QUALITY

    item.sell_in = get_updated_sell_in_value(item.sell_in)


def get_updated_sell_in_value(sell_in_value):
    sell_in_value -= 1
    return sell_in_value

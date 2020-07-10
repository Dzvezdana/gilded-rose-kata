class GildedRoseUpdater(object):
    """
    Used to update items properties.
    """
    def __init__(self, items) -> None:
        """
        Args:
            items (list): List of items.
        """
        self.items = items

    def update_quality(self) -> None:
        """
        Iterates through and updates items.
        """
        for item in self.items:
            item.update_quality()

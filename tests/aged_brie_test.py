from tests.settings import *

import unittest

class AgedBrie(unittest.TestCase):

    def setUp(self):
        items = [] 

    @pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
    def test_update_quality_with_a_single_aged_brie_item(self):
        items = [Item("Aged Brie", 5, 10)]
        GildedRose(items).update_quality()
        expected = {'sell_in': 4 }
        item = items[0]
        self.assertEqual(item.sell_in, expected['sell_in'])
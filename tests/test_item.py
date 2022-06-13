from datetime import datetime
from unittest import TestCase

import json

from ppac.item import Item, decode_date


class TestItem(TestCase):
    def test_defaults(self):
        item = Item(id='myID')

        self.assertDictEqual(
            item.to_dict(),
            {
                'id': 'myID',
                'due_date': None,
                'start_date': None,
                'end_date': None,
                'labels': [],
            }
        )

    def test_to_dict(self):
        item = Item(
            id='myID',
            due_date=datetime(2022, 6, 12)
        )

        self.assertDictEqual(
            item.to_dict(),
            {
                'id': 'myID',
                'due_date': datetime(2022, 6, 12),
                'start_date': None,
                'end_date': None,
                'labels': [],
            }
        )

    def test_from_dict(self):
        item = Item.from_dict({
            'id': 'myID',
            'due_date': datetime(2022, 6, 12),
        })

        self.assertDictEqual(
            item.to_dict(),
            {
                'id': 'myID',
                'due_date': datetime(2022, 6, 12),
                'start_date': None,
                'end_date': None,
                'labels': [],
            }
        )

    def test_to_json_str(self):
        item = Item.from_dict({
            'id': 'myID',
            'due_date': datetime(2022, 6, 12),
        })

        self.assertDictEqual(
            json.loads(item.to_json_str(), object_hook=decode_date),
            {
                'id': 'myID',
                'due_date': datetime(2022, 6, 12),
                'start_date': None,
                'end_date': None,
                'labels': [],
            }
        )

    def test_from_json_str(self):
        item = Item.from_json_str(
            '{"due_date": "2022-05-03T12:34:44", "id": "myID"}')

        self.assertDictEqual(
            item.to_dict(),
            {
                'id': 'myID',
                'due_date': datetime(2022, 5, 3, 12, 34, 44),
                'start_date': None,
                'end_date': None,
                'labels': [],
            }
        )

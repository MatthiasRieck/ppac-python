"""
Planning item for project config as code.
"""

from dataclasses import dataclass
import dataclasses
from datetime import datetime, date
from typing import List
from .utils import datetime_to_str, str_to_datetime

import json


class DateTimeEncoder(json.JSONEncoder):
    """Class to convert datetime/date to string for serialization."""

    def default(self, o):
        if isinstance(o, (date, datetime)):
            return datetime_to_str(o)

        return o


def decode_date(value_dict):
    """Function to convert string to datetime for deserialization."""
    for k_item, v_item in value_dict.items():
        if k_item.endswith('_date') and v_item:
            value_dict[k_item] = str_to_datetime(v_item)
    return value_dict


@dataclass
class Item:
    """Plannig item for project planning as code."""
    id: str  # pylint: disable=C0103
    due_date: datetime = None
    start_date: datetime = None
    end_date: datetime = None
    labels: List[str] = dataclasses.field(default_factory=list)

    @property
    def name(self):
        return self.id.split('/')[-1]

    def to_dict(self):
        return dataclasses.asdict(self)

    def to_json_str(self, indent=0):
        return json.dumps(self.to_dict(), indent=indent, cls=DateTimeEncoder)

    @classmethod
    def from_dict(cls, value):
        return Item(**value)

    @classmethod
    def from_json_str(cls, value):
        return Item.from_dict(json.loads(value, object_hook=decode_date))

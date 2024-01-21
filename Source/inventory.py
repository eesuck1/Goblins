from Source.item import Item
from Source.message import Refuse, ToSay


class Inventory:
    def __init__(self):
        self._volume_ = 0
        self._max_volume_ = 40
        self._weight_ = 0
        self._max_weight_ = 20
        self._items_ = []

    def add_item(self, item: Item) -> None | Refuse | ToSay:
        if self._volume_ + item.volume > self._max_volume_:
            return Refuse("Can't put it here")
        elif self._weight_ + item.weight > self._max_weight_:
            self._items_.append(item)

            return ToSay("It'll tore soon")

        self._items_.append(item)
        self._volume_ += item.volume
        self._weight_ += item.weight

    def drop_item(self, item: Item) -> None:
        self._items_.remove(item)

    @property
    def items(self) -> list[Item, ...]:
        return self._items_

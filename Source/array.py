from typing import Any


class Array:
    def __init__(self, shape: tuple[int, int, int], filler: Any):
        self._shape_ = shape
        self._filler_ = filler

        self._array_ = self.fill()

    def fill(self) -> list:
        return [[[self._filler_ for _ in range(self._shape_[-1])] for _ in range(self._shape_[-2])] for _ in
                range(self._shape_[-3])]

    @property
    def array(self) -> list:
        return self._array_

    @property
    def shape(self) -> tuple[int, int, int]:
        return self._shape_

    def __getitem__(self, item: int) -> Any:
        return self._array_[item]

    def __setitem__(self, key, value) -> None:
        self._array_[key] = value

    def __str__(self) -> str:
        return str(self._array_)

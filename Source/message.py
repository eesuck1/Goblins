class Message:
    def __init__(self, message: str):
        self._message_ = message

    def __str__(self) -> str:
        return self._message_

    @property
    def message(self) -> str:
        return self._message_


class Refuse(Message):
    def __init__(self, message: str):
        super().__init__(message)


class ToSay(Message):
    def __init__(self, message: str):
        super().__init__(message)

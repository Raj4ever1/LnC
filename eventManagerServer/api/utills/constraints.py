from enum import Enum


class TransactionStatus(Enum):
    NOT_STARTED = "not_started"
    ON_GOING = "on_going"
    COMPLETED = "completed"
    CANCELED = "canceled"

class GameIdEnum(Enum):
    CRICKET = 1
    CHESS = 2

class GameNoPlayersEnum(Enum):
    CRICKET = 11
    CHESS = 2
    
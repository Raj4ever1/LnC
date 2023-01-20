from enum import Enum


class TransactionStatus(Enum):
    NOT_STARTED = "not_started"
    ON_GOING = "on_going"
    COMPLETED = "completed"
    CANCELED = "canceled"
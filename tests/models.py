from datetime import date, datetime
from typing import Optional

import pydantic
from pydantic import Field


class User(pydantic.BaseModel):
    id: int
    firstname: str
    lastname: str
    birthday: date
    signed_up: bool = False


class SimpleUser(pydantic.BaseModel):
    firstname: str
    lastname: str


class NonBaseModelUser:
    firstname: str
    lastname: str


class Boolean(pydantic.BaseModel):
    true: Optional[bool] = None
    false: Optional[bool] = None


class UserOptional(pydantic.BaseModel):
    firstname: str = "John"
    age: Optional[int] = None
    created: Optional[datetime] = datetime(year=2002, month=2, day=20, hour=22, minute=22)


class DefaultFactory(pydantic.BaseModel):
    firstname: str
    created: Optional[datetime] = Field(default_factory=datetime.now)


class LotsOfDates(pydantic.BaseModel):
    start: date
    end: date
    timestamp: datetime

    @pydantic.field_validator("start", mode="before")
    def parse_start_date(cls, value):
        return datetime.strptime(value, "%A, %d. %B %Y").date()

    @pydantic.field_validator("end", mode="before")
    def parse_end_date(cls, value):
        return datetime.strptime(value, "%d.%m.%Y").date()

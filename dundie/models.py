from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, validator
from dundie.utils.email import check_valid_email


class InvalidEmailError(Exception):
    ...


class Person(BaseModel):
    pk: str
    name: str
    dept: str
    role: str

    @validator("pk")
    def validate_email(cls, v):
        if not check_valid_email(v):
            raise InvalidEmailError(f"Invalid email for {v!r}")
        return v

    def __str__(self):
        return f"{self.name} - {self.role}"


class Balance(BaseModel):
    person: Person
    value: Decimal

    @validator("value", pre=True)
    # valida antes da criação da instância
    def value_logic(cls, v):
        return Decimal(v) * 2

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class Movement(BaseModel):
    person: Person
    date: datetime
    actor: str
    value: Decimal

    class Config:
        json_encoders = {Person: lambda p: p.pk}


person = Person(
    pk="bruno@rocha.com", name="Bruno", dept="engineering", role="programmer"
)

balance = Balance(person=person, value=100)
print(balance.json(models_as_dict=False))

{"person": "bruno@rocha.com", "value": 200}

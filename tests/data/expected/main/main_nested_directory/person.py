# generated by datamodel-codegen:
#   filename:  person.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field, NonNegativeInt

from .definitions import food, friends, pet
from .definitions.drink import coffee, tea
from .definitions.machine import robot


class Person(BaseModel):
    first_name: str = Field(..., description="The person's first name.")
    last_name: str = Field(..., description="The person's last name.")
    age: Optional[NonNegativeInt] = Field(None, description='Age in years.')
    pets: Optional[List[pet.Pet]] = None
    friends: Optional[friends.Friends] = None
    robot: Optional[robot.Robot] = None
    comment: Optional[Any] = None
    drink: Optional[List[Union[coffee.Coffee, tea.Tea]]] = None
    food: Optional[List[Union[food.Noodle, food.Soup]]] = None


Person.update_forward_refs()

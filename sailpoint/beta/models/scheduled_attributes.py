# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ScheduledAttributes(BaseModel):
    """
    Attributes related to a scheduled trigger
    """ # noqa: E501
    frequency: StrictStr = Field(description="Frequency of execution")
    time_zone: Optional[StrictStr] = Field(default=None, description="Time zone identifier", alias="timeZone")
    cron_string: Optional[StrictStr] = Field(default=None, alias="cronString")
    weekly_days: Optional[List[StrictStr]] = Field(default=None, description="Scheduled days of the week for execution", alias="weeklyDays")
    weekly_times: Optional[List[StrictStr]] = Field(default=None, description="Scheduled execution times", alias="weeklyTimes")
    __properties: ClassVar[List[str]] = ["frequency", "timeZone", "cronString", "weeklyDays", "weeklyTimes"]

    @field_validator('frequency')
    def frequency_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['daily', 'weekly', 'monthly', 'yearly', 'cronSchedule']):
            raise ValueError("must be one of enum values ('daily', 'weekly', 'monthly', 'yearly', 'cronSchedule')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)


    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ScheduledAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScheduledAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "frequency": obj.get("frequency"),
            "timeZone": obj.get("timeZone"),
            "cronString": obj.get("cronString"),
            "weeklyDays": obj.get("weeklyDays"),
            "weeklyTimes": obj.get("weeklyTimes")
        })
        return _obj


# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json
import warnings

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from sailpoint.v2024.models.standard_level import StandardLevel
from typing import Optional, Set
from typing_extensions import Self

class ClientLogConfiguration(BaseModel):
    """
    Client Runtime Logging Configuration
    """ # noqa: E501
    client_id: Optional[StrictStr] = Field(default=None, description="Log configuration's client ID", alias="clientId")
    duration_minutes: Optional[Annotated[int, Field(le=1440, strict=True, ge=5)]] = Field(default=240, description="Duration in minutes for log configuration to remain in effect before resetting to defaults.", alias="durationMinutes")
    expiration: Optional[datetime] = Field(default=None, description="Expiration date-time of the log configuration request.  Can be no greater than 24 hours from current date-time.")
    root_level: StandardLevel = Field(alias="rootLevel")
    log_levels: Optional[Dict[str, StandardLevel]] = Field(default=None, description="Mapping of identifiers to Standard Log Level values", alias="logLevels")
    __properties: ClassVar[List[str]] = ["clientId", "durationMinutes", "expiration", "rootLevel", "logLevels"]

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
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ClientLogConfiguration from a JSON string"""
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
        """Create an instance of ClientLogConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clientId": obj.get("clientId"),
            "durationMinutes": obj.get("durationMinutes") if obj.get("durationMinutes") is not None else 240,
            "expiration": obj.get("expiration"),
            "rootLevel": obj.get("rootLevel"),
            "logLevels": dict((_k, _v) for _k, _v in obj.get("logLevels").items()) if obj.get("logLevels") is not None else None
        })
        return _obj



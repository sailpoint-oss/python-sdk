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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Outlier(BaseModel):
    """
    Outlier
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The identity's unique identifier for the outlier record")
    identity_id: Optional[StrictStr] = Field(default=None, description="The ID of the identity that is detected as an outlier", alias="identityId")
    type: Optional[StrictStr] = Field(default=None, description="The type of outlier summary")
    first_detection_date: Optional[datetime] = Field(default=None, description="The first date the outlier was detected", alias="firstDetectionDate")
    latest_detection_date: Optional[datetime] = Field(default=None, description="The most recent date the outlier was detected", alias="latestDetectionDate")
    ignored: Optional[StrictBool] = Field(default=None, description="Flag whether or not the outlier has been ignored")
    attributes: Optional[Dict[str, Any]] = Field(default=None, description="Object containing mapped identity attributes")
    score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The outlier score determined by the detection engine ranging from 0..1")
    unignore_type: Optional[StrictStr] = Field(default=None, description="Enum value of if the outlier manually or automatically un-ignored. Will be NULL if outlier is not ignored", alias="unignoreType")
    unignore_date: Optional[datetime] = Field(default=None, description="shows date when last time has been unignored outlier", alias="unignoreDate")
    ignore_date: Optional[datetime] = Field(default=None, description="shows date when last time has been ignored outlier", alias="ignoreDate")
    __properties: ClassVar[List[str]] = ["id", "identityId", "type", "firstDetectionDate", "latestDetectionDate", "ignored", "attributes", "score", "unignoreType", "unignoreDate", "ignoreDate"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('LOW_SIMILARITY', 'STRUCTURAL'):
            raise ValueError("must be one of enum values ('LOW_SIMILARITY', 'STRUCTURAL')")
        return value

    @field_validator('unignore_type')
    def unignore_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('MANUAL', 'AUTOMATIC', 'null'):
            raise ValueError("must be one of enum values ('MANUAL', 'AUTOMATIC', 'null')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Outlier from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if unignore_type (nullable) is None
        # and model_fields_set contains the field
        if self.unignore_type is None and "unignore_type" in self.model_fields_set:
            _dict['unignoreType'] = None

        # set to None if unignore_date (nullable) is None
        # and model_fields_set contains the field
        if self.unignore_date is None and "unignore_date" in self.model_fields_set:
            _dict['unignoreDate'] = None

        # set to None if ignore_date (nullable) is None
        # and model_fields_set contains the field
        if self.ignore_date is None and "ignore_date" in self.model_fields_set:
            _dict['ignoreDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Outlier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "identityId": obj.get("identityId"),
            "type": obj.get("type"),
            "firstDetectionDate": obj.get("firstDetectionDate"),
            "latestDetectionDate": obj.get("latestDetectionDate"),
            "ignored": obj.get("ignored"),
            "attributes": obj.get("attributes"),
            "score": obj.get("score"),
            "unignoreType": obj.get("unignoreType"),
            "unignoreDate": obj.get("unignoreDate"),
            "ignoreDate": obj.get("ignoreDate")
        })
        return _obj


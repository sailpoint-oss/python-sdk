# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json
import warnings

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.v2025.models.scheduled_action_response_content_backup_options_object_options_value import ScheduledActionResponseContentBackupOptionsObjectOptionsValue
from typing import Optional, Set
from typing_extensions import Self

class ScheduledActionPayloadContentBackupOptions(BaseModel):
    """
    Options for BACKUP type jobs. Required for BACKUP jobs.
    """ # noqa: E501
    include_types: Optional[List[StrictStr]] = Field(default=None, description="Object types that are to be included in the backup.", alias="includeTypes")
    object_options: Optional[Dict[str, ScheduledActionResponseContentBackupOptionsObjectOptionsValue]] = Field(default=None, description="Map of objectType string to the options to be passed to the target service for that objectType.", alias="objectOptions")
    __properties: ClassVar[List[str]] = ["includeTypes", "objectOptions"]

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
        """Create an instance of ScheduledActionPayloadContentBackupOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in object_options (dict)
        _field_dict = {}
        if self.object_options:
            for _key_object_options in self.object_options:
                if self.object_options[_key_object_options]:
                    _field_dict[_key_object_options] = self.object_options[_key_object_options].to_dict()
            _dict['objectOptions'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScheduledActionPayloadContentBackupOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "includeTypes": obj.get("includeTypes"),
            "objectOptions": dict(
                (_k, ScheduledActionResponseContentBackupOptionsObjectOptionsValue.from_dict(_v))
                for _k, _v in obj["objectOptions"].items()
            )
            if obj.get("objectOptions") is not None
            else None
        })
        return _obj



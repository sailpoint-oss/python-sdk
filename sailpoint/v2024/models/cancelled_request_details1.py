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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.v2024.models.owner_dto import OwnerDto
from typing import Optional, Set
from typing_extensions import Self

class CancelledRequestDetails1(BaseModel):
    """
    Provides additional details for a request that has been cancelled.
    """ # noqa: E501
    comment: Optional[StrictStr] = Field(default=None, description="Comment made by the owner when cancelling the associated request.")
    owner: Optional[OwnerDto] = None
    modified: Optional[datetime] = Field(default=None, description="Date comment was added by the owner when cancelling the associated request.")
    __properties: ClassVar[List[str]] = ["comment", "owner", "modified"]

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
        """Create an instance of CancelledRequestDetails1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CancelledRequestDetails1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "comment": obj.get("comment"),
            "owner": OwnerDto.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "modified": obj.get("modified")
        })
        return _obj


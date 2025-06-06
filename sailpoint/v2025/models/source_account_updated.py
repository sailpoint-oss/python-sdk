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
from typing import Optional, Set
from typing_extensions import Self

class SourceAccountUpdated(BaseModel):
    """
    SourceAccountUpdated
    """ # noqa: E501
    uuid: Optional[StrictStr] = Field(default=None, description="Source unique identifier for the identity. UUID is generated by the source system.")
    id: StrictStr = Field(description="SailPoint generated unique identifier.")
    native_identifier: StrictStr = Field(description="Unique ID of the account on the source.", alias="nativeIdentifier")
    source_id: StrictStr = Field(description="The ID of the source.", alias="sourceId")
    source_name: StrictStr = Field(description="The name of the source.", alias="sourceName")
    identity_id: StrictStr = Field(description="The ID of the identity that is correlated with this account.", alias="identityId")
    identity_name: StrictStr = Field(description="The name of the identity that is correlated with this account.", alias="identityName")
    attributes: Dict[str, Any] = Field(description="The attributes of the account. The contents of attributes depends on the account schema for the source.")
    __properties: ClassVar[List[str]] = ["uuid", "id", "nativeIdentifier", "sourceId", "sourceName", "identityId", "identityName", "attributes"]

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
        """Create an instance of SourceAccountUpdated from a JSON string"""
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
        """Create an instance of SourceAccountUpdated from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "id": obj.get("id"),
            "nativeIdentifier": obj.get("nativeIdentifier"),
            "sourceId": obj.get("sourceId"),
            "sourceName": obj.get("sourceName"),
            "identityId": obj.get("identityId"),
            "identityName": obj.get("identityName"),
            "attributes": obj.get("attributes")
        })
        return _obj



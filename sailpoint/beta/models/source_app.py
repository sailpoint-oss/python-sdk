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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.beta.models.base_reference_dto1 import BaseReferenceDto1
from sailpoint.beta.models.source_app_account_source import SourceAppAccountSource
from typing import Optional, Set
from typing_extensions import Self

class SourceApp(BaseModel):
    """
    SourceApp
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The source app id")
    cloud_app_id: Optional[StrictStr] = Field(default=None, description="The deprecated source app id", alias="cloudAppId")
    name: Optional[StrictStr] = Field(default=None, description="The source app name")
    created: Optional[datetime] = Field(default=None, description="Time when the source app was created")
    modified: Optional[datetime] = Field(default=None, description="Time when the source app was last modified")
    enabled: Optional[StrictBool] = Field(default=False, description="True if the source app is enabled")
    provision_request_enabled: Optional[StrictBool] = Field(default=False, description="True if the source app is provision request enabled", alias="provisionRequestEnabled")
    description: Optional[StrictStr] = Field(default=None, description="The description of the source app")
    match_all_accounts: Optional[StrictBool] = Field(default=False, description="True if the source app match all accounts", alias="matchAllAccounts")
    app_center_enabled: Optional[StrictBool] = Field(default=True, description="True if the source app is shown in the app center", alias="appCenterEnabled")
    account_source: Optional[SourceAppAccountSource] = Field(default=None, alias="accountSource")
    owner: Optional[BaseReferenceDto1] = Field(default=None, description="The owner of source app")
    __properties: ClassVar[List[str]] = ["id", "cloudAppId", "name", "created", "modified", "enabled", "provisionRequestEnabled", "description", "matchAllAccounts", "appCenterEnabled", "accountSource", "owner"]

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
        """Create an instance of SourceApp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account_source
        if self.account_source:
            _dict['accountSource'] = self.account_source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # set to None if account_source (nullable) is None
        # and model_fields_set contains the field
        if self.account_source is None and "account_source" in self.model_fields_set:
            _dict['accountSource'] = None

        # set to None if owner (nullable) is None
        # and model_fields_set contains the field
        if self.owner is None and "owner" in self.model_fields_set:
            _dict['owner'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SourceApp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "cloudAppId": obj.get("cloudAppId"),
            "name": obj.get("name"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else False,
            "provisionRequestEnabled": obj.get("provisionRequestEnabled") if obj.get("provisionRequestEnabled") is not None else False,
            "description": obj.get("description"),
            "matchAllAccounts": obj.get("matchAllAccounts") if obj.get("matchAllAccounts") is not None else False,
            "appCenterEnabled": obj.get("appCenterEnabled") if obj.get("appCenterEnabled") is not None else True,
            "accountSource": SourceAppAccountSource.from_dict(obj["accountSource"]) if obj.get("accountSource") is not None else None,
            "owner": BaseReferenceDto1.from_dict(obj["owner"]) if obj.get("owner") is not None else None
        })
        return _obj


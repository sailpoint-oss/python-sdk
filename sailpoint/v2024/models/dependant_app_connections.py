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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.v2024.models.base_reference_dto import BaseReferenceDto
from sailpoint.v2024.models.dependant_app_connections_account_source import DependantAppConnectionsAccountSource
from typing import Optional, Set
from typing_extensions import Self

class DependantAppConnections(BaseModel):
    """
    DependantAppConnections
    """ # noqa: E501
    cloud_app_id: Optional[StrictStr] = Field(default=None, description="Id of the connected Application", alias="cloudAppId")
    description: Optional[StrictStr] = Field(default=None, description="Description of the connected Application")
    enabled: Optional[StrictBool] = Field(default=True, description="Is the Application enabled")
    provision_request_enabled: Optional[StrictBool] = Field(default=True, description="Is Provisioning enabled for connected Application", alias="provisionRequestEnabled")
    account_source: Optional[DependantAppConnectionsAccountSource] = Field(default=None, alias="accountSource")
    launcher_count: Optional[StrictInt] = Field(default=None, description="The amount of launchers for connected Application (long type)", alias="launcherCount")
    match_all_account: Optional[StrictBool] = Field(default=False, description="Is Provisioning enabled for connected Application", alias="matchAllAccount")
    owner: Optional[List[BaseReferenceDto]] = Field(default=None, description="The owner of the connected Application")
    app_center_enabled: Optional[StrictBool] = Field(default=False, description="Is App Center enabled for connected Application", alias="appCenterEnabled")
    __properties: ClassVar[List[str]] = ["cloudAppId", "description", "enabled", "provisionRequestEnabled", "accountSource", "launcherCount", "matchAllAccount", "owner", "appCenterEnabled"]

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
        """Create an instance of DependantAppConnections from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in owner (list)
        _items = []
        if self.owner:
            for _item_owner in self.owner:
                if _item_owner:
                    _items.append(_item_owner.to_dict())
            _dict['owner'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DependantAppConnections from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloudAppId": obj.get("cloudAppId"),
            "description": obj.get("description"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "provisionRequestEnabled": obj.get("provisionRequestEnabled") if obj.get("provisionRequestEnabled") is not None else True,
            "accountSource": DependantAppConnectionsAccountSource.from_dict(obj["accountSource"]) if obj.get("accountSource") is not None else None,
            "launcherCount": obj.get("launcherCount"),
            "matchAllAccount": obj.get("matchAllAccount") if obj.get("matchAllAccount") is not None else False,
            "owner": [BaseReferenceDto.from_dict(_item) for _item in obj["owner"]] if obj.get("owner") is not None else None,
            "appCenterEnabled": obj.get("appCenterEnabled") if obj.get("appCenterEnabled") is not None else False
        })
        return _obj



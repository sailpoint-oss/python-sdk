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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.beta.models.multi_host_integrations_connector_attributes_connector_file_upload_history import MultiHostIntegrationsConnectorAttributesConnectorFileUploadHistory
from sailpoint.beta.models.multi_host_integrations_connector_attributes_multi_host_attributes import MultiHostIntegrationsConnectorAttributesMultiHostAttributes
from typing import Optional, Set
from typing_extensions import Self

class MultiHostIntegrationsConnectorAttributes(BaseModel):
    """
    Connector specific configuration. This configuration will differ for Multi-Host Integration type.
    """ # noqa: E501
    max_allowed_sources: Optional[StrictInt] = Field(default=None, description="Maximum sources allowed count of a Multi-Host Integration", alias="maxAllowedSources")
    last_source_upload_count: Optional[StrictInt] = Field(default=None, description="Last upload sources count of a Multi-Host Integration", alias="lastSourceUploadCount")
    connector_file_upload_history: Optional[MultiHostIntegrationsConnectorAttributesConnectorFileUploadHistory] = Field(default=None, alias="connectorFileUploadHistory")
    multihost_status: Optional[StrictStr] = Field(default=None, description="Multi-Host integration status.")
    show_account_schema: Optional[StrictBool] = Field(default=True, description="Show account schema", alias="showAccountSchema")
    show_entitlement_schema: Optional[StrictBool] = Field(default=True, description="Show entitlement schema", alias="showEntitlementSchema")
    multi_host_attributes: Optional[MultiHostIntegrationsConnectorAttributesMultiHostAttributes] = Field(default=None, alias="multiHostAttributes")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["maxAllowedSources", "lastSourceUploadCount", "connectorFileUploadHistory", "multihost_status", "showAccountSchema", "showEntitlementSchema", "multiHostAttributes"]

    @field_validator('multihost_status')
    def multihost_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ready', 'processing', 'fileUploadInProgress', 'sourceCreationInProgress', 'aggregationGroupingInProgress', 'aggregationScheduleInProgress', 'deleteInProgress', 'deleteFailed']):
            raise ValueError("must be one of enum values ('ready', 'processing', 'fileUploadInProgress', 'sourceCreationInProgress', 'aggregationGroupingInProgress', 'aggregationScheduleInProgress', 'deleteInProgress', 'deleteFailed')")
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
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MultiHostIntegrationsConnectorAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of connector_file_upload_history
        if self.connector_file_upload_history:
            _dict['connectorFileUploadHistory'] = self.connector_file_upload_history.to_dict()
        # override the default output from pydantic by calling `to_dict()` of multi_host_attributes
        if self.multi_host_attributes:
            _dict['multiHostAttributes'] = self.multi_host_attributes.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MultiHostIntegrationsConnectorAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maxAllowedSources": obj.get("maxAllowedSources"),
            "lastSourceUploadCount": obj.get("lastSourceUploadCount"),
            "connectorFileUploadHistory": MultiHostIntegrationsConnectorAttributesConnectorFileUploadHistory.from_dict(obj["connectorFileUploadHistory"]) if obj.get("connectorFileUploadHistory") is not None else None,
            "multihost_status": obj.get("multihost_status"),
            "showAccountSchema": obj.get("showAccountSchema") if obj.get("showAccountSchema") is not None else True,
            "showEntitlementSchema": obj.get("showEntitlementSchema") if obj.get("showEntitlementSchema") is not None else True,
            "multiHostAttributes": MultiHostIntegrationsConnectorAttributesMultiHostAttributes.from_dict(obj["multiHostAttributes"]) if obj.get("multiHostAttributes") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


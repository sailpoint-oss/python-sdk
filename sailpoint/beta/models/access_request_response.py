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
import warnings

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.beta.models.access_request_tracking import AccessRequestTracking
from typing import Optional, Set
from typing_extensions import Self

class AccessRequestResponse(BaseModel):
    """
    AccessRequestResponse
    """ # noqa: E501
    new_requests: Optional[List[AccessRequestTracking]] = Field(default=None, description="A list of new access request tracking data mapped to the values requested.", alias="newRequests")
    existing_requests: Optional[List[AccessRequestTracking]] = Field(default=None, description="A list of existing access request tracking data mapped to the values requested.  This indicates access has already been requested for this item.", alias="existingRequests")
    __properties: ClassVar[List[str]] = ["newRequests", "existingRequests"]

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
        """Create an instance of AccessRequestResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in new_requests (list)
        _items = []
        if self.new_requests:
            for _item_new_requests in self.new_requests:
                if _item_new_requests:
                    _items.append(_item_new_requests.to_dict())
            _dict['newRequests'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in existing_requests (list)
        _items = []
        if self.existing_requests:
            for _item_existing_requests in self.existing_requests:
                if _item_existing_requests:
                    _items.append(_item_existing_requests.to_dict())
            _dict['existingRequests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessRequestResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "newRequests": [AccessRequestTracking.from_dict(_item) for _item in obj["newRequests"]] if obj.get("newRequests") is not None else None,
            "existingRequests": [AccessRequestTracking.from_dict(_item) for _item in obj["existingRequests"]] if obj.get("existingRequests") is not None else None
        })
        return _obj



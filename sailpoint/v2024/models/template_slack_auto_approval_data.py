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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TemplateSlackAutoApprovalData(BaseModel):
    """
    TemplateSlackAutoApprovalData
    """ # noqa: E501
    is_auto_approved: Optional[StrictStr] = Field(default=None, alias="isAutoApproved")
    item_id: Optional[StrictStr] = Field(default=None, alias="itemId")
    item_type: Optional[StrictStr] = Field(default=None, alias="itemType")
    auto_approval_message_json: Optional[StrictStr] = Field(default=None, alias="autoApprovalMessageJSON")
    auto_approval_title: Optional[StrictStr] = Field(default=None, alias="autoApprovalTitle")
    __properties: ClassVar[List[str]] = ["isAutoApproved", "itemId", "itemType", "autoApprovalMessageJSON", "autoApprovalTitle"]

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
        """Create an instance of TemplateSlackAutoApprovalData from a JSON string"""
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
        # set to None if is_auto_approved (nullable) is None
        # and model_fields_set contains the field
        if self.is_auto_approved is None and "is_auto_approved" in self.model_fields_set:
            _dict['isAutoApproved'] = None

        # set to None if item_id (nullable) is None
        # and model_fields_set contains the field
        if self.item_id is None and "item_id" in self.model_fields_set:
            _dict['itemId'] = None

        # set to None if item_type (nullable) is None
        # and model_fields_set contains the field
        if self.item_type is None and "item_type" in self.model_fields_set:
            _dict['itemType'] = None

        # set to None if auto_approval_message_json (nullable) is None
        # and model_fields_set contains the field
        if self.auto_approval_message_json is None and "auto_approval_message_json" in self.model_fields_set:
            _dict['autoApprovalMessageJSON'] = None

        # set to None if auto_approval_title (nullable) is None
        # and model_fields_set contains the field
        if self.auto_approval_title is None and "auto_approval_title" in self.model_fields_set:
            _dict['autoApprovalTitle'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TemplateSlackAutoApprovalData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isAutoApproved": obj.get("isAutoApproved"),
            "itemId": obj.get("itemId"),
            "itemType": obj.get("itemType"),
            "autoApprovalMessageJSON": obj.get("autoApprovalMessageJSON"),
            "autoApprovalTitle": obj.get("autoApprovalTitle")
        })
        return _obj


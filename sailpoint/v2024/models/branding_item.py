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

class BrandingItem(BaseModel):
    """
    BrandingItem
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="name of branding item")
    product_name: Optional[StrictStr] = Field(default=None, description="product name", alias="productName")
    action_button_color: Optional[StrictStr] = Field(default=None, description="hex value of color for action button", alias="actionButtonColor")
    active_link_color: Optional[StrictStr] = Field(default=None, description="hex value of color for link", alias="activeLinkColor")
    navigation_color: Optional[StrictStr] = Field(default=None, description="hex value of color for navigation bar", alias="navigationColor")
    email_from_address: Optional[StrictStr] = Field(default=None, description="email from address", alias="emailFromAddress")
    standard_logo_url: Optional[StrictStr] = Field(default=None, description="url to standard logo", alias="standardLogoURL")
    login_informational_message: Optional[StrictStr] = Field(default=None, description="login information message", alias="loginInformationalMessage")
    __properties: ClassVar[List[str]] = ["name", "productName", "actionButtonColor", "activeLinkColor", "navigationColor", "emailFromAddress", "standardLogoURL", "loginInformationalMessage"]

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
        """Create an instance of BrandingItem from a JSON string"""
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
        # set to None if product_name (nullable) is None
        # and model_fields_set contains the field
        if self.product_name is None and "product_name" in self.model_fields_set:
            _dict['productName'] = None

        # set to None if action_button_color (nullable) is None
        # and model_fields_set contains the field
        if self.action_button_color is None and "action_button_color" in self.model_fields_set:
            _dict['actionButtonColor'] = None

        # set to None if active_link_color (nullable) is None
        # and model_fields_set contains the field
        if self.active_link_color is None and "active_link_color" in self.model_fields_set:
            _dict['activeLinkColor'] = None

        # set to None if navigation_color (nullable) is None
        # and model_fields_set contains the field
        if self.navigation_color is None and "navigation_color" in self.model_fields_set:
            _dict['navigationColor'] = None

        # set to None if email_from_address (nullable) is None
        # and model_fields_set contains the field
        if self.email_from_address is None and "email_from_address" in self.model_fields_set:
            _dict['emailFromAddress'] = None

        # set to None if standard_logo_url (nullable) is None
        # and model_fields_set contains the field
        if self.standard_logo_url is None and "standard_logo_url" in self.model_fields_set:
            _dict['standardLogoURL'] = None

        # set to None if login_informational_message (nullable) is None
        # and model_fields_set contains the field
        if self.login_informational_message is None and "login_informational_message" in self.model_fields_set:
            _dict['loginInformationalMessage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BrandingItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "productName": obj.get("productName"),
            "actionButtonColor": obj.get("actionButtonColor"),
            "activeLinkColor": obj.get("activeLinkColor"),
            "navigationColor": obj.get("navigationColor"),
            "emailFromAddress": obj.get("emailFromAddress"),
            "standardLogoURL": obj.get("standardLogoURL"),
            "loginInformationalMessage": obj.get("loginInformationalMessage")
        })
        return _obj


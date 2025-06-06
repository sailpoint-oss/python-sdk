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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from sailpoint.v2025.models.feature_value_dto import FeatureValueDto
from sailpoint.v2025.models.recommender_calculations_identity_attributes_value import RecommenderCalculationsIdentityAttributesValue
from typing import Optional, Set
from typing_extensions import Self

class RecommenderCalculations(BaseModel):
    """
    RecommenderCalculations
    """ # noqa: E501
    identity_id: Optional[StrictStr] = Field(default=None, description="The ID of the identity", alias="identityId")
    entitlement_id: Optional[StrictStr] = Field(default=None, description="The entitlement ID", alias="entitlementId")
    recommendation: Optional[StrictStr] = Field(default=None, description="The actual recommendation")
    overall_weighted_score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The overall weighted score", alias="overallWeightedScore")
    feature_weighted_scores: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="The weighted score of each individual feature", alias="featureWeightedScores")
    threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The configured value against which the overallWeightedScore is compared")
    identity_attributes: Optional[Dict[str, RecommenderCalculationsIdentityAttributesValue]] = Field(default=None, description="The values for your configured features", alias="identityAttributes")
    feature_values: Optional[FeatureValueDto] = Field(default=None, alias="featureValues")
    __properties: ClassVar[List[str]] = ["identityId", "entitlementId", "recommendation", "overallWeightedScore", "featureWeightedScores", "threshold", "identityAttributes", "featureValues"]

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
        """Create an instance of RecommenderCalculations from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in identity_attributes (dict)
        _field_dict = {}
        if self.identity_attributes:
            for _key_identity_attributes in self.identity_attributes:
                if self.identity_attributes[_key_identity_attributes]:
                    _field_dict[_key_identity_attributes] = self.identity_attributes[_key_identity_attributes].to_dict()
            _dict['identityAttributes'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of feature_values
        if self.feature_values:
            _dict['featureValues'] = self.feature_values.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecommenderCalculations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identityId": obj.get("identityId"),
            "entitlementId": obj.get("entitlementId"),
            "recommendation": obj.get("recommendation"),
            "overallWeightedScore": obj.get("overallWeightedScore"),
            "featureWeightedScores": obj.get("featureWeightedScores"),
            "threshold": obj.get("threshold"),
            "identityAttributes": dict(
                (_k, RecommenderCalculationsIdentityAttributesValue.from_dict(_v))
                for _k, _v in obj["identityAttributes"].items()
            )
            if obj.get("identityAttributes") is not None
            else None,
            "featureValues": FeatureValueDto.from_dict(obj["featureValues"]) if obj.get("featureValues") is not None else None
        })
        return _obj



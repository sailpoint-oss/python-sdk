# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ConnectedObjectType(str, Enum):
    """
    An enumeration of the types of Objects associated with a Governance Group. Supported object types are ACCESS_PROFILE, ROLE, SOD_POLICY and SOURCE.
    """

    """
    allowed enum values
    """
    ACCESS_PROFILE = 'ACCESS_PROFILE'
    ROLE = 'ROLE'
    SOD_POLICY = 'SOD_POLICY'
    SOURCE = 'SOURCE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConnectedObjectType from a JSON string"""
        return cls(json.loads(json_str))



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


class RequestedItemStatusRequestState(str, Enum):
    """
    Indicates the state of an access request: * EXECUTING: The request is executing, which indicates the system is doing some processing. * REQUEST_COMPLETED: Indicates the request  has been completed. * CANCELLED: The request was cancelled with no user input. * TERMINATED: The request has been terminated before it was able to complete. * PROVISIONING_VERIFICATION_PENDING: The request has finished any approval steps and provisioning is waiting to be verified. * REJECTED: The request was rejected. * PROVISIONING_FAILED: The request has failed to complete. * NOT_ALL_ITEMS_PROVISIONED: One or more of the requested items failed to complete, but there were one or more  successes. * ERROR: An error occurred during request processing.
    """

    """
    allowed enum values
    """
    EXECUTING = 'EXECUTING'
    REQUEST_COMPLETED = 'REQUEST_COMPLETED'
    CANCELLED = 'CANCELLED'
    TERMINATED = 'TERMINATED'
    PROVISIONING_VERIFICATION_PENDING = 'PROVISIONING_VERIFICATION_PENDING'
    REJECTED = 'REJECTED'
    PROVISIONING_FAILED = 'PROVISIONING_FAILED'
    NOT_ALL_ITEMS_PROVISIONED = 'NOT_ALL_ITEMS_PROVISIONED'
    ERROR = 'ERROR'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RequestedItemStatusRequestState from a JSON string"""
        return cls(json.loads(json_str))



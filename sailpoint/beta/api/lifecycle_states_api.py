# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing import List
from typing_extensions import Annotated
from sailpoint.beta.models.json_patch_operation import JsonPatchOperation
from sailpoint.beta.models.lifecycle_state import LifecycleState

from sailpoint.beta.api_client import ApiClient, RequestSerialized
from sailpoint.beta.api_response import ApiResponse
from sailpoint.beta.rest import RESTResponseType


class LifecycleStatesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_lifecycle_states(
        self,
        identity_profile_id: Annotated[StrictStr, Field(description="Identity Profile ID.")],
        lifecycle_state_id: Annotated[StrictStr, Field(description="Lifecycle State ID.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> LifecycleState:
        """Get lifecycle state

        Use this endpoint to get a lifecycle state by its ID and its associated identity profile ID.   A token with ORG_ADMIN or API authority is required to call this API. 

        :param identity_profile_id: Identity Profile ID. (required)
        :type identity_profile_id: str
        :param lifecycle_state_id: Lifecycle State ID. (required)
        :type lifecycle_state_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_lifecycle_states_serialize(
            identity_profile_id=identity_profile_id,
            lifecycle_state_id=lifecycle_state_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "LifecycleState",
            '400': "ErrorResponseDto",
            '401': "ListAccessModelMetadataAttribute401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessModelMetadataAttribute429Response",
            '500': "ErrorResponseDto",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_lifecycle_states_with_http_info(
        self,
        identity_profile_id: Annotated[StrictStr, Field(description="Identity Profile ID.")],
        lifecycle_state_id: Annotated[StrictStr, Field(description="Lifecycle State ID.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[LifecycleState]:
        """Get lifecycle state

        Use this endpoint to get a lifecycle state by its ID and its associated identity profile ID.   A token with ORG_ADMIN or API authority is required to call this API. 

        :param identity_profile_id: Identity Profile ID. (required)
        :type identity_profile_id: str
        :param lifecycle_state_id: Lifecycle State ID. (required)
        :type lifecycle_state_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_lifecycle_states_serialize(
            identity_profile_id=identity_profile_id,
            lifecycle_state_id=lifecycle_state_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "LifecycleState",
            '400': "ErrorResponseDto",
            '401': "ListAccessModelMetadataAttribute401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessModelMetadataAttribute429Response",
            '500': "ErrorResponseDto",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_lifecycle_states_without_preload_content(
        self,
        identity_profile_id: Annotated[StrictStr, Field(description="Identity Profile ID.")],
        lifecycle_state_id: Annotated[StrictStr, Field(description="Lifecycle State ID.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get lifecycle state

        Use this endpoint to get a lifecycle state by its ID and its associated identity profile ID.   A token with ORG_ADMIN or API authority is required to call this API. 

        :param identity_profile_id: Identity Profile ID. (required)
        :type identity_profile_id: str
        :param lifecycle_state_id: Lifecycle State ID. (required)
        :type lifecycle_state_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_lifecycle_states_serialize(
            identity_profile_id=identity_profile_id,
            lifecycle_state_id=lifecycle_state_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "LifecycleState",
            '400': "ErrorResponseDto",
            '401': "ListAccessModelMetadataAttribute401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessModelMetadataAttribute429Response",
            '500': "ErrorResponseDto",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_lifecycle_states_serialize(
        self,
        identity_profile_id,
        lifecycle_state_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if identity_profile_id is not None:
            _path_params['identity-profile-id'] = identity_profile_id
        if lifecycle_state_id is not None:
            _path_params['lifecycle-state-id'] = lifecycle_state_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept( _query_params,
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'userAuth', 
            'userAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/identity-profiles/{identity-profile-id}/lifecycle-states/{lifecycle-state-id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def update_lifecycle_states(
        self,
        identity_profile_id: Annotated[StrictStr, Field(description="Identity Profile ID.")],
        lifecycle_state_id: Annotated[StrictStr, Field(description="Lifecycle State ID.")],
        json_patch_operation: Annotated[List[JsonPatchOperation], Field(description="A list of lifecycle state update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields can be updated: * enabled * description * accountActions * accessProfileIds * emailNotificationOption ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> LifecycleState:
        """Update lifecycle state

        Use this endpoint to update individual lifecycle state fields, using the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  A token with ORG_ADMIN or API authority is required to call this API. 

        :param identity_profile_id: Identity Profile ID. (required)
        :type identity_profile_id: str
        :param lifecycle_state_id: Lifecycle State ID. (required)
        :type lifecycle_state_id: str
        :param json_patch_operation: A list of lifecycle state update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields can be updated: * enabled * description * accountActions * accessProfileIds * emailNotificationOption  (required)
        :type json_patch_operation: List[JsonPatchOperation]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._update_lifecycle_states_serialize(
            identity_profile_id=identity_profile_id,
            lifecycle_state_id=lifecycle_state_id,
            json_patch_operation=json_patch_operation,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "LifecycleState",
            '400': "ErrorResponseDto",
            '401': "ListAccessModelMetadataAttribute401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessModelMetadataAttribute429Response",
            '500': "ErrorResponseDto",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def update_lifecycle_states_with_http_info(
        self,
        identity_profile_id: Annotated[StrictStr, Field(description="Identity Profile ID.")],
        lifecycle_state_id: Annotated[StrictStr, Field(description="Lifecycle State ID.")],
        json_patch_operation: Annotated[List[JsonPatchOperation], Field(description="A list of lifecycle state update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields can be updated: * enabled * description * accountActions * accessProfileIds * emailNotificationOption ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[LifecycleState]:
        """Update lifecycle state

        Use this endpoint to update individual lifecycle state fields, using the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  A token with ORG_ADMIN or API authority is required to call this API. 

        :param identity_profile_id: Identity Profile ID. (required)
        :type identity_profile_id: str
        :param lifecycle_state_id: Lifecycle State ID. (required)
        :type lifecycle_state_id: str
        :param json_patch_operation: A list of lifecycle state update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields can be updated: * enabled * description * accountActions * accessProfileIds * emailNotificationOption  (required)
        :type json_patch_operation: List[JsonPatchOperation]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._update_lifecycle_states_serialize(
            identity_profile_id=identity_profile_id,
            lifecycle_state_id=lifecycle_state_id,
            json_patch_operation=json_patch_operation,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "LifecycleState",
            '400': "ErrorResponseDto",
            '401': "ListAccessModelMetadataAttribute401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessModelMetadataAttribute429Response",
            '500': "ErrorResponseDto",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def update_lifecycle_states_without_preload_content(
        self,
        identity_profile_id: Annotated[StrictStr, Field(description="Identity Profile ID.")],
        lifecycle_state_id: Annotated[StrictStr, Field(description="Lifecycle State ID.")],
        json_patch_operation: Annotated[List[JsonPatchOperation], Field(description="A list of lifecycle state update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields can be updated: * enabled * description * accountActions * accessProfileIds * emailNotificationOption ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update lifecycle state

        Use this endpoint to update individual lifecycle state fields, using the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  A token with ORG_ADMIN or API authority is required to call this API. 

        :param identity_profile_id: Identity Profile ID. (required)
        :type identity_profile_id: str
        :param lifecycle_state_id: Lifecycle State ID. (required)
        :type lifecycle_state_id: str
        :param json_patch_operation: A list of lifecycle state update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields can be updated: * enabled * description * accountActions * accessProfileIds * emailNotificationOption  (required)
        :type json_patch_operation: List[JsonPatchOperation]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._update_lifecycle_states_serialize(
            identity_profile_id=identity_profile_id,
            lifecycle_state_id=lifecycle_state_id,
            json_patch_operation=json_patch_operation,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "LifecycleState",
            '400': "ErrorResponseDto",
            '401': "ListAccessModelMetadataAttribute401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessModelMetadataAttribute429Response",
            '500': "ErrorResponseDto",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _update_lifecycle_states_serialize(
        self,
        identity_profile_id,
        lifecycle_state_id,
        json_patch_operation,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'JsonPatchOperation': '',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if identity_profile_id is not None:
            _path_params['identity-profile-id'] = identity_profile_id
        if lifecycle_state_id is not None:
            _path_params['lifecycle-state-id'] = lifecycle_state_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if json_patch_operation is not None:
            _body_params = json_patch_operation


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept( _query_params,
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json-patch+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'userAuth', 
            'userAuth'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/identity-profiles/{identity-profile-id}/lifecycle-states/{lifecycle-state-id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )



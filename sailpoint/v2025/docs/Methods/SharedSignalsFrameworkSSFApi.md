---
id: v2025-shared-signals-framework--ssf
title: Shared_Signals_Framework__SSF
pagination_label: Shared_Signals_Framework__SSF
sidebar_label: Shared_Signals_Framework__SSF
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Shared_Signals_Framework__SSF', 'V2025Shared_Signals_Framework__SSF'] 
slug: /tools/sdk/python/v2025/methods/shared-signals-framework--ssf
tags: ['SDK', 'Software Development Kit', 'Shared_Signals_Framework__SSF', 'V2025Shared_Signals_Framework__SSF']
---

# sailpoint.v2025.SharedSignalsFrameworkSSFApi
  The SSF Transmitter Service is a security event notification system that monitors identity attribute changes
and automatically triggers session revocation events when specific lifecycle conditions are met.

Use this API to implement transmitter functionality so administrators can discover the transmitter and manage streams.
Transmitters send identity data and events from Identity Security Cloud to external receivers over the Secure Sync Framework (SSF).
The SSF configuration and JWKS endpoints support discovery and verification; the stream management endpoints support creating, updating, and managing streams and verifying receivers.
In Identity Security Cloud, administrators can use the &quot;Connections&quot; &gt; &quot;Shared Signals&quot; area to view and manage transmitters and their streams.
 
All URIs are relative to *https://sailpoint.api.identitynow.com/v2025*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-stream**](#create-stream) | **POST** `/ssf/streams` | Create stream
[**delete-stream**](#delete-stream) | **DELETE** `/ssf/streams` | Delete stream
[**get-jwks-data**](#get-jwks-data) | **GET** `/ssf/jwks` | Get JWKS
[**get-ssf-configuration**](#get-ssf-configuration) | **GET** `/.well-known/ssf-configuration` | Get SSF configuration
[**get-stream**](#get-stream) | **GET** `/ssf/streams` | Get stream(s)
[**get-stream-status**](#get-stream-status) | **GET** `/ssf/streams/status` | Get stream status
[**send-stream-verification**](#send-stream-verification) | **POST** `/ssf/streams/verify` | Verify stream
[**set-stream-configuration**](#set-stream-configuration) | **PUT** `/ssf/streams` | Replace stream configuration
[**update-stream-configuration**](#update-stream-configuration) | **PATCH** `/ssf/streams` | Update stream configuration
[**update-stream-status**](#update-stream-status) | **POST** `/ssf/streams/status` | Update stream status


## create-stream
Create stream
An SSF stream is associated with the client ID of the OAuth 2.0 access token used to create the stream.
One SSF stream is allowed for each client ID.

You can create a maximum of 10 SSF stream configurations for one org.


[API Spec](https://developer.sailpoint.com/docs/api/v2025/create-stream)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_stream_request | [**CreateStreamRequest**](../models/create-stream-request) | True  | 

### Return type
[**StreamConfigResponse**](../models/stream-config-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
201 | Stream created. | StreamConfigResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.shared_signals_framework_ssf_api import SharedSignalsFrameworkSSFApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.create_stream_request import CreateStreamRequest
from sailpoint.v2025.models.stream_config_response import StreamConfigResponse
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_stream_request = '''{
          "delivery" : {
            "method" : "urn:ietf:rfc:8935",
            "endpoint_url" : "https://receiver.example.com/ssf/events",
            "authorization_header" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
          },
          "description" : "Production event stream",
          "events_requested" : [ "https://schemas.openid.net/secevent/caep/event-type/session-revoked" ]
        }''' # CreateStreamRequest | 

    try:
        # Create stream
        new_create_stream_request = CreateStreamRequest.from_json(create_stream_request)
        results = SharedSignalsFrameworkSSFApi(api_client).create_stream(create_stream_request=new_create_stream_request)
        # Below is a request that includes all optional parameters
        # results = SharedSignalsFrameworkSSFApi(api_client).create_stream(new_create_stream_request)
        print("The response of SharedSignalsFrameworkSSFApi->create_stream:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling SharedSignalsFrameworkSSFApi->create_stream: %s\n" % e)
```



[[Back to top]](#) 

## delete-stream
Delete stream
Deletes a stream by its ID. There is no request body; the stream is identified by the required
query parameter `stream_id`. On success the response has no body (204 No Content).

The associated stream with the client ID (through the request OAuth 2.0 access token) is deleted.


[API Spec](https://developer.sailpoint.com/docs/api/v2025/delete-stream)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | stream_id | **str** | True  | ID of the stream to delete. Required; omitted or empty returns 400.

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No content - indicates the request was successful but there is no content to be returned in the response. |  |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.shared_signals_framework_ssf_api import SharedSignalsFrameworkSSFApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    stream_id = '550e8400-e29b-41d4-a716-446655440000' # str | ID of the stream to delete. Required; omitted or empty returns 400. # str | ID of the stream to delete. Required; omitted or empty returns 400.

    try:
        # Delete stream
        
        SharedSignalsFrameworkSSFApi(api_client).delete_stream(stream_id=stream_id)
        # Below is a request that includes all optional parameters
        # SharedSignalsFrameworkSSFApi(api_client).delete_stream(stream_id)
    except Exception as e:
        print("Exception when calling SharedSignalsFrameworkSSFApi->delete_stream: %s\n" % e)
```



[[Back to top]](#) 

## get-jwks-data
Get JWKS
Returns the transmitter's JSON Web Key Set (JWKS) for verifying signed delivery requests.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/get-jwks-data)

### Parameters 
This endpoint does not need any parameter. 

### Return type
[**JWKS**](../models/jwks)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | JSON Web Key Set (RFC 7517) containing the transmitter&#39;s public keys. | JWKS |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.shared_signals_framework_ssf_api import SharedSignalsFrameworkSSFApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.jwks import JWKS
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:

    try:
        # Get JWKS
        
        results = SharedSignalsFrameworkSSFApi(api_client).get_jwks_data()
        # Below is a request that includes all optional parameters
        # results = SharedSignalsFrameworkSSFApi(api_client).get_jwks_data()
        print("The response of SharedSignalsFrameworkSSFApi->get_jwks_data:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling SharedSignalsFrameworkSSFApi->get_jwks_data: %s\n" % e)
```



[[Back to top]](#) 

## get-ssf-configuration
Get SSF configuration
Returns the SSF transmitter discovery metadata (well-known configuration).

[API Spec](https://developer.sailpoint.com/docs/api/v2025/get-ssf-configuration)

### Parameters 
This endpoint does not need any parameter. 

### Return type
[**TransmitterMetadata**](../models/transmitter-metadata)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | SSF transmitter configuration (issuer, jwks_uri, endpoints, authorization_schemes). | TransmitterMetadata |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.shared_signals_framework_ssf_api import SharedSignalsFrameworkSSFApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.transmitter_metadata import TransmitterMetadata
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:

    try:
        # Get SSF configuration
        
        results = SharedSignalsFrameworkSSFApi(api_client).get_ssf_configuration()
        # Below is a request that includes all optional parameters
        # results = SharedSignalsFrameworkSSFApi(api_client).get_ssf_configuration()
        print("The response of SharedSignalsFrameworkSSFApi->get_ssf_configuration:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling SharedSignalsFrameworkSSFApi->get_ssf_configuration: %s\n" % e)
```



[[Back to top]](#) 

## get-stream
Get stream(s)
Retrieves either a list of all SSF stream configurations or the individual configuration if specified by ID.

As stream configurations are tied to a client ID, you can only view the stream associated with the client ID
of the request OAuth 2.0 access token.

Query parameter `aud` (co filter) can be used to filter by audience.


[API Spec](https://developer.sailpoint.com/docs/api/v2025/get-stream)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | stream_id | **str** |   (optional) | If provided, returns that stream; otherwise returns list of all streams.

### Return type
[**GetStream200Response**](../models/get-stream200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Single stream (when stream_id is provided) or list of streams (when stream_id is omitted). | GetStream200Response |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.shared_signals_framework_ssf_api import SharedSignalsFrameworkSSFApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.get_stream200_response import GetStream200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    stream_id = '550e8400-e29b-41d4-a716-446655440000' # str | If provided, returns that stream; otherwise returns list of all streams. (optional) # str | If provided, returns that stream; otherwise returns list of all streams. (optional)

    try:
        # Get stream(s)
        
        results = SharedSignalsFrameworkSSFApi(api_client).get_stream()
        # Below is a request that includes all optional parameters
        # results = SharedSignalsFrameworkSSFApi(api_client).get_stream(stream_id)
        print("The response of SharedSignalsFrameworkSSFApi->get_stream:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling SharedSignalsFrameworkSSFApi->get_stream: %s\n" % e)
```



[[Back to top]](#) 

## get-stream-status
Get stream status
Returns the status (enabled, paused, disabled) and optional reason for the stream associated with the client ID of the request's OAuth 2.0 access token. The stream_id query parameter is required.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/get-stream-status)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | stream_id | **str** | True  | ID of the stream whose status to retrieve.

### Return type
[**StreamStatusResponse**](../models/stream-status-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Stream status (enabled, paused, or disabled; reason may be set when status was updated). | StreamStatusResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.shared_signals_framework_ssf_api import SharedSignalsFrameworkSSFApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.stream_status_response import StreamStatusResponse
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    stream_id = '550e8400-e29b-41d4-a716-446655440000' # str | ID of the stream whose status to retrieve. # str | ID of the stream whose status to retrieve.

    try:
        # Get stream status
        
        results = SharedSignalsFrameworkSSFApi(api_client).get_stream_status(stream_id=stream_id)
        # Below is a request that includes all optional parameters
        # results = SharedSignalsFrameworkSSFApi(api_client).get_stream_status(stream_id)
        print("The response of SharedSignalsFrameworkSSFApi->get_stream_status:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling SharedSignalsFrameworkSSFApi->get_stream_status: %s\n" % e)
```



[[Back to top]](#) 

## send-stream-verification
Verify stream
Verifies an SSF stream by publishing a verification event requested by a security events provider.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/send-stream-verification)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | verification_request | [**VerificationRequest**](../models/verification-request) | True  | 

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No content - indicates the request was successful but there is no content to be returned in the response. |  |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.shared_signals_framework_ssf_api import SharedSignalsFrameworkSSFApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.verification_request import VerificationRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    verification_request = '''{
          "stream_id" : "550e8400-e29b-41d4-a716-446655440000",
          "state" : "verification-challenge-state-123"
        }''' # VerificationRequest | 

    try:
        # Verify stream
        new_verification_request = VerificationRequest.from_json(verification_request)
        SharedSignalsFrameworkSSFApi(api_client).send_stream_verification(verification_request=new_verification_request)
        # Below is a request that includes all optional parameters
        # SharedSignalsFrameworkSSFApi(api_client).send_stream_verification(new_verification_request)
    except Exception as e:
        print("Exception when calling SharedSignalsFrameworkSSFApi->send_stream_verification: %s\n" % e)
```



[[Back to top]](#) 

## set-stream-configuration
Replace stream configuration
Replaces a stream's configuration (PUT). stream_id and delivery are required; full receiver-supplied properties.

The associated stream with the client ID (through the request OAuth 2.0 access token) is replaced.


[API Spec](https://developer.sailpoint.com/docs/api/v2025/set-stream-configuration)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | replace_stream_configuration_request | [**ReplaceStreamConfigurationRequest**](../models/replace-stream-configuration-request) | True  | 

### Return type
[**UpdateStreamConfigResponse**](../models/update-stream-config-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Replaced stream configuration (same JSON shape as PATCH/GET single stream). | UpdateStreamConfigResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.shared_signals_framework_ssf_api import SharedSignalsFrameworkSSFApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.replace_stream_configuration_request import ReplaceStreamConfigurationRequest
from sailpoint.v2025.models.update_stream_config_response import UpdateStreamConfigResponse
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    replace_stream_configuration_request = '''{
          "delivery" : {
            "method" : "urn:ietf:rfc:8935",
            "endpoint_url" : "https://receiver.example.com/ssf/events",
            "authorization_header" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
          },
          "stream_id" : "550e8400-e29b-41d4-a716-446655440000",
          "description" : "Production event stream",
          "events_requested" : [ "https://schemas.openid.net/secevent/caep/event-type/session-revoked" ]
        }''' # ReplaceStreamConfigurationRequest | 

    try:
        # Replace stream configuration
        new_replace_stream_configuration_request = ReplaceStreamConfigurationRequest.from_json(replace_stream_configuration_request)
        results = SharedSignalsFrameworkSSFApi(api_client).set_stream_configuration(replace_stream_configuration_request=new_replace_stream_configuration_request)
        # Below is a request that includes all optional parameters
        # results = SharedSignalsFrameworkSSFApi(api_client).set_stream_configuration(new_replace_stream_configuration_request)
        print("The response of SharedSignalsFrameworkSSFApi->set_stream_configuration:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling SharedSignalsFrameworkSSFApi->set_stream_configuration: %s\n" % e)
```



[[Back to top]](#) 

## update-stream-configuration
Update stream configuration
Partially updates a stream's configuration (PATCH). Only provided fields are updated.

The associated stream with the client ID (through the request OAuth 2.0 access token) is updated.


[API Spec](https://developer.sailpoint.com/docs/api/v2025/update-stream-configuration)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | update_stream_configuration_request | [**UpdateStreamConfigurationRequest**](../models/update-stream-configuration-request) | True  | 

### Return type
[**UpdateStreamConfigResponse**](../models/update-stream-config-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Updated stream configuration (same JSON shape as GET single stream, plus updatedAt). | UpdateStreamConfigResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.shared_signals_framework_ssf_api import SharedSignalsFrameworkSSFApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.update_stream_config_response import UpdateStreamConfigResponse
from sailpoint.v2025.models.update_stream_configuration_request import UpdateStreamConfigurationRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    update_stream_configuration_request = '''{
          "delivery" : {
            "method" : "urn:ietf:rfc:8935",
            "endpoint_url" : "https://receiver.example.com/ssf/events",
            "authorization_header" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
          },
          "stream_id" : "550e8400-e29b-41d4-a716-446655440000",
          "description" : "Updated production event stream configuration",
          "events_requested" : [ "https://schemas.openid.net/secevent/caep/event-type/session-revoked" ]
        }''' # UpdateStreamConfigurationRequest | 

    try:
        # Update stream configuration
        new_update_stream_configuration_request = UpdateStreamConfigurationRequest.from_json(update_stream_configuration_request)
        results = SharedSignalsFrameworkSSFApi(api_client).update_stream_configuration(update_stream_configuration_request=new_update_stream_configuration_request)
        # Below is a request that includes all optional parameters
        # results = SharedSignalsFrameworkSSFApi(api_client).update_stream_configuration(new_update_stream_configuration_request)
        print("The response of SharedSignalsFrameworkSSFApi->update_stream_configuration:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling SharedSignalsFrameworkSSFApi->update_stream_configuration: %s\n" % e)
```



[[Back to top]](#) 

## update-stream-status
Update stream status
Updates the operational status (enabled, paused, disabled) with an optional reason for the stream associated with the client ID of the request's OAuth 2.0 access token.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/update-stream-status)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | update_stream_status_request | [**UpdateStreamStatusRequest**](../models/update-stream-status-request) | True  | 

### Return type
[**StreamStatusResponse**](../models/stream-status-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Updated stream status (same JSON shape as GET /ssf/streams/status). | StreamStatusResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.shared_signals_framework_ssf_api import SharedSignalsFrameworkSSFApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.stream_status_response import StreamStatusResponse
from sailpoint.v2025.models.update_stream_status_request import UpdateStreamStatusRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    update_stream_status_request = '''{
          "reason" : "manually paused",
          "stream_id" : "550e8400-e29b-41d4-a716-446655440000",
          "status" : "paused"
        }''' # UpdateStreamStatusRequest | 

    try:
        # Update stream status
        new_update_stream_status_request = UpdateStreamStatusRequest.from_json(update_stream_status_request)
        results = SharedSignalsFrameworkSSFApi(api_client).update_stream_status(update_stream_status_request=new_update_stream_status_request)
        # Below is a request that includes all optional parameters
        # results = SharedSignalsFrameworkSSFApi(api_client).update_stream_status(new_update_stream_status_request)
        print("The response of SharedSignalsFrameworkSSFApi->update_stream_status:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling SharedSignalsFrameworkSSFApi->update_stream_status: %s\n" % e)
```



[[Back to top]](#) 




# sailpoint.beta.IAIRoleMiningApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_potential_role_provision_request**](IAIRoleMiningApi.md#create_potential_role_provision_request) | **POST** /role-mining-sessions/{sessionId}/potential-roles/{potentialRoleId}/provision | Create request to provision a potential role into an actual role.
[**create_role_mining_sessions**](IAIRoleMiningApi.md#create_role_mining_sessions) | **POST** /role-mining-sessions | Create a role mining session
[**download_role_mining_potential_role_zip**](IAIRoleMiningApi.md#download_role_mining_potential_role_zip) | **GET** /role-mining-sessions/{sessionId}/potential-roles/{potentialRoleId}/export-async/{exportId}/download | Export (download) details for a potential role in a role mining session
[**export_role_mining_potential_role**](IAIRoleMiningApi.md#export_role_mining_potential_role) | **GET** /role-mining-sessions/{sessionId}/potential-roles/{potentialRoleId}/export | Export (download) details for a potential role in a role mining session
[**export_role_mining_potential_role_async**](IAIRoleMiningApi.md#export_role_mining_potential_role_async) | **POST** /role-mining-sessions/{sessionId}/potential-roles/{potentialRoleId}/export-async | Asynchronously export details for a potential role in a role mining session and upload to S3
[**export_role_mining_potential_role_status**](IAIRoleMiningApi.md#export_role_mining_potential_role_status) | **GET** /role-mining-sessions/{sessionId}/potential-roles/{potentialRoleId}/export-async/{exportId} | Retrieve status of a potential role export job
[**get_all_potential_role_summaries**](IAIRoleMiningApi.md#get_all_potential_role_summaries) | **GET** /role-mining-potential-roles | Retrieves all potential role summaries
[**get_entitlement_distribution_potential_role**](IAIRoleMiningApi.md#get_entitlement_distribution_potential_role) | **GET** /role-mining-sessions/{sessionId}/potential-roles/{potentialRoleId}/entitlement-popularity-distribution | Retrieves entitlement popularity distribution for a potential role in a role mining session
[**get_entitlements_potential_role**](IAIRoleMiningApi.md#get_entitlements_potential_role) | **GET** /role-mining-sessions/{sessionId}/potential-roles/{potentialRoleId}/entitlement-popularities | Retrieves entitlements for a potential role in a role mining session
[**get_excluded_entitlements_potential_role**](IAIRoleMiningApi.md#get_excluded_entitlements_potential_role) | **GET** /role-mining-sessions/{sessionId}/potential-roles/{potentialRoleId}/excluded-entitlements | Retrieves excluded entitlements for a potential role in a role mining session
[**get_identities_potential_role**](IAIRoleMiningApi.md#get_identities_potential_role) | **GET** /role-mining-sessions/{sessionId}/potential-roles/{potentialRoleId}/identities | Retrieves identities for a potential role in a role mining session
[**get_potential_role**](IAIRoleMiningApi.md#get_potential_role) | **GET** /role-mining-sessions/{sessionId}/potential-role-summaries/{potentialRoleId} | Retrieves a specific potential role
[**get_potential_role_applications**](IAIRoleMiningApi.md#get_potential_role_applications) | **GET** /role-mining-sessions/{sessionId}/potential-role-summaries/{potentialRoleId}/applications | Retrieves the applications of a potential role for a role mining session
[**get_potential_role_source_identity_usage**](IAIRoleMiningApi.md#get_potential_role_source_identity_usage) | **GET** /role-mining-potential-roles/{potentialRoleId}/sources/{sourceId}/identityUsage | Retrieves potential role source usage
[**get_potential_role_summaries**](IAIRoleMiningApi.md#get_potential_role_summaries) | **GET** /role-mining-sessions/{sessionId}/potential-role-summaries | Retrieves all potential role summaries
[**get_role_mining_potential_role**](IAIRoleMiningApi.md#get_role_mining_potential_role) | **GET** /role-mining-potential-roles/{potentialRoleId} | Retrieves a specific potential role
[**get_role_mining_session**](IAIRoleMiningApi.md#get_role_mining_session) | **GET** /role-mining-sessions/{sessionId} | Get a role mining session
[**get_role_mining_session_status**](IAIRoleMiningApi.md#get_role_mining_session_status) | **GET** /role-mining-sessions/{sessionId}/status | Get role mining session status state
[**get_role_mining_sessions**](IAIRoleMiningApi.md#get_role_mining_sessions) | **GET** /role-mining-sessions | Retrieves all role mining sessions
[**get_saved_potential_roles**](IAIRoleMiningApi.md#get_saved_potential_roles) | **GET** /role-mining-potential-roles/saved | Retrieves all saved potential roles
[**patch_potential_role**](IAIRoleMiningApi.md#patch_potential_role) | **PATCH** /role-mining-sessions/{sessionId}/potential-role-summaries/{potentialRoleId} | Update a potential role
[**patch_potential_role_0**](IAIRoleMiningApi.md#patch_potential_role_0) | **PATCH** /role-mining-potential-roles/{potentialRoleId} | Update a potential role
[**patch_role_mining_session**](IAIRoleMiningApi.md#patch_role_mining_session) | **PATCH** /role-mining-sessions/{sessionId} | Patch a role mining session
[**update_entitlements_potential_role**](IAIRoleMiningApi.md#update_entitlements_potential_role) | **POST** /role-mining-sessions/{sessionId}/potential-roles/{potentialRoleId}/edit-entitlements | Edit entitlements for a potential role to exclude some entitlements


# **create_potential_role_provision_request**
> RoleMiningPotentialRoleSummary create_potential_role_provision_request(session_id, potential_role_id, min_entitlement_popularity=min_entitlement_popularity, include_common_access=include_common_access, role_mining_potential_role_provision_request=role_mining_potential_role_provision_request)

Create request to provision a potential role into an actual role.

This method starts a job to provision a potential role

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_potential_role_provision_request import RoleMiningPotentialRoleProvisionRequest
from sailpoint.beta.models.role_mining_potential_role_summary import RoleMiningPotentialRoleSummary
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | A potential role id in a role mining session
    min_entitlement_popularity = 0 # int | Minimum popularity required for an entitlement to be included in the provisioned role. (optional) (default to 0)
    include_common_access = True # bool | Boolean determining whether common access entitlements will be included in the provisioned role. (optional) (default to True)
    role_mining_potential_role_provision_request = sailpoint.beta.RoleMiningPotentialRoleProvisionRequest() # RoleMiningPotentialRoleProvisionRequest | Required information to create a new role (optional)

    try:
        # Create request to provision a potential role into an actual role.
        api_response = api_instance.create_potential_role_provision_request(session_id, potential_role_id, min_entitlement_popularity=min_entitlement_popularity, include_common_access=include_common_access, role_mining_potential_role_provision_request=role_mining_potential_role_provision_request)
        print("The response of IAIRoleMiningApi->create_potential_role_provision_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->create_potential_role_provision_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| A potential role id in a role mining session | 
 **min_entitlement_popularity** | **int**| Minimum popularity required for an entitlement to be included in the provisioned role. | [optional] [default to 0]
 **include_common_access** | **bool**| Boolean determining whether common access entitlements will be included in the provisioned role. | [optional] [default to True]
 **role_mining_potential_role_provision_request** | [**RoleMiningPotentialRoleProvisionRequest**](RoleMiningPotentialRoleProvisionRequest.md)| Required information to create a new role | [optional] 

### Return type

[**RoleMiningPotentialRoleSummary**](RoleMiningPotentialRoleSummary.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. Returns a potential role summary including the status of the provison request |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role_mining_sessions**
> RoleMiningSessionResponse create_role_mining_sessions(role_mining_session_dto)

Create a role mining session

This submits a create role mining session request to the role mining application.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_session_dto import RoleMiningSessionDto
from sailpoint.beta.models.role_mining_session_response import RoleMiningSessionResponse
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    role_mining_session_dto = sailpoint.beta.RoleMiningSessionDto() # RoleMiningSessionDto | Role mining session parameters

    try:
        # Create a role mining session
        api_response = api_instance.create_role_mining_sessions(role_mining_session_dto)
        print("The response of IAIRoleMiningApi->create_role_mining_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->create_role_mining_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_mining_session_dto** | [**RoleMiningSessionDto**](RoleMiningSessionDto.md)| Role mining session parameters | 

### Return type

[**RoleMiningSessionResponse**](RoleMiningSessionResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Submitted a role mining session request |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_role_mining_potential_role_zip**
> bytearray download_role_mining_potential_role_zip(session_id, potential_role_id, export_id)

Export (download) details for a potential role in a role mining session

This endpoint downloads a completed export of information for a potential role in a role mining session.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '278359a6-04b7-4669-9468-924cf580964a' # str | A potential role id in a role mining session
    export_id = '4940ffd4-836f-48a3-b2b0-6d498c3fdf40' # str | The id of a previously run export job for this potential role

    try:
        # Export (download) details for a potential role in a role mining session
        api_response = api_instance.download_role_mining_potential_role_zip(session_id, potential_role_id, export_id)
        print("The response of IAIRoleMiningApi->download_role_mining_potential_role_zip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->download_role_mining_potential_role_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| A potential role id in a role mining session | 
 **export_id** | **str**| The id of a previously run export job for this potential role | 

### Return type

**bytearray**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a zip file containing csv files for identities and entitlements for the potential role. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_role_mining_potential_role**
> bytearray export_role_mining_potential_role(session_id, potential_role_id)

Export (download) details for a potential role in a role mining session

This endpoint downloads all the information for a potential role in a role mining session. Includes identities and entitlements in the potential role.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | A potential role id in a role mining session

    try:
        # Export (download) details for a potential role in a role mining session
        api_response = api_instance.export_role_mining_potential_role(session_id, potential_role_id)
        print("The response of IAIRoleMiningApi->export_role_mining_potential_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->export_role_mining_potential_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| A potential role id in a role mining session | 

### Return type

**bytearray**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a zip file containing csv files for identities and entitlements for the potential role. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_role_mining_potential_role_async**
> RoleMiningPotentialRoleExportResponse export_role_mining_potential_role_async(session_id, potential_role_id, role_mining_potential_role_export_request=role_mining_potential_role_export_request)

Asynchronously export details for a potential role in a role mining session and upload to S3

This endpoint uploads all the information for a potential role in a role mining session to S3 as a downloadable zip archive.  Includes identities and entitlements in the potential role.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_potential_role_export_request import RoleMiningPotentialRoleExportRequest
from sailpoint.beta.models.role_mining_potential_role_export_response import RoleMiningPotentialRoleExportResponse
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '278359a6-04b7-4669-9468-924cf580964a' # str | A potential role id in a role mining session
    role_mining_potential_role_export_request = sailpoint.beta.RoleMiningPotentialRoleExportRequest() # RoleMiningPotentialRoleExportRequest |  (optional)

    try:
        # Asynchronously export details for a potential role in a role mining session and upload to S3
        api_response = api_instance.export_role_mining_potential_role_async(session_id, potential_role_id, role_mining_potential_role_export_request=role_mining_potential_role_export_request)
        print("The response of IAIRoleMiningApi->export_role_mining_potential_role_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->export_role_mining_potential_role_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| A potential role id in a role mining session | 
 **role_mining_potential_role_export_request** | [**RoleMiningPotentialRoleExportRequest**](RoleMiningPotentialRoleExportRequest.md)|  | [optional] 

### Return type

[**RoleMiningPotentialRoleExportResponse**](RoleMiningPotentialRoleExportResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Job Submitted. Returns a reportId that can be used to download the zip once complete |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_role_mining_potential_role_status**
> RoleMiningPotentialRoleExportResponse export_role_mining_potential_role_status(session_id, potential_role_id, export_id)

Retrieve status of a potential role export job

This endpoint retrieves information about the current status of a potential role export.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_potential_role_export_response import RoleMiningPotentialRoleExportResponse
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '278359a6-04b7-4669-9468-924cf580964a' # str | A potential role id in a role mining session
    export_id = '4940ffd4-836f-48a3-b2b0-6d498c3fdf40' # str | The id of a previously run export job for this potential role

    try:
        # Retrieve status of a potential role export job
        api_response = api_instance.export_role_mining_potential_role_status(session_id, potential_role_id, export_id)
        print("The response of IAIRoleMiningApi->export_role_mining_potential_role_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->export_role_mining_potential_role_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| A potential role id in a role mining session | 
 **export_id** | **str**| The id of a previously run export job for this potential role | 

### Return type

[**RoleMiningPotentialRoleExportResponse**](RoleMiningPotentialRoleExportResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns the current status of this export |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_potential_role_summaries**
> List[RoleMiningPotentialRoleSummary] get_all_potential_role_summaries(sorters=sorters, filters=filters, offset=offset, limit=limit, count=count)

Retrieves all potential role summaries

Returns all potential role summaries that match the query parameters

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_potential_role_summary import RoleMiningPotentialRoleSummary
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    sorters = 'createdDate' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **createdDate, identityCount, entitlementCount, freshness, quality** (optional)
    filters = '(createdByName co \"int\") and (createdById sw \"2c9180907\") and (type eq \"COMMON\") and ((name co \"entt\") or (saved eq true))' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **createdById**: *eq, sw, co*  **createdByName**: *eq, sw, co*  **description**: *sw, co*  **endDate**: *le, lt*  **freshness**: *eq, ge, gt, le, lt*  **name**: *eq, sw, co, ge, gt, le, lt*  **quality**: *eq, ge, gt, le, lt*  **startDate**: *ge, gt*  **saved**: *eq*  **type**: *eq, ge, gt, le, lt*  **scopingMethod**: *eq*  **sessionState**: *eq*  **identityAttribute**: *co* (optional)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Retrieves all potential role summaries
        api_response = api_instance.get_all_potential_role_summaries(sorters=sorters, filters=filters, offset=offset, limit=limit, count=count)
        print("The response of IAIRoleMiningApi->get_all_potential_role_summaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_all_potential_role_summaries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **createdDate, identityCount, entitlementCount, freshness, quality** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **createdById**: *eq, sw, co*  **createdByName**: *eq, sw, co*  **description**: *sw, co*  **endDate**: *le, lt*  **freshness**: *eq, ge, gt, le, lt*  **name**: *eq, sw, co, ge, gt, le, lt*  **quality**: *eq, ge, gt, le, lt*  **startDate**: *ge, gt*  **saved**: *eq*  **type**: *eq, ge, gt, le, lt*  **scopingMethod**: *eq*  **sessionState**: *eq*  **identityAttribute**: *co* | [optional] 
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[RoleMiningPotentialRoleSummary]**](RoleMiningPotentialRoleSummary.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns all potential role summaries that match the query parameters. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlement_distribution_potential_role**
> Dict[str, int] get_entitlement_distribution_potential_role(session_id, potential_role_id, include_common_access=include_common_access)

Retrieves entitlement popularity distribution for a potential role in a role mining session

This method returns entitlement popularity distribution for a potential role in a role mining session.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | A potential role id in a role mining session
    include_common_access = True # bool | Boolean determining whether common access entitlements will be included or not (optional)

    try:
        # Retrieves entitlement popularity distribution for a potential role in a role mining session
        api_response = api_instance.get_entitlement_distribution_potential_role(session_id, potential_role_id, include_common_access=include_common_access)
        print("The response of IAIRoleMiningApi->get_entitlement_distribution_potential_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_entitlement_distribution_potential_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| A potential role id in a role mining session | 
 **include_common_access** | **bool**| Boolean determining whether common access entitlements will be included or not | [optional] 

### Return type

**Dict[str, int]**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a map containing entitlement popularity distribution for a potential role. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlements_potential_role**
> List[RoleMiningEntitlement] get_entitlements_potential_role(session_id, potential_role_id, include_common_access=include_common_access, sorters=sorters, filters=filters, offset=offset, limit=limit, count=count)

Retrieves entitlements for a potential role in a role mining session

This method returns entitlements for a potential role in a role mining session.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_entitlement import RoleMiningEntitlement
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | A potential role id in a role mining session
    include_common_access = True # bool | Boolean determining whether common access entitlements will be included or not (optional)
    sorters = 'popularity' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **popularity**  The default sort is **popularity** in descending order.  (optional)
    filters = 'applicationName sw \"AD\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **applicationName**: *sw*  **entitlementRef.name**: *sw* (optional)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Retrieves entitlements for a potential role in a role mining session
        api_response = api_instance.get_entitlements_potential_role(session_id, potential_role_id, include_common_access=include_common_access, sorters=sorters, filters=filters, offset=offset, limit=limit, count=count)
        print("The response of IAIRoleMiningApi->get_entitlements_potential_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_entitlements_potential_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| A potential role id in a role mining session | 
 **include_common_access** | **bool**| Boolean determining whether common access entitlements will be included or not | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **popularity**  The default sort is **popularity** in descending order.  | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **applicationName**: *sw*  **entitlementRef.name**: *sw* | [optional] 
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[RoleMiningEntitlement]**](RoleMiningEntitlement.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of entitlements for a potential role. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_excluded_entitlements_potential_role**
> List[RoleMiningEntitlement] get_excluded_entitlements_potential_role(session_id, potential_role_id, sorters=sorters, filters=filters, offset=offset, limit=limit, count=count)

Retrieves excluded entitlements for a potential role in a role mining session

This method returns excluded entitlements for a potential role in a role mining session.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_entitlement import RoleMiningEntitlement
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | A potential role id in a role mining session
    sorters = 'populariity' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **popularity** (optional)
    filters = 'applicationName sw \"AD\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **applicationName**: *sw*  **entitlementRef.name**: *sw* (optional)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Retrieves excluded entitlements for a potential role in a role mining session
        api_response = api_instance.get_excluded_entitlements_potential_role(session_id, potential_role_id, sorters=sorters, filters=filters, offset=offset, limit=limit, count=count)
        print("The response of IAIRoleMiningApi->get_excluded_entitlements_potential_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_excluded_entitlements_potential_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| A potential role id in a role mining session | 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **popularity** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **applicationName**: *sw*  **entitlementRef.name**: *sw* | [optional] 
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[RoleMiningEntitlement]**](RoleMiningEntitlement.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of excluded entitlements for a potential roles. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identities_potential_role**
> List[RoleMiningIdentity] get_identities_potential_role(session_id, potential_role_id, sorters=sorters, filters=filters, offset=offset, limit=limit, count=count)

Retrieves identities for a potential role in a role mining session

This method returns identities for a potential role in a role mining session.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_identity import RoleMiningIdentity
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | A potential role id in a role mining session
    sorters = 'name' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name** (optional)
    filters = 'filters_example' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **name**: *sw* (optional)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Retrieves identities for a potential role in a role mining session
        api_response = api_instance.get_identities_potential_role(session_id, potential_role_id, sorters=sorters, filters=filters, offset=offset, limit=limit, count=count)
        print("The response of IAIRoleMiningApi->get_identities_potential_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_identities_potential_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| A potential role id in a role mining session | 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **name**: *sw* | [optional] 
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[RoleMiningIdentity]**](RoleMiningIdentity.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of identities for a potential role. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_potential_role**
> RoleMiningPotentialRole get_potential_role(session_id, potential_role_id)

Retrieves a specific potential role

This method returns a specific potential role for a role mining session.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_potential_role import RoleMiningPotentialRole
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | A potential role id in a role mining session

    try:
        # Retrieves a specific potential role
        api_response = api_instance.get_potential_role(session_id, potential_role_id)
        print("The response of IAIRoleMiningApi->get_potential_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_potential_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| A potential role id in a role mining session | 

### Return type

[**RoleMiningPotentialRole**](RoleMiningPotentialRole.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of potential roles for a role mining session. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_potential_role_applications**
> List[RoleMiningPotentialRoleApplication] get_potential_role_applications(session_id, potential_role_id, offset=offset, limit=limit, count=count)

Retrieves the applications of a potential role for a role mining session

This method returns the applications of a potential role for a role mining session.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_potential_role_application import RoleMiningPotentialRoleApplication
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | A potential role id in a role mining session
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Retrieves the applications of a potential role for a role mining session
        api_response = api_instance.get_potential_role_applications(session_id, potential_role_id, offset=offset, limit=limit, count=count)
        print("The response of IAIRoleMiningApi->get_potential_role_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_potential_role_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| A potential role id in a role mining session | 
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[RoleMiningPotentialRoleApplication]**](RoleMiningPotentialRoleApplication.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of potential roles for a role mining session. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_potential_role_source_identity_usage**
> List[RoleMiningPotentialRoleSourceUsage] get_potential_role_source_identity_usage(potential_role_id, source_id, sorters=sorters, offset=offset, limit=limit, count=count)

Retrieves potential role source usage

This method returns source usageCount (as number of days in the last 90 days) for each identity in a potential role.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_potential_role_source_usage import RoleMiningPotentialRoleSourceUsage
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    potential_role_id = 'e0cc5d7d-bf7f-4f81-b2af-8885b09d9923' # str | A potential role id
    source_id = '2c9180877620c1460176267f336a106f' # str | A source id
    sorters = '-usageCount' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters/) Sorting is supported for the following fields: **displayName, email, usageCount** (optional)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Retrieves potential role source usage
        api_response = api_instance.get_potential_role_source_identity_usage(potential_role_id, source_id, sorters=sorters, offset=offset, limit=limit, count=count)
        print("The response of IAIRoleMiningApi->get_potential_role_source_identity_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_potential_role_source_identity_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **potential_role_id** | **str**| A potential role id | 
 **source_id** | **str**| A source id | 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters/) Sorting is supported for the following fields: **displayName, email, usageCount** | [optional] 
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[RoleMiningPotentialRoleSourceUsage]**](RoleMiningPotentialRoleSourceUsage.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of source usage for the identities in a potential role. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_potential_role_summaries**
> List[RoleMiningPotentialRoleSummary] get_potential_role_summaries(session_id, sorters=sorters, filters=filters, offset=offset, limit=limit, count=count)

Retrieves all potential role summaries

This method returns the potential role summaries for a role mining session.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_potential_role_summary import RoleMiningPotentialRoleSummary
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    sorters = 'createdDate' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **createdDate** (optional)
    filters = '(createdByName co \"int\")and (createdById sw \"2c9180907\")and (type eq \"COMMON\")and ((name co \"entt\")or (saved eq true))' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **createdById**: *eq, sw, co*  **createdByName**: *eq, sw, co*  **description**: *sw, co*  **endDate**: *le, lt*  **freshness**: *eq, ge, gt, le, lt*  **name**: *eq, sw, co*  **quality**: *eq, ge, gt, le, lt*  **startDate**: *ge, gt*  **saved**: *eq*  **type**: *eq* (optional)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Retrieves all potential role summaries
        api_response = api_instance.get_potential_role_summaries(session_id, sorters=sorters, filters=filters, offset=offset, limit=limit, count=count)
        print("The response of IAIRoleMiningApi->get_potential_role_summaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_potential_role_summaries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **createdDate** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **createdById**: *eq, sw, co*  **createdByName**: *eq, sw, co*  **description**: *sw, co*  **endDate**: *le, lt*  **freshness**: *eq, ge, gt, le, lt*  **name**: *eq, sw, co*  **quality**: *eq, ge, gt, le, lt*  **startDate**: *ge, gt*  **saved**: *eq*  **type**: *eq* | [optional] 
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[RoleMiningPotentialRoleSummary]**](RoleMiningPotentialRoleSummary.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of potential role summaries for a role mining session. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_mining_potential_role**
> RoleMiningPotentialRole get_role_mining_potential_role(potential_role_id)

Retrieves a specific potential role

This method returns a specific potential role.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_potential_role import RoleMiningPotentialRole
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    potential_role_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | A potential role id

    try:
        # Retrieves a specific potential role
        api_response = api_instance.get_role_mining_potential_role(potential_role_id)
        print("The response of IAIRoleMiningApi->get_role_mining_potential_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_role_mining_potential_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **potential_role_id** | **str**| A potential role id | 

### Return type

[**RoleMiningPotentialRole**](RoleMiningPotentialRole.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of potential roles for a role mining session. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_mining_session**
> RoleMiningSessionResponse get_role_mining_session(session_id)

Get a role mining session

The method retrieves a role mining session.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_session_response import RoleMiningSessionResponse
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id to be retrieved.

    try:
        # Get a role mining session
        api_response = api_instance.get_role_mining_session(session_id)
        print("The response of IAIRoleMiningApi->get_role_mining_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_role_mining_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id to be retrieved. | 

### Return type

[**RoleMiningSessionResponse**](RoleMiningSessionResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a role mining session |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Client Error - Returned if the request body is invalid. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_mining_session_status**
> RoleMiningSessionStatus get_role_mining_session_status(session_id)

Get role mining session status state

This method returns a role mining session status for a customer.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_session_status import RoleMiningSessionStatus
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id

    try:
        # Get role mining session status state
        api_response = api_instance.get_role_mining_session_status(session_id)
        print("The response of IAIRoleMiningApi->get_role_mining_session_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_role_mining_session_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 

### Return type

[**RoleMiningSessionStatus**](RoleMiningSessionStatus.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns session status |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_mining_sessions**
> List[RoleMiningSessionDto] get_role_mining_sessions(filters=filters, sorters=sorters, offset=offset, limit=limit, count=count)

Retrieves all role mining sessions

Returns all role mining sessions that match the query parameters

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_session_dto import RoleMiningSessionDto
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    filters = 'saved eq \"true\" and name sw \"RM Session\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **saved**: *eq*  **name**: *eq, sw* (optional)
    sorters = 'createdBy,createdDate' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **createdBy, createdDate** (optional)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Retrieves all role mining sessions
        api_response = api_instance.get_role_mining_sessions(filters=filters, sorters=sorters, offset=offset, limit=limit, count=count)
        print("The response of IAIRoleMiningApi->get_role_mining_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_role_mining_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **saved**: *eq*  **name**: *eq, sw* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **createdBy, createdDate** | [optional] 
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[RoleMiningSessionDto]**](RoleMiningSessionDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns all role mining sessions that match the query parameters. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saved_potential_roles**
> List[RoleMiningSessionDraftRoleDto] get_saved_potential_roles(sorters=sorters, offset=offset, limit=limit, count=count)

Retrieves all saved potential roles

This method returns all saved potential roles (draft roles).

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_session_draft_role_dto import RoleMiningSessionDraftRoleDto
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    sorters = 'modified' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters/) Sorting is supported for the following fields: **modified** (optional)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Retrieves all saved potential roles
        api_response = api_instance.get_saved_potential_roles(sorters=sorters, offset=offset, limit=limit, count=count)
        print("The response of IAIRoleMiningApi->get_saved_potential_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->get_saved_potential_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters/) Sorting is supported for the following fields: **modified** | [optional] 
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[RoleMiningSessionDraftRoleDto]**](RoleMiningSessionDraftRoleDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of draft roles for a role mining session. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_potential_role**
> object patch_potential_role(session_id, potential_role_id, patch_potential_role_request_inner)

Update a potential role

The method updates an existing potential role using.  The following fields can be modified:  * `description`  * `name`  * `saved`   >**NOTE: All other fields cannot be modified.** 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.patch_potential_role_request_inner import PatchPotentialRoleRequestInner
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The potential role summary id
    patch_potential_role_request_inner = [{op=remove, path=/description}, {op=replace, path=/description, value=Acct I - Potential Role}, {op=remove, path=/saved}, {op=replace, path=/saved, value=false}, {op=remove, path=/name}, {op=replace, path=/name, value=Potential Role Accounting}] # List[PatchPotentialRoleRequestInner] | 

    try:
        # Update a potential role
        api_response = api_instance.patch_potential_role(session_id, potential_role_id, patch_potential_role_request_inner)
        print("The response of IAIRoleMiningApi->patch_potential_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->patch_potential_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| The potential role summary id | 
 **patch_potential_role_request_inner** | [**List[PatchPotentialRoleRequestInner]**](PatchPotentialRoleRequestInner.md)|  | 

### Return type

**object**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns the potential role summary based on the potentialRoleId provided. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_potential_role_0**
> object patch_potential_role_0(session_id, potential_role_id, patch_potential_role_request_inner)

Update a potential role

The method updates an existing potential role using.  The following fields can be modified:  * `description`  * `name`  * `saved`   >**NOTE: All other fields cannot be modified.** 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.patch_potential_role_request_inner import PatchPotentialRoleRequestInner
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The potential role summary id
    patch_potential_role_request_inner = [{op=remove, path=/description}, {op=replace, path=/description, value=Acct I - Potential Role}, {op=remove, path=/saved}, {op=replace, path=/saved, value=false}, {op=remove, path=/name}, {op=replace, path=/name, value=Potential Role Accounting}] # List[PatchPotentialRoleRequestInner] | 

    try:
        # Update a potential role
        api_response = api_instance.patch_potential_role_0(session_id, potential_role_id, patch_potential_role_request_inner)
        print("The response of IAIRoleMiningApi->patch_potential_role_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->patch_potential_role_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| The potential role summary id | 
 **patch_potential_role_request_inner** | [**List[PatchPotentialRoleRequestInner]**](PatchPotentialRoleRequestInner.md)|  | 

### Return type

**object**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns the potential role summary based on the potentialRoleId provided. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_role_mining_session**
> object patch_role_mining_session(session_id, json_patch_operation)

Patch a role mining session

The  method updates an existing role mining session using PATCH. Supports op in {\"replace\"} and changes to pruneThreshold and/or minNumIdentitiesInPotentialRole. The potential roles in this role mining session is then re-calculated.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.json_patch_operation import JsonPatchOperation
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id to be patched
    json_patch_operation = [{op=replace, path=/pruneThreshold, value=83}, {op=replace, path=/minNumIdentitiesInPotentialRole, value=10}, {op=replace, path=/saved, value=false}, {op=replace, path=/name, value=RM Session - 07/10/22}, {op=add, path=/name, value=RM Session - 07/10/22}] # List[JsonPatchOperation] | Replace pruneThreshold and/or minNumIdentitiesInPotentialRole in role mining session. Update saved status or saved name for a role mining session.

    try:
        # Patch a role mining session
        api_response = api_instance.patch_role_mining_session(session_id, json_patch_operation)
        print("The response of IAIRoleMiningApi->patch_role_mining_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->patch_role_mining_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id to be patched | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| Replace pruneThreshold and/or minNumIdentitiesInPotentialRole in role mining session. Update saved status or saved name for a role mining session. | 

### Return type

**object**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted - Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entitlements_potential_role**
> RoleMiningPotentialRole update_entitlements_potential_role(session_id, potential_role_id, role_mining_potential_role_edit_entitlements)

Edit entitlements for a potential role to exclude some entitlements

This endpoint adds or removes entitlements from an exclusion list for a potential role.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_mining_potential_role import RoleMiningPotentialRole
from sailpoint.beta.models.role_mining_potential_role_edit_entitlements import RoleMiningPotentialRoleEditEntitlements
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IAIRoleMiningApi(api_client)
    session_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role mining session id
    potential_role_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | A potential role id in a role mining session
    role_mining_potential_role_edit_entitlements = sailpoint.beta.RoleMiningPotentialRoleEditEntitlements() # RoleMiningPotentialRoleEditEntitlements | Role mining session parameters

    try:
        # Edit entitlements for a potential role to exclude some entitlements
        api_response = api_instance.update_entitlements_potential_role(session_id, potential_role_id, role_mining_potential_role_edit_entitlements)
        print("The response of IAIRoleMiningApi->update_entitlements_potential_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRoleMiningApi->update_entitlements_potential_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The role mining session id | 
 **potential_role_id** | **str**| A potential role id in a role mining session | 
 **role_mining_potential_role_edit_entitlements** | [**RoleMiningPotentialRoleEditEntitlements**](RoleMiningPotentialRoleEditEntitlements.md)| Role mining session parameters | 

### Return type

[**RoleMiningPotentialRole**](RoleMiningPotentialRole.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Adds or removes entitlements from a potential role&#39;s entitlement exclusion list. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


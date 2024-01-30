# sailpoint.v3.SODPolicyApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sod_policy**](SODPolicyApi.md#create_sod_policy) | **POST** /sod-policies | Create SOD policy
[**delete_sod_policy**](SODPolicyApi.md#delete_sod_policy) | **DELETE** /sod-policies/{id} | Delete SOD policy by ID
[**delete_sod_policy_schedule**](SODPolicyApi.md#delete_sod_policy_schedule) | **DELETE** /sod-policies/{id}/schedule | Delete SOD policy schedule
[**get_custom_violation_report**](SODPolicyApi.md#get_custom_violation_report) | **GET** /sod-violation-report/{reportResultId}/download/{fileName} | Download custom violation report
[**get_default_violation_report**](SODPolicyApi.md#get_default_violation_report) | **GET** /sod-violation-report/{reportResultId}/download | Download violation report
[**get_sod_all_report_run_status**](SODPolicyApi.md#get_sod_all_report_run_status) | **GET** /sod-violation-report | Get multi-report run task status
[**get_sod_policy**](SODPolicyApi.md#get_sod_policy) | **GET** /sod-policies/{id} | Get SOD policy by ID
[**get_sod_policy_schedule**](SODPolicyApi.md#get_sod_policy_schedule) | **GET** /sod-policies/{id}/schedule | Get SOD policy schedule
[**get_sod_violation_report_run_status**](SODPolicyApi.md#get_sod_violation_report_run_status) | **GET** /sod-policies/sod-violation-report-status/{reportResultId} | Get violation report run status
[**get_sod_violation_report_status**](SODPolicyApi.md#get_sod_violation_report_status) | **GET** /sod-policies/{id}/violation-report | Get SOD violation report status
[**list_sod_policies**](SODPolicyApi.md#list_sod_policies) | **GET** /sod-policies | List SOD policies
[**patch_sod_policy**](SODPolicyApi.md#patch_sod_policy) | **PATCH** /sod-policies/{id} | Patch SOD policy by ID
[**put_policy_schedule**](SODPolicyApi.md#put_policy_schedule) | **PUT** /sod-policies/{id}/schedule | Update SOD Policy schedule
[**put_sod_policy**](SODPolicyApi.md#put_sod_policy) | **PUT** /sod-policies/{id} | Update SOD policy by ID
[**start_evaluate_sod_policy**](SODPolicyApi.md#start_evaluate_sod_policy) | **POST** /sod-policies/{id}/evaluate | Evaluate one policy by ID
[**start_sod_all_policies_for_org**](SODPolicyApi.md#start_sod_all_policies_for_org) | **POST** /sod-violation-report/run | Runs all policies for org
[**start_sod_policy**](SODPolicyApi.md#start_sod_policy) | **POST** /sod-policies/{id}/violation-report/run | Runs SOD policy violation report


# **create_sod_policy**
> SodPolicy create_sod_policy(sod_policy)

Create SOD policy

This creates both General and Conflicting Access Based policy, with a limit of 50 entitlements for each (left & right) criteria for Conflicting Access Based SOD policy. Requires role of ORG_ADMIN.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.sod_policy import SodPolicy
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    sod_policy = {name=Conflicting-Policy-Name, description=This policy ensures compliance of xyz, ownerRef={type=IDENTITY, id=2c91808568c529c60168cca6f90c1313, name=Owner Name}, externalPolicyReference=XYZ policy, compensatingControls=Have a manager review the transaction decisions for their "out of compliance" employee, correctionAdvice=Based on the role of the employee, managers should remove access that is not required for their job function., state=ENFORCED, tags=[string], creatorId=0f11f2a4-7c94-4bf3-a2bd-742580fe3bde, modifierId=0f11f2a4-7c94-4bf3-a2bd-742580fe3bde, violationOwnerAssignmentConfig={assignmentRule=MANAGER, ownerRef={type=IDENTITY, id=2c91808568c529c60168cca6f90c1313, name=Violation Owner Name}}, scheduled=true, type=CONFLICTING_ACCESS_BASED, conflictingAccessCriteria={leftCriteria={name=money-in, criteriaList=[{type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a66}, {type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a67}]}, rightCriteria={name=money-out, criteriaList=[{type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a68}, {type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a69}]}}} # SodPolicy | 

    try:
        # Create SOD policy
        api_response = api_instance.create_sod_policy(sod_policy)
        print("The response of SODPolicyApi->create_sod_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->create_sod_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sod_policy** | [**SodPolicy**](SodPolicy.md)|  | 

### Return type

[**SodPolicy**](SodPolicy.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SOD policy created |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sod_policy**
> delete_sod_policy(id, logical=logical)

Delete SOD policy by ID

This deletes a specified SOD policy. Requires role of ORG_ADMIN.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The ID of the SOD Policy to delete.
    logical = True # bool | Indicates whether this is a soft delete (logical true) or a hard delete.  Soft delete marks the policy as deleted and just save it with this status. It could be fully deleted or recovered further.  Hard delete vise versa permanently delete SOD request during this call. (optional) (default to True)

    try:
        # Delete SOD policy by ID
        api_instance.delete_sod_policy(id, logical=logical)
    except Exception as e:
        print("Exception when calling SODPolicyApi->delete_sod_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SOD Policy to delete. | 
 **logical** | **bool**| Indicates whether this is a soft delete (logical true) or a hard delete.  Soft delete marks the policy as deleted and just save it with this status. It could be fully deleted or recovered further.  Hard delete vise versa permanently delete SOD request during this call. | [optional] [default to True]

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sod_policy_schedule**
> delete_sod_policy_schedule(id)

Delete SOD policy schedule

This deletes schedule for a specified SOD policy by ID.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The ID of the SOD policy the schedule must be deleted for.

    try:
        # Delete SOD policy schedule
        api_instance.delete_sod_policy_schedule(id)
    except Exception as e:
        print("Exception when calling SODPolicyApi->delete_sod_policy_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SOD policy the schedule must be deleted for. | 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content response. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_violation_report**
> bytearray get_custom_violation_report(report_result_id, file_name)

Download custom violation report

This allows to download a specified named violation report for a given report reference.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    report_result_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The ID of the report reference to download.
    file_name = 'custom-name' # str | Custom Name for the  file.

    try:
        # Download custom violation report
        api_response = api_instance.get_custom_violation_report(report_result_id, file_name)
        print("The response of SODPolicyApi->get_custom_violation_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->get_custom_violation_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_result_id** | **str**| The ID of the report reference to download. | 
 **file_name** | **str**| Custom Name for the  file. | 

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
**200** | Returns the zip file with given custom name that contains the violation report file. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_violation_report**
> bytearray get_default_violation_report(report_result_id)

Download violation report

This allows to download a violation report for a given report reference.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    report_result_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The ID of the report reference to download.

    try:
        # Download violation report
        api_response = api_instance.get_default_violation_report(report_result_id)
        print("The response of SODPolicyApi->get_default_violation_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->get_default_violation_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_result_id** | **str**| The ID of the report reference to download. | 

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
**200** | Returns the PolicyReport.zip that contains the violation report file. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sod_all_report_run_status**
> ReportResultReference get_sod_all_report_run_status()

Get multi-report run task status

This endpoint gets the status for a violation report for all policy run.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.report_result_reference import ReportResultReference
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)

    try:
        # Get multi-report run task status
        api_response = api_instance.get_sod_all_report_run_status()
        print("The response of SODPolicyApi->get_sod_all_report_run_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->get_sod_all_report_run_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ReportResultReference**](ReportResultReference.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of the violation report run task for all policy run. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sod_policy**
> SodPolicy get_sod_policy(id)

Get SOD policy by ID

This gets specified SOD policy. Requires role of ORG_ADMIN.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.sod_policy import SodPolicy
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The ID of the SOD Policy to retrieve.

    try:
        # Get SOD policy by ID
        api_response = api_instance.get_sod_policy(id)
        print("The response of SODPolicyApi->get_sod_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->get_sod_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SOD Policy to retrieve. | 

### Return type

[**SodPolicy**](SodPolicy.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SOD policy ID. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sod_policy_schedule**
> SodPolicySchedule get_sod_policy_schedule(id)

Get SOD policy schedule

This endpoint gets a specified SOD policy's schedule.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.sod_policy_schedule import SodPolicySchedule
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The ID of the SOD policy schedule to retrieve.

    try:
        # Get SOD policy schedule
        api_response = api_instance.get_sod_policy_schedule(id)
        print("The response of SODPolicyApi->get_sod_policy_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->get_sod_policy_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SOD policy schedule to retrieve. | 

### Return type

[**SodPolicySchedule**](SodPolicySchedule.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SOD policy schedule. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sod_violation_report_run_status**
> ReportResultReference get_sod_violation_report_run_status(report_result_id)

Get violation report run status

This gets the status for a violation report run task that has already been invoked.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.report_result_reference import ReportResultReference
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    report_result_id = '2e8d8180-24bc-4d21-91c6-7affdb473b0d' # str | The ID of the report reference to retrieve.

    try:
        # Get violation report run status
        api_response = api_instance.get_sod_violation_report_run_status(report_result_id)
        print("The response of SODPolicyApi->get_sod_violation_report_run_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->get_sod_violation_report_run_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_result_id** | **str**| The ID of the report reference to retrieve. | 

### Return type

[**ReportResultReference**](ReportResultReference.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of the violation report run task. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sod_violation_report_status**
> ReportResultReference get_sod_violation_report_status(id)

Get SOD violation report status

This gets the status for a violation report run task that has already been invoked.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.report_result_reference import ReportResultReference
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The ID of the violation report to retrieve status for.

    try:
        # Get SOD violation report status
        api_response = api_instance.get_sod_violation_report_status(id)
        print("The response of SODPolicyApi->get_sod_violation_report_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->get_sod_violation_report_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the violation report to retrieve status for. | 

### Return type

[**ReportResultReference**](ReportResultReference.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of the violation report run task. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sod_policies**
> List[SodPolicy] list_sod_policies(limit=limit, offset=offset, count=count, filters=filters)

List SOD policies

This gets list of all SOD policies. Requires role of ORG_ADMIN

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.sod_policy import SodPolicy
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'id eq \"bc693f07e7b645539626c25954c58554\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq*  **name**: *eq*  **state**: *eq* (optional)

    try:
        # List SOD policies
        api_response = api_instance.list_sod_policies(limit=limit, offset=offset, count=count, filters=filters)
        print("The response of SODPolicyApi->list_sod_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->list_sod_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq*  **name**: *eq*  **state**: *eq* | [optional] 

### Return type

[**List[SodPolicy]**](SodPolicy.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all SOD policies. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sod_policy**
> SodPolicy patch_sod_policy(id, json_patch_operation)

Patch SOD policy by ID

Allows updating SOD Policy fields other than [\"id\",\"created\",\"creatorId\",\"policyQuery\",\"type\"] using the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. Requires role of ORG_ADMIN. This endpoint can only patch CONFLICTING_ACCESS_BASED type policies. Do not use this endpoint to patch general policies - doing so will build an API exception. 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.json_patch_operation import JsonPatchOperation
from sailpoint.v3.models.sod_policy import SodPolicy
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    id = '2c918083-5d19-1a86-015d-28455b4a2329' # str | The ID of the SOD policy being modified.
    json_patch_operation = [{op=replace, path=/description, value=Modified description}, {op=replace, path=/conflictingAccessCriteria/leftCriteria/name, value=money-in-modified}, {op=replace, path=/conflictingAccessCriteria/rightCriteria, value={name=money-out-modified, criteriaList=[{type=ENTITLEMENT, id=2c918087682f9a86016839c0509c1ab2}]}}] # List[JsonPatchOperation] | A list of SOD Policy update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields are patchable: * name * description * ownerRef * externalPolicyReference * compensatingControls * correctionAdvice * state * tags * violationOwnerAssignmentConfig * scheduled * conflictingAccessCriteria 

    try:
        # Patch SOD policy by ID
        api_response = api_instance.patch_sod_policy(id, json_patch_operation)
        print("The response of SODPolicyApi->patch_sod_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->patch_sod_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SOD policy being modified. | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| A list of SOD Policy update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields are patchable: * name * description * ownerRef * externalPolicyReference * compensatingControls * correctionAdvice * state * tags * violationOwnerAssignmentConfig * scheduled * conflictingAccessCriteria  | 

### Return type

[**SodPolicy**](SodPolicy.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Indicates the PATCH operation succeeded, and returns the SOD policy&#39;s new representation. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_policy_schedule**
> SodPolicySchedule put_policy_schedule(id, sod_policy_schedule)

Update SOD Policy schedule

This updates schedule for a specified SOD policy.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.sod_policy_schedule import SodPolicySchedule
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The ID of the SOD policy to update its schedule.
    sod_policy_schedule = sailpoint.v3.SodPolicySchedule() # SodPolicySchedule | 

    try:
        # Update SOD Policy schedule
        api_response = api_instance.put_policy_schedule(id, sod_policy_schedule)
        print("The response of SODPolicyApi->put_policy_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->put_policy_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SOD policy to update its schedule. | 
 **sod_policy_schedule** | [**SodPolicySchedule**](SodPolicySchedule.md)|  | 

### Return type

[**SodPolicySchedule**](SodPolicySchedule.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created or updated SOD policy schedule. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sod_policy**
> SodPolicy put_sod_policy(id, sod_policy)

Update SOD policy by ID

This updates a specified SOD policy. Requires role of ORG_ADMIN.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.sod_policy import SodPolicy
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The ID of the SOD policy to update.
    sod_policy = {name=Conflicting-Policy-Name, description=Modified Description, externalPolicyReference=XYZ policy, compensatingControls=Have a manager review the transaction decisions for their "out of compliance" employee, correctionAdvice=Based on the role of the employee, managers should remove access that is not required for their job function., state=ENFORCED, tags=[string], violationOwnerAssignmentConfig={assignmentRule=MANAGER, ownerRef={type=IDENTITY, id=2c91808568c529c60168cca6f90c1313, name=Violation Owner Name}}, scheduled=true, type=CONFLICTING_ACCESS_BASED, conflictingAccessCriteria={leftCriteria={name=money-in, criteriaList=[{type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a66}, {type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a67}]}, rightCriteria={name=money-out, criteriaList=[{type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a68}, {type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a69}]}}} # SodPolicy | 

    try:
        # Update SOD policy by ID
        api_response = api_instance.put_sod_policy(id, sod_policy)
        print("The response of SODPolicyApi->put_sod_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->put_sod_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SOD policy to update. | 
 **sod_policy** | [**SodPolicy**](SodPolicy.md)|  | 

### Return type

[**SodPolicy**](SodPolicy.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SOD Policy by ID |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_evaluate_sod_policy**
> ReportResultReference start_evaluate_sod_policy(id)

Evaluate one policy by ID

Runs the scheduled report for the policy retrieved by passed policy ID.  The report schedule is fetched from the policy retrieved by ID.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.report_result_reference import ReportResultReference
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The SOD policy ID to run.

    try:
        # Evaluate one policy by ID
        api_response = api_instance.start_evaluate_sod_policy(id)
        print("The response of SODPolicyApi->start_evaluate_sod_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->start_evaluate_sod_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The SOD policy ID to run. | 

### Return type

[**ReportResultReference**](ReportResultReference.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference to the violation report run task. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_sod_all_policies_for_org**
> ReportResultReference start_sod_all_policies_for_org(multi_policy_request=multi_policy_request)

Runs all policies for org

Runs multi-policy report for the org. If a policy reports more than 5000 violations, the report mentions that the violation limit was exceeded for that policy. If the request is empty, the report runs for all policies. Otherwise, the report runs for only the filtered policy list provided.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.multi_policy_request import MultiPolicyRequest
from sailpoint.v3.models.report_result_reference import ReportResultReference
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    multi_policy_request = {filteredPolicyList=[b868cd40-ffa4-4337-9c07-1a51846cfa94, 63a07a7b-39a4-48aa-956d-50c827deba2a]} # MultiPolicyRequest |  (optional)

    try:
        # Runs all policies for org
        api_response = api_instance.start_sod_all_policies_for_org(multi_policy_request=multi_policy_request)
        print("The response of SODPolicyApi->start_sod_all_policies_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->start_sod_all_policies_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_policy_request** | [**MultiPolicyRequest**](MultiPolicyRequest.md)|  | [optional] 

### Return type

[**ReportResultReference**](ReportResultReference.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference to the violation report run task. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_sod_policy**
> ReportResultReference start_sod_policy(id)

Runs SOD policy violation report

This invokes processing of violation report for given SOD policy. If the policy reports more than 5000 violations, the report returns with violation limit exceeded message.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.report_result_reference import ReportResultReference
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.SODPolicyApi(api_client)
    id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The SOD policy ID to run.

    try:
        # Runs SOD policy violation report
        api_response = api_instance.start_sod_policy(id)
        print("The response of SODPolicyApi->start_sod_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODPolicyApi->start_sod_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The SOD policy ID to run. | 

### Return type

[**ReportResultReference**](ReportResultReference.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference to the violation report run task. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


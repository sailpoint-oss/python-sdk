# sailpoint.v3.SODPolicyApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_violation_report**](SODPolicyApi.md#get_custom_violation_report) | **GET** /sod-violation-report/{reportResultId}/download/{fileName} | Download custom violation report
[**get_default_violation_report**](SODPolicyApi.md#get_default_violation_report) | **GET** /sod-violation-report/{reportResultId}/download | Download violation report
[**get_sod_all_report_run_status**](SODPolicyApi.md#get_sod_all_report_run_status) | **GET** /sod-violation-report | Get multi-report run task status
[**start_sod_all_policies_for_org**](SODPolicyApi.md#start_sod_all_policies_for_org) | **POST** /sod-violation-report/run | Runs all policies for org


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


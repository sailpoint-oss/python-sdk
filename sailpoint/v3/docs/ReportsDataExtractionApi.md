# sailpoint.v3.ReportsDataExtractionApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_report**](ReportsDataExtractionApi.md#cancel_report) | **POST** /reports/{id}/cancel | Cancel Report
[**get_report**](ReportsDataExtractionApi.md#get_report) | **GET** /reports/{taskResultId} | Get Report File
[**get_report_result**](ReportsDataExtractionApi.md#get_report_result) | **GET** /reports/{taskResultId}/result | Get Report Result
[**start_report**](ReportsDataExtractionApi.md#start_report) | **POST** /reports/run | Run Report


# **cancel_report**
> cancel_report(id)

Cancel Report

Cancels a running report.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
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
    api_instance = sailpoint.v3.ReportsDataExtractionApi(api_client)
    id = 'a1ed223247144cc29d23c632624b4767' # str | ID of the running Report to cancel

    try:
        # Cancel Report
        api_instance.cancel_report(id)
    except Exception as e:
        print("Exception when calling ReportsDataExtractionApi->cancel_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the running Report to cancel | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content - indicates the request was successful but there is no content to be returned in the response. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> bytearray get_report(task_result_id, file_format, name=name, auditable=auditable)

Get Report File

Gets a report in file format.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
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
    api_instance = sailpoint.v3.ReportsDataExtractionApi(api_client)
    task_result_id = 'ef38f94347e94562b5bb8424a56397d8' # str | Unique identifier of the task result which handled report
    file_format = 'csv' # str | Output format of the requested report file
    name = 'Identities Details Report' # str | preferred Report file name, by default will be used report name from task result. (optional)
    auditable = False # bool | Enables auditing for current report download. Will create an audit event and sent it to the REPORT cloud-audit kafka topic.  Event will be created if there is any result present by requested taskResultId. (optional) (default to False)

    try:
        # Get Report File
        api_response = api_instance.get_report(task_result_id, file_format, name=name, auditable=auditable)
        print("The response of ReportsDataExtractionApi->get_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsDataExtractionApi->get_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_result_id** | **str**| Unique identifier of the task result which handled report | 
 **file_format** | **str**| Output format of the requested report file | 
 **name** | **str**| preferred Report file name, by default will be used report name from task result. | [optional] 
 **auditable** | **bool**| Enables auditing for current report download. Will create an audit event and sent it to the REPORT cloud-audit kafka topic.  Event will be created if there is any result present by requested taskResultId. | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv, application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report file in selected format. CSV by default. |  * Content-disposition - The requested report&#39;s filename <br>  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_result**
> ReportResults get_report_result(task_result_id, completed=completed)

Get Report Result

Get the report results for a report that was run or is running. Returns empty report result in case there are no active task definitions with used in payload task definition name.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.report_results import ReportResults
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
    api_instance = sailpoint.v3.ReportsDataExtractionApi(api_client)
    task_result_id = 'ef38f94347e94562b5bb8424a56397d8' # str | Unique identifier of the task result which handled report
    completed = False # bool | state of task result to apply ordering when results are fetching from the DB (optional) (default to False)

    try:
        # Get Report Result
        api_response = api_instance.get_report_result(task_result_id, completed=completed)
        print("The response of ReportsDataExtractionApi->get_report_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsDataExtractionApi->get_report_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_result_id** | **str**| Unique identifier of the task result which handled report | 
 **completed** | **bool**| state of task result to apply ordering when results are fetching from the DB | [optional] [default to False]

### Return type

[**ReportResults**](ReportResults.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about report that was run or is running. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_report**
> TaskResultDetails start_report(report_details)

Run Report

Runs a report according to input report details. If non-concurrent task is already running then it returns, otherwise new task creates and returns.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.report_details import ReportDetails
from sailpoint.v3.models.task_result_details import TaskResultDetails
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
    api_instance = sailpoint.v3.ReportsDataExtractionApi(api_client)
    report_details = sailpoint.v3.ReportDetails() # ReportDetails | 

    try:
        # Run Report
        api_response = api_instance.start_report(report_details)
        print("The response of ReportsDataExtractionApi->start_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsDataExtractionApi->start_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_details** | [**ReportDetails**](ReportDetails.md)|  | 

### Return type

[**TaskResultDetails**](TaskResultDetails.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about running report task. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


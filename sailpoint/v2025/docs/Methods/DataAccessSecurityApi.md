---
id: v2025-data-access-security
title: Data_Access_Security
pagination_label: Data_Access_Security
sidebar_label: Data_Access_Security
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Data_Access_Security', 'V2025Data_Access_Security'] 
slug: /tools/sdk/python/v2025/methods/data-access-security
tags: ['SDK', 'Software Development Kit', 'Data_Access_Security', 'V2025Data_Access_Security']
---

# sailpoint.v2025.DataAccessSecurityApi
  Use this API to trigger and manage DAS tasks such as scans-starting them on demand, updating schedules, and retrieving statuses.
 
All URIs are relative to *https://sailpoint.api.identitynow.com/v2025*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel-task**](#cancel-task) | **POST** `/das/tasks/cancel/{id}` | Cancel a DAS task.
[**create-schedule**](#create-schedule) | **POST** `/das/tasks/schedules` | Create a new schedule.
[**delete-schedule**](#delete-schedule) | **DELETE** `/das/tasks/schedules/{id}` | Delete a DAS schedule.
[**delete-task**](#delete-task) | **DELETE** `/das/tasks/{id}` | Delete a DAS task.
[**get-schedule**](#get-schedule) | **GET** `/das/tasks/schedules/{id}` | Get a DAS schedule.
[**get-schedules**](#get-schedules) | **GET** `/das/tasks/schedules` | List all schedules.
[**get-task**](#get-task) | **GET** `/das/tasks/{id}` | Get a DAS task.
[**get-tasks**](#get-tasks) | **GET** `/das/tasks` | Lists all DAS tasks.
[**put-schedule**](#put-schedule) | **PUT** `/das/tasks/schedules/{id}` | Update a schedule.
[**start-task-rerun**](#start-task-rerun) | **POST** `/das/tasks/rerun/{id}` | Rerun a DAS task.


## cancel-task
Cancel a DAS task.
This end-point sends a request to cancel a task in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/cancel-task)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **int** | True  | The unique identifier of the task to cancel.

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No Content |  |  -  |
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
from sailpoint.v2025.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 1001 # int | The unique identifier of the task to cancel. # int | The unique identifier of the task to cancel.

    try:
        # Cancel a DAS task.
        
        DataAccessSecurityApi(api_client).cancel_task(id=id)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).cancel_task(id)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->cancel_task: %s\n" % e)
```



[[Back to top]](#) 

## create-schedule
Create a new schedule.


[API Spec](https://developer.sailpoint.com/docs/api/v2025/create-schedule)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_schedule_request | [**CreateScheduleRequest**](../models/create-schedule-request) | True  | 

### Return type
**int**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | OK | int |  -  |
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
from sailpoint.v2025.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.create_schedule_request import CreateScheduleRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_schedule_request = '''{
          "scheduleTaskName" : "Daily Data Sync",
          "scheduleType" : "Daily",
          "active" : true,
          "interval" : 1440,
          "startTime" : 1762237200,
          "endTime" : 1762240800,
          "taskTypeName" : "DataSync",
          "daysOfWeek" : [ "Monday", "Wednesday", "Friday" ],
          "applicationId" : 2001,
          "runAfterScheduleTaskId" : 1000
        }''' # CreateScheduleRequest | 

    try:
        # Create a new schedule.
        new_create_schedule_request = CreateScheduleRequest.from_json(create_schedule_request)
        results = DataAccessSecurityApi(api_client).create_schedule(create_schedule_request=new_create_schedule_request)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).create_schedule(new_create_schedule_request)
        print("The response of DataAccessSecurityApi->create_schedule:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->create_schedule: %s\n" % e)
```



[[Back to top]](#) 

## delete-schedule
Delete a DAS schedule.
This end-point sends a request to delete a schedule in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/delete-schedule)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **int** | True  | The unique identifier of the schedule to delete.

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No Content |  |  -  |
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
from sailpoint.v2025.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 1001 # int | The unique identifier of the schedule to delete. # int | The unique identifier of the schedule to delete.

    try:
        # Delete a DAS schedule.
        
        DataAccessSecurityApi(api_client).delete_schedule(id=id)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).delete_schedule(id)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->delete_schedule: %s\n" % e)
```



[[Back to top]](#) 

## delete-task
Delete a DAS task.
This end-point sends a request to delete a task in Data Access Security.


[API Spec](https://developer.sailpoint.com/docs/api/v2025/delete-task)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **int** | True  | The unique identifier of the task to delete.

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No Content |  |  -  |
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
from sailpoint.v2025.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 1001 # int | The unique identifier of the task to delete. # int | The unique identifier of the task to delete.

    try:
        # Delete a DAS task.
        
        DataAccessSecurityApi(api_client).delete_task(id=id)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).delete_task(id)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->delete_task: %s\n" % e)
```



[[Back to top]](#) 

## get-schedule
Get a DAS schedule.
This end-point gets a schedule in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/get-schedule)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **int** | True  | The unique identifier of the schedule to retrieve.

### Return type
[**ScheduleInfo**](../models/schedule-info)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | A schedule object. | ScheduleInfo |  -  |
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
from sailpoint.v2025.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.schedule_info import ScheduleInfo
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 1001 # int | The unique identifier of the schedule to retrieve. # int | The unique identifier of the schedule to retrieve.

    try:
        # Get a DAS schedule.
        
        results = DataAccessSecurityApi(api_client).get_schedule(id=id)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).get_schedule(id)
        print("The response of DataAccessSecurityApi->get_schedule:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->get_schedule: %s\n" % e)
```



[[Back to top]](#) 

## get-schedules
List all schedules.
This end-point lists all the schedules in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/get-schedules)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | filters | **str** |   (optional) | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **scheduleTaskIds**: *eq, in*  **taskTypeName**: *eq, in*  **status**: *eq*  **applicationId**: *eq*  **fullName**: *eq*  **nameSubString**: *eq*  **scheduleType**: *eq*  Supported composite operators are *and, or*
  Query | limit | **int** |   (optional) (default to 250) | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | offset | **int** |   (optional) (default to 0) | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | count | **bool** |   (optional) (default to False) | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.

### Return type
[**List[ScheduleInfo]**](../models/schedule-info)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | List of Schedule objects. | List[ScheduleInfo] |  -  |
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
from sailpoint.v2025.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.schedule_info import ScheduleInfo
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    filters = 'ScheduleType eq \"Daily\" and startTime eq 1762237200' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **scheduleTaskIds**: *eq, in*  **taskTypeName**: *eq, in*  **status**: *eq*  **applicationId**: *eq*  **fullName**: *eq*  **nameSubString**: *eq*  **scheduleType**: *eq*  Supported composite operators are *and, or* (optional) # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **scheduleTaskIds**: *eq, in*  **taskTypeName**: *eq, in*  **status**: *eq*  **applicationId**: *eq*  **fullName**: *eq*  **nameSubString**: *eq*  **scheduleType**: *eq*  Supported composite operators are *and, or* (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250) # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0) # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False) # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # List all schedules.
        
        results = DataAccessSecurityApi(api_client).get_schedules()
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).get_schedules(filters, limit, offset, count)
        print("The response of DataAccessSecurityApi->get_schedules:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->get_schedules: %s\n" % e)
```



[[Back to top]](#) 

## get-task
Get a DAS task.
This end-point gets a task in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/get-task)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **int** | True  | The unique identifier of the task to retrieve.

### Return type
[**TaskInfo**](../models/task-info)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | A Task object. | TaskInfo |  -  |
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
from sailpoint.v2025.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.task_info import TaskInfo
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 1001 # int | The unique identifier of the task to retrieve. # int | The unique identifier of the task to retrieve.

    try:
        # Get a DAS task.
        
        results = DataAccessSecurityApi(api_client).get_task(id=id)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).get_task(id)
        print("The response of DataAccessSecurityApi->get_task:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->get_task: %s\n" % e)
```



[[Back to top]](#) 

## get-tasks
Lists all DAS tasks.
This end-point lists all the tasks in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/get-tasks)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | filters | **str** |   (optional) | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **taskIds**: *eq, in*  **statuses**: *eq, in*  **taskTypeName**: *eq, in*  **taskName**: *eq*  **endBeforeTime**: *eq*  Supported composite operators are *and, or*  Example: taskTypeName eq \"DataSync\" and endBeforeTime eq 1762240800
  Query | limit | **int** |   (optional) (default to 250) | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | offset | **int** |   (optional) (default to 0) | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | count | **bool** |   (optional) (default to False) | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.

### Return type
[**List[TaskInfo]**](../models/task-info)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | OK. Returns a list of Data Access Security tasks. | List[TaskInfo] |  -  |
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
from sailpoint.v2025.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.task_info import TaskInfo
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    filters = 'TaskTypeName eq \"DataClassification and EndBeforeTime eq 1762240800' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **taskIds**: *eq, in*  **statuses**: *eq, in*  **taskTypeName**: *eq, in*  **taskName**: *eq*  **endBeforeTime**: *eq*  Supported composite operators are *and, or*  Example: taskTypeName eq \"DataSync\" and endBeforeTime eq 1762240800 (optional) # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **taskIds**: *eq, in*  **statuses**: *eq, in*  **taskTypeName**: *eq, in*  **taskName**: *eq*  **endBeforeTime**: *eq*  Supported composite operators are *and, or*  Example: taskTypeName eq \"DataSync\" and endBeforeTime eq 1762240800 (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250) # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0) # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False) # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Lists all DAS tasks.
        
        results = DataAccessSecurityApi(api_client).get_tasks()
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).get_tasks(filters, limit, offset, count)
        print("The response of DataAccessSecurityApi->get_tasks:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->get_tasks: %s\n" % e)
```



[[Back to top]](#) 

## put-schedule
Update a schedule.


[API Spec](https://developer.sailpoint.com/docs/api/v2025/put-schedule)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **int** | True  | The unique identifier of the schedule to update.
 Body  | update_schedule_request | [**UpdateScheduleRequest**](../models/update-schedule-request) | True  | 

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No Content |  |  -  |
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
from sailpoint.v2025.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.update_schedule_request import UpdateScheduleRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 1001 # int | The unique identifier of the schedule to update. # int | The unique identifier of the schedule to update.
    update_schedule_request = '''{
          "scheduleTaskName" : "Daily Data Sync",
          "scheduleType" : "Daily",
          "active" : true,
          "interval" : 1440,
          "startTime" : 1762237200,
          "endTime" : 1762240800,
          "taskTypeName" : "DataSync",
          "daysOfWeek" : [ "Monday", "Wednesday", "Friday" ],
          "applicationId" : 2001,
          "runAfterScheduleTaskId" : 1000
        }''' # UpdateScheduleRequest | 

    try:
        # Update a schedule.
        new_update_schedule_request = UpdateScheduleRequest.from_json(update_schedule_request)
        DataAccessSecurityApi(api_client).put_schedule(id=id, update_schedule_request=new_update_schedule_request)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).put_schedule(id, new_update_schedule_request)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->put_schedule: %s\n" % e)
```



[[Back to top]](#) 

## start-task-rerun
Rerun a DAS task.
This end-point sends a request to re-run a task in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/start-task-rerun)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **int** | True  | The unique identifier of the task to rerun.

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No Content |  |  -  |
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
from sailpoint.v2025.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 1001 # int | The unique identifier of the task to rerun. # int | The unique identifier of the task to rerun.

    try:
        # Rerun a DAS task.
        
        DataAccessSecurityApi(api_client).start_task_rerun(id=id)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).start_task_rerun(id)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->start_task_rerun: %s\n" % e)
```



[[Back to top]](#) 




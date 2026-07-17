---
id: data-access-security
title: Data_Access_Security
pagination_label: Data_Access_Security
sidebar_label: Data_Access_Security
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Data_Access_Security', 'Data_Access_Security'] 
slug: /tools/sdk/python/data-access-security/methods/data-access-security
tags: ['SDK', 'Software Development Kit', 'Data_Access_Security', 'Data_Access_Security']
---

# sailpoint.data_access_security.DataAccessSecurityApi
  Use this API to enable data ownership election campaigns, assign resource owners, and respond to identity lifecycle events to maintain continuous accountability.
This API can also trigger and manage DAS tasks such as scans-starting them on demand, updating configurations or schedules, and retrieving statuses. Additionally, you can onboard and manage applications at scale by creating and configuring them, setting scanning schedules, retrieving metadata, and associating them with Virtual Appliances and Identity Collectors.
 
All URIs are relative to *https://sailpoint.api.identitynow.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel-task-v1**](#cancel-task-v1) | **POST** `/das/v1/tasks/cancel/{id}` | Cancel a DAS task.
[**create-application-v1**](#create-application-v1) | **POST** `/das/v1/applications` | Create application
[**create-identity-collector-v1**](#create-identity-collector-v1) | **POST** `/das/identity-collectors/v1` | Create identity collector
[**create-schedule-v1**](#create-schedule-v1) | **POST** `/das/v1/tasks/schedules` | Create a new schedule.
[**das-v1-owners-assign-post**](#das-v1-owners-assign-post) | **POST** `/das/v1/owners/assign` | Assign owner to application resource.
[**das-v1-owners-owner-identity-id-resources-get**](#das-v1-owners-owner-identity-id-resources-get) | **GET** `/das/v1/owners/{ownerIdentityId}/resources` | List resources for owner.
[**das-v1-owners-reelect-post**](#das-v1-owners-reelect-post) | **POST** `/das/v1/owners/reelect` | Re-elect resource owner.
[**das-v1-owners-resources-resource-id-get**](#das-v1-owners-resources-resource-id-get) | **GET** `/das/v1/owners/resources/{resourceId}` | List owners for resource.
[**das-v1-owners-source-identity-id-reassign-destination-identity-id-post**](#das-v1-owners-source-identity-id-reassign-destination-identity-id-post) | **POST** `/das/v1/owners/{sourceIdentityId}/reassign/{destinationIdentityId}` | Reassign resource owner.
[**delete-application-v1**](#delete-application-v1) | **DELETE** `/das/v1/applications/{id}` | Delete an application by identifier.
[**delete-identity-collector-v1**](#delete-identity-collector-v1) | **DELETE** `/das/identity-collectors/v1/{id}` | Delete identity collector by identifier
[**delete-schedule-v1**](#delete-schedule-v1) | **DELETE** `/das/v1/tasks/schedules/{id}` | Delete a DAS schedule.
[**delete-task-v1**](#delete-task-v1) | **DELETE** `/das/v1/tasks/{id}` | Delete a DAS task.
[**get-application-v1**](#get-application-v1) | **GET** `/das/v1/applications/{id}` | Retrieve application details by identifier.
[**get-applications-v1**](#get-applications-v1) | **GET** `/das/v1/applications` | Search applications in DAS.
[**get-owners-v1**](#get-owners-v1) | **GET** `/das/v1/owners/applications/{appId}` | Retrieve owners per application.
[**get-schedule-v1**](#get-schedule-v1) | **GET** `/das/v1/tasks/schedules/{id}` | Get a DAS schedule.
[**get-schedules-v1**](#get-schedules-v1) | **GET** `/das/v1/tasks/schedules` | List all schedules.
[**get-task-v1**](#get-task-v1) | **GET** `/das/v1/tasks/{id}` | Get a DAS task.
[**get-tasks-v1**](#get-tasks-v1) | **GET** `/das/v1/tasks` | Lists all DAS tasks.
[**list-identity-collectors-v1**](#list-identity-collectors-v1) | **GET** `/das/identity-collectors/v1` | List identity collectors
[**put-application-v1**](#put-application-v1) | **PUT** `/das/v1/applications/{id}` | Update application by identifier.
[**put-identity-collector-v1**](#put-identity-collector-v1) | **PUT** `/das/identity-collectors/v1/{id}` | Update identity collector by identifier
[**put-schedule-v1**](#put-schedule-v1) | **PUT** `/das/v1/tasks/schedules/{id}` | Update a schedule.
[**start-task-rerun-v1**](#start-task-rerun-v1) | **POST** `/das/v1/tasks/rerun/{id}` | Rerun a DAS task.


## cancel-task-v1
Cancel a DAS task.
This end-point sends a request to cancel a task in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/cancel-task-v-1)

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
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 1001 # int | The unique identifier of the task to cancel. # int | The unique identifier of the task to cancel.

    try:
        # Cancel a DAS task.
        
        DataAccessSecurityApi(api_client).cancel_task_v1(id=id)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).cancel_task_v1(id)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->cancel_task_v1: %s\n" % e)
```



[[Back to top]](#) 

## create-application-v1
Create application
This endpoint creates a new application in Data Access Security with the specified configuration.

[API Spec](https://developer.sailpoint.com/docs/api/create-application-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | base_create_application_request | [**BaseCreateApplicationRequest**](../models/base-create-application-request) | True  | Request body containing the details required to create a new application.

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No Content |  |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.base_create_application_request import BaseCreateApplicationRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    base_create_application_request = '''{
          "adIdentityCollectorId" : 987654321,
          "applicationType" : 9,
          "nisIdentityCollectorId" : 192837465,
          "executeNow" : false,
          "name" : "HR File Server",
          "description" : "Stores HR documents and employee records.",
          "dataClassificationSettings" : {
            "isEnabled" : true,
            "clusterId" : "cluster-001"
          },
          "activityConfigurationSettings" : {
            "excludeFolders" : [ "/tmp", "/archive" ],
            "excludeFileExtensions" : [ ".log", ".bak" ],
            "excludeActions" : [ "delete", "move" ],
            "isEnabled" : true,
            "retentionTimePeriod" : 30,
            "retentionTimeType" : "days",
            "clusterId" : "cluster-001",
            "excludeUsers" : [ "user1", "user2" ]
          },
          "applicationCrawlerSettings" : {
            "calculateResourceSize" : 2,
            "excludedResources" : [ "resourceA", "resourceB" ],
            "crawlPublicFolders" : true,
            "excludedPathsByRegex" : "^/archive/.*",
            "isEnabled" : true,
            "crawlSnapshotsFolder" : true,
            "crawlMailboxes" : false,
            "crawlTopLevelShares" : [ "share1", "share2" ],
            "clusterId" : "cluster-001",
            "includeResources" : [ "resourceX", "resourceY" ]
          },
          "identityCollectorId" : 123456789,
          "permissionCollectorSettings" : {
            "analyzeUniquePermissions" : true,
            "calculateRiskiestPermissions" : false,
            "isEnabled" : true,
            "calculateEffectivePermissions" : true,
            "clusterId" : "cluster-001",
            "effectivePermissionsSource" : "S3"
          },
          "tags" : [ {
            "key" : 1,
            "value" : "Confidential"
          } ]
        }''' # BaseCreateApplicationRequest | Request body containing the details required to create a new application.

    try:
        # Create application
        new_base_create_application_request = BaseCreateApplicationRequest.from_json(base_create_application_request)
        DataAccessSecurityApi(api_client).create_application_v1(base_create_application_request=new_base_create_application_request)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).create_application_v1(new_base_create_application_request)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->create_application_v1: %s\n" % e)
```



[[Back to top]](#) 

## create-identity-collector-v1
Create identity collector
This endpoint creates a new identity collector in Data Access Security for the specified source. The identity collector type is derived from the source.

[API Spec](https://developer.sailpoint.com/docs/api/create-identity-collector-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | createidentitycollectorrequest | [**Createidentitycollectorrequest**](../models/createidentitycollectorrequest) | True  | Request body containing the details required to create a new identity collector.

### Return type
[**CreateIdentityCollectorV1200Response**](../models/create-identity-collector-v1200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | The identity collector was created successfully. | CreateIdentityCollectorV1200Response |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.create_identity_collector_v1200_response import CreateIdentityCollectorV1200Response
from sailpoint.data_access_security.models.createidentitycollectorrequest import Createidentitycollectorrequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    createidentitycollectorrequest = '''{
          "sourceId" : "2c9180835d2e5168015d32f890ca1581",
          "name" : "Active Directory Identity Collector"
        }''' # Createidentitycollectorrequest | Request body containing the details required to create a new identity collector.

    try:
        # Create identity collector
        new_createidentitycollectorrequest = Createidentitycollectorrequest.from_json(createidentitycollectorrequest)
        results = DataAccessSecurityApi(api_client).create_identity_collector_v1(createidentitycollectorrequest=new_createidentitycollectorrequest)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).create_identity_collector_v1(new_createidentitycollectorrequest)
        print("The response of DataAccessSecurityApi->create_identity_collector_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->create_identity_collector_v1: %s\n" % e)
```



[[Back to top]](#) 

## create-schedule-v1
Create a new schedule.


[API Spec](https://developer.sailpoint.com/docs/api/create-schedule-v-1)

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
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.create_schedule_request import CreateScheduleRequest
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
        results = DataAccessSecurityApi(api_client).create_schedule_v1(create_schedule_request=new_create_schedule_request)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).create_schedule_v1(new_create_schedule_request)
        print("The response of DataAccessSecurityApi->create_schedule_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->create_schedule_v1: %s\n" % e)
```



[[Back to top]](#) 

## das-v1-owners-assign-post
Assign owner to application resource.


[API Spec](https://developer.sailpoint.com/docs/api/das-v1-owners-assign-post)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | assign_resource_owner_request | [**AssignResourceOwnerRequest**](../models/assign-resource-owner-request) | True  | The request body must contain the application ID, resource path, and identity ID to be assigned as the resource owner.

### Return type
**int**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | 1 - success, otherwise failure. | int |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.assign_resource_owner_request import AssignResourceOwnerRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    assign_resource_owner_request = '''{
          "fullPath" : "/shared/hr/documents/employee-records.pdf",
          "identityId" : "d290f1ee-6c54-4b01-90e6-d701748f0851",
          "appId" : 12345
        }''' # AssignResourceOwnerRequest | The request body must contain the application ID, resource path, and identity ID to be assigned as the resource owner.

    try:
        # Assign owner to application resource.
        new_assign_resource_owner_request = AssignResourceOwnerRequest.from_json(assign_resource_owner_request)
        results = DataAccessSecurityApi(api_client).das_v1_owners_assign_post(assign_resource_owner_request=new_assign_resource_owner_request)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).das_v1_owners_assign_post(new_assign_resource_owner_request)
        print("The response of DataAccessSecurityApi->das_v1_owners_assign_post:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->das_v1_owners_assign_post: %s\n" % e)
```



[[Back to top]](#) 

## das-v1-owners-owner-identity-id-resources-get
List resources for owner.


[API Spec](https://developer.sailpoint.com/docs/api/das-v1-owners-owner-identity-id-resources-get)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | owner_identity_id | **str** | True  | Unique identifier for the owner. This should be a UUID representing the owner's identity.
  Query | limit | **int** |   (optional) (default to 250) | Not applicable for this endpoint. Do not use.
  Query | offset | **int** |   (optional) (default to 0) | Not applicable for this endpoint. Do not use.

### Return type
[**List[ResourceModel]**](../models/resource-model)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | A list of resources owned by the specified identity was retrieved successfully. | List[ResourceModel] |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.resource_model import ResourceModel
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    owner_identity_id = 'a3f1c2d4-5678-4e9b-8c2d-123456789abc' # str | Unique identifier for the owner. This should be a UUID representing the owner's identity. # str | Unique identifier for the owner. This should be a UUID representing the owner's identity.
    limit = 250 # int | Not applicable for this endpoint. Do not use. (optional) (default to 250) # int | Not applicable for this endpoint. Do not use. (optional) (default to 250)
    offset = 0 # int | Not applicable for this endpoint. Do not use. (optional) (default to 0) # int | Not applicable for this endpoint. Do not use. (optional) (default to 0)

    try:
        # List resources for owner.
        
        results = DataAccessSecurityApi(api_client).das_v1_owners_owner_identity_id_resources_get(owner_identity_id=owner_identity_id)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).das_v1_owners_owner_identity_id_resources_get(owner_identity_id, limit, offset)
        print("The response of DataAccessSecurityApi->das_v1_owners_owner_identity_id_resources_get:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->das_v1_owners_owner_identity_id_resources_get: %s\n" % e)
```



[[Back to top]](#) 

## das-v1-owners-reelect-post
Re-elect resource owner.


[API Spec](https://developer.sailpoint.com/docs/api/das-v1-owners-reelect-post)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | reelect_request | [**ReelectRequest**](../models/reelect-request) | True  | The request body must contain details for re-electing a resource owner. Date/time fields should use epoch format in seconds.

### Return type
**int**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | The number of elections CREATED. In case of failure, some elections may not be STARTED. | int |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.reelect_request import ReelectRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    reelect_request = '''{
          "ownerId" : "c1a2b3d4-e5f6-7890-abcd-1234567890ab",
          "campaignName" : "Annual Resource Owner Election",
          "reviewers" : [ "d4e5f6a7-b8c9-0123-4567-89abcdef0123", "e7f8g9h0-i1j2-3456-7890-klmnopqrstuv" ]
        }''' # ReelectRequest | The request body must contain details for re-electing a resource owner. Date/time fields should use epoch format in seconds.

    try:
        # Re-elect resource owner.
        new_reelect_request = ReelectRequest.from_json(reelect_request)
        results = DataAccessSecurityApi(api_client).das_v1_owners_reelect_post(reelect_request=new_reelect_request)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).das_v1_owners_reelect_post(new_reelect_request)
        print("The response of DataAccessSecurityApi->das_v1_owners_reelect_post:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->das_v1_owners_reelect_post: %s\n" % e)
```



[[Back to top]](#) 

## das-v1-owners-resources-resource-id-get
List owners for resource.


[API Spec](https://developer.sailpoint.com/docs/api/das-v1-owners-resources-resource-id-get)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | resource_id | **int** | True  | Unique identifier for the resource.
  Query | limit | **int** |   (optional) (default to 250) | Not applicable for this endpoint. Do not use.
  Query | offset | **int** |   (optional) (default to 0) | Not applicable for this endpoint. Do not use.

### Return type
**List[str]**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | A list of owner identity UUIDs for the specified resource was retrieved successfully. | List[str] |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    resource_id = 101 # int | Unique identifier for the resource. # int | Unique identifier for the resource.
    limit = 250 # int | Not applicable for this endpoint. Do not use. (optional) (default to 250) # int | Not applicable for this endpoint. Do not use. (optional) (default to 250)
    offset = 0 # int | Not applicable for this endpoint. Do not use. (optional) (default to 0) # int | Not applicable for this endpoint. Do not use. (optional) (default to 0)

    try:
        # List owners for resource.
        
        results = DataAccessSecurityApi(api_client).das_v1_owners_resources_resource_id_get(resource_id=resource_id)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).das_v1_owners_resources_resource_id_get(resource_id, limit, offset)
        print("The response of DataAccessSecurityApi->das_v1_owners_resources_resource_id_get:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->das_v1_owners_resources_resource_id_get: %s\n" % e)
```



[[Back to top]](#) 

## das-v1-owners-source-identity-id-reassign-destination-identity-id-post
Reassign resource owner.


[API Spec](https://developer.sailpoint.com/docs/api/das-v1-owners-source-identity-id-reassign-destination-identity-id-post)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | source_identity_id | **str** | True  | Unique identifier for the source owner. This should be a UUID representing the identity to reassign from.
Path   | destination_identity_id | **str** | True  | Unique identifier for the destination owner. This should be a UUID representing the identity to reassign to.

### Return type
**int**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | The number of resources whose owners were overwritten. | int |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    source_identity_id = 'a3f1c2d4-5678-4e9b-8c2d-123456789abc' # str | Unique identifier for the source owner. This should be a UUID representing the identity to reassign from. # str | Unique identifier for the source owner. This should be a UUID representing the identity to reassign from.
    destination_identity_id = 'b4e2d3c5-6789-4f0a-9d3e-234567890bcd' # str | Unique identifier for the destination owner. This should be a UUID representing the identity to reassign to. # str | Unique identifier for the destination owner. This should be a UUID representing the identity to reassign to.

    try:
        # Reassign resource owner.
        
        results = DataAccessSecurityApi(api_client).das_v1_owners_source_identity_id_reassign_destination_identity_id_post(source_identity_id=source_identity_id, destination_identity_id=destination_identity_id)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).das_v1_owners_source_identity_id_reassign_destination_identity_id_post(source_identity_id, destination_identity_id)
        print("The response of DataAccessSecurityApi->das_v1_owners_source_identity_id_reassign_destination_identity_id_post:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->das_v1_owners_source_identity_id_reassign_destination_identity_id_post: %s\n" % e)
```



[[Back to top]](#) 

## delete-application-v1
Delete an application by identifier.
This endpoint deletes an application from Data Access Security by its unique identifier.

[API Spec](https://developer.sailpoint.com/docs/api/delete-application-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **int** | True  | The unique identifier of the application to delete.

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No Content |  |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 12345 # int | The unique identifier of the application to delete. # int | The unique identifier of the application to delete.

    try:
        # Delete an application by identifier.
        
        DataAccessSecurityApi(api_client).delete_application_v1(id=id)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).delete_application_v1(id)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->delete_application_v1: %s\n" % e)
```



[[Back to top]](#) 

## delete-identity-collector-v1
Delete identity collector by identifier
This endpoint deletes an identity collector from Data Access Security by its unique identifier.

[API Spec](https://developer.sailpoint.com/docs/api/delete-identity-collector-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **int** | True  | The unique identifier of the identity collector to delete.

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No Content |  |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 12345 # int | The unique identifier of the identity collector to delete. # int | The unique identifier of the identity collector to delete.

    try:
        # Delete identity collector by identifier
        
        DataAccessSecurityApi(api_client).delete_identity_collector_v1(id=id)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).delete_identity_collector_v1(id)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->delete_identity_collector_v1: %s\n" % e)
```



[[Back to top]](#) 

## delete-schedule-v1
Delete a DAS schedule.
This end-point sends a request to delete a schedule in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/delete-schedule-v-1)

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
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 1001 # int | The unique identifier of the schedule to delete. # int | The unique identifier of the schedule to delete.

    try:
        # Delete a DAS schedule.
        
        DataAccessSecurityApi(api_client).delete_schedule_v1(id=id)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).delete_schedule_v1(id)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->delete_schedule_v1: %s\n" % e)
```



[[Back to top]](#) 

## delete-task-v1
Delete a DAS task.
This end-point sends a request to delete a task in Data Access Security.


[API Spec](https://developer.sailpoint.com/docs/api/delete-task-v-1)

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
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 1001 # int | The unique identifier of the task to delete. # int | The unique identifier of the task to delete.

    try:
        # Delete a DAS task.
        
        DataAccessSecurityApi(api_client).delete_task_v1(id=id)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).delete_task_v1(id)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->delete_task_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-application-v1
Retrieve application details by identifier.
This endpoint retrieves the details of a specific application in Data Access Security by its unique identifier.

[API Spec](https://developer.sailpoint.com/docs/api/get-application-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **int** | True  | The unique identifier of the application to retrieve.

### Return type
[**ApplicationItem**](../models/application-item)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | The application details were retrieved successfully. | ApplicationItem |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.application_item import ApplicationItem
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 12345 # int | The unique identifier of the application to retrieve. # int | The unique identifier of the application to retrieve.

    try:
        # Retrieve application details by identifier.
        
        results = DataAccessSecurityApi(api_client).get_application_v1(id=id)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).get_application_v1(id)
        print("The response of DataAccessSecurityApi->get_application_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->get_application_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-applications-v1
Search applications in DAS.
This endpoint lists all the applications in Data Access Security with optional filtering.

[API Spec](https://developer.sailpoint.com/docs/api/get-applications-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | filters | **str** |   (optional) | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **appIds**: *eq, in*  **tagIds**: *eq, in*  **statuses**: *eq, in*  **groupCodes**: *eq, in*  **virtualAppId**: *eq*  **appName**: *eq*  **supportsValidation**: *eq*  Supported composite operators are *and, or*
  Query | limit | **int** |   (optional) (default to 250) | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | offset | **int** |   (optional) (default to 0) | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | count | **bool** |   (optional) (default to False) | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.

### Return type
[**List[ApplicationItem]**](../models/application-item)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | A list of applications matching the filter criteria. | List[ApplicationItem] |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.application_item import ApplicationItem
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    filters = 'AppType eq \'ActiveDirectory\' and Statuses eq \'Passed\'' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **appIds**: *eq, in*  **tagIds**: *eq, in*  **statuses**: *eq, in*  **groupCodes**: *eq, in*  **virtualAppId**: *eq*  **appName**: *eq*  **supportsValidation**: *eq*  Supported composite operators are *and, or* (optional) # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **appIds**: *eq, in*  **tagIds**: *eq, in*  **statuses**: *eq, in*  **groupCodes**: *eq, in*  **virtualAppId**: *eq*  **appName**: *eq*  **supportsValidation**: *eq*  Supported composite operators are *and, or* (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250) # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0) # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False) # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Search applications in DAS.
        
        results = DataAccessSecurityApi(api_client).get_applications_v1()
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).get_applications_v1(filters, limit, offset, count)
        print("The response of DataAccessSecurityApi->get_applications_v1:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->get_applications_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-owners-v1
Retrieve owners per application.


[API Spec](https://developer.sailpoint.com/docs/api/get-owners-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | app_id | **int** | True  | The unique identifier of the application for which to retrieve owners.
  Query | limit | **int** |   (optional) (default to 250) | Not applicable for this endpoint. Do not use.
  Query | offset | **int** |   (optional) (default to 0) | Not applicable for this endpoint. Do not use.

### Return type
[**List[DataOwnerModel]**](../models/data-owner-model)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | OK. Returns a list of DataOwnerModel objects. | List[DataOwnerModel] |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.data_owner_model import DataOwnerModel
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    app_id = 2001 # int | The unique identifier of the application for which to retrieve owners. # int | The unique identifier of the application for which to retrieve owners.
    limit = 250 # int | Not applicable for this endpoint. Do not use. (optional) (default to 250) # int | Not applicable for this endpoint. Do not use. (optional) (default to 250)
    offset = 0 # int | Not applicable for this endpoint. Do not use. (optional) (default to 0) # int | Not applicable for this endpoint. Do not use. (optional) (default to 0)

    try:
        # Retrieve owners per application.
        
        results = DataAccessSecurityApi(api_client).get_owners_v1(app_id=app_id)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).get_owners_v1(app_id, limit, offset)
        print("The response of DataAccessSecurityApi->get_owners_v1:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->get_owners_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-schedule-v1
Get a DAS schedule.
This end-point gets a schedule in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/get-schedule-v-1)

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
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.schedule_info import ScheduleInfo
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 1001 # int | The unique identifier of the schedule to retrieve. # int | The unique identifier of the schedule to retrieve.

    try:
        # Get a DAS schedule.
        
        results = DataAccessSecurityApi(api_client).get_schedule_v1(id=id)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).get_schedule_v1(id)
        print("The response of DataAccessSecurityApi->get_schedule_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->get_schedule_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-schedules-v1
List all schedules.
This end-point lists all the schedules in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/get-schedules-v-1)

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
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.schedule_info import ScheduleInfo
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    filters = 'ScheduleType eq \"Daily\" and startTime eq 1762237200' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **scheduleTaskIds**: *eq, in*  **taskTypeName**: *eq, in*  **status**: *eq*  **applicationId**: *eq*  **fullName**: *eq*  **nameSubString**: *eq*  **scheduleType**: *eq*  Supported composite operators are *and, or* (optional) # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **scheduleTaskIds**: *eq, in*  **taskTypeName**: *eq, in*  **status**: *eq*  **applicationId**: *eq*  **fullName**: *eq*  **nameSubString**: *eq*  **scheduleType**: *eq*  Supported composite operators are *and, or* (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250) # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0) # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False) # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # List all schedules.
        
        results = DataAccessSecurityApi(api_client).get_schedules_v1()
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).get_schedules_v1(filters, limit, offset, count)
        print("The response of DataAccessSecurityApi->get_schedules_v1:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->get_schedules_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-task-v1
Get a DAS task.
This end-point gets a task in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/get-task-v-1)

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
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.task_info import TaskInfo
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 1001 # int | The unique identifier of the task to retrieve. # int | The unique identifier of the task to retrieve.

    try:
        # Get a DAS task.
        
        results = DataAccessSecurityApi(api_client).get_task_v1(id=id)
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).get_task_v1(id)
        print("The response of DataAccessSecurityApi->get_task_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->get_task_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-tasks-v1
Lists all DAS tasks.
This end-point lists all the tasks in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/get-tasks-v-1)

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
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.task_info import TaskInfo
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    filters = 'TaskTypeName eq \"DataClassification and EndBeforeTime eq 1762240800' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **taskIds**: *eq, in*  **statuses**: *eq, in*  **taskTypeName**: *eq, in*  **taskName**: *eq*  **endBeforeTime**: *eq*  Supported composite operators are *and, or*  Example: taskTypeName eq \"DataSync\" and endBeforeTime eq 1762240800 (optional) # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **taskIds**: *eq, in*  **statuses**: *eq, in*  **taskTypeName**: *eq, in*  **taskName**: *eq*  **endBeforeTime**: *eq*  Supported composite operators are *and, or*  Example: taskTypeName eq \"DataSync\" and endBeforeTime eq 1762240800 (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250) # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0) # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False) # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Lists all DAS tasks.
        
        results = DataAccessSecurityApi(api_client).get_tasks_v1()
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).get_tasks_v1(filters, limit, offset, count)
        print("The response of DataAccessSecurityApi->get_tasks_v1:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->get_tasks_v1: %s\n" % e)
```



[[Back to top]](#) 

## list-identity-collectors-v1
List identity collectors
This endpoint lists the identity collectors in Data Access Security with optional filtering and pagination.

Sorting is not supported for this endpoint; supplying the `sorters` query parameter results in a validation error.

[API Spec](https://developer.sailpoint.com/docs/api/list-identity-collectors-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | filters | **str** |   (optional) | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **sourceId**: *eq*  **type**: *eq, in*  **id**: *eq, in*  Supported composite operators are *and, or*
  Query | limit | **int** |   (optional) (default to 250) | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | offset | **int** |   (optional) (default to 0) | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | count | **bool** |   (optional) (default to False) | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.

### Return type
[**List[Identitycollectorlistitem]**](../models/identitycollectorlistitem)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | A list of identity collectors matching the filter criteria. | List[Identitycollectorlistitem] |  * X-Total-Count - The total number of results matching the filter criteria, regardless of paging limits.  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.identitycollectorlistitem import Identitycollectorlistitem
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    filters = 'sourceId eq \"2c9180835d2e5168015d32f890ca1581\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **sourceId**: *eq*  **type**: *eq, in*  **id**: *eq, in*  Supported composite operators are *and, or* (optional) # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **sourceId**: *eq*  **type**: *eq, in*  **id**: *eq, in*  Supported composite operators are *and, or* (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250) # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0) # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False) # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # List identity collectors
        
        results = DataAccessSecurityApi(api_client).list_identity_collectors_v1()
        # Below is a request that includes all optional parameters
        # results = DataAccessSecurityApi(api_client).list_identity_collectors_v1(filters, limit, offset, count)
        print("The response of DataAccessSecurityApi->list_identity_collectors_v1:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->list_identity_collectors_v1: %s\n" % e)
```



[[Back to top]](#) 

## put-application-v1
Update application by identifier.
This endpoint updates an existing application in Data Access Security with the specified configuration.

[API Spec](https://developer.sailpoint.com/docs/api/put-application-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **int** | True  | The unique identifier of the application to update.
 Body  | base_create_application_request | [**BaseCreateApplicationRequest**](../models/base-create-application-request) | True  | Request body containing the updated details for the application.

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No Content |  |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.base_create_application_request import BaseCreateApplicationRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 12345 # int | The unique identifier of the application to update. # int | The unique identifier of the application to update.
    base_create_application_request = '''{
          "adIdentityCollectorId" : 987654321,
          "applicationType" : 9,
          "nisIdentityCollectorId" : 192837465,
          "executeNow" : false,
          "name" : "HR File Server",
          "description" : "Stores HR documents and employee records.",
          "dataClassificationSettings" : {
            "isEnabled" : true,
            "clusterId" : "cluster-001"
          },
          "activityConfigurationSettings" : {
            "excludeFolders" : [ "/tmp", "/archive" ],
            "excludeFileExtensions" : [ ".log", ".bak" ],
            "excludeActions" : [ "delete", "move" ],
            "isEnabled" : true,
            "retentionTimePeriod" : 30,
            "retentionTimeType" : "days",
            "clusterId" : "cluster-001",
            "excludeUsers" : [ "user1", "user2" ]
          },
          "applicationCrawlerSettings" : {
            "calculateResourceSize" : 2,
            "excludedResources" : [ "resourceA", "resourceB" ],
            "crawlPublicFolders" : true,
            "excludedPathsByRegex" : "^/archive/.*",
            "isEnabled" : true,
            "crawlSnapshotsFolder" : true,
            "crawlMailboxes" : false,
            "crawlTopLevelShares" : [ "share1", "share2" ],
            "clusterId" : "cluster-001",
            "includeResources" : [ "resourceX", "resourceY" ]
          },
          "identityCollectorId" : 123456789,
          "permissionCollectorSettings" : {
            "analyzeUniquePermissions" : true,
            "calculateRiskiestPermissions" : false,
            "isEnabled" : true,
            "calculateEffectivePermissions" : true,
            "clusterId" : "cluster-001",
            "effectivePermissionsSource" : "S3"
          },
          "tags" : [ {
            "key" : 1,
            "value" : "Confidential"
          } ]
        }''' # BaseCreateApplicationRequest | Request body containing the updated details for the application.

    try:
        # Update application by identifier.
        new_base_create_application_request = BaseCreateApplicationRequest.from_json(base_create_application_request)
        DataAccessSecurityApi(api_client).put_application_v1(id=id, base_create_application_request=new_base_create_application_request)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).put_application_v1(id, new_base_create_application_request)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->put_application_v1: %s\n" % e)
```



[[Back to top]](#) 

## put-identity-collector-v1
Update identity collector by identifier
This endpoint updates the name of an existing identity collector in Data Access Security. The `sourceId` and `type` cannot be changed and must match the current values.

[API Spec](https://developer.sailpoint.com/docs/api/put-identity-collector-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **int** | True  | The unique identifier of the identity collector to update.
 Body  | updateidentitycollectorrequest | [**Updateidentitycollectorrequest**](../models/updateidentitycollectorrequest) | True  | Request body containing the updated details for the identity collector.

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No Content |  |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
409 | Conflict - Returned if an identity collector with the same name already exists. | PutIdentityCollectorV1409Response |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.updateidentitycollectorrequest import Updateidentitycollectorrequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 12345 # int | The unique identifier of the identity collector to update. # int | The unique identifier of the identity collector to update.
    updateidentitycollectorrequest = '''{
          "sourceId" : "2c9180835d2e5168015d32f890ca1581",
          "name" : "Active Directory Identity Collector",
          "type" : "Active Directory"
        }''' # Updateidentitycollectorrequest | Request body containing the updated details for the identity collector.

    try:
        # Update identity collector by identifier
        new_updateidentitycollectorrequest = Updateidentitycollectorrequest.from_json(updateidentitycollectorrequest)
        DataAccessSecurityApi(api_client).put_identity_collector_v1(id=id, updateidentitycollectorrequest=new_updateidentitycollectorrequest)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).put_identity_collector_v1(id, new_updateidentitycollectorrequest)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->put_identity_collector_v1: %s\n" % e)
```



[[Back to top]](#) 

## put-schedule-v1
Update a schedule.


[API Spec](https://developer.sailpoint.com/docs/api/put-schedule-v-1)

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
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.data_access_security.models.update_schedule_request import UpdateScheduleRequest
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
        DataAccessSecurityApi(api_client).put_schedule_v1(id=id, update_schedule_request=new_update_schedule_request)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).put_schedule_v1(id, new_update_schedule_request)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->put_schedule_v1: %s\n" % e)
```



[[Back to top]](#) 

## start-task-rerun-v1
Rerun a DAS task.
This end-point sends a request to re-run a task in Data Access Security.

[API Spec](https://developer.sailpoint.com/docs/api/start-task-rerun-v-1)

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
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTasksV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTasksV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.data_access_security.api.data_access_security_api import DataAccessSecurityApi
from sailpoint.data_access_security.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 1001 # int | The unique identifier of the task to rerun. # int | The unique identifier of the task to rerun.

    try:
        # Rerun a DAS task.
        
        DataAccessSecurityApi(api_client).start_task_rerun_v1(id=id)
        # Below is a request that includes all optional parameters
        # DataAccessSecurityApi(api_client).start_task_rerun_v1(id)
    except Exception as e:
        print("Exception when calling DataAccessSecurityApi->start_task_rerun_v1: %s\n" % e)
```



[[Back to top]](#) 




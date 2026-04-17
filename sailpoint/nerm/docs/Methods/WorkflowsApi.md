---
id: workflows
title: Workflows
pagination_label: workflows
sidebar_label: workflows
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'workflows', 'workflows'] 
slug: /tools/sdk/python//methods/workflows
tags: ['SDK', 'Software Development Kit', 'workflows', 'workflows']
---

# sailpoint.nerm.WorkflowsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-automated-workflow**](#create-automated-workflow) | **POST** `/workflows/automated_workflows` | Create an automated workflow
[**create-batch-workflow**](#create-batch-workflow) | **POST** `/workflows/batch_workflows` | Create a batch workflow
[**create-create-workflow**](#create-create-workflow) | **POST** `/workflows/create_workflows` | Create a create workflow
[**create-login-workflow**](#create-login-workflow) | **POST** `/workflows/login_workflows` | Create a login workflow
[**create-password-update-workflow**](#create-password-update-workflow) | **POST** `/workflows/password_reset_workflows` | Create a password reset workflow
[**create-registration-workflow**](#create-registration-workflow) | **POST** `/workflows/registration_workflows` | Create a registration workflow
[**create-update-workflow**](#create-update-workflow) | **POST** `/workflows/update_workflows` | Create an update workflow


## create-automated-workflow
Create an automated workflow
Create an automated workflow

[API Spec](https://developer.sailpoint.com/docs/api//create-automated-workflow)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_automated_workflow_request | [**CreateAutomatedWorkflowRequest**](../models/create-automated-workflow-request) | True  | 

### Return type
[**CreateCreateWorkflow200Response**](../models/create-create-workflow200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateCreateWorkflow200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflows_api import WorkflowsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_automated_workflow_request import CreateAutomatedWorkflowRequest
from sailpoint.nerm.models.create_create_workflow200_response import CreateCreateWorkflow200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_automated_workflow_request = '''sailpoint.nerm.CreateAutomatedWorkflowRequest()''' # CreateAutomatedWorkflowRequest | 

    try:
        # Create an automated workflow
        new_create_automated_workflow_request = CreateAutomatedWorkflowRequest.from_json(create_automated_workflow_request)
        results = WorkflowsApi(api_client).create_automated_workflow(create_automated_workflow_request=new_create_automated_workflow_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowsApi(api_client).create_automated_workflow(new_create_automated_workflow_request)
        print("The response of WorkflowsApi->create_automated_workflow:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowsApi->create_automated_workflow: %s\n" % e)
```



[[Back to top]](#) 

## create-batch-workflow
Create a batch workflow
Create a batch workflow

[API Spec](https://developer.sailpoint.com/docs/api//create-batch-workflow)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_batch_workflow_request | [**CreateBatchWorkflowRequest**](../models/create-batch-workflow-request) | True  | 

### Return type
[**CreateCreateWorkflow200Response**](../models/create-create-workflow200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateCreateWorkflow200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflows_api import WorkflowsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_batch_workflow_request import CreateBatchWorkflowRequest
from sailpoint.nerm.models.create_create_workflow200_response import CreateCreateWorkflow200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_batch_workflow_request = '''sailpoint.nerm.CreateBatchWorkflowRequest()''' # CreateBatchWorkflowRequest | 

    try:
        # Create a batch workflow
        new_create_batch_workflow_request = CreateBatchWorkflowRequest.from_json(create_batch_workflow_request)
        results = WorkflowsApi(api_client).create_batch_workflow(create_batch_workflow_request=new_create_batch_workflow_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowsApi(api_client).create_batch_workflow(new_create_batch_workflow_request)
        print("The response of WorkflowsApi->create_batch_workflow:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowsApi->create_batch_workflow: %s\n" % e)
```



[[Back to top]](#) 

## create-create-workflow
Create a create workflow
Create a create workflow

[API Spec](https://developer.sailpoint.com/docs/api//create-create-workflow)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_create_workflow_request | [**CreateCreateWorkflowRequest**](../models/create-create-workflow-request) | True  | 

### Return type
[**CreateCreateWorkflow200Response**](../models/create-create-workflow200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateCreateWorkflow200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflows_api import WorkflowsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_create_workflow200_response import CreateCreateWorkflow200Response
from sailpoint.nerm.models.create_create_workflow_request import CreateCreateWorkflowRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_create_workflow_request = '''sailpoint.nerm.CreateCreateWorkflowRequest()''' # CreateCreateWorkflowRequest | 

    try:
        # Create a create workflow
        new_create_create_workflow_request = CreateCreateWorkflowRequest.from_json(create_create_workflow_request)
        results = WorkflowsApi(api_client).create_create_workflow(create_create_workflow_request=new_create_create_workflow_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowsApi(api_client).create_create_workflow(new_create_create_workflow_request)
        print("The response of WorkflowsApi->create_create_workflow:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowsApi->create_create_workflow: %s\n" % e)
```



[[Back to top]](#) 

## create-login-workflow
Create a login workflow
Create a login workflow

[API Spec](https://developer.sailpoint.com/docs/api//create-login-workflow)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_login_workflow_request | [**CreateLoginWorkflowRequest**](../models/create-login-workflow-request) | True  | 

### Return type
[**CreateCreateWorkflow200Response**](../models/create-create-workflow200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateCreateWorkflow200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflows_api import WorkflowsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_create_workflow200_response import CreateCreateWorkflow200Response
from sailpoint.nerm.models.create_login_workflow_request import CreateLoginWorkflowRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_login_workflow_request = '''sailpoint.nerm.CreateLoginWorkflowRequest()''' # CreateLoginWorkflowRequest | 

    try:
        # Create a login workflow
        new_create_login_workflow_request = CreateLoginWorkflowRequest.from_json(create_login_workflow_request)
        results = WorkflowsApi(api_client).create_login_workflow(create_login_workflow_request=new_create_login_workflow_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowsApi(api_client).create_login_workflow(new_create_login_workflow_request)
        print("The response of WorkflowsApi->create_login_workflow:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowsApi->create_login_workflow: %s\n" % e)
```



[[Back to top]](#) 

## create-password-update-workflow
Create a password reset workflow
Create a password reset workflow

[API Spec](https://developer.sailpoint.com/docs/api//create-password-update-workflow)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_login_workflow_request | [**CreateLoginWorkflowRequest**](../models/create-login-workflow-request) | True  | 

### Return type
[**CreateCreateWorkflow200Response**](../models/create-create-workflow200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateCreateWorkflow200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflows_api import WorkflowsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_create_workflow200_response import CreateCreateWorkflow200Response
from sailpoint.nerm.models.create_login_workflow_request import CreateLoginWorkflowRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_login_workflow_request = '''sailpoint.nerm.CreateLoginWorkflowRequest()''' # CreateLoginWorkflowRequest | 

    try:
        # Create a password reset workflow
        new_create_login_workflow_request = CreateLoginWorkflowRequest.from_json(create_login_workflow_request)
        results = WorkflowsApi(api_client).create_password_update_workflow(create_login_workflow_request=new_create_login_workflow_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowsApi(api_client).create_password_update_workflow(new_create_login_workflow_request)
        print("The response of WorkflowsApi->create_password_update_workflow:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowsApi->create_password_update_workflow: %s\n" % e)
```



[[Back to top]](#) 

## create-registration-workflow
Create a registration workflow
Create a registration workflow

[API Spec](https://developer.sailpoint.com/docs/api//create-registration-workflow)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_create_workflow_request | [**CreateCreateWorkflowRequest**](../models/create-create-workflow-request) | True  | 

### Return type
[**CreateCreateWorkflow200Response**](../models/create-create-workflow200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateCreateWorkflow200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflows_api import WorkflowsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_create_workflow200_response import CreateCreateWorkflow200Response
from sailpoint.nerm.models.create_create_workflow_request import CreateCreateWorkflowRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_create_workflow_request = '''sailpoint.nerm.CreateCreateWorkflowRequest()''' # CreateCreateWorkflowRequest | 

    try:
        # Create a registration workflow
        new_create_create_workflow_request = CreateCreateWorkflowRequest.from_json(create_create_workflow_request)
        results = WorkflowsApi(api_client).create_registration_workflow(create_create_workflow_request=new_create_create_workflow_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowsApi(api_client).create_registration_workflow(new_create_create_workflow_request)
        print("The response of WorkflowsApi->create_registration_workflow:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowsApi->create_registration_workflow: %s\n" % e)
```



[[Back to top]](#) 

## create-update-workflow
Create an update workflow
Create an update workflow

[API Spec](https://developer.sailpoint.com/docs/api//create-update-workflow)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_update_workflow_request | [**CreateUpdateWorkflowRequest**](../models/create-update-workflow-request) | True  | 

### Return type
[**CreateCreateWorkflow200Response**](../models/create-create-workflow200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateCreateWorkflow200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflows_api import WorkflowsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_create_workflow200_response import CreateCreateWorkflow200Response
from sailpoint.nerm.models.create_update_workflow_request import CreateUpdateWorkflowRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_update_workflow_request = '''sailpoint.nerm.CreateUpdateWorkflowRequest()''' # CreateUpdateWorkflowRequest | 

    try:
        # Create an update workflow
        new_create_update_workflow_request = CreateUpdateWorkflowRequest.from_json(create_update_workflow_request)
        results = WorkflowsApi(api_client).create_update_workflow(create_update_workflow_request=new_create_update_workflow_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowsApi(api_client).create_update_workflow(new_create_update_workflow_request)
        print("The response of WorkflowsApi->create_update_workflow:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowsApi->create_update_workflow: %s\n" % e)
```



[[Back to top]](#) 




---
id: forms
title: Forms
pagination_label: forms
sidebar_label: forms
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'forms', 'forms'] 
slug: /tools/sdk/python//methods/forms
tags: ['SDK', 'Software Development Kit', 'forms', 'forms']
---

# sailpoint.nerm.FormsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-form**](#create-form) | **POST** `/forms` | Create a form
[**delete-form-by-id**](#delete-form-by-id) | **DELETE** `/forms/{id}` | Delete form by id
[**delete-form-by-uid**](#delete-form-by-uid) | **DELETE** `/forms/{uid}` | Delete form by UID
[**get-form-by-id**](#get-form-by-id) | **GET** `/forms/{id}` | Get form data by Id
[**get-form-by-uid**](#get-form-by-uid) | **GET** `/forms/{uid}` | Get form data by UID
[**get-forms**](#get-forms) | **GET** `/forms` | Get forms
[**update-form-by-id**](#update-form-by-id) | **PATCH** `/forms/{id}` | Update form data by id
[**update-form-by-uid**](#update-form-by-uid) | **PATCH** `/forms/{uid}` | Update form data by UID


## create-form
Create a form
This endpoint can create a form

[API Spec](https://developer.sailpoint.com/docs/api//create-form)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_form_request | [**CreateFormRequest**](../models/create-form-request) | True  | 

### Return type
[**GetForms200Response**](../models/get-forms200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetForms200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.forms_api import FormsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_form_request import CreateFormRequest
from sailpoint.nerm.models.get_forms200_response import GetForms200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_form_request = '''sailpoint.nerm.CreateFormRequest()''' # CreateFormRequest | 

    try:
        # Create a form
        new_create_form_request = CreateFormRequest.from_json(create_form_request)
        results = FormsApi(api_client).create_form(create_form_request=new_create_form_request)
        # Below is a request that includes all optional parameters
        # results = FormsApi(api_client).create_form(new_create_form_request)
        print("The response of FormsApi->create_form:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormsApi->create_form: %s\n" % e)
```



[[Back to top]](#) 

## delete-form-by-id
Delete form by id
Delete form by id

[API Spec](https://developer.sailpoint.com/docs/api//delete-form-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**CreateAttribute201Response**](../models/create-attribute201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateAttribute201Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.forms_api import FormsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_attribute201_response import CreateAttribute201Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete form by id
        
        results = FormsApi(api_client).delete_form_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = FormsApi(api_client).delete_form_by_id(id)
        print("The response of FormsApi->delete_form_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormsApi->delete_form_by_id: %s\n" % e)
```



[[Back to top]](#) 

## delete-form-by-uid
Delete form by UID
Delete form by UID

[API Spec](https://developer.sailpoint.com/docs/api//delete-form-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**CreateAttribute201Response**](../models/create-attribute201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateAttribute201Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.forms_api import FormsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_attribute201_response import CreateAttribute201Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Delete form by UID
        
        results = FormsApi(api_client).delete_form_by_uid()
        # Below is a request that includes all optional parameters
        # results = FormsApi(api_client).delete_form_by_uid(uid)
        print("The response of FormsApi->delete_form_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormsApi->delete_form_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-form-by-id
Get form data by Id
Info for a specific form

[API Spec](https://developer.sailpoint.com/docs/api//get-form-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetForms200Response**](../models/get-forms200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetForms200Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.forms_api import FormsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_forms200_response import GetForms200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Get form data by Id
        
        results = FormsApi(api_client).get_form_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = FormsApi(api_client).get_form_by_id(id)
        print("The response of FormsApi->get_form_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormsApi->get_form_by_id: %s\n" % e)
```



[[Back to top]](#) 

## get-form-by-uid
Get form data by UID
Info for a specific form

[API Spec](https://developer.sailpoint.com/docs/api//get-form-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**GetForms200Response**](../models/get-forms200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetForms200Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.forms_api import FormsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_forms200_response import GetForms200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Get form data by UID
        
        results = FormsApi(api_client).get_form_by_uid()
        # Below is a request that includes all optional parameters
        # results = FormsApi(api_client).get_form_by_uid(uid)
        print("The response of FormsApi->get_form_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormsApi->get_form_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-forms
Get forms
Get defined forms in the system

[API Spec](https://developer.sailpoint.com/docs/api//get-forms)

### Parameters 
This endpoint does not need any parameter. 

### Return type
[**GetForms200Response**](../models/get-forms200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetForms200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.forms_api import FormsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_forms200_response import GetForms200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:

    try:
        # Get forms
        
        results = FormsApi(api_client).get_forms()
        # Below is a request that includes all optional parameters
        # results = FormsApi(api_client).get_forms()
        print("The response of FormsApi->get_forms:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormsApi->get_forms: %s\n" % e)
```



[[Back to top]](#) 

## update-form-by-id
Update form data by id
Update info for a specific form

[API Spec](https://developer.sailpoint.com/docs/api//update-form-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | update_form_by_id_request | [**UpdateFormByIdRequest**](../models/update-form-by-id-request) | True  | 

### Return type
[**CreateAttribute201Response**](../models/create-attribute201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateAttribute201Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.forms_api import FormsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_attribute201_response import CreateAttribute201Response
from sailpoint.nerm.models.update_form_by_id_request import UpdateFormByIdRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    update_form_by_id_request = '''sailpoint.nerm.UpdateFormByIdRequest()''' # UpdateFormByIdRequest | 

    try:
        # Update form data by id
        new_update_form_by_id_request = UpdateFormByIdRequest.from_json(update_form_by_id_request)
        results = FormsApi(api_client).update_form_by_id(id=id, update_form_by_id_request=new_update_form_by_id_request)
        # Below is a request that includes all optional parameters
        # results = FormsApi(api_client).update_form_by_id(id, new_update_form_by_id_request)
        print("The response of FormsApi->update_form_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormsApi->update_form_by_id: %s\n" % e)
```



[[Back to top]](#) 

## update-form-by-uid
Update form data by UID
Update info for a specific form

[API Spec](https://developer.sailpoint.com/docs/api//update-form-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | update_form_by_id_request | [**UpdateFormByIdRequest**](../models/update-form-by-id-request) | True  | 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**CreateAttribute201Response**](../models/create-attribute201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateAttribute201Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.forms_api import FormsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_attribute201_response import CreateAttribute201Response
from sailpoint.nerm.models.update_form_by_id_request import UpdateFormByIdRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    update_form_by_id_request = '''sailpoint.nerm.UpdateFormByIdRequest()''' # UpdateFormByIdRequest | 
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Update form data by UID
        new_update_form_by_id_request = UpdateFormByIdRequest.from_json(update_form_by_id_request)
        results = FormsApi(api_client).update_form_by_uid(update_form_by_id_request=new_update_form_by_id_request)
        # Below is a request that includes all optional parameters
        # results = FormsApi(api_client).update_form_by_uid(new_update_form_by_id_request, uid)
        print("The response of FormsApi->update_form_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormsApi->update_form_by_uid: %s\n" % e)
```



[[Back to top]](#) 




---
id: profiles
title: Profiles
pagination_label: profiles
sidebar_label: profiles
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'profiles', 'profiles'] 
slug: /tools/sdk/python//methods/profiles
tags: ['SDK', 'Software Development Kit', 'profiles', 'profiles']
---

# sailpoint.nerm.ProfilesApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-profiles**](#create-profiles) | **POST** `/profiles` | Create multiple profiles
[**delete-profile-by-id**](#delete-profile-by-id) | **DELETE** `/profiles/{id}` | Delete a single profile
[**delete-profiles**](#delete-profiles) | **DELETE** `/profiles` | Delete multiple profiles
[**get-profile-avatar**](#get-profile-avatar) | **GET** `/profiles/{id}/avatar` | Retrieves profile avatar URL
[**get-profile-by-id**](#get-profile-by-id) | **GET** `/profiles/{id}` | Find profile by id
[**get-profile-upload**](#get-profile-upload) | **GET** `/profiles/{id}/upload/{attribute_id}` | Retrieves profile attribute attachment URL
[**get-profiles**](#get-profiles) | **GET** `/profiles` | Get profiles
[**patch-profile-by-id**](#patch-profile-by-id) | **PATCH** `/profiles/{id}` | Update a profile by id
[**patch-profiles**](#patch-profiles) | **PATCH** `/profiles` | Update multiple profiles
[**submit-profile**](#submit-profile) | **POST** `/profile` | Create a profile
[**submit-profile-avatar**](#submit-profile-avatar) | **POST** `/profiles/{id}/avatar` | Uploads new profile avatar
[**submit-profile-upload**](#submit-profile-upload) | **POST** `/profiles/{id}/upload/{attribute_id}` | Uploads profile attachment attribute


## create-profiles
Create multiple profiles
Create multiple profiles

[API Spec](https://developer.sailpoint.com/docs/api//create-profiles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_profiles_request | [**CreateProfilesRequest**](../models/create-profiles-request) | True  | 

### Return type
[**SearchAdvancedSearch200Response**](../models/search-advanced-search200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SearchAdvancedSearch200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profiles_api import ProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_profiles_request import CreateProfilesRequest
from sailpoint.nerm.models.search_advanced_search200_response import SearchAdvancedSearch200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_profiles_request = '''sailpoint.nerm.CreateProfilesRequest()''' # CreateProfilesRequest | 

    try:
        # Create multiple profiles
        new_create_profiles_request = CreateProfilesRequest.from_json(create_profiles_request)
        results = ProfilesApi(api_client).create_profiles(create_profiles_request=new_create_profiles_request)
        # Below is a request that includes all optional parameters
        # results = ProfilesApi(api_client).create_profiles(new_create_profiles_request)
        print("The response of ProfilesApi->create_profiles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfilesApi->create_profiles: %s\n" % e)
```



[[Back to top]](#) 

## delete-profile-by-id
Delete a single profile
Delete a single profile

[API Spec](https://developer.sailpoint.com/docs/api//delete-profile-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | The Profile was successfully deleted. |  |  -  |
400 | Error deleting Profile | DeleteMasterRecord400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profiles_api import ProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete a single profile
        
        ProfilesApi(api_client).delete_profile_by_id(id=id)
        # Below is a request that includes all optional parameters
        # ProfilesApi(api_client).delete_profile_by_id(id)
    except Exception as e:
        print("Exception when calling ProfilesApi->delete_profile_by_id: %s\n" % e)
```



[[Back to top]](#) 

## delete-profiles
Delete multiple profiles
Delete multiple profiles

[API Spec](https://developer.sailpoint.com/docs/api//delete-profiles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_profiles_request | [**CreateProfilesRequest**](../models/create-profiles-request) | True  | 

### Return type
[**DeleteProfiles200Response**](../models/delete-profiles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | DeleteProfiles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profiles_api import ProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_profiles_request import CreateProfilesRequest
from sailpoint.nerm.models.delete_profiles200_response import DeleteProfiles200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_profiles_request = '''sailpoint.nerm.CreateProfilesRequest()''' # CreateProfilesRequest | 

    try:
        # Delete multiple profiles
        new_create_profiles_request = CreateProfilesRequest.from_json(create_profiles_request)
        results = ProfilesApi(api_client).delete_profiles(create_profiles_request=new_create_profiles_request)
        # Below is a request that includes all optional parameters
        # results = ProfilesApi(api_client).delete_profiles(new_create_profiles_request)
        print("The response of ProfilesApi->delete_profiles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfilesApi->delete_profiles: %s\n" % e)
```



[[Back to top]](#) 

## get-profile-avatar
Retrieves profile avatar URL
Retrieves the URL of the profile avatar

[API Spec](https://developer.sailpoint.com/docs/api//get-profile-avatar)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**Url**](../models/url)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | Url |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profiles_api import ProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.url import Url
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Retrieves profile avatar URL
        
        results = ProfilesApi(api_client).get_profile_avatar(id=id)
        # Below is a request that includes all optional parameters
        # results = ProfilesApi(api_client).get_profile_avatar(id)
        print("The response of ProfilesApi->get_profile_avatar:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfilesApi->get_profile_avatar: %s\n" % e)
```



[[Back to top]](#) 

## get-profile-by-id
Find profile by id
Find profile by id

[API Spec](https://developer.sailpoint.com/docs/api//get-profile-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetSingleSchemaMappedProfile200Response**](../models/get-single-schema-mapped-profile200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetSingleSchemaMappedProfile200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profiles_api import ProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_single_schema_mapped_profile200_response import GetSingleSchemaMappedProfile200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find profile by id
        
        results = ProfilesApi(api_client).get_profile_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = ProfilesApi(api_client).get_profile_by_id(id)
        print("The response of ProfilesApi->get_profile_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfilesApi->get_profile_by_id: %s\n" % e)
```



[[Back to top]](#) 

## get-profile-upload
Retrieves profile attribute attachment URL
Retrieves the URL of an attachment attribute value from a profile

[API Spec](https://developer.sailpoint.com/docs/api//get-profile-upload)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
Path   | attribute_id | **str** | True  | The id of the attachment attribute

### Return type
[**Url**](../models/url)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | Url |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profiles_api import ProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.url import Url
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    attribute_id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | The id of the attachment attribute # str | The id of the attachment attribute

    try:
        # Retrieves profile attribute attachment URL
        
        results = ProfilesApi(api_client).get_profile_upload(id=id, attribute_id=attribute_id)
        # Below is a request that includes all optional parameters
        # results = ProfilesApi(api_client).get_profile_upload(id, attribute_id)
        print("The response of ProfilesApi->get_profile_upload:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfilesApi->get_profile_upload: %s\n" % e)
```



[[Back to top]](#) 

## get-profiles
Get profiles
Get profiles

[API Spec](https://developer.sailpoint.com/docs/api//get-profiles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | exclude_attributes | **bool** |   (optional) (default to False) | Allows for optimization by not returning the associated attribute data for the returned profiles
  Query | name | **str** |   (optional) | object name for filtering
  Query | profile_type_id | **str** |   (optional) | Profile Type ID for filtering
  Query | status | **str** |   (optional) | status value for filtering
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").
  Query | after_id | **str** |   (optional) | Represents the ID where the query should begin from. If blank, it represents the first ID. When used, forces sorting by ID ascending and does not allow use of `offset`. When `after_id` is specified it changes the mode of the API such that any filter parameters other than `profile_type_id`, `limit`, and `offset` are not supported and will be either silently ignored or result in an HTTP 400 error. For example you can not include an `after_id` along with an `archived=false` in the same request. Can be used alongside `metadata` parameter.
  Query | updated_after | **date** |   (optional) | Adds support for filtering profiles based on the date of the latest modification made on them. Can be used alongside the after_id parameter.

### Return type
[**GetSchemaMappedProfilesCollection200Response**](../models/get-schema-mapped-profiles-collection200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetSchemaMappedProfilesCollection200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profiles_api import ProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_schema_mapped_profiles_collection200_response import GetSchemaMappedProfilesCollection200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    exclude_attributes = False # bool | Allows for optimization by not returning the associated attribute data for the returned profiles (optional) (default to False) # bool | Allows for optimization by not returning the associated attribute data for the returned profiles (optional) (default to False)
    name = 'name' # str | object name for filtering (optional) # str | object name for filtering (optional)
    profile_type_id = '79ed1cb6-9977-4965-9bfe-f2bcc242523e' # str | Profile Type ID for filtering (optional) # str | Profile Type ID for filtering (optional)
    status = 'Active' # str | status value for filtering (optional) # str | status value for filtering (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)
    after_id = '4eaa719f-4312-4c5b-9264-d0eb04d4a02a' # str | Represents the ID where the query should begin from. If blank, it represents the first ID. When used, forces sorting by ID ascending and does not allow use of `offset`. When `after_id` is specified it changes the mode of the API such that any filter parameters other than `profile_type_id`, `limit`, and `offset` are not supported and will be either silently ignored or result in an HTTP 400 error. For example you can not include an `after_id` along with an `archived=false` in the same request. Can be used alongside `metadata` parameter. (optional) # str | Represents the ID where the query should begin from. If blank, it represents the first ID. When used, forces sorting by ID ascending and does not allow use of `offset`. When `after_id` is specified it changes the mode of the API such that any filter parameters other than `profile_type_id`, `limit`, and `offset` are not supported and will be either silently ignored or result in an HTTP 400 error. For example you can not include an `after_id` along with an `archived=false` in the same request. Can be used alongside `metadata` parameter. (optional)
    updated_after = 'Sun May 04 20:00:00 EDT 2025' # date | Adds support for filtering profiles based on the date of the latest modification made on them. Can be used alongside the after_id parameter. (optional) # date | Adds support for filtering profiles based on the date of the latest modification made on them. Can be used alongside the after_id parameter. (optional)

    try:
        # Get profiles
        
        results = ProfilesApi(api_client).get_profiles()
        # Below is a request that includes all optional parameters
        # results = ProfilesApi(api_client).get_profiles(limit, offset, order, exclude_attributes, name, profile_type_id, status, metadata, after_id, updated_after)
        print("The response of ProfilesApi->get_profiles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfilesApi->get_profiles: %s\n" % e)
```



[[Back to top]](#) 

## patch-profile-by-id
Update a profile by id
Update a profile by id

[API Spec](https://developer.sailpoint.com/docs/api//patch-profile-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | submit_profile_request | [**SubmitProfileRequest**](../models/submit-profile-request) | True  | 

### Return type
[**GetSingleSchemaMappedProfile200Response**](../models/get-single-schema-mapped-profile200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetSingleSchemaMappedProfile200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profiles_api import ProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_single_schema_mapped_profile200_response import GetSingleSchemaMappedProfile200Response
from sailpoint.nerm.models.submit_profile_request import SubmitProfileRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    submit_profile_request = '''sailpoint.nerm.SubmitProfileRequest()''' # SubmitProfileRequest | 

    try:
        # Update a profile by id
        new_submit_profile_request = SubmitProfileRequest.from_json(submit_profile_request)
        results = ProfilesApi(api_client).patch_profile_by_id(id=id, submit_profile_request=new_submit_profile_request)
        # Below is a request that includes all optional parameters
        # results = ProfilesApi(api_client).patch_profile_by_id(id, new_submit_profile_request)
        print("The response of ProfilesApi->patch_profile_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfilesApi->patch_profile_by_id: %s\n" % e)
```



[[Back to top]](#) 

## patch-profiles
Update multiple profiles
Update multiple profiles

[API Spec](https://developer.sailpoint.com/docs/api//patch-profiles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_profiles_request | [**CreateProfilesRequest**](../models/create-profiles-request) | True  | 

### Return type
[**SearchAdvancedSearch200Response**](../models/search-advanced-search200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SearchAdvancedSearch200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profiles_api import ProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_profiles_request import CreateProfilesRequest
from sailpoint.nerm.models.search_advanced_search200_response import SearchAdvancedSearch200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_profiles_request = '''sailpoint.nerm.CreateProfilesRequest()''' # CreateProfilesRequest | 

    try:
        # Update multiple profiles
        new_create_profiles_request = CreateProfilesRequest.from_json(create_profiles_request)
        results = ProfilesApi(api_client).patch_profiles(create_profiles_request=new_create_profiles_request)
        # Below is a request that includes all optional parameters
        # results = ProfilesApi(api_client).patch_profiles(new_create_profiles_request)
        print("The response of ProfilesApi->patch_profiles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfilesApi->patch_profiles: %s\n" % e)
```



[[Back to top]](#) 

## submit-profile
Create a profile
Create a profile

[API Spec](https://developer.sailpoint.com/docs/api//submit-profile)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_profile_request | [**SubmitProfileRequest**](../models/submit-profile-request) | True  | 

### Return type
[**GetSingleSchemaMappedProfile200Response**](../models/get-single-schema-mapped-profile200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetSingleSchemaMappedProfile200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profiles_api import ProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_single_schema_mapped_profile200_response import GetSingleSchemaMappedProfile200Response
from sailpoint.nerm.models.submit_profile_request import SubmitProfileRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_profile_request = '''sailpoint.nerm.SubmitProfileRequest()''' # SubmitProfileRequest | 

    try:
        # Create a profile
        new_submit_profile_request = SubmitProfileRequest.from_json(submit_profile_request)
        results = ProfilesApi(api_client).submit_profile(submit_profile_request=new_submit_profile_request)
        # Below is a request that includes all optional parameters
        # results = ProfilesApi(api_client).submit_profile(new_submit_profile_request)
        print("The response of ProfilesApi->submit_profile:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfilesApi->submit_profile: %s\n" % e)
```



[[Back to top]](#) 

## submit-profile-avatar
Uploads new profile avatar
Uploads a new profile avatar

[API Spec](https://developer.sailpoint.com/docs/api//submit-profile-avatar)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
   | file | **bytearray** |   (optional) | 

### Return type
[**Url**](../models/url)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | Url |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profiles_api import ProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.url import Url
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    file = None # bytearray |  (optional) # bytearray |  (optional)

    try:
        # Uploads new profile avatar
        
        results = ProfilesApi(api_client).submit_profile_avatar(id=id)
        # Below is a request that includes all optional parameters
        # results = ProfilesApi(api_client).submit_profile_avatar(id, file)
        print("The response of ProfilesApi->submit_profile_avatar:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfilesApi->submit_profile_avatar: %s\n" % e)
```



[[Back to top]](#) 

## submit-profile-upload
Uploads profile attachment attribute
Uploads a new attachment attribute value to a profile. The upload must be a FORM data type; this is not a JSON API. The upload must include the binary content of the payload under the 'file' named form element. The upload must not attempt to include the file name or its content type as a other form or JSON as parameters. The upload must not attempt to upload the file body as the POST body payload; it has to arrive as a FORM parameter. Do not use a `File/Binary` payload type for the POST operation in your API client.


[API Spec](https://developer.sailpoint.com/docs/api//submit-profile-upload)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
Path   | attribute_id | **str** | True  | The id of the attachment attribute
   | file | **bytearray** |   (optional) | 

### Return type
[**Url**](../models/url)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | Url |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profiles_api import ProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.url import Url
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    attribute_id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | The id of the attachment attribute # str | The id of the attachment attribute
    file = None # bytearray |  (optional) # bytearray |  (optional)

    try:
        # Uploads profile attachment attribute
        
        results = ProfilesApi(api_client).submit_profile_upload(id=id, attribute_id=attribute_id)
        # Below is a request that includes all optional parameters
        # results = ProfilesApi(api_client).submit_profile_upload(id, attribute_id, file)
        print("The response of ProfilesApi->submit_profile_upload:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfilesApi->submit_profile_upload: %s\n" % e)
```



[[Back to top]](#) 




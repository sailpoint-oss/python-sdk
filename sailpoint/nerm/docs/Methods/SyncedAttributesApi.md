---
id: synced-attributes
title: Synced_attributes
pagination_label: synced_attributes
sidebar_label: synced_attributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'synced_attributes', 'synced_attributes'] 
slug: /tools/sdk/python//methods/synced-attributes
tags: ['SDK', 'Software Development Kit', 'synced_attributes', 'synced_attributes']
---

# sailpoint.nerm.SyncedAttributesApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-synced-attribute**](#create-synced-attribute) | **POST** `/profile_types/{profile_type_id}/synced_attributes` | Create a synced attribute
[**delete-synced-attribute**](#delete-synced-attribute) | **DELETE** `/profile_types/{profile_type_id}/synced_attributes/{ne_attribute_id}` | Delete synced attribute
[**get-profile-type-attributes**](#get-profile-type-attributes) | **GET** `/profile_types/{profile_type_id}/ne_attributes` | profile_types/ne_attributes synced status


## create-synced-attribute
Create a synced attribute
Create synced attribute

[API Spec](https://developer.sailpoint.com/docs/api//create-synced-attribute)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | synced_attribute1 | [**SyncedAttribute1**](../models/synced-attribute1) | True  | 

### Return type
[**CreateSyncedAttribute201Response**](../models/create-synced-attribute201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
201 | Expected response to a valid request | CreateSyncedAttribute201Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.synced_attributes_api import SyncedAttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_synced_attribute201_response import CreateSyncedAttribute201Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    synced_attribute1 = '''{'key': sailpoint.nerm.SyncedAttribute1()}''' # SyncedAttribute1 | 

    try:
        # Create a synced attribute
        new_synced_attribute1 = SyncedAttribute1.from_json(synced_attribute1)
        results = SyncedAttributesApi(api_client).create_synced_attribute(synced_attribute1=new_synced_attribute1)
        # Below is a request that includes all optional parameters
        # results = SyncedAttributesApi(api_client).create_synced_attribute(new_synced_attribute1)
        print("The response of SyncedAttributesApi->create_synced_attribute:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling SyncedAttributesApi->create_synced_attribute: %s\n" % e)
```



[[Back to top]](#) 

## delete-synced-attribute
Delete synced attribute
Delete a synced attribute.

[API Spec](https://developer.sailpoint.com/docs/api//delete-synced-attribute)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | profile_type_id | **str** |   (optional) | Profile Type ID for filtering
  Query | ne_attribute_id | **str** |   (optional) | ID of an attribute for filtering

### Return type
[**DeleteProfileTypeById200Response**](../models/delete-profile-type-by-id200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Info about the operation | DeleteProfileTypeById200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.synced_attributes_api import SyncedAttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.delete_profile_type_by_id200_response import DeleteProfileTypeById200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    profile_type_id = '79ed1cb6-9977-4965-9bfe-f2bcc242523e' # str | Profile Type ID for filtering (optional) # str | Profile Type ID for filtering (optional)
    ne_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8' # str | ID of an attribute for filtering (optional) # str | ID of an attribute for filtering (optional)

    try:
        # Delete synced attribute
        
        results = SyncedAttributesApi(api_client).delete_synced_attribute()
        # Below is a request that includes all optional parameters
        # results = SyncedAttributesApi(api_client).delete_synced_attribute(profile_type_id, ne_attribute_id)
        print("The response of SyncedAttributesApi->delete_synced_attribute:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling SyncedAttributesApi->delete_synced_attribute: %s\n" % e)
```



[[Back to top]](#) 

## get-profile-type-attributes
profile_types/ne_attributes synced status
Get ne attributes and synced attribute relationship to profile type.

[API Spec](https://developer.sailpoint.com/docs/api//get-profile-type-attributes)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | profile_type_id | **str** |   (optional) | Profile Type ID for filtering
  Query | active_filter | **str** |   (optional) | Filter for profile type synced attributes
  Query | search | **str** |   (optional) | Filter by string
  Query | page | **int** |   (optional) | Pagination items per page
  Query | sort | [**GetProfileTypeAttributesSortParameter**](../models/get-profile-type-attributes-sort-parameter) |   (optional) | How records should be sorted

### Return type
[**GetProfileTypeAttributes200Response**](../models/get-profile-type-attributes200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetProfileTypeAttributes200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.synced_attributes_api import SyncedAttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_profile_type_attributes200_response import GetProfileTypeAttributes200Response
from sailpoint.nerm.models.get_profile_type_attributes_sort_parameter import GetProfileTypeAttributesSortParameter
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    profile_type_id = '79ed1cb6-9977-4965-9bfe-f2bcc242523e' # str | Profile Type ID for filtering (optional) # str | Profile Type ID for filtering (optional)
    active_filter = 'all' # str | Filter for profile type synced attributes (optional) # str | Filter for profile type synced attributes (optional)
    search = 'search' # str | Filter by string (optional) # str | Filter by string (optional)
    page = 5 # int | Pagination items per page (optional) # int | Pagination items per page (optional)
    sort = '''sailpoint.nerm.GetProfileTypeAttributesSortParameter()''' # GetProfileTypeAttributesSortParameter | How records should be sorted (optional)

    try:
        # profile_types/ne_attributes synced status
        
        results = SyncedAttributesApi(api_client).get_profile_type_attributes()
        # Below is a request that includes all optional parameters
        # results = SyncedAttributesApi(api_client).get_profile_type_attributes(profile_type_id, active_filter, search, page, sort)
        print("The response of SyncedAttributesApi->get_profile_type_attributes:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling SyncedAttributesApi->get_profile_type_attributes: %s\n" % e)
```



[[Back to top]](#) 




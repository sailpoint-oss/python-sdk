---
id: isc-accounts
title: Isc_accounts
pagination_label: isc_accounts
sidebar_label: isc_accounts
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'isc_accounts', 'isc_accounts'] 
slug: /tools/sdk/python//methods/isc-accounts
tags: ['SDK', 'Software Development Kit', 'isc_accounts', 'isc_accounts']
---

# sailpoint.nerm.IscAccountsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-schema-mapped-profiles-collection**](#get-schema-mapped-profiles-collection) | **GET** `/isc/accounts` | Get Profiles
[**get-single-schema-mapped-profile**](#get-single-schema-mapped-profile) | **GET** `/isc/accounts/{id}` | Get Profile
[**update-profile**](#update-profile) | **PATCH** `/isc/accounts/{id}` | Update Profile


## get-schema-mapped-profiles-collection
Get Profiles
Retrieve schema-mapped profiles collection. It returns a collection of stored profiles, optionally using schema-mapped field names if requested.

[API Spec](https://developer.sailpoint.com/docs/api//get-schema-mapped-profiles-collection)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | use_schema | **bool** |   (optional) (default to False) | The use_schema parameter returns schema-mapped field names in the Profiles API response when set to true.
  Query | override_sync_toggle | **bool** |   (optional) (default to False) | The override_sync_toggle parameter returns all non-employee and assignment profiles regardless of the sync status when set to true.
  Query | category | **str** |   (optional) | Filters profiles by profile type category
  Query | status | **str** |   (optional) | The status of the profile. It can be multiple values with comma separated.

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
from sailpoint.nerm.api.isc_accounts_api import IscAccountsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_schema_mapped_profiles_collection200_response import GetSchemaMappedProfilesCollection200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    use_schema = False # bool | The use_schema parameter returns schema-mapped field names in the Profiles API response when set to true. (optional) (default to False) # bool | The use_schema parameter returns schema-mapped field names in the Profiles API response when set to true. (optional) (default to False)
    override_sync_toggle = False # bool | The override_sync_toggle parameter returns all non-employee and assignment profiles regardless of the sync status when set to true. (optional) (default to False) # bool | The override_sync_toggle parameter returns all non-employee and assignment profiles regardless of the sync status when set to true. (optional) (default to False)
    category = 'non-employee' # str | Filters profiles by profile type category (optional) # str | Filters profiles by profile type category (optional)
    status = 'active,on leave' # str | The status of the profile. It can be multiple values with comma separated. (optional) # str | The status of the profile. It can be multiple values with comma separated. (optional)

    try:
        # Get Profiles
        
        results = IscAccountsApi(api_client).get_schema_mapped_profiles_collection()
        # Below is a request that includes all optional parameters
        # results = IscAccountsApi(api_client).get_schema_mapped_profiles_collection(limit, offset, use_schema, override_sync_toggle, category, status)
        print("The response of IscAccountsApi->get_schema_mapped_profiles_collection:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IscAccountsApi->get_schema_mapped_profiles_collection: %s\n" % e)
```



[[Back to top]](#) 

## get-single-schema-mapped-profile
Get Profile
It returns a single stored profile, optionally with schema-mapped field names.

[API Spec](https://developer.sailpoint.com/docs/api//get-single-schema-mapped-profile)

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
from sailpoint.nerm.api.isc_accounts_api import IscAccountsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_single_schema_mapped_profile200_response import GetSingleSchemaMappedProfile200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Get Profile
        
        results = IscAccountsApi(api_client).get_single_schema_mapped_profile(id=id)
        # Below is a request that includes all optional parameters
        # results = IscAccountsApi(api_client).get_single_schema_mapped_profile(id)
        print("The response of IscAccountsApi->get_single_schema_mapped_profile:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IscAccountsApi->get_single_schema_mapped_profile: %s\n" % e)
```



[[Back to top]](#) 

## update-profile
Update Profile
Updates a profile only through ISC schema-mapped attributes, performs a reverse mapping to match the NERM attributes to update.

[API Spec](https://developer.sailpoint.com/docs/api//update-profile)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | update_profile_request | [**UpdateProfileRequest**](../models/update-profile-request) |   (optional) | 

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
from sailpoint.nerm.api.isc_accounts_api import IscAccountsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_single_schema_mapped_profile200_response import GetSingleSchemaMappedProfile200Response
from sailpoint.nerm.models.update_profile_request import UpdateProfileRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    update_profile_request = '''sailpoint.nerm.UpdateProfileRequest()''' # UpdateProfileRequest |  (optional)

    try:
        # Update Profile
        
        results = IscAccountsApi(api_client).update_profile(id=id)
        # Below is a request that includes all optional parameters
        # results = IscAccountsApi(api_client).update_profile(id, new_update_profile_request)
        print("The response of IscAccountsApi->update_profile:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IscAccountsApi->update_profile: %s\n" % e)
```



[[Back to top]](#) 




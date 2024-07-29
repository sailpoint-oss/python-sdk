# sailpoint.v3.IdentityProfilesApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity_profile**](IdentityProfilesApi.md#create_identity_profile) | **POST** /identity-profiles | Create an Identity Profile
[**delete_identity_profile**](IdentityProfilesApi.md#delete_identity_profile) | **DELETE** /identity-profiles/{identity-profile-id} | Delete an Identity Profile
[**delete_identity_profiles**](IdentityProfilesApi.md#delete_identity_profiles) | **POST** /identity-profiles/bulk-delete | Delete Identity Profiles
[**export_identity_profiles**](IdentityProfilesApi.md#export_identity_profiles) | **GET** /identity-profiles/export | Export Identity Profiles
[**get_default_identity_attribute_config**](IdentityProfilesApi.md#get_default_identity_attribute_config) | **GET** /identity-profiles/{identity-profile-id}/default-identity-attribute-config | Get default Identity Attribute Config
[**get_identity_profile**](IdentityProfilesApi.md#get_identity_profile) | **GET** /identity-profiles/{identity-profile-id} | Get single Identity Profile
[**import_identity_profiles**](IdentityProfilesApi.md#import_identity_profiles) | **POST** /identity-profiles/import | Import Identity Profiles
[**list_identity_profiles**](IdentityProfilesApi.md#list_identity_profiles) | **GET** /identity-profiles | Identity Profiles List
[**show_identity_preview**](IdentityProfilesApi.md#show_identity_preview) | **POST** /identity-profiles/identity-preview | Generate Identity Profile Preview
[**sync_identity_profile**](IdentityProfilesApi.md#sync_identity_profile) | **POST** /identity-profiles/{identity-profile-id}/process-identities | Process identities under profile
[**update_identity_profile**](IdentityProfilesApi.md#update_identity_profile) | **PATCH** /identity-profiles/{identity-profile-id} | Update the Identity Profile


# **create_identity_profile**
> IdentityProfile create_identity_profile(identity_profile)

Create an Identity Profile

This creates an Identity Profile.  A token with ORG_ADMIN authority is required to call this API to create an Identity Profile.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.identity_profile import IdentityProfile
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
    api_instance = sailpoint.v3.IdentityProfilesApi(api_client)
    identity_profile = sailpoint.v3.IdentityProfile() # IdentityProfile | 

    try:
        # Create an Identity Profile
        api_response = api_instance.create_identity_profile(identity_profile)
        print("The response of IdentityProfilesApi->create_identity_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProfilesApi->create_identity_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_profile** | [**IdentityProfile**](IdentityProfile.md)|  | 

### Return type

[**IdentityProfile**](IdentityProfile.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Identity Profile |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_profile**
> TaskResultSimplified delete_identity_profile(identity_profile_id)

Delete an Identity Profile

This deletes an Identity Profile based on ID.  On success, this endpoint will return a reference to the bulk delete task result.  A token with ORG_ADMIN authority is required to call this API.  The following rights are required to access this endpoint: idn:identity-profile:delete

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.task_result_simplified import TaskResultSimplified
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
    api_instance = sailpoint.v3.IdentityProfilesApi(api_client)
    identity_profile_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The Identity Profile ID.

    try:
        # Delete an Identity Profile
        api_response = api_instance.delete_identity_profile(identity_profile_id)
        print("The response of IdentityProfilesApi->delete_identity_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProfilesApi->delete_identity_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_profile_id** | **str**| The Identity Profile ID. | 

### Return type

[**TaskResultSimplified**](TaskResultSimplified.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted - Returns a TaskResult object referencing the bulk delete job created. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_profiles**
> TaskResultSimplified delete_identity_profiles(request_body)

Delete Identity Profiles

This deletes multiple Identity Profiles via a list of supplied IDs.  On success, this endpoint will return a reference to the bulk delete task result.  A token with ORG_ADMIN authority is required to call this API.  The following rights are required to access this endpoint: idn:identity-profile:delete

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.task_result_simplified import TaskResultSimplified
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
    api_instance = sailpoint.v3.IdentityProfilesApi(api_client)
    request_body = ['request_body_example'] # List[str] | Identity Profile bulk delete request body.

    try:
        # Delete Identity Profiles
        api_response = api_instance.delete_identity_profiles(request_body)
        print("The response of IdentityProfilesApi->delete_identity_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProfilesApi->delete_identity_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Identity Profile bulk delete request body. | 

### Return type

[**TaskResultSimplified**](TaskResultSimplified.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted - Returns a TaskResult object referencing the bulk delete job created. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_identity_profiles**
> List[IdentityProfileExportedObject] export_identity_profiles(limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)

Export Identity Profiles

This exports existing identity profiles in the format specified by the sp-config service.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.identity_profile_exported_object import IdentityProfileExportedObject
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
    api_instance = sailpoint.v3.IdentityProfilesApi(api_client)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'id eq \"ef38f94347e94562b5bb8424a56397d8\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, ne*  **name**: *eq, ne*  **priority**: *eq, ne* (optional)
    sorters = 'id,name' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **id, name, priority** (optional)

    try:
        # Export Identity Profiles
        api_response = api_instance.export_identity_profiles(limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)
        print("The response of IdentityProfilesApi->export_identity_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProfilesApi->export_identity_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, ne*  **name**: *eq, ne*  **priority**: *eq, ne* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **id, name, priority** | [optional] 

### Return type

[**List[IdentityProfileExportedObject]**](IdentityProfileExportedObject.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of export objects with identity profiles. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_identity_attribute_config**
> IdentityAttributeConfig get_default_identity_attribute_config(identity_profile_id)

Get default Identity Attribute Config

This returns the default identity attribute config. A token with ORG_ADMIN authority is required to call this API to get the default identity attribute config.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.identity_attribute_config import IdentityAttributeConfig
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
    api_instance = sailpoint.v3.IdentityProfilesApi(api_client)
    identity_profile_id = '2b838de9-db9b-abcf-e646-d4f274ad4238' # str | The Identity Profile ID.

    try:
        # Get default Identity Attribute Config
        api_response = api_instance.get_default_identity_attribute_config(identity_profile_id)
        print("The response of IdentityProfilesApi->get_default_identity_attribute_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProfilesApi->get_default_identity_attribute_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_profile_id** | **str**| The Identity Profile ID. | 

### Return type

[**IdentityAttributeConfig**](IdentityAttributeConfig.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Identity Attribute Config object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_profile**
> IdentityProfile get_identity_profile(identity_profile_id)

Get single Identity Profile

This returns a single Identity Profile based on ID.  A token with ORG_ADMIN or API authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.identity_profile import IdentityProfile
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
    api_instance = sailpoint.v3.IdentityProfilesApi(api_client)
    identity_profile_id = '2b838de9-db9b-abcf-e646-d4f274ad4238' # str | The Identity Profile ID.

    try:
        # Get single Identity Profile
        api_response = api_instance.get_identity_profile(identity_profile_id)
        print("The response of IdentityProfilesApi->get_identity_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProfilesApi->get_identity_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_profile_id** | **str**| The Identity Profile ID. | 

### Return type

[**IdentityProfile**](IdentityProfile.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Identity Profile object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_identity_profiles**
> ObjectImportResult import_identity_profiles(identity_profile_exported_object)

Import Identity Profiles

This imports previously exported identity profiles.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.identity_profile_exported_object import IdentityProfileExportedObject
from sailpoint.v3.models.object_import_result import ObjectImportResult
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
    api_instance = sailpoint.v3.IdentityProfilesApi(api_client)
    identity_profile_exported_object = [sailpoint.v3.IdentityProfileExportedObject()] # List[IdentityProfileExportedObject] | Previously exported Identity Profiles.

    try:
        # Import Identity Profiles
        api_response = api_instance.import_identity_profiles(identity_profile_exported_object)
        print("The response of IdentityProfilesApi->import_identity_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProfilesApi->import_identity_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_profile_exported_object** | [**List[IdentityProfileExportedObject]**](IdentityProfileExportedObject.md)| Previously exported Identity Profiles. | 

### Return type

[**ObjectImportResult**](ObjectImportResult.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of importing Identity Profiles. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identity_profiles**
> List[IdentityProfile] list_identity_profiles(limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)

Identity Profiles List

This returns a list of Identity Profiles based on the specified query parameters. A token with ORG_ADMIN or API authority is required to call this API to get a list of Identity Profiles.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.identity_profile import IdentityProfile
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
    api_instance = sailpoint.v3.IdentityProfilesApi(api_client)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'id eq \"ef38f94347e94562b5bb8424a56397d8\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, ne, ge, gt, in, le, lt, isnull, sw*  **name**: *eq, ne, in, le, lt, isnull, sw*  **priority**: *eq, ne* (optional)
    sorters = 'id,name' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **id, name, priority, created, modified, owner.id, owner.name** (optional)

    try:
        # Identity Profiles List
        api_response = api_instance.list_identity_profiles(limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)
        print("The response of IdentityProfilesApi->list_identity_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProfilesApi->list_identity_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, ne, ge, gt, in, le, lt, isnull, sw*  **name**: *eq, ne, in, le, lt, isnull, sw*  **priority**: *eq, ne* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **id, name, priority, created, modified, owner.id, owner.name** | [optional] 

### Return type

[**List[IdentityProfile]**](IdentityProfile.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of identityProfiles. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_identity_preview**
> IdentityPreviewResponse show_identity_preview(identity_preview_request)

Generate Identity Profile Preview

Use this API to generate a non-persisted preview of the identity object after applying `IdentityAttributeConfig` sent in request body. This API only allows `accountAttribute`, `reference` and `rule` transform types in the `IdentityAttributeConfig` sent in the request body. A token with ORG_ADMIN authority is required to call this API to generate an identity preview.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.identity_preview_request import IdentityPreviewRequest
from sailpoint.v3.models.identity_preview_response import IdentityPreviewResponse
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
    api_instance = sailpoint.v3.IdentityProfilesApi(api_client)
    identity_preview_request = sailpoint.v3.IdentityPreviewRequest() # IdentityPreviewRequest | Identity Preview request body.

    try:
        # Generate Identity Profile Preview
        api_response = api_instance.show_identity_preview(identity_preview_request)
        print("The response of IdentityProfilesApi->show_identity_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProfilesApi->show_identity_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_preview_request** | [**IdentityPreviewRequest**](IdentityPreviewRequest.md)| Identity Preview request body. | 

### Return type

[**IdentityPreviewResponse**](IdentityPreviewResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A preview of the identity attributes after applying identity attributes config sent in request body. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_identity_profile**
> object sync_identity_profile(identity_profile_id)

Process identities under profile

Process identities under the profile This operation should not be used to schedule your own identity processing or to perform system wide identity refreshes. The system will use a combination of [event-based processing](https://documentation.sailpoint.com/saas/help/setup/identity_processing.html?h=process#event-based-processing) and [scheduled processing](https://documentation.sailpoint.com/saas/help/setup/identity_processing.html?h=process#scheduled-processing) that runs every day at 8:00 AM and 8:00 PM in the tenant's timezone to keep your identities synchronized.  This should only be run on identity profiles that have the `identityRefreshRequired` attribute set to `true`. If `identityRefreshRequired` is false, then there is no benefit to running this operation. Typically, this operation is performed when a change is made to the identity profile or its related lifecycle states that requires a refresh. This operation will perform the following activities on all identities under the identity profile. 1. Updates identity attribute according to the identity profile mappings. 2. Determines the identity's correct manager through manager correlation. 3. Updates the identity's access according to their assigned lifecycle state. 4. Updates the identity's access based on role assignment criteria. A token with ORG_ADMIN authority is required to call this API.

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
    api_instance = sailpoint.v3.IdentityProfilesApi(api_client)
    identity_profile_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The Identity Profile ID to be processed

    try:
        # Process identities under profile
        api_response = api_instance.sync_identity_profile(identity_profile_id)
        print("The response of IdentityProfilesApi->sync_identity_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProfilesApi->sync_identity_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_profile_id** | **str**| The Identity Profile ID to be processed | 

### Return type

**object**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted - Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_identity_profile**
> IdentityProfile update_identity_profile(identity_profile_id, json_patch_operation)

Update the Identity Profile

This updates the specified Identity Profile.  A token with ORG_ADMIN authority is required to call this API to update the Identity Profile.  Some fields of the Schema cannot be updated. These fields are listed below: * id * name * created * modified * identityCount * identityRefreshRequired * Authoritative Source and Identity Attribute Configuration cannot be modified at once.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.identity_profile import IdentityProfile
from sailpoint.v3.models.json_patch_operation import JsonPatchOperation
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
    api_instance = sailpoint.v3.IdentityProfilesApi(api_client)
    identity_profile_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The Identity Profile ID
    json_patch_operation = [{op=add, path=/identityAttributeConfig/attributeTransforms/0, value={identityAttributeName=location, transformDefinition={type=accountAttribute, attributes={sourceName=Employees, attributeName=location, sourceId=2c91808878b7d63b0178c66ffcdc4ce4}}}}] # List[JsonPatchOperation] | A list of Identity Profile update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.

    try:
        # Update the Identity Profile
        api_response = api_instance.update_identity_profile(identity_profile_id, json_patch_operation)
        print("The response of IdentityProfilesApi->update_identity_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProfilesApi->update_identity_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_profile_id** | **str**| The Identity Profile ID | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| A list of Identity Profile update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. | 

### Return type

[**IdentityProfile**](IdentityProfile.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Identity Profile. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


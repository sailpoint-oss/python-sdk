# sailpoint.v2024.ConfigurationHubApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object_mapping**](ConfigurationHubApi.md#create_object_mapping) | **POST** /configuration-hub/object-mappings/{sourceOrg} | Creates an object mapping
[**create_object_mappings**](ConfigurationHubApi.md#create_object_mappings) | **POST** /configuration-hub/object-mappings/{sourceOrg}/bulk-create | Bulk creates object mappings
[**create_uploaded_configuration**](ConfigurationHubApi.md#create_uploaded_configuration) | **POST** /configuration-hub/backups/uploads | Upload a Configuration
[**delete_backup**](ConfigurationHubApi.md#delete_backup) | **DELETE** /configuration-hub/backups/{id} | Delete a Backup
[**delete_draft**](ConfigurationHubApi.md#delete_draft) | **DELETE** /configuration-hub/drafts/{id} | Delete a draft
[**delete_object_mapping**](ConfigurationHubApi.md#delete_object_mapping) | **DELETE** /configuration-hub/object-mappings/{sourceOrg}/{objectMappingId} | Deletes an object mapping
[**delete_uploaded_configuration**](ConfigurationHubApi.md#delete_uploaded_configuration) | **DELETE** /configuration-hub/backups/uploads/{id} | Delete an Uploaded Configuration
[**get_object_mappings**](ConfigurationHubApi.md#get_object_mappings) | **GET** /configuration-hub/object-mappings/{sourceOrg} | Gets list of object mappings
[**get_uploaded_configuration**](ConfigurationHubApi.md#get_uploaded_configuration) | **GET** /configuration-hub/backups/uploads/{id} | Get an Uploaded Configuration
[**list_backups**](ConfigurationHubApi.md#list_backups) | **GET** /configuration-hub/backups | List Backups
[**list_drafts**](ConfigurationHubApi.md#list_drafts) | **GET** /configuration-hub/drafts | List Drafts
[**list_uploaded_configurations**](ConfigurationHubApi.md#list_uploaded_configurations) | **GET** /configuration-hub/backups/uploads | List Uploaded Configurations
[**update_object_mappings**](ConfigurationHubApi.md#update_object_mappings) | **POST** /configuration-hub/object-mappings/{sourceOrg}/bulk-patch | Bulk updates object mappings


# **create_object_mapping**
> ObjectMappingResponse create_object_mapping(source_org, object_mapping_request)

Creates an object mapping

This creates an object mapping between current org and source org. Source org should be \"default\" when creating an object mapping that is not to be associated to any particular org. The request will need the following security scope: - sp:config-object-mapping:manage

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.object_mapping_request import ObjectMappingRequest
from sailpoint.v2024.models.object_mapping_response import ObjectMappingResponse
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.ConfigurationHubApi(api_client)
    source_org = 'source-org' # str | The name of the source org.
    object_mapping_request = {objectType=GOVERNANCE_GROUP, jsonPath=$.description, sourceValue=Sample Governance Group, targetValue=Sample Governance Group - Updated, enabled=true} # ObjectMappingRequest | The object mapping request body.

    try:
        # Creates an object mapping
        api_response = api_instance.create_object_mapping(source_org, object_mapping_request)
        print("The response of ConfigurationHubApi->create_object_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationHubApi->create_object_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_org** | **str**| The name of the source org. | 
 **object_mapping_request** | [**ObjectMappingRequest**](ObjectMappingRequest.md)| The object mapping request body. | 

### Return type

[**ObjectMappingResponse**](ObjectMappingResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created object mapping between current org and source org. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object_mappings**
> ObjectMappingBulkCreateResponse create_object_mappings(source_org, object_mapping_bulk_create_request)

Bulk creates object mappings

This creates a set of object mappings (Max 25) between current org and source org. Source org should be \"default\" when creating object mappings that are not to be associated to any particular org. The request will need the following security scope: - sp:config-object-mapping:manage

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.object_mapping_bulk_create_request import ObjectMappingBulkCreateRequest
from sailpoint.v2024.models.object_mapping_bulk_create_response import ObjectMappingBulkCreateResponse
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.ConfigurationHubApi(api_client)
    source_org = 'source-org' # str | The name of the source org.
    object_mapping_bulk_create_request = {newObjectsMappings=[{objectType=SOURCE, jsonPath=$.name, sourceValue=Original SOURCE Name, targetValue=New SOURCE Name, enabled=true}, {objectType=IDENTITY, jsonPath=$.name, sourceValue=Original IDENTITY Name, targetValue=New IDENTITY Name , enabled=true}]} # ObjectMappingBulkCreateRequest | The bulk create object mapping request body.

    try:
        # Bulk creates object mappings
        api_response = api_instance.create_object_mappings(source_org, object_mapping_bulk_create_request)
        print("The response of ConfigurationHubApi->create_object_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationHubApi->create_object_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_org** | **str**| The name of the source org. | 
 **object_mapping_bulk_create_request** | [**ObjectMappingBulkCreateRequest**](ObjectMappingBulkCreateRequest.md)| The bulk create object mapping request body. | 

### Return type

[**ObjectMappingBulkCreateResponse**](ObjectMappingBulkCreateResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created object mapping between current org and source org. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_uploaded_configuration**
> BackupResponse create_uploaded_configuration(data, name)

Upload a Configuration

This API uploads a JSON configuration file into a tenant.  Configuration files can be managed and deployed via Configuration Hub by uploading a json file which contains configuration data. The JSON file should be the same as the one used by our import endpoints. The object types supported by upload configuration file functionality are the same as the ones supported by our regular backup functionality.  Refer to [SaaS Configuration](https://developer.sailpoint.com/idn/docs/saas-configuration/#supported-objects) for more information about supported objects.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.backup_response import BackupResponse
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.ConfigurationHubApi(api_client)
    data = None # bytearray | JSON file containing the objects to be imported.
    name = 'name_example' # str | Name that will be assigned to the uploaded configuration file.

    try:
        # Upload a Configuration
        api_response = api_instance.create_uploaded_configuration(data, name)
        print("The response of ConfigurationHubApi->create_uploaded_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationHubApi->create_uploaded_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **bytearray**| JSON file containing the objects to be imported. | 
 **name** | **str**| Name that will be assigned to the uploaded configuration file. | 

### Return type

[**BackupResponse**](BackupResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Upload job accepted and queued for processing. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_backup**
> delete_backup(id)

Delete a Backup

This API deletes an existing backup for the current tenant.  On success, this endpoint will return an empty response.  The backup id can be obtained from the response after a backup was successfully created, or from the list backups endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.ConfigurationHubApi(api_client)
    id = '07659d7d-2cce-47c0-9e49-185787ee565a' # str | The id of the backup to delete.

    try:
        # Delete a Backup
        api_instance.delete_backup(id)
    except Exception as e:
        print("Exception when calling ConfigurationHubApi->delete_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the backup to delete. | 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

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
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_draft**
> delete_draft(id)

Delete a draft

This API deletes an existing draft for the current tenant.  On success, this endpoint will return an empty response.  The draft id can be obtained from the response after a draft was successfully created, or from the list drafts endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.ConfigurationHubApi(api_client)
    id = '07659d7d-2cce-47c0-9e49-185787ee565a' # str | The id of the draft to delete.

    try:
        # Delete a draft
        api_instance.delete_draft(id)
    except Exception as e:
        print("Exception when calling ConfigurationHubApi->delete_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the draft to delete. | 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

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
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_mapping**
> delete_object_mapping(source_org, object_mapping_id)

Deletes an object mapping

This deletes an existing object mapping. Source org should be \"default\" when deleting an object mapping that is not associated to any particular org. The request will need the following security scope: - sp:config-object-mapping:manage

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.ConfigurationHubApi(api_client)
    source_org = 'source-org' # str | The name of the source org.
    object_mapping_id = '3d6e0144-963f-4bd6-8d8d-d77b4e507ce4' # str | The id of the object mapping to be deleted.

    try:
        # Deletes an object mapping
        api_instance.delete_object_mapping(source_org, object_mapping_id)
    except Exception as e:
        print("Exception when calling ConfigurationHubApi->delete_object_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_org** | **str**| The name of the source org. | 
 **object_mapping_id** | **str**| The id of the object mapping to be deleted. | 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

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
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_uploaded_configuration**
> delete_uploaded_configuration(id)

Delete an Uploaded Configuration

This API deletes an uploaded configuration based on Id.  On success, this endpoint will return an empty response.  The uploaded configuration id can be obtained from the response after a successful upload, or the list uploaded configurations endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.ConfigurationHubApi(api_client)
    id = '3d0fe04b-57df-4a46-a83b-8f04b0f9d10b' # str | The id of the uploaded configuration.

    try:
        # Delete an Uploaded Configuration
        api_instance.delete_uploaded_configuration(id)
    except Exception as e:
        print("Exception when calling ConfigurationHubApi->delete_uploaded_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the uploaded configuration. | 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

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
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_mappings**
> List[ObjectMappingResponse] get_object_mappings(source_org)

Gets list of object mappings

This gets a list of existing object mappings between current org and source org. Source org should be \"default\" when getting object mappings that are not associated to any particular org. The request will need the following security scope: - sp:config-object-mapping:read

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.object_mapping_response import ObjectMappingResponse
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.ConfigurationHubApi(api_client)
    source_org = 'source-org' # str | The name of the source org.

    try:
        # Gets list of object mappings
        api_response = api_instance.get_object_mappings(source_org)
        print("The response of ConfigurationHubApi->get_object_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationHubApi->get_object_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_org** | **str**| The name of the source org. | 

### Return type

[**List[ObjectMappingResponse]**](ObjectMappingResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of existing object mappings between current org and source org. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_uploaded_configuration**
> BackupResponse get_uploaded_configuration(id)

Get an Uploaded Configuration

This API gets an existing uploaded configuration for the current tenant.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.backup_response import BackupResponse
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.ConfigurationHubApi(api_client)
    id = '3d0fe04b-57df-4a46-a83b-8f04b0f9d10b' # str | The id of the uploaded configuration.

    try:
        # Get an Uploaded Configuration
        api_response = api_instance.get_uploaded_configuration(id)
        print("The response of ConfigurationHubApi->get_uploaded_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationHubApi->get_uploaded_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the uploaded configuration. | 

### Return type

[**BackupResponse**](BackupResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets an uploaded configuration details. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_backups**
> List[BackupResponse] list_backups(filters=filters)

List Backups

This API gets a list of existing backups for the current tenant.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.backup_response import BackupResponse
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.ConfigurationHubApi(api_client)
    filters = 'status eq \"COMPLETE\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **status**: *eq* (optional)

    try:
        # List Backups
        api_response = api_instance.list_backups(filters=filters)
        print("The response of ConfigurationHubApi->list_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationHubApi->list_backups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **status**: *eq* | [optional] 

### Return type

[**List[BackupResponse]**](BackupResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of existing backups. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_drafts**
> List[DraftResponse] list_drafts(filters=filters)

List Drafts

This API gets a list of existing drafts for the current tenant.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.draft_response import DraftResponse
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.ConfigurationHubApi(api_client)
    filters = 'status eq \"COMPLETE\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **status**: *eq*  **approvalStatus**: *eq* (optional)

    try:
        # List Drafts
        api_response = api_instance.list_drafts(filters=filters)
        print("The response of ConfigurationHubApi->list_drafts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationHubApi->list_drafts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **status**: *eq*  **approvalStatus**: *eq* | [optional] 

### Return type

[**List[DraftResponse]**](DraftResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of existing drafts. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_uploaded_configurations**
> List[BackupResponse] list_uploaded_configurations(filters=filters)

List Uploaded Configurations

This API gets a list of existing uploaded configurations for the current tenant.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.backup_response import BackupResponse
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.ConfigurationHubApi(api_client)
    filters = 'status eq \"COMPLETE\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **status**: *eq* (optional)

    try:
        # List Uploaded Configurations
        api_response = api_instance.list_uploaded_configurations(filters=filters)
        print("The response of ConfigurationHubApi->list_uploaded_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationHubApi->list_uploaded_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **status**: *eq* | [optional] 

### Return type

[**List[BackupResponse]**](BackupResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of existing uploaded configurations. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_mappings**
> ObjectMappingBulkPatchResponse update_object_mappings(source_org, object_mapping_bulk_patch_request)

Bulk updates object mappings

This updates a set of object mappings, only enabled and targetValue fields can be updated. Source org should be \"default\" when updating object mappings that are not associated to any particular org. The request will need the following security scope: - sp:config-object-mapping:manage

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.object_mapping_bulk_patch_request import ObjectMappingBulkPatchRequest
from sailpoint.v2024.models.object_mapping_bulk_patch_response import ObjectMappingBulkPatchResponse
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.ConfigurationHubApi(api_client)
    source_org = 'source-org' # str | The name of the source org.
    object_mapping_bulk_patch_request = {patches={603b1a61-d03d-4ed1-864f-a508fbd1995d=[{op=replace, path=/enabled, value=true}], 00bece34-f50d-4227-8878-76f620b5a971=[{op=replace, path=/targetValue, value=New Target Value}]}} # ObjectMappingBulkPatchRequest | The object mapping request body.

    try:
        # Bulk updates object mappings
        api_response = api_instance.update_object_mappings(source_org, object_mapping_bulk_patch_request)
        print("The response of ConfigurationHubApi->update_object_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationHubApi->update_object_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_org** | **str**| The name of the source org. | 
 **object_mapping_bulk_patch_request** | [**ObjectMappingBulkPatchRequest**](ObjectMappingBulkPatchRequest.md)| The object mapping request body. | 

### Return type

[**ObjectMappingBulkPatchResponse**](ObjectMappingBulkPatchResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated object mappings. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


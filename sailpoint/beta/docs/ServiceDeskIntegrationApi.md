# beta.ServiceDeskIntegrationApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_desk_integration**](ServiceDeskIntegrationApi.md#create_service_desk_integration) | **POST** /service-desk-integrations | Create new Service Desk integration
[**delete_service_desk_integration**](ServiceDeskIntegrationApi.md#delete_service_desk_integration) | **DELETE** /service-desk-integrations/{id} | Delete a Service Desk integration
[**get_service_desk_integration**](ServiceDeskIntegrationApi.md#get_service_desk_integration) | **GET** /service-desk-integrations/{id} | Get a Service Desk integration
[**get_service_desk_integration_list**](ServiceDeskIntegrationApi.md#get_service_desk_integration_list) | **GET** /service-desk-integrations | List existing Service Desk Integrations
[**get_service_desk_integration_template**](ServiceDeskIntegrationApi.md#get_service_desk_integration_template) | **GET** /service-desk-integrations/templates/{scriptName} | Service Desk integration template by scriptName.
[**get_service_desk_integration_types**](ServiceDeskIntegrationApi.md#get_service_desk_integration_types) | **GET** /service-desk-integrations/types | Service Desk Integration Types List.
[**get_status_check_details**](ServiceDeskIntegrationApi.md#get_status_check_details) | **GET** /service-desk-integrations/status-check-configuration | Get the time check configuration
[**patch_service_desk_integration**](ServiceDeskIntegrationApi.md#patch_service_desk_integration) | **PATCH** /service-desk-integrations/{id} | Service Desk Integration Update PATCH
[**put_service_desk_integration**](ServiceDeskIntegrationApi.md#put_service_desk_integration) | **PUT** /service-desk-integrations/{id} | Update a Service Desk integration
[**update_status_check_details**](ServiceDeskIntegrationApi.md#update_status_check_details) | **PUT** /service-desk-integrations/status-check-configuration | Update the time check configuration


# **create_service_desk_integration**
> ServiceDeskIntegrationDto create_service_desk_integration(service_desk_integration_dto)

Create new Service Desk integration

Create a new Service Desk Integrations.  A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.service_desk_integration_dto import ServiceDeskIntegrationDto
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ServiceDeskIntegrationApi(api_client)
    service_desk_integration_dto = beta.ServiceDeskIntegrationDto() # ServiceDeskIntegrationDto | The specifics of a new integration to create

    try:
        # Create new Service Desk integration
        api_response = api_instance.create_service_desk_integration(service_desk_integration_dto)
        print("The response of ServiceDeskIntegrationApi->create_service_desk_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceDeskIntegrationApi->create_service_desk_integration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_desk_integration_dto** | [**ServiceDeskIntegrationDto**](ServiceDeskIntegrationDto.md)| The specifics of a new integration to create | 

### Return type

[**ServiceDeskIntegrationDto**](ServiceDeskIntegrationDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | details of the created integration |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_desk_integration**
> delete_service_desk_integration(id)

Delete a Service Desk integration

Delete an existing Service Desk integration by ID.  A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ServiceDeskIntegrationApi(api_client)
    id = 'anId' # str | ID of Service Desk integration to delete

    try:
        # Delete a Service Desk integration
        api_instance.delete_service_desk_integration(id)
    except Exception as e:
        print("Exception when calling ServiceDeskIntegrationApi->delete_service_desk_integration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Service Desk integration to delete | 

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
**204** | Service Desk integration with the given ID successfully deleted |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_desk_integration**
> ServiceDeskIntegrationDto get_service_desk_integration(id)

Get a Service Desk integration

Get an existing Service Desk integration by ID.  A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.service_desk_integration_dto import ServiceDeskIntegrationDto
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ServiceDeskIntegrationApi(api_client)
    id = 'anId' # str | ID of the Service Desk integration to get

    try:
        # Get a Service Desk integration
        api_response = api_instance.get_service_desk_integration(id)
        print("The response of ServiceDeskIntegrationApi->get_service_desk_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceDeskIntegrationApi->get_service_desk_integration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Service Desk integration to get | 

### Return type

[**ServiceDeskIntegrationDto**](ServiceDeskIntegrationDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServiceDeskIntegrationDto with the given ID |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_desk_integration_list**
> List[ServiceDeskIntegrationDto] get_service_desk_integration_list(offset=offset, limit=limit, sorters=sorters, filters=filters, count=count)

List existing Service Desk Integrations

Get a list of ServiceDeskIntegrationDto for existing Service Desk Integrations.  A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.service_desk_integration_dto import ServiceDeskIntegrationDto
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ServiceDeskIntegrationApi(api_client)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    sorters = 'name' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name** (optional)
    filters = 'id eq 2c91808b6ef1d43e016efba0ce470904' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq*  **type**: *eq, in*  **cluster**: *eq, in* (optional)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # List existing Service Desk Integrations
        api_response = api_instance.get_service_desk_integration_list(offset=offset, limit=limit, sorters=sorters, filters=filters, count=count)
        print("The response of ServiceDeskIntegrationApi->get_service_desk_integration_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceDeskIntegrationApi->get_service_desk_integration_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq*  **type**: *eq, in*  **cluster**: *eq, in* | [optional] 
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[ServiceDeskIntegrationDto]**](ServiceDeskIntegrationDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ServiceDeskIntegrationDto |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_desk_integration_template**
> ServiceDeskIntegrationTemplateDto get_service_desk_integration_template(script_name)

Service Desk integration template by scriptName.

This API endpoint returns an existing Service Desk integration template by scriptName.  A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.service_desk_integration_template_dto import ServiceDeskIntegrationTemplateDto
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ServiceDeskIntegrationApi(api_client)
    script_name = 'aScriptName' # str | The scriptName value of the Service Desk integration template to get

    try:
        # Service Desk integration template by scriptName.
        api_response = api_instance.get_service_desk_integration_template(script_name)
        print("The response of ServiceDeskIntegrationApi->get_service_desk_integration_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceDeskIntegrationApi->get_service_desk_integration_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_name** | **str**| The scriptName value of the Service Desk integration template to get | 

### Return type

[**ServiceDeskIntegrationTemplateDto**](ServiceDeskIntegrationTemplateDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with the ServiceDeskIntegrationTemplateDto with the specified scriptName. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_desk_integration_types**
> List[ServiceDeskIntegrationTemplateType] get_service_desk_integration_types()

Service Desk Integration Types List.

This API endpoint returns the current list of supported Service Desk integration types.  A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.service_desk_integration_template_type import ServiceDeskIntegrationTemplateType
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ServiceDeskIntegrationApi(api_client)

    try:
        # Service Desk Integration Types List.
        api_response = api_instance.get_service_desk_integration_types()
        print("The response of ServiceDeskIntegrationApi->get_service_desk_integration_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceDeskIntegrationApi->get_service_desk_integration_types: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ServiceDeskIntegrationTemplateType]**](ServiceDeskIntegrationTemplateType.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with an array of the currently supported Service Desk integration types. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_check_details**
> QueuedCheckConfigDetails get_status_check_details()

Get the time check configuration

Get the time check configuration of queued SDIM tickets.  A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.queued_check_config_details import QueuedCheckConfigDetails
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ServiceDeskIntegrationApi(api_client)

    try:
        # Get the time check configuration
        api_response = api_instance.get_status_check_details()
        print("The response of ServiceDeskIntegrationApi->get_status_check_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceDeskIntegrationApi->get_status_check_details: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**QueuedCheckConfigDetails**](QueuedCheckConfigDetails.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QueuedCheckConfigDetails containing the configured values |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_service_desk_integration**
> ServiceDeskIntegrationDto patch_service_desk_integration(id, json_patch)

Service Desk Integration Update PATCH

Update an existing ServiceDeskIntegration by ID with a PATCH request.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.json_patch import JsonPatch
from beta.models.service_desk_integration_dto import ServiceDeskIntegrationDto
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ServiceDeskIntegrationApi(api_client)
    id = 'anId' # str | ID of the Service Desk integration to update
    json_patch = [{op=replace, path=/ownerRef, value={id=2c9180867d05b227017d09921a205b4d, type=IDENTITY, name=Angelo2 tester}}] # JsonPatch | A list of SDIM update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  PATCH can only be applied to the following fields:   * `beforeProvisioningRule`   * `description`   * `ownerRef`  A 403 Forbidden Error indicates that you attempted to PATCH a field that is not allowed. 

    try:
        # Service Desk Integration Update PATCH
        api_response = api_instance.patch_service_desk_integration(id, json_patch)
        print("The response of ServiceDeskIntegrationApi->patch_service_desk_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceDeskIntegrationApi->patch_service_desk_integration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Service Desk integration to update | 
 **json_patch** | [**JsonPatch**](JsonPatch.md)| A list of SDIM update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  PATCH can only be applied to the following fields:   * &#x60;beforeProvisioningRule&#x60;   * &#x60;description&#x60;   * &#x60;ownerRef&#x60;  A 403 Forbidden Error indicates that you attempted to PATCH a field that is not allowed.  | 

### Return type

[**ServiceDeskIntegrationDto**](ServiceDeskIntegrationDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServiceDeskIntegrationDto as updated |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_desk_integration**
> ServiceDeskIntegrationDto put_service_desk_integration(id, service_desk_integration_dto)

Update a Service Desk integration

Update an existing Service Desk integration by ID with updated value in JSON form as the request body.  A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.service_desk_integration_dto import ServiceDeskIntegrationDto
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ServiceDeskIntegrationApi(api_client)
    id = 'anId' # str | ID of the Service Desk integration to update
    service_desk_integration_dto = beta.ServiceDeskIntegrationDto() # ServiceDeskIntegrationDto | The specifics of the integration to update

    try:
        # Update a Service Desk integration
        api_response = api_instance.put_service_desk_integration(id, service_desk_integration_dto)
        print("The response of ServiceDeskIntegrationApi->put_service_desk_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceDeskIntegrationApi->put_service_desk_integration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Service Desk integration to update | 
 **service_desk_integration_dto** | [**ServiceDeskIntegrationDto**](ServiceDeskIntegrationDto.md)| The specifics of the integration to update | 

### Return type

[**ServiceDeskIntegrationDto**](ServiceDeskIntegrationDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServiceDeskIntegrationDto as updated |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_status_check_details**
> QueuedCheckConfigDetails update_status_check_details(queued_check_config_details)

Update the time check configuration

Update the time check configuration of queued SDIM tickets.  A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.queued_check_config_details import QueuedCheckConfigDetails
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ServiceDeskIntegrationApi(api_client)
    queued_check_config_details = beta.QueuedCheckConfigDetails() # QueuedCheckConfigDetails | the modified time check configuration

    try:
        # Update the time check configuration
        api_response = api_instance.update_status_check_details(queued_check_config_details)
        print("The response of ServiceDeskIntegrationApi->update_status_check_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceDeskIntegrationApi->update_status_check_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queued_check_config_details** | [**QueuedCheckConfigDetails**](QueuedCheckConfigDetails.md)| the modified time check configuration | 

### Return type

[**QueuedCheckConfigDetails**](QueuedCheckConfigDetails.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QueuedCheckConfigDetails as updated |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# beta.ConnectorRuleManagementApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connector_rule**](ConnectorRuleManagementApi.md#create_connector_rule) | **POST** /connector-rules | Create Connector Rule
[**delete_connector_rule**](ConnectorRuleManagementApi.md#delete_connector_rule) | **DELETE** /connector-rules/{id} | Delete a Connector-Rule
[**get_connector_rule**](ConnectorRuleManagementApi.md#get_connector_rule) | **GET** /connector-rules/{id} | Connector-Rule by ID
[**get_connector_rule_list**](ConnectorRuleManagementApi.md#get_connector_rule_list) | **GET** /connector-rules | List Connector Rules
[**update_connector_rule**](ConnectorRuleManagementApi.md#update_connector_rule) | **PUT** /connector-rules/{id} | Update a Connector Rule
[**validate_connector_rule**](ConnectorRuleManagementApi.md#validate_connector_rule) | **POST** /connector-rules/validate | Validate Connector Rule


# **create_connector_rule**
> ConnectorRuleResponse create_connector_rule(connector_rule_create_request)

Create Connector Rule

Creates a new connector rule. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.connector_rule_create_request import ConnectorRuleCreateRequest
from beta.models.connector_rule_response import ConnectorRuleResponse
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
    api_instance = beta.ConnectorRuleManagementApi(api_client)
    connector_rule_create_request = beta.ConnectorRuleCreateRequest() # ConnectorRuleCreateRequest | The connector rule to create

    try:
        # Create Connector Rule
        api_response = api_instance.create_connector_rule(connector_rule_create_request)
        print("The response of ConnectorRuleManagementApi->create_connector_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorRuleManagementApi->create_connector_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_rule_create_request** | [**ConnectorRuleCreateRequest**](ConnectorRuleCreateRequest.md)| The connector rule to create | 

### Return type

[**ConnectorRuleResponse**](ConnectorRuleResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created connector rule |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connector_rule**
> delete_connector_rule(id)

Delete a Connector-Rule

Deletes the connector rule specified by the given ID. A token with ORG_ADMIN authority is required to call this API.

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
    api_instance = beta.ConnectorRuleManagementApi(api_client)
    id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | ID of the connector rule to delete

    try:
        # Delete a Connector-Rule
        api_instance.delete_connector_rule(id)
    except Exception as e:
        print("Exception when calling ConnectorRuleManagementApi->delete_connector_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the connector rule to delete | 

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

# **get_connector_rule**
> ConnectorRuleResponse get_connector_rule(id)

Connector-Rule by ID

Returns the connector rule specified by ID. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.connector_rule_response import ConnectorRuleResponse
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
    api_instance = beta.ConnectorRuleManagementApi(api_client)
    id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | ID of the connector rule to retrieve

    try:
        # Connector-Rule by ID
        api_response = api_instance.get_connector_rule(id)
        print("The response of ConnectorRuleManagementApi->get_connector_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorRuleManagementApi->get_connector_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the connector rule to retrieve | 

### Return type

[**ConnectorRuleResponse**](ConnectorRuleResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector rule with the given ID |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_rule_list**
> List[ConnectorRuleResponse] get_connector_rule_list()

List Connector Rules

Returns the list of connector rules. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.connector_rule_response import ConnectorRuleResponse
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
    api_instance = beta.ConnectorRuleManagementApi(api_client)

    try:
        # List Connector Rules
        api_response = api_instance.get_connector_rule_list()
        print("The response of ConnectorRuleManagementApi->get_connector_rule_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorRuleManagementApi->get_connector_rule_list: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ConnectorRuleResponse]**](ConnectorRuleResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of connector rules |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connector_rule**
> ConnectorRuleResponse update_connector_rule(id, connector_rule_update_request=connector_rule_update_request)

Update a Connector Rule

Updates an existing connector rule with the one provided in the request body. Note that the fields 'id', 'name', and 'type' are immutable. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.connector_rule_response import ConnectorRuleResponse
from beta.models.connector_rule_update_request import ConnectorRuleUpdateRequest
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
    api_instance = beta.ConnectorRuleManagementApi(api_client)
    id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | ID of the connector rule to update
    connector_rule_update_request = beta.ConnectorRuleUpdateRequest() # ConnectorRuleUpdateRequest | The connector rule with updated data (optional)

    try:
        # Update a Connector Rule
        api_response = api_instance.update_connector_rule(id, connector_rule_update_request=connector_rule_update_request)
        print("The response of ConnectorRuleManagementApi->update_connector_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorRuleManagementApi->update_connector_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the connector rule to update | 
 **connector_rule_update_request** | [**ConnectorRuleUpdateRequest**](ConnectorRuleUpdateRequest.md)| The connector rule with updated data | [optional] 

### Return type

[**ConnectorRuleResponse**](ConnectorRuleResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated connector rule |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_connector_rule**
> ConnectorRuleValidationResponse validate_connector_rule(source_code)

Validate Connector Rule

Returns a list of issues within the code to fix, if any. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.connector_rule_validation_response import ConnectorRuleValidationResponse
from beta.models.source_code import SourceCode
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
    api_instance = beta.ConnectorRuleManagementApi(api_client)
    source_code = beta.SourceCode() # SourceCode | The code to validate

    try:
        # Validate Connector Rule
        api_response = api_instance.validate_connector_rule(source_code)
        print("The response of ConnectorRuleManagementApi->validate_connector_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorRuleManagementApi->validate_connector_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_code** | [**SourceCode**](SourceCode.md)| The code to validate | 

### Return type

[**ConnectorRuleValidationResponse**](ConnectorRuleValidationResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of the code&#39;s eligibility as a connector rule |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


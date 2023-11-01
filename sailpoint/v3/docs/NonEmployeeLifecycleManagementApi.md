# v3.NonEmployeeLifecycleManagementApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_non_employee_request**](NonEmployeeLifecycleManagementApi.md#approve_non_employee_request) | **POST** /non-employee-approvals/{id}/approve | Approve a Non-Employee Request
[**create_non_employee_record**](NonEmployeeLifecycleManagementApi.md#create_non_employee_record) | **POST** /non-employee-records | Create Non-Employee Record
[**create_non_employee_request**](NonEmployeeLifecycleManagementApi.md#create_non_employee_request) | **POST** /non-employee-requests | Create Non-Employee Request
[**create_non_employee_source**](NonEmployeeLifecycleManagementApi.md#create_non_employee_source) | **POST** /non-employee-sources | Create Non-Employee Source
[**create_non_employee_source_schema_attributes**](NonEmployeeLifecycleManagementApi.md#create_non_employee_source_schema_attributes) | **POST** /non-employee-sources/{sourceId}/schema-attributes | Create a new Schema Attribute for Non-Employee Source
[**delete_non_employee_record**](NonEmployeeLifecycleManagementApi.md#delete_non_employee_record) | **DELETE** /non-employee-records/{id} | Delete Non-Employee Record
[**delete_non_employee_records_in_bulk**](NonEmployeeLifecycleManagementApi.md#delete_non_employee_records_in_bulk) | **POST** /non-employee-records/bulk-delete | Delete Multiple Non-Employee Records
[**delete_non_employee_request**](NonEmployeeLifecycleManagementApi.md#delete_non_employee_request) | **DELETE** /non-employee-requests/{id} | Delete Non-Employee Request
[**delete_non_employee_schema_attribute**](NonEmployeeLifecycleManagementApi.md#delete_non_employee_schema_attribute) | **DELETE** /non-employee-sources/{sourceId}/schema-attributes/{attributeId} | Delete a Schema Attribute for Non-Employee Source
[**delete_non_employee_source**](NonEmployeeLifecycleManagementApi.md#delete_non_employee_source) | **DELETE** /non-employee-sources/{sourceId} | Delete Non-Employee Source
[**delete_non_employee_source_schema_attributes**](NonEmployeeLifecycleManagementApi.md#delete_non_employee_source_schema_attributes) | **DELETE** /non-employee-sources/{sourceId}/schema-attributes | Delete all custom schema attributes for Non-Employee Source
[**export_non_employee_records**](NonEmployeeLifecycleManagementApi.md#export_non_employee_records) | **GET** /non-employee-sources/{id}/non-employees/download | Exports Non-Employee Records to CSV
[**export_non_employee_source_schema_template**](NonEmployeeLifecycleManagementApi.md#export_non_employee_source_schema_template) | **GET** /non-employee-sources/{id}/schema-attributes-template/download | Exports Source Schema Template
[**get_non_employee_approval**](NonEmployeeLifecycleManagementApi.md#get_non_employee_approval) | **GET** /non-employee-approvals/{id} | Get a non-employee approval item detail
[**get_non_employee_approval_summary**](NonEmployeeLifecycleManagementApi.md#get_non_employee_approval_summary) | **GET** /non-employee-approvals/summary/{requested-for} | Get Summary of Non-Employee Approval Requests
[**get_non_employee_bulk_upload_status**](NonEmployeeLifecycleManagementApi.md#get_non_employee_bulk_upload_status) | **GET** /non-employee-sources/{id}/non-employee-bulk-upload/status | Obtain the status of bulk upload on the source
[**get_non_employee_record**](NonEmployeeLifecycleManagementApi.md#get_non_employee_record) | **GET** /non-employee-records/{id} | Get a Non-Employee Record
[**get_non_employee_request**](NonEmployeeLifecycleManagementApi.md#get_non_employee_request) | **GET** /non-employee-requests/{id} | Get a Non-Employee Request
[**get_non_employee_request_summary**](NonEmployeeLifecycleManagementApi.md#get_non_employee_request_summary) | **GET** /non-employee-requests/summary/{requested-for} | Get Summary of Non-Employee Requests
[**get_non_employee_schema_attribute**](NonEmployeeLifecycleManagementApi.md#get_non_employee_schema_attribute) | **GET** /non-employee-sources/{sourceId}/schema-attributes/{attributeId} | Get Schema Attribute Non-Employee Source
[**get_non_employee_source**](NonEmployeeLifecycleManagementApi.md#get_non_employee_source) | **GET** /non-employee-sources/{sourceId} | Get a Non-Employee Source
[**get_non_employee_source_schema_attributes**](NonEmployeeLifecycleManagementApi.md#get_non_employee_source_schema_attributes) | **GET** /non-employee-sources/{sourceId}/schema-attributes | List Schema Attributes Non-Employee Source
[**import_non_employee_records_in_bulk**](NonEmployeeLifecycleManagementApi.md#import_non_employee_records_in_bulk) | **POST** /non-employee-sources/{id}/non-employee-bulk-upload | Imports, or Updates, Non-Employee Records
[**list_non_employee_approvals**](NonEmployeeLifecycleManagementApi.md#list_non_employee_approvals) | **GET** /non-employee-approvals | Get List of Non-Employee Approval Requests
[**list_non_employee_records**](NonEmployeeLifecycleManagementApi.md#list_non_employee_records) | **GET** /non-employee-records | List Non-Employee Records
[**list_non_employee_requests**](NonEmployeeLifecycleManagementApi.md#list_non_employee_requests) | **GET** /non-employee-requests | List Non-Employee Requests
[**list_non_employee_sources**](NonEmployeeLifecycleManagementApi.md#list_non_employee_sources) | **GET** /non-employee-sources | List Non-Employee Sources
[**patch_non_employee_record**](NonEmployeeLifecycleManagementApi.md#patch_non_employee_record) | **PATCH** /non-employee-records/{id} | Patch Non-Employee Record
[**patch_non_employee_schema_attribute**](NonEmployeeLifecycleManagementApi.md#patch_non_employee_schema_attribute) | **PATCH** /non-employee-sources/{sourceId}/schema-attributes/{attributeId} | Patch a Schema Attribute for Non-Employee Source
[**patch_non_employee_source**](NonEmployeeLifecycleManagementApi.md#patch_non_employee_source) | **PATCH** /non-employee-sources/{sourceId} | Patch a Non-Employee Source
[**reject_non_employee_request**](NonEmployeeLifecycleManagementApi.md#reject_non_employee_request) | **POST** /non-employee-approvals/{id}/reject | Reject a Non-Employee Request
[**update_non_employee_record**](NonEmployeeLifecycleManagementApi.md#update_non_employee_record) | **PUT** /non-employee-records/{id} | Update Non-Employee Record


# **approve_non_employee_request**
> NonEmployeeApprovalItem approve_non_employee_request(id, non_employee_approval_decision)

Approve a Non-Employee Request

Approves a non-employee approval request and notifies the next approver. The current user must be the requested approver.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_approval_decision import NonEmployeeApprovalDecision
from v3.models.non_employee_approval_item import NonEmployeeApprovalItem
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    id = 'e136567de87e4d029e60b3c3c55db56d' # str | Non-Employee approval item id (UUID)
    non_employee_approval_decision = v3.NonEmployeeApprovalDecision() # NonEmployeeApprovalDecision | 

    try:
        # Approve a Non-Employee Request
        api_response = api_instance.approve_non_employee_request(id, non_employee_approval_decision)
        print("The response of NonEmployeeLifecycleManagementApi->approve_non_employee_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->approve_non_employee_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Non-Employee approval item id (UUID) | 
 **non_employee_approval_decision** | [**NonEmployeeApprovalDecision**](NonEmployeeApprovalDecision.md)|  | 

### Return type

[**NonEmployeeApprovalItem**](NonEmployeeApprovalItem.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Non-Employee approval item object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_non_employee_record**
> NonEmployeeRecord create_non_employee_record(non_employee_request_body)

Create Non-Employee Record

This request will create a non-employee record. Requires role context of `idn:nesr:create`

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_record import NonEmployeeRecord
from v3.models.non_employee_request_body import NonEmployeeRequestBody
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    non_employee_request_body = v3.NonEmployeeRequestBody() # NonEmployeeRequestBody | Non-Employee record creation request body.

    try:
        # Create Non-Employee Record
        api_response = api_instance.create_non_employee_record(non_employee_request_body)
        print("The response of NonEmployeeLifecycleManagementApi->create_non_employee_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->create_non_employee_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_employee_request_body** | [**NonEmployeeRequestBody**](NonEmployeeRequestBody.md)| Non-Employee record creation request body. | 

### Return type

[**NonEmployeeRecord**](NonEmployeeRecord.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created non-employee record. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_non_employee_request**
> NonEmployeeRequest create_non_employee_request(non_employee_request_body)

Create Non-Employee Request

This request will create a non-employee request and notify the approver. Requires role context of `idn:nesr:create` or the user must own the source.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_request import NonEmployeeRequest
from v3.models.non_employee_request_body import NonEmployeeRequestBody
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    non_employee_request_body = v3.NonEmployeeRequestBody() # NonEmployeeRequestBody | Non-Employee creation request body

    try:
        # Create Non-Employee Request
        api_response = api_instance.create_non_employee_request(non_employee_request_body)
        print("The response of NonEmployeeLifecycleManagementApi->create_non_employee_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->create_non_employee_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_employee_request_body** | [**NonEmployeeRequestBody**](NonEmployeeRequestBody.md)| Non-Employee creation request body | 

### Return type

[**NonEmployeeRequest**](NonEmployeeRequest.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Non-Employee request creation object |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_non_employee_source**
> NonEmployeeSourceWithCloudExternalId create_non_employee_source(non_employee_source_request_body)

Create Non-Employee Source

This request will create a non-employee source. Requires role context of `idn:nesr:create`

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_source_request_body import NonEmployeeSourceRequestBody
from v3.models.non_employee_source_with_cloud_external_id import NonEmployeeSourceWithCloudExternalId
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    non_employee_source_request_body = v3.NonEmployeeSourceRequestBody() # NonEmployeeSourceRequestBody | Non-Employee source creation request body.

    try:
        # Create Non-Employee Source
        api_response = api_instance.create_non_employee_source(non_employee_source_request_body)
        print("The response of NonEmployeeLifecycleManagementApi->create_non_employee_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->create_non_employee_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_employee_source_request_body** | [**NonEmployeeSourceRequestBody**](NonEmployeeSourceRequestBody.md)| Non-Employee source creation request body. | 

### Return type

[**NonEmployeeSourceWithCloudExternalId**](NonEmployeeSourceWithCloudExternalId.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created non-employee source. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_non_employee_source_schema_attributes**
> NonEmployeeSchemaAttribute create_non_employee_source_schema_attributes(source_id, non_employee_schema_attribute_body)

Create a new Schema Attribute for Non-Employee Source

This API creates a new schema attribute for Non-Employee Source. The schema technical name must be unique in the source. Attempts to create a schema attribute with an existing name will result in a \"400.1.409 Reference conflict\" response. At most, 10 custom attributes can be created per schema. Attempts to create more than 10 will result in a \"400.1.4 Limit violation\" response. Requires role context of `idn:nesr:create`

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_schema_attribute import NonEmployeeSchemaAttribute
from v3.models.non_employee_schema_attribute_body import NonEmployeeSchemaAttributeBody
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    source_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The Source id
    non_employee_schema_attribute_body = v3.NonEmployeeSchemaAttributeBody() # NonEmployeeSchemaAttributeBody | 

    try:
        # Create a new Schema Attribute for Non-Employee Source
        api_response = api_instance.create_non_employee_source_schema_attributes(source_id, non_employee_schema_attribute_body)
        print("The response of NonEmployeeLifecycleManagementApi->create_non_employee_source_schema_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->create_non_employee_source_schema_attributes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id | 
 **non_employee_schema_attribute_body** | [**NonEmployeeSchemaAttributeBody**](NonEmployeeSchemaAttributeBody.md)|  | 

### Return type

[**NonEmployeeSchemaAttribute**](NonEmployeeSchemaAttribute.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Schema Attribute created. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_non_employee_record**
> delete_non_employee_record(id)

Delete Non-Employee Record

This request will delete a non-employee record. Requires role context of `idn:nesr:delete`

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | Non-Employee record id (UUID)

    try:
        # Delete Non-Employee Record
        api_instance.delete_non_employee_record(id)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->delete_non_employee_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Non-Employee record id (UUID) | 

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
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_non_employee_records_in_bulk**
> delete_non_employee_records_in_bulk(delete_non_employee_records_in_bulk_request)

Delete Multiple Non-Employee Records

This request will delete multiple non-employee records based on the non-employee ids provided. Requires role context of `idn:nesr:delete`

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.delete_non_employee_records_in_bulk_request import DeleteNonEmployeeRecordsInBulkRequest
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    delete_non_employee_records_in_bulk_request = v3.DeleteNonEmployeeRecordsInBulkRequest() # DeleteNonEmployeeRecordsInBulkRequest | Non-Employee bulk delete request body.

    try:
        # Delete Multiple Non-Employee Records
        api_instance.delete_non_employee_records_in_bulk(delete_non_employee_records_in_bulk_request)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->delete_non_employee_records_in_bulk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_non_employee_records_in_bulk_request** | [**DeleteNonEmployeeRecordsInBulkRequest**](DeleteNonEmployeeRecordsInBulkRequest.md)| Non-Employee bulk delete request body. | 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content - indicates the request was successful but there is no content to be returned in the response. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_non_employee_request**
> delete_non_employee_request(id)

Delete Non-Employee Request

This request will delete a non-employee request.  Requires role context of `idn:nesr:delete`

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    id = 'ac110005-7156-1150-8171-5b292e3e0084' # str | Non-Employee request id in the UUID format

    try:
        # Delete Non-Employee Request
        api_instance.delete_non_employee_request(id)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->delete_non_employee_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Non-Employee request id in the UUID format | 

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

# **delete_non_employee_schema_attribute**
> delete_non_employee_schema_attribute(attribute_id, source_id)

Delete a Schema Attribute for Non-Employee Source

This end-point deletes a specific schema attribute for a non-employee source. Requires role context of `idn:nesr:delete` 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    attribute_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The Schema Attribute Id (UUID)
    source_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The Source id

    try:
        # Delete a Schema Attribute for Non-Employee Source
        api_instance.delete_non_employee_schema_attribute(attribute_id, source_id)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->delete_non_employee_schema_attribute: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**| The Schema Attribute Id (UUID) | 
 **source_id** | **str**| The Source id | 

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
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_non_employee_source**
> delete_non_employee_source(source_id)

Delete Non-Employee Source

This request will delete a non-employee source. Requires role context of `idn:nesr:delete`.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    source_id = 'e136567de87e4d029e60b3c3c55db56d' # str | Source Id

    try:
        # Delete Non-Employee Source
        api_instance.delete_non_employee_source(source_id)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->delete_non_employee_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| Source Id | 

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
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_non_employee_source_schema_attributes**
> delete_non_employee_source_schema_attributes(source_id)

Delete all custom schema attributes for Non-Employee Source

This end-point deletes all custom schema attributes for a non-employee source. Requires role context of `idn:nesr:delete`

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    source_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The Source id

    try:
        # Delete all custom schema attributes for Non-Employee Source
        api_instance.delete_non_employee_source_schema_attributes(source_id)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->delete_non_employee_source_schema_attributes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id | 

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
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_non_employee_records**
> export_non_employee_records(id)

Exports Non-Employee Records to CSV

This requests a CSV download for all non-employees from a provided source. Requires role context of `idn:nesr:read`

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    id = 'e136567de87e4d029e60b3c3c55db56d' # str | Source Id (UUID)

    try:
        # Exports Non-Employee Records to CSV
        api_instance.export_non_employee_records(id)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->export_non_employee_records: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Source Id (UUID) | 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exported CSV |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_non_employee_source_schema_template**
> export_non_employee_source_schema_template(id)

Exports Source Schema Template

This requests a download for the Source Schema Template for a provided source. Requires role context of `idn:nesr:read`

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | Source Id (UUID)

    try:
        # Exports Source Schema Template
        api_instance.export_non_employee_source_schema_template(id)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->export_non_employee_source_schema_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Source Id (UUID) | 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exported Source Schema Template |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_employee_approval**
> NonEmployeeApprovalItemDetail get_non_employee_approval(id, include_detail=include_detail)

Get a non-employee approval item detail

Gets a non-employee approval item detail. There are two contextual uses for this endpoint:   1. The user has the role context of `idn:nesr:read`, in which case they can get any approval.   2. The user owns the requested approval.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_approval_item_detail import NonEmployeeApprovalItemDetail
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    id = 'e136567de87e4d029e60b3c3c55db56d' # str | Non-Employee approval item id (UUID)
    include_detail = true # bool | The object nonEmployeeRequest will not be included detail when set to false. *Default value is true* (optional)

    try:
        # Get a non-employee approval item detail
        api_response = api_instance.get_non_employee_approval(id, include_detail=include_detail)
        print("The response of NonEmployeeLifecycleManagementApi->get_non_employee_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->get_non_employee_approval: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Non-Employee approval item id (UUID) | 
 **include_detail** | **bool**| The object nonEmployeeRequest will not be included detail when set to false. *Default value is true* | [optional] 

### Return type

[**NonEmployeeApprovalItemDetail**](NonEmployeeApprovalItemDetail.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Non-Employee approval item object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_employee_approval_summary**
> NonEmployeeApprovalSummary get_non_employee_approval_summary(requested_for)

Get Summary of Non-Employee Approval Requests

This request will retrieve a summary of non-employee approval requests. There are two contextual uses for the `requested-for` path parameter:   1. The user has the role context of `idn:nesr:read`, in which case he or she may request a summary of all non-employee approval requests assigned to a particular approver by passing in that approver's id.   2. The current user is an approver, in which case \"me\" should be provided as the `requested-for` value. This will provide the approver with a summary of the approval items assigned to him or her.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_approval_summary import NonEmployeeApprovalSummary
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    requested_for = '2c91808280430dfb0180431a59440460' # str | The identity (UUID) of the approver for whom for whom the summary is being retrieved. Use \"me\" instead to indicate the current user.

    try:
        # Get Summary of Non-Employee Approval Requests
        api_response = api_instance.get_non_employee_approval_summary(requested_for)
        print("The response of NonEmployeeLifecycleManagementApi->get_non_employee_approval_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->get_non_employee_approval_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requested_for** | **str**| The identity (UUID) of the approver for whom for whom the summary is being retrieved. Use \&quot;me\&quot; instead to indicate the current user. | 

### Return type

[**NonEmployeeApprovalSummary**](NonEmployeeApprovalSummary.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | summary of non-employee approval requests |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_employee_bulk_upload_status**
> NonEmployeeBulkUploadStatus get_non_employee_bulk_upload_status(id)

Obtain the status of bulk upload on the source

The nonEmployeeBulkUploadStatus API returns the status of the newest bulk upload job for the specified source. Requires role context of `idn:nesr:read` 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_bulk_upload_status import NonEmployeeBulkUploadStatus
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    id = 'e136567de87e4d029e60b3c3c55db56d' # str | Source ID (UUID)

    try:
        # Obtain the status of bulk upload on the source
        api_response = api_instance.get_non_employee_bulk_upload_status(id)
        print("The response of NonEmployeeLifecycleManagementApi->get_non_employee_bulk_upload_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->get_non_employee_bulk_upload_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Source ID (UUID) | 

### Return type

[**NonEmployeeBulkUploadStatus**](NonEmployeeBulkUploadStatus.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of the newest bulk-upload job, if any. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_employee_record**
> NonEmployeeRecord get_non_employee_record(id)

Get a Non-Employee Record

This gets a non-employee record. Requires role context of `idn:nesr:read`

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_record import NonEmployeeRecord
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | Non-Employee record id (UUID)

    try:
        # Get a Non-Employee Record
        api_response = api_instance.get_non_employee_record(id)
        print("The response of NonEmployeeLifecycleManagementApi->get_non_employee_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->get_non_employee_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Non-Employee record id (UUID) | 

### Return type

[**NonEmployeeRecord**](NonEmployeeRecord.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Non-Employee record object |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_employee_request**
> NonEmployeeRequest get_non_employee_request(id)

Get a Non-Employee Request

This gets a non-employee request. There are two contextual uses for this endpoint:   1. The user has the role context of `idn:nesr:read`, in this case the user can get the non-employee request for any user.   2. The user must be the owner of the non-employee request.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_request import NonEmployeeRequest
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    id = 'ac110005-7156-1150-8171-5b292e3e0084' # str | Non-Employee request id (UUID)

    try:
        # Get a Non-Employee Request
        api_response = api_instance.get_non_employee_request(id)
        print("The response of NonEmployeeLifecycleManagementApi->get_non_employee_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->get_non_employee_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Non-Employee request id (UUID) | 

### Return type

[**NonEmployeeRequest**](NonEmployeeRequest.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Non-Employee request object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_employee_request_summary**
> NonEmployeeRequestSummary get_non_employee_request_summary(requested_for)

Get Summary of Non-Employee Requests

This request will retrieve a summary of non-employee requests. There are two contextual uses for the `requested-for` path parameter:   1. The user has the role context of `idn:nesr:read`, in which case he or she may request a summary of all non-employee approval requests assigned to a particular account manager by passing in that manager's id.   2. The current user is an account manager, in which case \"me\" should be provided as the `requested-for` value. This will provide the user with a summary of the non-employee requests in the source(s) he or she manages.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_request_summary import NonEmployeeRequestSummary
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    requested_for = '2c91808280430dfb0180431a59440460' # str | The identity (UUID) of the non-employee account manager for whom the summary is being retrieved. Use \"me\" instead to indicate the current user.

    try:
        # Get Summary of Non-Employee Requests
        api_response = api_instance.get_non_employee_request_summary(requested_for)
        print("The response of NonEmployeeLifecycleManagementApi->get_non_employee_request_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->get_non_employee_request_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requested_for** | **str**| The identity (UUID) of the non-employee account manager for whom the summary is being retrieved. Use \&quot;me\&quot; instead to indicate the current user. | 

### Return type

[**NonEmployeeRequestSummary**](NonEmployeeRequestSummary.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Non-Employee request summary object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_employee_schema_attribute**
> NonEmployeeSchemaAttribute get_non_employee_schema_attribute(attribute_id, source_id)

Get Schema Attribute Non-Employee Source

This API gets a schema attribute by Id for the specified Non-Employee SourceId. Requires role context of `idn:nesr:read` or the user must be an account manager of the source.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_schema_attribute import NonEmployeeSchemaAttribute
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    attribute_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The Schema Attribute Id (UUID)
    source_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The Source id

    try:
        # Get Schema Attribute Non-Employee Source
        api_response = api_instance.get_non_employee_schema_attribute(attribute_id, source_id)
        print("The response of NonEmployeeLifecycleManagementApi->get_non_employee_schema_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->get_non_employee_schema_attribute: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**| The Schema Attribute Id (UUID) | 
 **source_id** | **str**| The Source id | 

### Return type

[**NonEmployeeSchemaAttribute**](NonEmployeeSchemaAttribute.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Schema Attribute |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_employee_source**
> NonEmployeeSource get_non_employee_source(source_id)

Get a Non-Employee Source

This gets a non-employee source. There are two contextual uses for the requested-for path parameter:    1. The user has the role context of `idn:nesr:read`, in which case he or she may request any source.   2. The current user is an account manager, in which case the user can only request sources that they own.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_source import NonEmployeeSource
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    source_id = '2c91808b7c28b350017c2a2ec5790aa1' # str | Source Id

    try:
        # Get a Non-Employee Source
        api_response = api_instance.get_non_employee_source(source_id)
        print("The response of NonEmployeeLifecycleManagementApi->get_non_employee_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->get_non_employee_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| Source Id | 

### Return type

[**NonEmployeeSource**](NonEmployeeSource.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Non-Employee source object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_employee_source_schema_attributes**
> List[NonEmployeeSchemaAttribute] get_non_employee_source_schema_attributes(source_id)

List Schema Attributes Non-Employee Source

This API gets the list of schema attributes for the specified Non-Employee SourceId. There are 8 mandatory attributes added to each new Non-Employee Source automatically. Additionaly, user can add up to 10 custom attributes. This interface returns all the mandatory attributes followed by any custom attributes. At most, a total of 18 attributes will be returned. Requires role context of `idn:nesr:read` or the user must be an account manager of the source.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_schema_attribute import NonEmployeeSchemaAttribute
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    source_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The Source id

    try:
        # List Schema Attributes Non-Employee Source
        api_response = api_instance.get_non_employee_source_schema_attributes(source_id)
        print("The response of NonEmployeeLifecycleManagementApi->get_non_employee_source_schema_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->get_non_employee_source_schema_attributes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id | 

### Return type

[**List[NonEmployeeSchemaAttribute]**](NonEmployeeSchemaAttribute.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Schema Attributes |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_non_employee_records_in_bulk**
> NonEmployeeBulkUploadJob import_non_employee_records_in_bulk(id, data)

Imports, or Updates, Non-Employee Records

This post will import, or update, Non-Employee records found in the CSV. Requires role context of `idn:nesr:create`

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_bulk_upload_job import NonEmployeeBulkUploadJob
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    id = 'e136567de87e4d029e60b3c3c55db56d' # str | Source Id (UUID)
    data = None # bytearray | 

    try:
        # Imports, or Updates, Non-Employee Records
        api_response = api_instance.import_non_employee_records_in_bulk(id, data)
        print("The response of NonEmployeeLifecycleManagementApi->import_non_employee_records_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->import_non_employee_records_in_bulk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Source Id (UUID) | 
 **data** | **bytearray**|  | 

### Return type

[**NonEmployeeBulkUploadJob**](NonEmployeeBulkUploadJob.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The CSV was accepted to be bulk inserted now or at a later time. |  -  |
**400** | Client Error - Returned if the request body is invalid. The response body will contain the list of specific errors with one on each line.  |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_non_employee_approvals**
> List[NonEmployeeApprovalItem] list_non_employee_approvals(requested_for=requested_for, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)

Get List of Non-Employee Approval Requests

This gets a list of non-employee approval requests. There are two contextual uses for this endpoint:   1. The user has the role context of `idn:nesr:read`, in which case they can list the approvals for any approver.   2. The user owns the requested approval.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_approval_item import NonEmployeeApprovalItem
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    requested_for = '2c91808280430dfb0180431a59440460' # str | The identity for whom the request was made. *me* indicates the current user. (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'approvalStatus eq \"Pending\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **approvalStatus**: *eq* (optional)
    sorters = 'created' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **created, modified** (optional)

    try:
        # Get List of Non-Employee Approval Requests
        api_response = api_instance.list_non_employee_approvals(requested_for=requested_for, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)
        print("The response of NonEmployeeLifecycleManagementApi->list_non_employee_approvals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->list_non_employee_approvals: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requested_for** | **str**| The identity for whom the request was made. *me* indicates the current user. | [optional] 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **approvalStatus**: *eq* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **created, modified** | [optional] 

### Return type

[**List[NonEmployeeApprovalItem]**](NonEmployeeApprovalItem.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of approval items. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_non_employee_records**
> List[NonEmployeeRecord] list_non_employee_records(limit=limit, offset=offset, count=count, sorters=sorters, filters=filters)

List Non-Employee Records

This gets a list of non-employee records. There are two contextual uses for this endpoint:   1. The user has the role context of `idn:nesr:read`, in which case they can get a list of all of the non-employees.   2. The user is an account manager, in which case they can get a list of the non-employees that they manage.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_record import NonEmployeeRecord
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    sorters = 'accountName,sourceId' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **id, accountName, sourceId, manager, firstName, lastName, email, phone, startDate, endDate, created, modified** (optional)
    filters = 'sourceId eq \"2c91808568c529c60168cca6f90c1313\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **sourceId**: *eq* (optional)

    try:
        # List Non-Employee Records
        api_response = api_instance.list_non_employee_records(limit=limit, offset=offset, count=count, sorters=sorters, filters=filters)
        print("The response of NonEmployeeLifecycleManagementApi->list_non_employee_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->list_non_employee_records: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **id, accountName, sourceId, manager, firstName, lastName, email, phone, startDate, endDate, created, modified** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **sourceId**: *eq* | [optional] 

### Return type

[**List[NonEmployeeRecord]**](NonEmployeeRecord.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Non-Employee record objects |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_non_employee_requests**
> List[NonEmployeeRequest] list_non_employee_requests(requested_for, limit=limit, offset=offset, count=count, sorters=sorters, filters=filters)

List Non-Employee Requests

This gets a list of non-employee requests. There are two contextual uses for the `requested-for` path parameter:   1. The user has the role context of `idn:nesr:read`, in which case he or she may request a list non-employee requests assigned to a particular account manager by passing in that manager's id.   2. The current user is an account manager, in which case \"me\" should be provided as the `requested-for` value. This will provide the user with a list of the non-employee requests in the source(s) he or she manages.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_request import NonEmployeeRequest
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    requested_for = 'e136567de87e4d029e60b3c3c55db56d' # str | The identity for whom the request was made. *me* indicates the current user.
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    sorters = 'created,approvalStatus' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **created, approvalStatus, firstName, lastName, email, phone, accountName, startDate, endDate** (optional)
    filters = 'sourceId eq \"2c91808568c529c60168cca6f90c1313\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **sourceId**: *eq*  (optional)

    try:
        # List Non-Employee Requests
        api_response = api_instance.list_non_employee_requests(requested_for, limit=limit, offset=offset, count=count, sorters=sorters, filters=filters)
        print("The response of NonEmployeeLifecycleManagementApi->list_non_employee_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->list_non_employee_requests: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requested_for** | **str**| The identity for whom the request was made. *me* indicates the current user. | 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **created, approvalStatus, firstName, lastName, email, phone, accountName, startDate, endDate** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **sourceId**: *eq*  | [optional] 

### Return type

[**List[NonEmployeeRequest]**](NonEmployeeRequest.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of non-employee request objects. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_non_employee_sources**
> List[NonEmployeeSourceWithNECount] list_non_employee_sources(requested_for, limit=limit, offset=offset, count=count, non_employee_count=non_employee_count, sorters=sorters)

List Non-Employee Sources

This gets a list of non-employee sources. There are two contextual uses for the requested-for path parameter:    1. The user has the role context of `idn:nesr:read`, in which case he or she may request a list sources assigned to a particular account manager by passing in that manager's id.   2. The current user is an account manager, in which case \"me\" should be provided as the `requested-for` value. This will provide the user with a list of the sources that he or she owns.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_source_with_ne_count import NonEmployeeSourceWithNECount
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    requested_for = 'me' # str | The identity for whom the request was made. *me* indicates the current user.
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    non_employee_count = true # bool | The flag to determine whether return a non-employee count associate with source. (optional)
    sorters = 'name,created' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, created, sourceId** (optional)

    try:
        # List Non-Employee Sources
        api_response = api_instance.list_non_employee_sources(requested_for, limit=limit, offset=offset, count=count, non_employee_count=non_employee_count, sorters=sorters)
        print("The response of NonEmployeeLifecycleManagementApi->list_non_employee_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->list_non_employee_sources: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requested_for** | **str**| The identity for whom the request was made. *me* indicates the current user. | 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **non_employee_count** | **bool**| The flag to determine whether return a non-employee count associate with source. | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, created, sourceId** | [optional] 

### Return type

[**List[NonEmployeeSourceWithNECount]**](NonEmployeeSourceWithNECount.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of non-employee sources objects. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_non_employee_record**
> NonEmployeeRecord patch_non_employee_record(id, json_patch_operation)

Patch Non-Employee Record

This request will patch a non-employee record. There are two contextual uses for this endpoint:   1. The user has the role context of `idn:nesr:update`, in which case they update all available fields.   2. The user is owner of the source, in this case they can only update the end date.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.json_patch_operation import JsonPatchOperation
from v3.models.non_employee_record import NonEmployeeRecord
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | Non-employee record id (UUID)
    json_patch_operation = [{op=replace, path=/endDate, value=2019-08-23T18:40:35.772Z}] # List[JsonPatchOperation] | A list of non-employee update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. Attributes are restricted by user type. Owner of source can update end date. Organization admins can update all available fields.

    try:
        # Patch Non-Employee Record
        api_response = api_instance.patch_non_employee_record(id, json_patch_operation)
        print("The response of NonEmployeeLifecycleManagementApi->patch_non_employee_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->patch_non_employee_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Non-employee record id (UUID) | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| A list of non-employee update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. Attributes are restricted by user type. Owner of source can update end date. Organization admins can update all available fields. | 

### Return type

[**NonEmployeeRecord**](NonEmployeeRecord.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A patched non-employee record. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_non_employee_schema_attribute**
> NonEmployeeSchemaAttribute patch_non_employee_schema_attribute(attribute_id, source_id, json_patch_operation)

Patch a Schema Attribute for Non-Employee Source

This end-point patches a specific schema attribute for a non-employee SourceId. Requires role context of `idn:nesr:update` 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.json_patch_operation import JsonPatchOperation
from v3.models.non_employee_schema_attribute import NonEmployeeSchemaAttribute
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    attribute_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The Schema Attribute Id (UUID)
    source_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The Source id
    json_patch_operation = [{op=replace, path=/label, value={new attribute label=null}}] # List[JsonPatchOperation] | A list of schema attribute update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. The following properties are allowed for update ':' 'label', 'helpText', 'placeholder', 'required'.

    try:
        # Patch a Schema Attribute for Non-Employee Source
        api_response = api_instance.patch_non_employee_schema_attribute(attribute_id, source_id, json_patch_operation)
        print("The response of NonEmployeeLifecycleManagementApi->patch_non_employee_schema_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->patch_non_employee_schema_attribute: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**| The Schema Attribute Id (UUID) | 
 **source_id** | **str**| The Source id | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| A list of schema attribute update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. The following properties are allowed for update &#39;:&#39; &#39;label&#39;, &#39;helpText&#39;, &#39;placeholder&#39;, &#39;required&#39;. | 

### Return type

[**NonEmployeeSchemaAttribute**](NonEmployeeSchemaAttribute.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Schema Attribute was successfully patched. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_non_employee_source**
> NonEmployeeSource patch_non_employee_source(source_id, json_patch_operation)

Patch a Non-Employee Source

patch a non-employee source. (partial update) <br/> Patchable field: **name, description, approvers, accountManagers** Requires role context of `idn:nesr:update`.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.json_patch_operation import JsonPatchOperation
from v3.models.non_employee_source import NonEmployeeSource
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    source_id = 'e136567de87e4d029e60b3c3c55db56d' # str | Source Id
    json_patch_operation = [{op=replace, path=/name, value={new name=null}}, {op=replace, path=/approvers, value=[2c91809f703bb37a017040a2fe8748c7, 48b1f463c9e8427db5a5071bd81914b8]}] # List[JsonPatchOperation] | A list of non-employee source update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.

    try:
        # Patch a Non-Employee Source
        api_response = api_instance.patch_non_employee_source(source_id, json_patch_operation)
        print("The response of NonEmployeeLifecycleManagementApi->patch_non_employee_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->patch_non_employee_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| Source Id | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| A list of non-employee source update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. | 

### Return type

[**NonEmployeeSource**](NonEmployeeSource.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A patched non-employee source object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_non_employee_request**
> NonEmployeeApprovalItem reject_non_employee_request(id, non_employee_reject_approval_decision)

Reject a Non-Employee Request

This endpoint will reject an approval item request and notify user. The current user must be the requested approver.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_approval_item import NonEmployeeApprovalItem
from v3.models.non_employee_reject_approval_decision import NonEmployeeRejectApprovalDecision
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    id = 'e136567de87e4d029e60b3c3c55db56d' # str | Non-Employee approval item id (UUID)
    non_employee_reject_approval_decision = v3.NonEmployeeRejectApprovalDecision() # NonEmployeeRejectApprovalDecision | 

    try:
        # Reject a Non-Employee Request
        api_response = api_instance.reject_non_employee_request(id, non_employee_reject_approval_decision)
        print("The response of NonEmployeeLifecycleManagementApi->reject_non_employee_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->reject_non_employee_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Non-Employee approval item id (UUID) | 
 **non_employee_reject_approval_decision** | [**NonEmployeeRejectApprovalDecision**](NonEmployeeRejectApprovalDecision.md)|  | 

### Return type

[**NonEmployeeApprovalItem**](NonEmployeeApprovalItem.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Non-Employee approval item object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_non_employee_record**
> NonEmployeeRecord update_non_employee_record(id, non_employee_request_body)

Update Non-Employee Record

This request will update a non-employee record. There are two contextual uses for this endpoint:   1. The user has the role context of `idn:nesr:update`, in which case they update all available fields.   2. The user is owner of the source, in this case they can only update the end date.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.non_employee_record import NonEmployeeRecord
from v3.models.non_employee_request_body import NonEmployeeRequestBody
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.NonEmployeeLifecycleManagementApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | Non-employee record id (UUID)
    non_employee_request_body = v3.NonEmployeeRequestBody() # NonEmployeeRequestBody | Non-employee record creation request body. Attributes are restricted by user type. Owner of source can update end date. Organization admins can update all available fields.

    try:
        # Update Non-Employee Record
        api_response = api_instance.update_non_employee_record(id, non_employee_request_body)
        print("The response of NonEmployeeLifecycleManagementApi->update_non_employee_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonEmployeeLifecycleManagementApi->update_non_employee_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Non-employee record id (UUID) | 
 **non_employee_request_body** | [**NonEmployeeRequestBody**](NonEmployeeRequestBody.md)| Non-employee record creation request body. Attributes are restricted by user type. Owner of source can update end date. Organization admins can update all available fields. | 

### Return type

[**NonEmployeeRecord**](NonEmployeeRecord.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An updated non-employee record. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


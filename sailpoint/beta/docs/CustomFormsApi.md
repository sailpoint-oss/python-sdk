# beta.CustomFormsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_form_definition**](CustomFormsApi.md#create_form_definition) | **POST** /form-definitions | Creates a form definition.
[**create_form_definition_dynamic_schema**](CustomFormsApi.md#create_form_definition_dynamic_schema) | **POST** /form-definitions/forms-action-dynamic-schema | Generate JSON Schema dynamically.
[**create_form_instance**](CustomFormsApi.md#create_form_instance) | **POST** /form-instances | Creates a form instance.
[**delete_form_definition**](CustomFormsApi.md#delete_form_definition) | **DELETE** /form-definitions/{formDefinitionID} | Deletes a form definition.
[**export_form_definitions_by_tenant**](CustomFormsApi.md#export_form_definitions_by_tenant) | **GET** /form-definitions/export | List form definitions by tenant.
[**get_form_definition_by_key**](CustomFormsApi.md#get_form_definition_by_key) | **GET** /form-definitions/{formDefinitionID} | Return a form definition.
[**get_form_instance_by_key**](CustomFormsApi.md#get_form_instance_by_key) | **GET** /form-instances/{formInstanceID} | Returns a form instance.
[**import_form_definitions**](CustomFormsApi.md#import_form_definitions) | **POST** /form-definitions/import | Import form definitions from export.
[**patch_form_definition**](CustomFormsApi.md#patch_form_definition) | **PATCH** /form-definitions/{formDefinitionID} | Patch a form definition.
[**patch_form_instance**](CustomFormsApi.md#patch_form_instance) | **PATCH** /form-instances/{formInstanceID} | Patch a form instance.
[**search_form_definitions_by_tenant**](CustomFormsApi.md#search_form_definitions_by_tenant) | **GET** /form-definitions | Export form definitions by tenant.
[**search_form_element_data_by_element_id**](CustomFormsApi.md#search_form_element_data_by_element_id) | **GET** /form-instances/{formInstanceID}/data-source/{formElementID} | Retrieves dynamic data by element.
[**search_form_instances_by_tenant**](CustomFormsApi.md#search_form_instances_by_tenant) | **GET** /form-instances | List form instances by tenant.
[**search_pre_defined_select_options**](CustomFormsApi.md#search_pre_defined_select_options) | **GET** /form-definitions/predefined-select-options | List predefined select options.
[**show_preview_data_source**](CustomFormsApi.md#show_preview_data_source) | **POST** /form-definitions/{formDefinitionID}/data-source | Preview form definition data source.


# **create_form_definition**
> FormDefinitionResponse create_form_definition(body=body)

Creates a form definition.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.create_form_definition_request import CreateFormDefinitionRequest
from beta.models.form_definition_response import FormDefinitionResponse
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
    api_instance = beta.CustomFormsApi(api_client)
    body = {name=my form, description=my form description, owner={type=IDENTITY, id=00000000-0000-0000-0000-000000000000}} # CreateFormDefinitionRequest | Body is the request payload to create form definition request (optional)

    try:
        # Creates a form definition.
        api_response = api_instance.create_form_definition(body=body)
        print("The response of CustomFormsApi->create_form_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->create_form_definition: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFormDefinitionRequest**](CreateFormDefinitionRequest.md)| Body is the request payload to create form definition request | [optional] 

### Return type

[**FormDefinitionResponse**](FormDefinitionResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns a new form definition |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_form_definition_dynamic_schema**
> FormDefinitionDynamicSchemaResponse create_form_definition_dynamic_schema(body=body)

Generate JSON Schema dynamically.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.form_definition_dynamic_schema_request import FormDefinitionDynamicSchemaRequest
from beta.models.form_definition_dynamic_schema_response import FormDefinitionDynamicSchemaResponse
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
    api_instance = beta.CustomFormsApi(api_client)
    body = {id=sp:forms, attributes={formDefinitionId=00000000-0000-0000-0000-000000000000}, description=AnotherDescription, type=action, versionNumber=1} # FormDefinitionDynamicSchemaRequest | Body is the request payload to create a form definition dynamic schema (optional)

    try:
        # Generate JSON Schema dynamically.
        api_response = api_instance.create_form_definition_dynamic_schema(body=body)
        print("The response of CustomFormsApi->create_form_definition_dynamic_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->create_form_definition_dynamic_schema: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormDefinitionDynamicSchemaRequest**](FormDefinitionDynamicSchemaRequest.md)| Body is the request payload to create a form definition dynamic schema | [optional] 

### Return type

[**FormDefinitionDynamicSchemaResponse**](FormDefinitionDynamicSchemaResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a form elements dynamic schema |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**404** | An error with the item not found |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_form_instance**
> FormInstanceResponse create_form_instance(body=body)

Creates a form instance.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.create_form_instance_request import CreateFormInstanceRequest
from beta.models.form_instance_response import FormInstanceResponse
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
    api_instance = beta.CustomFormsApi(api_client)
    body = {expire=2023-06-20T15:57:55.332882Z, formDefinitionId=00000000-0000-0000-0000-000000000000, recipients=[{type=IDENTITY, id=an-identity-id}], createdBy={type=WORKFLOW_EXECUTION, id=a-workflow-execution-id}} # CreateFormInstanceRequest | Body is the request payload to create a form instance (optional)

    try:
        # Creates a form instance.
        api_response = api_instance.create_form_instance(body=body)
        print("The response of CustomFormsApi->create_form_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->create_form_instance: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFormInstanceRequest**](CreateFormInstanceRequest.md)| Body is the request payload to create a form instance | [optional] 

### Return type

[**FormInstanceResponse**](FormInstanceResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns a new form instance |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_form_definition**
> object delete_form_definition(form_definition_id)

Deletes a form definition.

Parameter `{formDefinitionID}` should match a form definition ID.

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
    api_instance = beta.CustomFormsApi(api_client)
    form_definition_id = '00000000-0000-0000-0000-000000000000' # str | Form definition ID

    try:
        # Deletes a form definition.
        api_response = api_instance.delete_form_definition(form_definition_id)
        print("The response of CustomFormsApi->delete_form_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->delete_form_definition: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_definition_id** | **str**| Form definition ID | 

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
**204** | Returns an empty body |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**404** | An error with the item not found |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_form_definitions_by_tenant**
> List[ExportFormDefinitionsByTenant200ResponseInner] export_form_definitions_by_tenant(offset=offset, limit=limit, filters=filters, sorters=sorters)

List form definitions by tenant.

No parameters required.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.export_form_definitions_by_tenant200_response_inner import ExportFormDefinitionsByTenant200ResponseInner
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
    api_instance = beta.CustomFormsApi(api_client)
    offset = 0 # int | Offset  Integer specifying the offset of the first result from the beginning of the collection. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). The offset value is record-based, not page-based, and the index starts at 0. (optional) (default to 0)
    limit = 250 # int | Limit  Integer specifying the maximum number of records to return in a single API call. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). If it is not specified, a default limit is used. (optional) (default to 250)
    filters = 'name sw \"my form\"' # str | Filters  Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results) Filtering is supported for the following fields and operators: <b>name</b>: <i>eq, gt, sw, in</i> <b>description</b>: <i>eq, gt, sw, in</i> <b>created</b>: <i>eq, gt, sw, in</i> <b>modified</b>: <i>eq, gt, sw, in</i> (optional)
    sorters = 'name' # str | Sorters  Item will be sorted in the returned array if the sorters expression evaluates to true for that item. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters/#sorting-results). Sorting is supported for the following fields: <b>name</b> <b>description</b> <b>created</b> <b>modified</b> (optional) (default to 'name')

    try:
        # List form definitions by tenant.
        api_response = api_instance.export_form_definitions_by_tenant(offset=offset, limit=limit, filters=filters, sorters=sorters)
        print("The response of CustomFormsApi->export_form_definitions_by_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->export_form_definitions_by_tenant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset  Integer specifying the offset of the first result from the beginning of the collection. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). The offset value is record-based, not page-based, and the index starts at 0. | [optional] [default to 0]
 **limit** | **int**| Limit  Integer specifying the maximum number of records to return in a single API call. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). If it is not specified, a default limit is used. | [optional] [default to 250]
 **filters** | **str**| Filters  Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results) Filtering is supported for the following fields and operators: &lt;b&gt;name&lt;/b&gt;: &lt;i&gt;eq, gt, sw, in&lt;/i&gt; &lt;b&gt;description&lt;/b&gt;: &lt;i&gt;eq, gt, sw, in&lt;/i&gt; &lt;b&gt;created&lt;/b&gt;: &lt;i&gt;eq, gt, sw, in&lt;/i&gt; &lt;b&gt;modified&lt;/b&gt;: &lt;i&gt;eq, gt, sw, in&lt;/i&gt; | [optional] 
 **sorters** | **str**| Sorters  Item will be sorted in the returned array if the sorters expression evaluates to true for that item. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters/#sorting-results). Sorting is supported for the following fields: &lt;b&gt;name&lt;/b&gt; &lt;b&gt;description&lt;/b&gt; &lt;b&gt;created&lt;/b&gt; &lt;b&gt;modified&lt;/b&gt; | [optional] [default to &#39;name&#39;]

### Return type

[**List[ExportFormDefinitionsByTenant200ResponseInner]**](ExportFormDefinitionsByTenant200ResponseInner.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of form definition objects by tenant used by SP-Config |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_definition_by_key**
> FormDefinitionResponse get_form_definition_by_key(form_definition_id)

Return a form definition.

Parameter `{formDefinitionID}` should match a form definition ID.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.form_definition_response import FormDefinitionResponse
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
    api_instance = beta.CustomFormsApi(api_client)
    form_definition_id = '00000000-0000-0000-0000-000000000000' # str | Form definition ID

    try:
        # Return a form definition.
        api_response = api_instance.get_form_definition_by_key(form_definition_id)
        print("The response of CustomFormsApi->get_form_definition_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->get_form_definition_by_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_definition_id** | **str**| Form definition ID | 

### Return type

[**FormDefinitionResponse**](FormDefinitionResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a form definition |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**404** | An error with the item not found |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_instance_by_key**
> FormInstanceResponse get_form_instance_by_key(form_instance_id)

Returns a form instance.

Parameter `{formInstanceID}` should match a form instance ID.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.form_instance_response import FormInstanceResponse
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
    api_instance = beta.CustomFormsApi(api_client)
    form_instance_id = '00000000-0000-0000-0000-000000000000' # str | Form instance ID

    try:
        # Returns a form instance.
        api_response = api_instance.get_form_instance_by_key(form_instance_id)
        print("The response of CustomFormsApi->get_form_instance_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->get_form_instance_by_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_instance_id** | **str**| Form instance ID | 

### Return type

[**FormInstanceResponse**](FormInstanceResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a form instance by its key |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**404** | An error with the item not found |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_form_definitions**
> ImportFormDefinitions202Response import_form_definitions(body=body)

Import form definitions from export.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.export_form_definitions_by_tenant200_response_inner import ExportFormDefinitionsByTenant200ResponseInner
from beta.models.import_form_definitions202_response import ImportFormDefinitions202Response
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
    api_instance = beta.CustomFormsApi(api_client)
    body = [{version=1, self={name=All fields not required, id=05ed4edb-d0a9-41d9-ad0c-2f6e486ec4aa, type=FORM_DEFINITION}, object={id=05ed4edb-d0a9-41d9-ad0c-2f6e486ec4aa, name=All fields not required, description=description, owner={type=IDENTITY, id=3447d8ec2602455ab6f1e8408a0f0150}, usedBy=[{type=WORKFLOW, id=5008594c-dacc-4295-8fee-41df60477304}, {type=WORKFLOW, id=97e75a75-c179-4fbc-a2da-b5fa4aaa8743}], formInput=[{type=STRING, label=input1, description=A single dynamic scalar value (i.e. number, string, date, etc) that can be passed into the form for use in conditional logic}], formElements=[{id=3069272797630701, elementType=SECTION, config={label=First Section, formElements=[{id=3069272797630700, elementType=TEXT, key=firstName, config={label=First Name}}, {id=3498415402897539, elementType=TEXT, key=lastName, config={label=Last Name}}]}}], formConditions=[{ruleOperator=AND, rules=[{sourceType=INPUT, source=Department, operator=EQ, valueType=STRING, value=Sales}], effects=[{effectType=HIDE, config={element=2614088730489570}}]}], created=2022-10-04T19:27:04.456Z, modified=2022-11-16T20:45:02.172Z}}] # List[ExportFormDefinitionsByTenant200ResponseInner] | Body is the request payload to import form definitions (optional)

    try:
        # Import form definitions from export.
        api_response = api_instance.import_form_definitions(body=body)
        print("The response of CustomFormsApi->import_form_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->import_form_definitions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**List[ExportFormDefinitionsByTenant200ResponseInner]**](ExportFormDefinitionsByTenant200ResponseInner.md)| Body is the request payload to import form definitions | [optional] 

### Return type

[**ImportFormDefinitions202Response**](ImportFormDefinitions202Response.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Returns statuses of those form definition objects imported |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_form_definition**
> FormDefinitionResponse patch_form_definition(form_definition_id, body=body)

Patch a form definition.

Parameter `{formDefinitionID}` should match a form definition ID.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.form_definition_response import FormDefinitionResponse
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
    api_instance = beta.CustomFormsApi(api_client)
    form_definition_id = '00000000-0000-0000-0000-000000000000' # str | Form definition ID
    body = [{op=replace, path=/description, value=test-description}] # List[Dict[str, object]] | Body is the request payload to patch a form definition, check: https://jsonpatch.com (optional)

    try:
        # Patch a form definition.
        api_response = api_instance.patch_form_definition(form_definition_id, body=body)
        print("The response of CustomFormsApi->patch_form_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->patch_form_definition: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_definition_id** | **str**| Form definition ID | 
 **body** | [**List[Dict[str, object]]**](Dict.md)| Body is the request payload to patch a form definition, check: https://jsonpatch.com | [optional] 

### Return type

[**FormDefinitionResponse**](FormDefinitionResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the form definition updated |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**404** | An error with the user permissions occurred |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_form_instance**
> FormInstanceResponse patch_form_instance(form_instance_id, body=body)

Patch a form instance.

Parameter `{formInstanceID}` should match a form instance ID.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.form_instance_response import FormInstanceResponse
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
    api_instance = beta.CustomFormsApi(api_client)
    form_instance_id = '00000000-0000-0000-0000-000000000000' # str | Form instance ID
    body = [{op=replace, path=/state, value=SUBMITTED}, {op=replace, path=/formData, value={a-key-1=a-value-1, a-key-2=true, a-key-3=1}}] # List[Dict[str, object]] | Body is the request payload to patch a form instance, check: https://jsonpatch.com (optional)

    try:
        # Patch a form instance.
        api_response = api_instance.patch_form_instance(form_instance_id, body=body)
        print("The response of CustomFormsApi->patch_form_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->patch_form_instance: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_instance_id** | **str**| Form instance ID | 
 **body** | [**List[Dict[str, object]]**](Dict.md)| Body is the request payload to patch a form instance, check: https://jsonpatch.com | [optional] 

### Return type

[**FormInstanceResponse**](FormInstanceResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the form instance updated |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**404** | An error with the item not found |  -  |
**409** | An error with the request property conflicts with stored |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_form_definitions_by_tenant**
> ListFormDefinitionsByTenantResponse search_form_definitions_by_tenant(offset=offset, limit=limit, filters=filters, sorters=sorters)

Export form definitions by tenant.

No parameters required.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.list_form_definitions_by_tenant_response import ListFormDefinitionsByTenantResponse
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
    api_instance = beta.CustomFormsApi(api_client)
    offset = 0 # int | Offset  Integer specifying the offset of the first result from the beginning of the collection. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). The offset value is record-based, not page-based, and the index starts at 0. (optional) (default to 0)
    limit = 250 # int | Limit  Integer specifying the maximum number of records to return in a single API call. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). If it is not specified, a default limit is used. (optional) (default to 250)
    filters = 'name sw \"my form\"' # str | Filters  Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results) Filtering is supported for the following fields and operators: <b>name</b>: <i>eq, gt, sw, in</i> <b>description</b>: <i>eq, gt, sw, in</i> <b>created</b>: <i>eq, gt, sw, in</i> <b>modified</b>: <i>eq, gt, sw, in</i> (optional)
    sorters = 'name' # str | Sorters  Item will be sorted in the returned array if the sorters expression evaluates to true for that item. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters/#sorting-results). Sorting is supported for the following fields: <b>name</b> <b>description</b> <b>created</b> <b>modified</b> (optional) (default to 'name')

    try:
        # Export form definitions by tenant.
        api_response = api_instance.search_form_definitions_by_tenant(offset=offset, limit=limit, filters=filters, sorters=sorters)
        print("The response of CustomFormsApi->search_form_definitions_by_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->search_form_definitions_by_tenant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset  Integer specifying the offset of the first result from the beginning of the collection. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). The offset value is record-based, not page-based, and the index starts at 0. | [optional] [default to 0]
 **limit** | **int**| Limit  Integer specifying the maximum number of records to return in a single API call. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). If it is not specified, a default limit is used. | [optional] [default to 250]
 **filters** | **str**| Filters  Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results) Filtering is supported for the following fields and operators: &lt;b&gt;name&lt;/b&gt;: &lt;i&gt;eq, gt, sw, in&lt;/i&gt; &lt;b&gt;description&lt;/b&gt;: &lt;i&gt;eq, gt, sw, in&lt;/i&gt; &lt;b&gt;created&lt;/b&gt;: &lt;i&gt;eq, gt, sw, in&lt;/i&gt; &lt;b&gt;modified&lt;/b&gt;: &lt;i&gt;eq, gt, sw, in&lt;/i&gt; | [optional] 
 **sorters** | **str**| Sorters  Item will be sorted in the returned array if the sorters expression evaluates to true for that item. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters/#sorting-results). Sorting is supported for the following fields: &lt;b&gt;name&lt;/b&gt; &lt;b&gt;description&lt;/b&gt; &lt;b&gt;created&lt;/b&gt; &lt;b&gt;modified&lt;/b&gt; | [optional] [default to &#39;name&#39;]

### Return type

[**ListFormDefinitionsByTenantResponse**](ListFormDefinitionsByTenantResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of form definitions by tenant |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_form_element_data_by_element_id**
> ListFormElementDataByElementIDResponse search_form_element_data_by_element_id(form_instance_id, form_element_id, limit=limit, filters=filters)

Retrieves dynamic data by element.

Parameter `{formInstanceID}` should match a form instance ID. Parameter `{formElementID}` should match a form element ID at the data source configuration.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.list_form_element_data_by_element_id_response import ListFormElementDataByElementIDResponse
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
    api_instance = beta.CustomFormsApi(api_client)
    form_instance_id = '00000000-0000-0000-0000-000000000000' # str | Form instance ID
    form_element_id = '1' # str | Form element ID
    limit = 250 # int | Limit  Integer specifying the maximum number of records to return in a single API call. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). If it is not specified, a default limit is used. (optional) (default to 250)
    filters = 'label sw \"my label\"' # str | Filters  Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results) Filtering is supported for the following fields and operators: <b>value</b>: <i>eq, ne, in</i> <b>label</b>: <i>eq, ne, in</i> <b>subLabel</b>: <i>eq, ne, in</i> (optional)

    try:
        # Retrieves dynamic data by element.
        api_response = api_instance.search_form_element_data_by_element_id(form_instance_id, form_element_id, limit=limit, filters=filters)
        print("The response of CustomFormsApi->search_form_element_data_by_element_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->search_form_element_data_by_element_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_instance_id** | **str**| Form instance ID | 
 **form_element_id** | **str**| Form element ID | 
 **limit** | **int**| Limit  Integer specifying the maximum number of records to return in a single API call. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). If it is not specified, a default limit is used. | [optional] [default to 250]
 **filters** | **str**| Filters  Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results) Filtering is supported for the following fields and operators: &lt;b&gt;value&lt;/b&gt;: &lt;i&gt;eq, ne, in&lt;/i&gt; &lt;b&gt;label&lt;/b&gt;: &lt;i&gt;eq, ne, in&lt;/i&gt; &lt;b&gt;subLabel&lt;/b&gt;: &lt;i&gt;eq, ne, in&lt;/i&gt; | [optional] 

### Return type

[**ListFormElementDataByElementIDResponse**](ListFormElementDataByElementIDResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieves dynamic data to aid in correctly completing a valid form by form element ID from data source configuration |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**404** | An error with the item not found |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_form_instances_by_tenant**
> ListFormInstancesByTenantResponse search_form_instances_by_tenant()

List form instances by tenant.

No parameters required.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.list_form_instances_by_tenant_response import ListFormInstancesByTenantResponse
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
    api_instance = beta.CustomFormsApi(api_client)

    try:
        # List form instances by tenant.
        api_response = api_instance.search_form_instances_by_tenant()
        print("The response of CustomFormsApi->search_form_instances_by_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->search_form_instances_by_tenant: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ListFormInstancesByTenantResponse**](ListFormInstancesByTenantResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of form instances by tenant |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_pre_defined_select_options**
> ListPredefinedSelectOptionsResponse search_pre_defined_select_options()

List predefined select options.

No parameters required.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.list_predefined_select_options_response import ListPredefinedSelectOptionsResponse
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
    api_instance = beta.CustomFormsApi(api_client)

    try:
        # List predefined select options.
        api_response = api_instance.search_pre_defined_select_options()
        print("The response of CustomFormsApi->search_pre_defined_select_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->search_pre_defined_select_options: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ListPredefinedSelectOptionsResponse**](ListPredefinedSelectOptionsResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of available predefined select options |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_preview_data_source**
> PreviewDataSourceResponse show_preview_data_source(form_definition_id, limit=limit, filters=filters, query=query, form_element_preview_request=form_element_preview_request)

Preview form definition data source.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.form_element_preview_request import FormElementPreviewRequest
from beta.models.preview_data_source_response import PreviewDataSourceResponse
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
    api_instance = beta.CustomFormsApi(api_client)
    form_definition_id = '00000000-0000-0000-0000-000000000000' # str | Form definition ID
    limit = 10 # int | Limit  Integer specifying the maximum number of records to return in a single API call. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). If it is not specified, a default limit is used. (optional) (default to 10)
    filters = 'label sw \"my label\"' # str | Filters  Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results) Filtering is supported for the following fields and operators: <b>value</b>: <i>eq, gt, sw, in</i> <b>label</b>: <i>eq, gt, sw, in</i> <b>subLabel</b>: <i>eq, gt, sw, in</i> (optional)
    query = 'support' # str | Query  String specifying to query against (optional)
    form_element_preview_request = beta.FormElementPreviewRequest() # FormElementPreviewRequest | Body is the request payload to create a form definition dynamic schema (optional)

    try:
        # Preview form definition data source.
        api_response = api_instance.show_preview_data_source(form_definition_id, limit=limit, filters=filters, query=query, form_element_preview_request=form_element_preview_request)
        print("The response of CustomFormsApi->show_preview_data_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFormsApi->show_preview_data_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_definition_id** | **str**| Form definition ID | 
 **limit** | **int**| Limit  Integer specifying the maximum number of records to return in a single API call. The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). If it is not specified, a default limit is used. | [optional] [default to 10]
 **filters** | **str**| Filters  Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results) Filtering is supported for the following fields and operators: &lt;b&gt;value&lt;/b&gt;: &lt;i&gt;eq, gt, sw, in&lt;/i&gt; &lt;b&gt;label&lt;/b&gt;: &lt;i&gt;eq, gt, sw, in&lt;/i&gt; &lt;b&gt;subLabel&lt;/b&gt;: &lt;i&gt;eq, gt, sw, in&lt;/i&gt; | [optional] 
 **query** | **str**| Query  String specifying to query against | [optional] 
 **form_element_preview_request** | [**FormElementPreviewRequest**](FormElementPreviewRequest.md)| Body is the request payload to create a form definition dynamic schema | [optional] 

### Return type

[**PreviewDataSourceResponse**](PreviewDataSourceResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a preview of a form definition data source |  -  |
**400** | An error with the request occurred |  -  |
**401** | An error with the authorization occurred |  -  |
**403** | An error with the user permissions occurred |  -  |
**404** | An error with the item not found |  -  |
**429** | Too many requests |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


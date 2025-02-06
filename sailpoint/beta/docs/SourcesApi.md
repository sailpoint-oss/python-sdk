# sailpoint.beta.SourcesApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provisioning_policy**](SourcesApi.md#create_provisioning_policy) | **POST** /sources/{sourceId}/provisioning-policies | Create Provisioning Policy
[**create_source**](SourcesApi.md#create_source) | **POST** /sources | Creates a source in IdentityNow.
[**create_source_schema**](SourcesApi.md#create_source_schema) | **POST** /sources/{sourceId}/schemas | Create Schema on Source
[**delete**](SourcesApi.md#delete) | **DELETE** /sources/{id} | Delete Source by ID
[**delete_accounts_async**](SourcesApi.md#delete_accounts_async) | **POST** /sources/{sourceId}/remove-accounts | Remove All Accounts in a Source
[**delete_native_change_detection_config**](SourcesApi.md#delete_native_change_detection_config) | **DELETE** /sources/{sourceId}/native-change-detection-config | Delete Native Change Detection Configuration
[**delete_provisioning_policy**](SourcesApi.md#delete_provisioning_policy) | **DELETE** /sources/{sourceId}/provisioning-policies/{usageType} | Delete Provisioning Policy by UsageType
[**delete_source_schema**](SourcesApi.md#delete_source_schema) | **DELETE** /sources/{sourceId}/schemas/{schemaId} | Delete Source Schema by ID
[**get_correlation_config**](SourcesApi.md#get_correlation_config) | **GET** /sources/{sourceId}/correlation-config | Get Source Correlation Configuration
[**get_native_change_detection_config**](SourcesApi.md#get_native_change_detection_config) | **GET** /sources/{sourceId}/native-change-detection-config | Native Change Detection Configuration
[**get_provisioning_policy**](SourcesApi.md#get_provisioning_policy) | **GET** /sources/{sourceId}/provisioning-policies/{usageType} | Get Provisioning Policy by UsageType
[**get_source**](SourcesApi.md#get_source) | **GET** /sources/{id} | Get Source by ID
[**get_source_accounts_schema**](SourcesApi.md#get_source_accounts_schema) | **GET** /sources/{sourceId}/schemas/accounts | Downloads source accounts schema template
[**get_source_attr_sync_config**](SourcesApi.md#get_source_attr_sync_config) | **GET** /sources/{id}/attribute-sync-config | Attribute Sync Config
[**get_source_config**](SourcesApi.md#get_source_config) | **GET** /sources/{id}/connectors/source-config | Gets source config with language translations
[**get_source_entitlement_request_config**](SourcesApi.md#get_source_entitlement_request_config) | **GET** /sources/{sourceId}/entitlement-request-config | Get Source Entitlement Request Configuration
[**get_source_entitlements_schema**](SourcesApi.md#get_source_entitlements_schema) | **GET** /sources/{sourceId}/schemas/entitlements | Downloads source entitlements schema template
[**get_source_schema**](SourcesApi.md#get_source_schema) | **GET** /sources/{sourceId}/schemas/{schemaId} | Get Source Schema by ID
[**get_source_schemas**](SourcesApi.md#get_source_schemas) | **GET** /sources/{sourceId}/schemas | List Schemas on Source
[**import_accounts**](SourcesApi.md#import_accounts) | **POST** /sources/{sourceId}/load-accounts | Account Aggregation
[**import_entitlements**](SourcesApi.md#import_entitlements) | **POST** /sources/{sourceId}/load-entitlements | Entitlement Aggregation
[**import_source_accounts_schema**](SourcesApi.md#import_source_accounts_schema) | **POST** /sources/{sourceId}/schemas/accounts | Uploads source accounts schema template
[**import_source_connector_file**](SourcesApi.md#import_source_connector_file) | **POST** /sources/{sourceId}/upload-connector-file | Upload connector file to source
[**import_source_entitlements_schema**](SourcesApi.md#import_source_entitlements_schema) | **POST** /sources/{sourceId}/schemas/entitlements | Uploads source entitlements schema template
[**import_uncorrelated_accounts**](SourcesApi.md#import_uncorrelated_accounts) | **POST** /sources/{sourceId}/load-uncorrelated-accounts | Process Uncorrelated Accounts
[**list_provisioning_policies**](SourcesApi.md#list_provisioning_policies) | **GET** /sources/{sourceId}/provisioning-policies | Lists ProvisioningPolicies
[**list_sources**](SourcesApi.md#list_sources) | **GET** /sources | Lists all sources in IdentityNow.
[**peek_resource_objects**](SourcesApi.md#peek_resource_objects) | **POST** /sources/{sourceId}/connector/peek-resource-objects | Peek source connector&#39;s resource objects
[**ping_cluster**](SourcesApi.md#ping_cluster) | **POST** /sources/{sourceId}/connector/ping-cluster | Ping cluster for source connector
[**put_correlation_config**](SourcesApi.md#put_correlation_config) | **PUT** /sources/{sourceId}/correlation-config | Update Source Correlation Configuration
[**put_native_change_detection_config**](SourcesApi.md#put_native_change_detection_config) | **PUT** /sources/{sourceId}/native-change-detection-config | Update Native Change Detection Configuration
[**put_provisioning_policy**](SourcesApi.md#put_provisioning_policy) | **PUT** /sources/{sourceId}/provisioning-policies/{usageType} | Update Provisioning Policy by UsageType
[**put_source**](SourcesApi.md#put_source) | **PUT** /sources/{id} | Update Source (Full)
[**put_source_attr_sync_config**](SourcesApi.md#put_source_attr_sync_config) | **PUT** /sources/{id}/attribute-sync-config | Update Attribute Sync Config
[**put_source_schema**](SourcesApi.md#put_source_schema) | **PUT** /sources/{sourceId}/schemas/{schemaId} | Update Source Schema (Full)
[**sync_attributes_for_source**](SourcesApi.md#sync_attributes_for_source) | **POST** /sources/{sourceId}/synchronize-attributes | Synchronize single source attributes.
[**test_source_configuration**](SourcesApi.md#test_source_configuration) | **POST** /sources/{sourceId}/connector/test-configuration | Test configuration for source connector
[**test_source_connection**](SourcesApi.md#test_source_connection) | **POST** /sources/{sourceId}/connector/check-connection | Check connection for source connector.
[**update_provisioning_policies_in_bulk**](SourcesApi.md#update_provisioning_policies_in_bulk) | **POST** /sources/{sourceId}/provisioning-policies/bulk-update | Bulk Update Provisioning Policies
[**update_provisioning_policy**](SourcesApi.md#update_provisioning_policy) | **PATCH** /sources/{sourceId}/provisioning-policies/{usageType} | Partial update of Provisioning Policy
[**update_source**](SourcesApi.md#update_source) | **PATCH** /sources/{id} | Update Source (Partial)
[**update_source_entitlement_request_config**](SourcesApi.md#update_source_entitlement_request_config) | **PUT** /sources/{sourceId}/entitlement-request-config | Update Source Entitlement Request Configuration
[**update_source_schema**](SourcesApi.md#update_source_schema) | **PATCH** /sources/{sourceId}/schemas/{schemaId} | Update Source Schema (Partial)


# **create_provisioning_policy**
> ProvisioningPolicyDto create_provisioning_policy(source_id, provisioning_policy_dto)

Create Provisioning Policy

This API generates a create policy/template based on field value transforms. This API is intended for use when setting up JDBC Provisioning type sources, but it will also work on other source types. Transforms can be used in the provisioning policy to create a new attribute that you only need during provisioning. Refer to [Transforms in Provisioning Policies](https://developer.sailpoint.com/idn/docs/transforms/guides/transforms-in-provisioning-policies) for more information.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.provisioning_policy_dto import ProvisioningPolicyDto
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The Source id
    provisioning_policy_dto = {name=Account, description=Account Provisioning Policy, usageType=CREATE, fields=[{name=displayName, transform={type=identityAttribute, attributes={name=displayName}}, attributes={}, isRequired=false, type=string, isMultiValued=false}, {name=distinguishedName, transform={type=usernameGenerator, attributes={sourceCheck=true, patterns=[CN=$fi $ln,OU=zzUsers,OU=Demo,DC=seri,DC=sailpointdemo,DC=com, CN=$fti $ln,OU=zzUsers,OU=Demo,DC=seri,DC=sailpointdemo,DC=com, CN=$fn $ln,OU=zzUsers,OU=Demo,DC=seri,DC=sailpointdemo,DC=com, CN=$fn$ln${uniqueCounter},OU=zzUsers,OU=Demo,DC=seri,DC=sailpointdemo,DC=com], fn={type=identityAttribute, attributes={name=firstname}}, ln={type=identityAttribute, attributes={name=lastname}}, fi={type=substring, attributes={input={type=identityAttribute, attributes={name=firstname}}, begin=0.0, end=1.0}}, fti={type=substring, attributes={input={type=identityAttribute, attributes={name=firstname}}, begin=0.0, end=2.0}}}}, attributes={cloudMaxUniqueChecks=5, cloudMaxSize=100, cloudRequired=true}, isRequired=false, type=, isMultiValued=false}, {name=description, transform={type=static, attributes={value=}}, attributes={}, isRequired=false, type=string, isMultiValued=false}]} # ProvisioningPolicyDto | 

    try:
        # Create Provisioning Policy
        api_response = api_instance.create_provisioning_policy(source_id, provisioning_policy_dto)
        print("The response of SourcesApi->create_provisioning_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->create_provisioning_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id | 
 **provisioning_policy_dto** | [**ProvisioningPolicyDto**](ProvisioningPolicyDto.md)|  | 

### Return type

[**ProvisioningPolicyDto**](ProvisioningPolicyDto.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created ProvisioningPolicyDto object |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_source**
> Source create_source(source, provision_as_csv=provision_as_csv)

Creates a source in IdentityNow.

This creates a specific source with a full source JSON representation. Any passwords are submitted as plain-text and encrypted upon receipt in IdentityNow. A token with ORG_ADMIN, SOURCE_ADMIN, or SOURCE_SUBADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.source import Source
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source = sailpoint.beta.Source() # Source | 
    provision_as_csv = false # bool | If this parameter is `true`, it configures the source as a Delimited File (CSV) source. Setting this to `true` will automatically set the `type` of the source to `DelimitedFile`.  You must use this query parameter to create a Delimited File source as you would in the UI.  If you don't set this query parameter and you attempt to set the `type` attribute directly, the request won't correctly generate the source.   (optional)

    try:
        # Creates a source in IdentityNow.
        api_response = api_instance.create_source(source, provision_as_csv=provision_as_csv)
        print("The response of SourcesApi->create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | [**Source**](Source.md)|  | 
 **provision_as_csv** | **bool**| If this parameter is &#x60;true&#x60;, it configures the source as a Delimited File (CSV) source. Setting this to &#x60;true&#x60; will automatically set the &#x60;type&#x60; of the source to &#x60;DelimitedFile&#x60;.  You must use this query parameter to create a Delimited File source as you would in the UI.  If you don&#39;t set this query parameter and you attempt to set the &#x60;type&#x60; attribute directly, the request won&#39;t correctly generate the source.   | [optional] 

### Return type

[**Source**](Source.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created Source object. Any passwords will only show the the encrypted cipher-text, as they are not decrypt-able in IdentityNow cloud-based services, per IdentityNow security design. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_source_schema**
> ModelSchema create_source_schema(source_id, model_schema)

Create Schema on Source

Use this API to create a new schema on the specified source in Identity Security Cloud (ISC).

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.model_schema import ModelSchema
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | Source ID.
    model_schema = sailpoint.beta.ModelSchema() # ModelSchema | 

    try:
        # Create Schema on Source
        api_response = api_instance.create_source_schema(source_id, model_schema)
        print("The response of SourcesApi->create_source_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->create_source_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| Source ID. | 
 **model_schema** | [**ModelSchema**](ModelSchema.md)|  | 

### Return type

[**ModelSchema**](ModelSchema.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The schema was successfully created on the specified source. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Delete202Response delete(id)

Delete Source by ID

Use this API to delete a specific source in Identity Security Cloud (ISC). The API removes all the accounts on the source first, and then it deletes the source. You can retrieve the actual task execution status with this method: GET `/task-status/{id}` A token with ORG_ADMIN, SOURCE_ADMIN, or SOURCE_SUBADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.delete202_response import Delete202Response
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    id = '2c9180835d191a86015d28455b4a2329' # str | Source ID.

    try:
        # Delete Source by ID
        api_response = api_instance.delete(id)
        print("The response of SourcesApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Source ID. | 

### Return type

[**Delete202Response**](Delete202Response.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

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

# **delete_accounts_async**
> TaskResultDto delete_accounts_async(source_id)

Remove All Accounts in a Source

Use this endpoint to remove all accounts from the system without provisioning changes to the source. Accounts that are removed could be re-created during the next aggregation.  This endpoint is good for: * Removing accounts that no longer exist on the source. * Removing accounts that won't be aggregated following updates to the source configuration. * Forcing accounts to be re-created following the next aggregation to re-run account processing, support testing, etc. 

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.task_result_dto import TaskResultDto
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = 'ebbf35756e1140699ce52b233121384a' # str | The source id

    try:
        # Remove All Accounts in a Source
        api_response = api_instance.delete_accounts_async(source_id)
        print("The response of SourcesApi->delete_accounts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->delete_accounts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The source id | 

### Return type

[**TaskResultDto**](TaskResultDto.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. Returns task result details of removal request. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_native_change_detection_config**
> delete_native_change_detection_config(source_id)

Delete Native Change Detection Configuration

Deletes the native change detection configuration for the source specified by the given ID. A token with API, or ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The source id

    try:
        # Delete Native Change Detection Configuration
        api_instance.delete_native_change_detection_config(source_id)
    except Exception as e:
        print("Exception when calling SourcesApi->delete_native_change_detection_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The source id | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

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

# **delete_provisioning_policy**
> delete_provisioning_policy(source_id, usage_type)

Delete Provisioning Policy by UsageType

Deletes the provisioning policy with the specified usage on an application.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.usage_type import UsageType
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The Source ID.
    usage_type = sailpoint.beta.UsageType() # UsageType | The type of provisioning policy usage.  In IdentityNow, a source can support various provisioning operations. For example, when a joiner is added to a source, this may trigger both CREATE and UPDATE provisioning operations.  Each usage type is considered a provisioning policy.  A source can have any number of these provisioning policies defined.  These are the common usage types:  CREATE - This usage type relates to 'Create Account Profile', the provisioning template for the account to be created. For example, this would be used for a joiner on a source.   UPDATE - This usage type relates to 'Update Account Profile', the provisioning template for the 'Update' connector operations. For example, this would be used for an attribute sync on a source. ENABLE - This usage type relates to 'Enable Account Profile', the provisioning template for the account to be enabled. For example, this could be used for a joiner on a source once the joiner's account is created.  DISABLE - This usage type relates to 'Disable Account Profile', the provisioning template for the account to be disabled. For example, this could be used when a leaver is removed temporarily from a source.  You can use these four usage types for all your provisioning policy needs. 

    try:
        # Delete Provisioning Policy by UsageType
        api_instance.delete_provisioning_policy(source_id, usage_type)
    except Exception as e:
        print("Exception when calling SourcesApi->delete_provisioning_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source ID. | 
 **usage_type** | [**UsageType**](.md)| The type of provisioning policy usage.  In IdentityNow, a source can support various provisioning operations. For example, when a joiner is added to a source, this may trigger both CREATE and UPDATE provisioning operations.  Each usage type is considered a provisioning policy.  A source can have any number of these provisioning policies defined.  These are the common usage types:  CREATE - This usage type relates to &#39;Create Account Profile&#39;, the provisioning template for the account to be created. For example, this would be used for a joiner on a source.   UPDATE - This usage type relates to &#39;Update Account Profile&#39;, the provisioning template for the &#39;Update&#39; connector operations. For example, this would be used for an attribute sync on a source. ENABLE - This usage type relates to &#39;Enable Account Profile&#39;, the provisioning template for the account to be enabled. For example, this could be used for a joiner on a source once the joiner&#39;s account is created.  DISABLE - This usage type relates to &#39;Disable Account Profile&#39;, the provisioning template for the account to be disabled. For example, this could be used when a leaver is removed temporarily from a source.  You can use these four usage types for all your provisioning policy needs.  | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

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

# **delete_source_schema**
> delete_source_schema(source_id, schema_id)

Delete Source Schema by ID

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The Source ID.
    schema_id = '2c9180835d191a86015d28455b4a2329' # str | The Schema ID.

    try:
        # Delete Source Schema by ID
        api_instance.delete_source_schema(source_id, schema_id)
    except Exception as e:
        print("Exception when calling SourcesApi->delete_source_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source ID. | 
 **schema_id** | **str**| The Schema ID. | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

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

# **get_correlation_config**
> CorrelationConfig get_correlation_config(source_id)

Get Source Correlation Configuration

This API returns the existing correlation configuration for a source specified by the given ID.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.correlation_config import CorrelationConfig
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The source id

    try:
        # Get Source Correlation Configuration
        api_response = api_instance.get_correlation_config(source_id)
        print("The response of SourcesApi->get_correlation_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_correlation_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The source id | 

### Return type

[**CorrelationConfig**](CorrelationConfig.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Correlation configuration for a source |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_native_change_detection_config**
> NativeChangeDetectionConfig get_native_change_detection_config(source_id)

Native Change Detection Configuration

This API returns the existing native change detection configuration for a source specified by the given ID. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.native_change_detection_config import NativeChangeDetectionConfig
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The source id

    try:
        # Native Change Detection Configuration
        api_response = api_instance.get_native_change_detection_config(source_id)
        print("The response of SourcesApi->get_native_change_detection_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_native_change_detection_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The source id | 

### Return type

[**NativeChangeDetectionConfig**](NativeChangeDetectionConfig.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Native change detection configuration for a source |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provisioning_policy**
> ProvisioningPolicyDto get_provisioning_policy(source_id, usage_type)

Get Provisioning Policy by UsageType

This end-point retrieves the ProvisioningPolicy with the specified usage on the specified Source in IdentityNow.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.provisioning_policy_dto import ProvisioningPolicyDto
from sailpoint.beta.models.usage_type import UsageType
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The Source ID.
    usage_type = sailpoint.beta.UsageType() # UsageType | The type of provisioning policy usage.  In IdentityNow, a source can support various provisioning operations. For example, when a joiner is added to a source, this may trigger both CREATE and UPDATE provisioning operations.  Each usage type is considered a provisioning policy.  A source can have any number of these provisioning policies defined.  These are the common usage types:  CREATE - This usage type relates to 'Create Account Profile', the provisioning template for the account to be created. For example, this would be used for a joiner on a source.   UPDATE - This usage type relates to 'Update Account Profile', the provisioning template for the 'Update' connector operations. For example, this would be used for an attribute sync on a source. ENABLE - This usage type relates to 'Enable Account Profile', the provisioning template for the account to be enabled. For example, this could be used for a joiner on a source once the joiner's account is created.  DISABLE - This usage type relates to 'Disable Account Profile', the provisioning template for the account to be disabled. For example, this could be used when a leaver is removed temporarily from a source.  You can use these four usage types for all your provisioning policy needs. 

    try:
        # Get Provisioning Policy by UsageType
        api_response = api_instance.get_provisioning_policy(source_id, usage_type)
        print("The response of SourcesApi->get_provisioning_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_provisioning_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source ID. | 
 **usage_type** | [**UsageType**](.md)| The type of provisioning policy usage.  In IdentityNow, a source can support various provisioning operations. For example, when a joiner is added to a source, this may trigger both CREATE and UPDATE provisioning operations.  Each usage type is considered a provisioning policy.  A source can have any number of these provisioning policies defined.  These are the common usage types:  CREATE - This usage type relates to &#39;Create Account Profile&#39;, the provisioning template for the account to be created. For example, this would be used for a joiner on a source.   UPDATE - This usage type relates to &#39;Update Account Profile&#39;, the provisioning template for the &#39;Update&#39; connector operations. For example, this would be used for an attribute sync on a source. ENABLE - This usage type relates to &#39;Enable Account Profile&#39;, the provisioning template for the account to be enabled. For example, this could be used for a joiner on a source once the joiner&#39;s account is created.  DISABLE - This usage type relates to &#39;Disable Account Profile&#39;, the provisioning template for the account to be disabled. For example, this could be used when a leaver is removed temporarily from a source.  You can use these four usage types for all your provisioning policy needs.  | 

### Return type

[**ProvisioningPolicyDto**](ProvisioningPolicyDto.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested ProvisioningPolicyDto was successfully retrieved. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source**
> Source get_source(id)

Get Source by ID

Use this API to get a source by a specified ID in Identity Security Cloud (ISC). A token with ORG_ADMIN, SOURCE_ADMIN, or SOURCE_SUBADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.source import Source
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    id = '2c9180835d191a86015d28455b4a2329' # str | Source ID.

    try:
        # Get Source by ID
        api_response = api_instance.get_source(id)
        print("The response of SourcesApi->get_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Source ID. | 

### Return type

[**Source**](Source.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Source object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_accounts_schema**
> get_source_accounts_schema(source_id)

Downloads source accounts schema template

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The Source id

    try:
        # Downloads source accounts schema template
        api_instance.get_source_accounts_schema(source_id)
    except Exception as e:
        print("Exception when calling SourcesApi->get_source_accounts_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully downloaded the file |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_attr_sync_config**
> AttrSyncSourceConfig get_source_attr_sync_config(id)

Attribute Sync Config

This API returns the existing attribute synchronization configuration for a source specified by the given ID. The response contains all attributes, regardless of whether they enabled or not. A token with ORG_ADMIN or HELPDESK authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.attr_sync_source_config import AttrSyncSourceConfig
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    id = '2c9180835d191a86015d28455b4a2329' # str | The source id

    try:
        # Attribute Sync Config
        api_response = api_instance.get_source_attr_sync_config(id)
        print("The response of SourcesApi->get_source_attr_sync_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_source_attr_sync_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The source id | 

### Return type

[**AttrSyncSourceConfig**](AttrSyncSourceConfig.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attribute synchronization configuration for a source |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_config**
> ConnectorDetail get_source_config(id, locale=locale)

Gets source config with language translations

Looks up and returns the source config for the requested source id after populating the source config values and applying language translations. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.connector_detail import ConnectorDetail
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    id = 'id_example' # str | The Source id
    locale = 'locale_example' # str | The locale to apply to the config. If no viable locale is given, it will default to \"en\" (optional)

    try:
        # Gets source config with language translations
        api_response = api_instance.get_source_config(id, locale=locale)
        print("The response of SourcesApi->get_source_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_source_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Source id | 
 **locale** | **str**| The locale to apply to the config. If no viable locale is given, it will default to \&quot;en\&quot; | [optional] 

### Return type

[**ConnectorDetail**](ConnectorDetail.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Connector Detail object |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_entitlement_request_config**
> SourceEntitlementRequestConfig get_source_entitlement_request_config(source_id)

Get Source Entitlement Request Configuration

This API gets the current entitlement request configuration for a source. This source-level configuration should apply for all the entitlements in the source.  Access request to any entitlements in the source should follow this configuration unless a separate entitlement-level configuration is defined. - During access request, this source-level entitlement request configuration overrides the global organization-level configuration. - However, the entitlement-level configuration (if defined) overrides this source-level configuration.  A token with ORG_ADMIN, SOURCE_ADMIN, or SOURCE_SUBADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.source_entitlement_request_config import SourceEntitlementRequestConfig
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The Source id

    try:
        # Get Source Entitlement Request Configuration
        api_response = api_instance.get_source_entitlement_request_config(source_id)
        print("The response of SourcesApi->get_source_entitlement_request_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_source_entitlement_request_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id | 

### Return type

[**SourceEntitlementRequestConfig**](SourceEntitlementRequestConfig.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Source Entitlement Request Configuration Details. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_entitlements_schema**
> get_source_entitlements_schema(source_id, schema_name=schema_name)

Downloads source entitlements schema template

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The Source id
    schema_name = '?schemaName=group' # str | Name of entitlement schema (optional)

    try:
        # Downloads source entitlements schema template
        api_instance.get_source_entitlements_schema(source_id, schema_name=schema_name)
    except Exception as e:
        print("Exception when calling SourcesApi->get_source_entitlements_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id | 
 **schema_name** | **str**| Name of entitlement schema | [optional] 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully downloaded the file |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_schema**
> ModelSchema get_source_schema(source_id, schema_id)

Get Source Schema by ID

Get the Source Schema by ID in IdentityNow. 

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.model_schema import ModelSchema
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The Source ID.
    schema_id = '2c9180835d191a86015d28455b4a2329' # str | The Schema ID.

    try:
        # Get Source Schema by ID
        api_response = api_instance.get_source_schema(source_id, schema_id)
        print("The response of SourcesApi->get_source_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_source_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source ID. | 
 **schema_id** | **str**| The Schema ID. | 

### Return type

[**ModelSchema**](ModelSchema.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Schema was successfully retrieved. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_schemas**
> List[ModelSchema] get_source_schemas(source_id, include_types=include_types, include_names=include_names)

List Schemas on Source

Use this API to list the schemas that exist on the specified source in Identity Security Cloud (ISC).

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.model_schema import ModelSchema
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | Source ID.
    include_types = 'group' # str | If set to 'group', then the account schema is filtered and only group schemas are returned. Only a value of 'group' is recognized presently.  Note: The API will check whether include-types is group or not, if not, it will list schemas based on include-names, if include-names is not provided, it will list all schemas. (optional)
    include_names = 'account' # str | A comma-separated list of schema names to filter result. (optional)

    try:
        # List Schemas on Source
        api_response = api_instance.get_source_schemas(source_id, include_types=include_types, include_names=include_names)
        print("The response of SourcesApi->get_source_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_source_schemas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| Source ID. | 
 **include_types** | **str**| If set to &#39;group&#39;, then the account schema is filtered and only group schemas are returned. Only a value of &#39;group&#39; is recognized presently.  Note: The API will check whether include-types is group or not, if not, it will list schemas based on include-names, if include-names is not provided, it will list all schemas. | [optional] 
 **include_names** | **str**| A comma-separated list of schema names to filter result. | [optional] 

### Return type

[**List[ModelSchema]**](ModelSchema.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The schemas were successfully retrieved. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_accounts**
> LoadAccountsTask import_accounts(source_id, file=file, disable_optimization=disable_optimization)

Account Aggregation

Starts an account aggregation on the specified source.  If the target source is a delimited file source, then the CSV file needs to be included in the request body. You will also need to set the Content-Type header to `multipart/form-data`. A token with ORG_ADMIN, SOURCE_ADMIN, or SOURCE_SUBADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.load_accounts_task import LoadAccountsTask
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = 'ef38f94347e94562b5bb8424a56397d8' # str | Source Id
    file = None # bytearray | The CSV file containing the source accounts to aggregate. (optional)
    disable_optimization = 'disable_optimization_example' # str | Use this flag to reprocess every account whether or not the data has changed. (optional)

    try:
        # Account Aggregation
        api_response = api_instance.import_accounts(source_id, file=file, disable_optimization=disable_optimization)
        print("The response of SourcesApi->import_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->import_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| Source Id | 
 **file** | **bytearray**| The CSV file containing the source accounts to aggregate. | [optional] 
 **disable_optimization** | **str**| Use this flag to reprocess every account whether or not the data has changed. | [optional] 

### Return type

[**LoadAccountsTask**](LoadAccountsTask.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Aggregate Accounts Task |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_entitlements**
> LoadEntitlementTask import_entitlements(source_id, file=file)

Entitlement Aggregation

Starts an entitlement aggregation on the specified source.  If the target source is a delimited file source, then the CSV file needs to be included in the request body.  You will also need to set the Content-Type header to `multipart/form-data`. A token with ORG_ADMIN, SOURCE_ADMIN, or SOURCE_SUBADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.load_entitlement_task import LoadEntitlementTask
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = 'ef38f94347e94562b5bb8424a56397d8' # str | Source Id
    file = None # bytearray | The CSV file containing the source entitlements to aggregate. (optional)

    try:
        # Entitlement Aggregation
        api_response = api_instance.import_entitlements(source_id, file=file)
        print("The response of SourcesApi->import_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->import_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| Source Id | 
 **file** | **bytearray**| The CSV file containing the source entitlements to aggregate. | [optional] 

### Return type

[**LoadEntitlementTask**](LoadEntitlementTask.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Aggregate Entitlements Task |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_source_accounts_schema**
> ModelSchema import_source_accounts_schema(source_id, file=file)

Uploads source accounts schema template

This API uploads a source schema template file to configure a source's account attributes.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.model_schema import ModelSchema
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The Source id
    file = None # bytearray |  (optional)

    try:
        # Uploads source accounts schema template
        api_response = api_instance.import_source_accounts_schema(source_id, file=file)
        print("The response of SourcesApi->import_source_accounts_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->import_source_accounts_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id | 
 **file** | **bytearray**|  | [optional] 

### Return type

[**ModelSchema**](ModelSchema.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully uploaded the file |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_source_connector_file**
> Source import_source_connector_file(source_id, file=file)

Upload connector file to source

This uploads a supplemental source connector file (like jdbc driver jars) to a source's S3 bucket. This also sends ETS and Audit events. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.source import Source
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The Source id
    file = None # bytearray |  (optional)

    try:
        # Upload connector file to source
        api_response = api_instance.import_source_connector_file(source_id, file=file)
        print("The response of SourcesApi->import_source_connector_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->import_source_connector_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id | 
 **file** | **bytearray**|  | [optional] 

### Return type

[**Source**](Source.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Uploaded the file successfully and sent all post-upload events |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_source_entitlements_schema**
> ModelSchema import_source_entitlements_schema(source_id, schema_name=schema_name, file=file)

Uploads source entitlements schema template

This API uploads a source schema template file to configure a source's entitlement attributes.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.model_schema import ModelSchema
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The Source id
    schema_name = '?schemaName=group' # str | Name of entitlement schema (optional)
    file = None # bytearray |  (optional)

    try:
        # Uploads source entitlements schema template
        api_response = api_instance.import_source_entitlements_schema(source_id, schema_name=schema_name, file=file)
        print("The response of SourcesApi->import_source_entitlements_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->import_source_entitlements_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id | 
 **schema_name** | **str**| Name of entitlement schema | [optional] 
 **file** | **bytearray**|  | [optional] 

### Return type

[**ModelSchema**](ModelSchema.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully uploaded the file |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_uncorrelated_accounts**
> LoadUncorrelatedAccountsTask import_uncorrelated_accounts(source_id, file=file)

Process Uncorrelated Accounts

File is required for upload. You will also need to set the Content-Type header to `multipart/form-data`

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.load_uncorrelated_accounts_task import LoadUncorrelatedAccountsTask
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '75dbec1ebe154d5785da27b95e1dd5d7' # str | Source Id
    file = None # bytearray |  (optional)

    try:
        # Process Uncorrelated Accounts
        api_response = api_instance.import_uncorrelated_accounts(source_id, file=file)
        print("The response of SourcesApi->import_uncorrelated_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->import_uncorrelated_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| Source Id | 
 **file** | **bytearray**|  | [optional] 

### Return type

[**LoadUncorrelatedAccountsTask**](LoadUncorrelatedAccountsTask.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Uncorrelated Accounts Task |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_provisioning_policies**
> List[ProvisioningPolicyDto] list_provisioning_policies(source_id)

Lists ProvisioningPolicies

This end-point lists all the ProvisioningPolicies in IdentityNow.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.provisioning_policy_dto import ProvisioningPolicyDto
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The Source id

    try:
        # Lists ProvisioningPolicies
        api_response = api_instance.list_provisioning_policies(source_id)
        print("The response of SourcesApi->list_provisioning_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->list_provisioning_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id | 

### Return type

[**List[ProvisioningPolicyDto]**](ProvisioningPolicyDto.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProvisioningPolicyDto objects |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sources**
> List[Source] list_sources(limit=limit, offset=offset, count=count, filters=filters, sorters=sorters, for_subadmin=for_subadmin, include_idn_source=include_idn_source)

Lists all sources in IdentityNow.

This end-point lists all the sources in IdentityNow.  A token with ORG_ADMIN, SOURCE_ADMIN, SOURCE_SUBADMIN, or ROLE_SUBADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.source import Source
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'name eq \"Employees\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in, ge, gt, le, lt, ne, isnull, sw*  **name**: *co, eq, in, sw, ge, gt, ne, isnull*  **type**: *eq, in, ge, gt, ne, isnull, sw*  **owner.id**: *eq, in, ge, gt, le, lt, ne, isnull, sw*  **features**: *ca, co*  **created**: *eq*  **modified**: *eq*  **managementWorkgroup.id**: *eq, ge, gt, in, le, lt, ne, isnull, sw*  **description**: *eq, sw*  **authoritative**: *eq, ne, isnull*  **healthy**: *isnull*  **status**: *eq, in, ge, gt, le, lt, ne, isnull, sw*  **connectionType**: *eq, ge, gt, in, le, lt, ne, isnull, sw*  **connectorName**: *eq, ge, gt, in, ne, isnull, sw*  **category**: *co, eq, ge, gt, in, le, lt, ne, sw* (optional)
    sorters = 'name' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **type, created, modified, name, owner.name, healthy, status, id, description, owner.id, accountCorrelationConfig.id, accountCorrelationConfig.name, managerCorrelationRule.type, managerCorrelationRule.id, managerCorrelationRule.name, authoritative, managementWorkgroup.id, connectorName, connectionType** (optional)
    for_subadmin = 'name' # str | Filter the returned list of sources for the identity specified by the parameter, which is the id of an identity with the role SOURCE_SUBADMIN. By convention, the value **me** indicates the identity id of the current user. Subadmins may only view Sources which they are able to administer; all other Sources will be filtered out when this parameter is set. If the current user is a SOURCE_SUBADMIN but fails to pass a valid value for this parameter, a 403 Forbidden is returned. (optional)
    include_idn_source = False # bool | Include the IdentityNow source in the response. (optional) (default to False)

    try:
        # Lists all sources in IdentityNow.
        api_response = api_instance.list_sources(limit=limit, offset=offset, count=count, filters=filters, sorters=sorters, for_subadmin=for_subadmin, include_idn_source=include_idn_source)
        print("The response of SourcesApi->list_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->list_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in, ge, gt, le, lt, ne, isnull, sw*  **name**: *co, eq, in, sw, ge, gt, ne, isnull*  **type**: *eq, in, ge, gt, ne, isnull, sw*  **owner.id**: *eq, in, ge, gt, le, lt, ne, isnull, sw*  **features**: *ca, co*  **created**: *eq*  **modified**: *eq*  **managementWorkgroup.id**: *eq, ge, gt, in, le, lt, ne, isnull, sw*  **description**: *eq, sw*  **authoritative**: *eq, ne, isnull*  **healthy**: *isnull*  **status**: *eq, in, ge, gt, le, lt, ne, isnull, sw*  **connectionType**: *eq, ge, gt, in, le, lt, ne, isnull, sw*  **connectorName**: *eq, ge, gt, in, ne, isnull, sw*  **category**: *co, eq, ge, gt, in, le, lt, ne, sw* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **type, created, modified, name, owner.name, healthy, status, id, description, owner.id, accountCorrelationConfig.id, accountCorrelationConfig.name, managerCorrelationRule.type, managerCorrelationRule.id, managerCorrelationRule.name, authoritative, managementWorkgroup.id, connectorName, connectionType** | [optional] 
 **for_subadmin** | **str**| Filter the returned list of sources for the identity specified by the parameter, which is the id of an identity with the role SOURCE_SUBADMIN. By convention, the value **me** indicates the identity id of the current user. Subadmins may only view Sources which they are able to administer; all other Sources will be filtered out when this parameter is set. If the current user is a SOURCE_SUBADMIN but fails to pass a valid value for this parameter, a 403 Forbidden is returned. | [optional] 
 **include_idn_source** | **bool**| Include the IdentityNow source in the response. | [optional] [default to False]

### Return type

[**List[Source]**](Source.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Source objects |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peek_resource_objects**
> ResourceObjectsResponse peek_resource_objects(source_id, resource_objects_request)

Peek source connector's resource objects

Retrieves a sample of data returned from account and group aggregation requests. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.resource_objects_request import ResourceObjectsRequest
from sailpoint.beta.models.resource_objects_response import ResourceObjectsResponse
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = 'cef3ee201db947c5912551015ba0c679' # str | The ID of the Source
    resource_objects_request = sailpoint.beta.ResourceObjectsRequest() # ResourceObjectsRequest | 

    try:
        # Peek source connector's resource objects
        api_response = api_instance.peek_resource_objects(source_id, resource_objects_request)
        print("The response of SourcesApi->peek_resource_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->peek_resource_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the Source | 
 **resource_objects_request** | [**ResourceObjectsRequest**](ResourceObjectsRequest.md)|  | 

### Return type

[**ResourceObjectsResponse**](ResourceObjectsResponse.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resource objects that was fetched from the source connector. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_cluster**
> StatusResponse ping_cluster(source_id)

Ping cluster for source connector

This endpoint validates that the cluster being used by the source is reachable from IdentityNow. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.status_response import StatusResponse
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = 'cef3ee201db947c5912551015ba0c679' # str | The ID of the Source

    try:
        # Ping cluster for source connector
        api_response = api_instance.ping_cluster(source_id)
        print("The response of SourcesApi->ping_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->ping_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the Source | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of pinging connection with the source connector. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_correlation_config**
> CorrelationConfig put_correlation_config(source_id, correlation_config)

Update Source Correlation Configuration

Replaces the correlation configuration for the source specified by the given ID with the configuration provided in the request body.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.correlation_config import CorrelationConfig
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The source id
    correlation_config = sailpoint.beta.CorrelationConfig() # CorrelationConfig | 

    try:
        # Update Source Correlation Configuration
        api_response = api_instance.put_correlation_config(source_id, correlation_config)
        print("The response of SourcesApi->put_correlation_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->put_correlation_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The source id | 
 **correlation_config** | [**CorrelationConfig**](CorrelationConfig.md)|  | 

### Return type

[**CorrelationConfig**](CorrelationConfig.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated correlation configuration for a source |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_native_change_detection_config**
> NativeChangeDetectionConfig put_native_change_detection_config(source_id, native_change_detection_config)

Update Native Change Detection Configuration

Replaces the native change detection configuration for the source specified by the given ID with the configuration provided in the request body.      A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.native_change_detection_config import NativeChangeDetectionConfig
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The source id
    native_change_detection_config = sailpoint.beta.NativeChangeDetectionConfig() # NativeChangeDetectionConfig | 

    try:
        # Update Native Change Detection Configuration
        api_response = api_instance.put_native_change_detection_config(source_id, native_change_detection_config)
        print("The response of SourcesApi->put_native_change_detection_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->put_native_change_detection_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The source id | 
 **native_change_detection_config** | [**NativeChangeDetectionConfig**](NativeChangeDetectionConfig.md)|  | 

### Return type

[**NativeChangeDetectionConfig**](NativeChangeDetectionConfig.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated native change detection configuration for a source |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_provisioning_policy**
> ProvisioningPolicyDto put_provisioning_policy(source_id, usage_type, provisioning_policy_dto)

Update Provisioning Policy by UsageType

This end-point updates the provisioning policy with the specified usage on the specified source in IdentityNow. Transforms can be used in the provisioning policy to create a new attribute that you only need during provisioning. Refer to [Transforms in Provisioning Policies](https://developer.sailpoint.com/idn/docs/transforms/guides/transforms-in-provisioning-policies) for more information.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.provisioning_policy_dto import ProvisioningPolicyDto
from sailpoint.beta.models.usage_type import UsageType
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The Source ID.
    usage_type = sailpoint.beta.UsageType() # UsageType | The type of provisioning policy usage.  In IdentityNow, a source can support various provisioning operations. For example, when a joiner is added to a source, this may trigger both CREATE and UPDATE provisioning operations.  Each usage type is considered a provisioning policy.  A source can have any number of these provisioning policies defined.  These are the common usage types:  CREATE - This usage type relates to 'Create Account Profile', the provisioning template for the account to be created. For example, this would be used for a joiner on a source.   UPDATE - This usage type relates to 'Update Account Profile', the provisioning template for the 'Update' connector operations. For example, this would be used for an attribute sync on a source. ENABLE - This usage type relates to 'Enable Account Profile', the provisioning template for the account to be enabled. For example, this could be used for a joiner on a source once the joiner's account is created.  DISABLE - This usage type relates to 'Disable Account Profile', the provisioning template for the account to be disabled. For example, this could be used when a leaver is removed temporarily from a source.  You can use these four usage types for all your provisioning policy needs. 
    provisioning_policy_dto = sailpoint.beta.ProvisioningPolicyDto() # ProvisioningPolicyDto | 

    try:
        # Update Provisioning Policy by UsageType
        api_response = api_instance.put_provisioning_policy(source_id, usage_type, provisioning_policy_dto)
        print("The response of SourcesApi->put_provisioning_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->put_provisioning_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source ID. | 
 **usage_type** | [**UsageType**](.md)| The type of provisioning policy usage.  In IdentityNow, a source can support various provisioning operations. For example, when a joiner is added to a source, this may trigger both CREATE and UPDATE provisioning operations.  Each usage type is considered a provisioning policy.  A source can have any number of these provisioning policies defined.  These are the common usage types:  CREATE - This usage type relates to &#39;Create Account Profile&#39;, the provisioning template for the account to be created. For example, this would be used for a joiner on a source.   UPDATE - This usage type relates to &#39;Update Account Profile&#39;, the provisioning template for the &#39;Update&#39; connector operations. For example, this would be used for an attribute sync on a source. ENABLE - This usage type relates to &#39;Enable Account Profile&#39;, the provisioning template for the account to be enabled. For example, this could be used for a joiner on a source once the joiner&#39;s account is created.  DISABLE - This usage type relates to &#39;Disable Account Profile&#39;, the provisioning template for the account to be disabled. For example, this could be used when a leaver is removed temporarily from a source.  You can use these four usage types for all your provisioning policy needs.  | 
 **provisioning_policy_dto** | [**ProvisioningPolicyDto**](ProvisioningPolicyDto.md)|  | 

### Return type

[**ProvisioningPolicyDto**](ProvisioningPolicyDto.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ProvisioningPolicyDto was successfully replaced. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_source**
> Source put_source(id, source)

Update Source (Full)

Use this API to update a source in Identity Security Cloud (ISC), using a full object representation. This means that when you use this API, it completely replaces the existing source configuration.  These fields are immutable, so they cannot be changed:  * id * type * authoritative * connector * connectorClass * passwordPolicies  Attempts to modify these fields will result in a 400 error.  A token with ORG_ADMIN, SOURCE_ADMIN, or SOURCE_SUBADMIN authority is required to call this API. 

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.source import Source
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    id = '2c9180835d191a86015d28455b4a2329' # str | Source ID.
    source = sailpoint.beta.Source() # Source | 

    try:
        # Update Source (Full)
        api_response = api_instance.put_source(id, source)
        print("The response of SourcesApi->put_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->put_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Source ID. | 
 **source** | [**Source**](Source.md)|  | 

### Return type

[**Source**](Source.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Source object. Any passwords will only show the the encrypted cipher-text so that they aren&#39;t decryptable in Identity Security Cloud (ISC) cloud-based services, per ISC security design. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_source_attr_sync_config**
> AttrSyncSourceConfig put_source_attr_sync_config(id, attr_sync_source_config)

Update Attribute Sync Config

Replaces the attribute synchronization configuration for the source specified by the given ID with the configuration provided in the request body. Only the \"enabled\" field of the values in the \"attributes\" array is mutable. Attempting to change other attributes or add new values to the \"attributes\" array will result in an error.      A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.attr_sync_source_config import AttrSyncSourceConfig
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    id = '2c9180835d191a86015d28455b4a2329' # str | The source id
    attr_sync_source_config = sailpoint.beta.AttrSyncSourceConfig() # AttrSyncSourceConfig | 

    try:
        # Update Attribute Sync Config
        api_response = api_instance.put_source_attr_sync_config(id, attr_sync_source_config)
        print("The response of SourcesApi->put_source_attr_sync_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->put_source_attr_sync_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The source id | 
 **attr_sync_source_config** | [**AttrSyncSourceConfig**](AttrSyncSourceConfig.md)|  | 

### Return type

[**AttrSyncSourceConfig**](AttrSyncSourceConfig.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated attribute synchronization configuration for a source |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_source_schema**
> ModelSchema put_source_schema(source_id, schema_id, model_schema)

Update Source Schema (Full)

This API will completely replace an existing Schema with the submitted payload. Some fields of the Schema cannot be updated. These fields are listed below. * id * name * created * modified Any attempt to modify these fields will result in an error response with a status code of 400.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.model_schema import ModelSchema
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The Source ID.
    schema_id = '2c9180835d191a86015d28455b4a2329' # str | The Schema ID.
    model_schema = sailpoint.beta.ModelSchema() # ModelSchema | 

    try:
        # Update Source Schema (Full)
        api_response = api_instance.put_source_schema(source_id, schema_id, model_schema)
        print("The response of SourcesApi->put_source_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->put_source_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source ID. | 
 **schema_id** | **str**| The Schema ID. | 
 **model_schema** | [**ModelSchema**](ModelSchema.md)|  | 

### Return type

[**ModelSchema**](ModelSchema.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Schema was successfully replaced. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_attributes_for_source**
> SourceSyncJob sync_attributes_for_source(source_id)

Synchronize single source attributes.

This end-point performs attribute synchronization for a selected source. A token with ORG_ADMIN or SOURCE_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.source_sync_job import SourceSyncJob
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = 'source_id_example' # str | The Source id

    try:
        # Synchronize single source attributes.
        api_response = api_instance.sync_attributes_for_source(source_id)
        print("The response of SourcesApi->sync_attributes_for_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sync_attributes_for_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id | 

### Return type

[**SourceSyncJob**](SourceSyncJob.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | A Source Sync job |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_source_configuration**
> StatusResponse test_source_configuration(source_id)

Test configuration for source connector

This endpoint performs a more detailed validation of the source's configuration that can take longer than the lighter weight credential validation performed by the checkConnection API. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.status_response import StatusResponse
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = 'cef3ee201db947c5912551015ba0c679' # str | The ID of the Source

    try:
        # Test configuration for source connector
        api_response = api_instance.test_source_configuration(source_id)
        print("The response of SourcesApi->test_source_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->test_source_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the Source | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of testing source connector configuration with response from it. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_source_connection**
> StatusResponse test_source_connection(source_id)

Check connection for source connector.

This endpoint validates that the configured credentials are valid and will properly authenticate with the source identified by the sourceId path parameter. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.status_response import StatusResponse
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = 'cef3ee201db947c5912551015ba0c679' # str | The ID of the Source.

    try:
        # Check connection for source connector.
        api_response = api_instance.test_source_connection(source_id)
        print("The response of SourcesApi->test_source_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->test_source_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the Source. | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of checking connection to the source connector with response from it. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_provisioning_policies_in_bulk**
> List[ProvisioningPolicyDto] update_provisioning_policies_in_bulk(source_id, provisioning_policy_dto)

Bulk Update Provisioning Policies

This end-point updates a list of provisioning policies on the specified source in IdentityNow.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.provisioning_policy_dto import ProvisioningPolicyDto
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The Source id.
    provisioning_policy_dto = [sailpoint.beta.ProvisioningPolicyDto()] # List[ProvisioningPolicyDto] | 

    try:
        # Bulk Update Provisioning Policies
        api_response = api_instance.update_provisioning_policies_in_bulk(source_id, provisioning_policy_dto)
        print("The response of SourcesApi->update_provisioning_policies_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->update_provisioning_policies_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id. | 
 **provisioning_policy_dto** | [**List[ProvisioningPolicyDto]**](ProvisioningPolicyDto.md)|  | 

### Return type

[**List[ProvisioningPolicyDto]**](ProvisioningPolicyDto.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of the ProvisioningPolicyDto was successfully replaced. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_provisioning_policy**
> ProvisioningPolicyDto update_provisioning_policy(source_id, usage_type, json_patch_operation)

Partial update of Provisioning Policy

This API selectively updates an existing Provisioning Policy using a JSONPatch payload. Transforms can be used in the provisioning policy to create a new attribute that you only need during provisioning. Refer to [Transforms in Provisioning Policies](https://developer.sailpoint.com/idn/docs/transforms/guides/transforms-in-provisioning-policies) for more information.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.json_patch_operation import JsonPatchOperation
from sailpoint.beta.models.provisioning_policy_dto import ProvisioningPolicyDto
from sailpoint.beta.models.usage_type import UsageType
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The Source id.
    usage_type = sailpoint.beta.UsageType() # UsageType | The type of provisioning policy usage.  In IdentityNow, a source can support various provisioning operations. For example, when a joiner is added to a source, this may trigger both CREATE and UPDATE provisioning operations.  Each usage type is considered a provisioning policy.  A source can have any number of these provisioning policies defined.  These are the common usage types:  CREATE - This usage type relates to 'Create Account Profile', the provisioning template for the account to be created. For example, this would be used for a joiner on a source.   UPDATE - This usage type relates to 'Update Account Profile', the provisioning template for the 'Update' connector operations. For example, this would be used for an attribute sync on a source. ENABLE - This usage type relates to 'Enable Account Profile', the provisioning template for the account to be enabled. For example, this could be used for a joiner on a source once the joiner's account is created.  DISABLE - This usage type relates to 'Disable Account Profile', the provisioning template for the account to be disabled. For example, this could be used when a leaver is removed temporarily from a source.  You can use these four usage types for all your provisioning policy needs. 
    json_patch_operation = [{op=add, path=/fields/0, value={name=email, transform={type=identityAttribute, attributes={name=email}}, attributes={}, isRequired=false, type=string, isMultiValued=false}}] # List[JsonPatchOperation] | The JSONPatch payload used to update the schema.

    try:
        # Partial update of Provisioning Policy
        api_response = api_instance.update_provisioning_policy(source_id, usage_type, json_patch_operation)
        print("The response of SourcesApi->update_provisioning_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->update_provisioning_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id. | 
 **usage_type** | [**UsageType**](.md)| The type of provisioning policy usage.  In IdentityNow, a source can support various provisioning operations. For example, when a joiner is added to a source, this may trigger both CREATE and UPDATE provisioning operations.  Each usage type is considered a provisioning policy.  A source can have any number of these provisioning policies defined.  These are the common usage types:  CREATE - This usage type relates to &#39;Create Account Profile&#39;, the provisioning template for the account to be created. For example, this would be used for a joiner on a source.   UPDATE - This usage type relates to &#39;Update Account Profile&#39;, the provisioning template for the &#39;Update&#39; connector operations. For example, this would be used for an attribute sync on a source. ENABLE - This usage type relates to &#39;Enable Account Profile&#39;, the provisioning template for the account to be enabled. For example, this could be used for a joiner on a source once the joiner&#39;s account is created.  DISABLE - This usage type relates to &#39;Disable Account Profile&#39;, the provisioning template for the account to be disabled. For example, this could be used when a leaver is removed temporarily from a source.  You can use these four usage types for all your provisioning policy needs.  | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| The JSONPatch payload used to update the schema. | 

### Return type

[**ProvisioningPolicyDto**](ProvisioningPolicyDto.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ProvisioningPolicyDto was successfully updated. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_source**
> Source update_source(id, json_patch_operation)

Update Source (Partial)

Use this API to partially update a source in Identity Security Cloud (ISC), using a list of patch operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  These fields are immutable, so they cannot be changed: * id * type * authoritative * created * modified * connector * connectorClass * passwordPolicies  Attempts to modify these fields will result in a 400 error.  A token with ORG_ADMIN, SOURCE_ADMIN, SOURCE_SUBADMIN, or API authority is required to call this API. 

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.json_patch_operation import JsonPatchOperation
from sailpoint.beta.models.source import Source
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    id = '2c9180835d191a86015d28455b4a2329' # str | Source ID.
    json_patch_operation = [{op=replace, path=/description, value=new description}] # List[JsonPatchOperation] | A list of account update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. Any password changes are submitted as plain-text and encrypted upon receipt in Identity Security Cloud (ISC).

    try:
        # Update Source (Partial)
        api_response = api_instance.update_source(id, json_patch_operation)
        print("The response of SourcesApi->update_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->update_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Source ID. | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| A list of account update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. Any password changes are submitted as plain-text and encrypted upon receipt in Identity Security Cloud (ISC). | 

### Return type

[**Source**](Source.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Source object. Any passwords will only show the the encrypted cipher-text so that they are not decryptable in Identity Security Cloud cloud-based services, per ISC security design. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_source_entitlement_request_config**
> SourceEntitlementRequestConfig update_source_entitlement_request_config(source_id, source_entitlement_request_config)

Update Source Entitlement Request Configuration

This API replaces the current entitlement request configuration for a source. This source-level configuration should apply for all the entitlements in the source.  Access request to any entitlements in the source should follow this configuration unless a separate entitlement-level configuration is defined. - During access request, this source-level entitlement request configuration overrides the global organization-level configuration. - However, the entitlement-level configuration (if defined) overrides this source-level configuration.  A token with ORG_ADMIN, SOURCE_ADMIN, or SOURCE_SUBADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.source_entitlement_request_config import SourceEntitlementRequestConfig
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The Source id
    source_entitlement_request_config = {accessRequestConfig={approvalSchemes=[]}} # SourceEntitlementRequestConfig | 

    try:
        # Update Source Entitlement Request Configuration
        api_response = api_instance.update_source_entitlement_request_config(source_id, source_entitlement_request_config)
        print("The response of SourcesApi->update_source_entitlement_request_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->update_source_entitlement_request_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id | 
 **source_entitlement_request_config** | [**SourceEntitlementRequestConfig**](SourceEntitlementRequestConfig.md)|  | 

### Return type

[**SourceEntitlementRequestConfig**](SourceEntitlementRequestConfig.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Source Entitlement Request Configuration Details. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_source_schema**
> ModelSchema update_source_schema(source_id, schema_id, json_patch_operation)

Update Source Schema (Partial)

Use this API to selectively update an existing Schema using a JSONPatch payload.   The following schema fields are immutable and cannot be updated:  - id - name - created - modified   To switch an account attribute to a group entitlement, you need to have the following in place:  - `isEntitlement: true` - Must define a schema for the group and [add it to the source](https://developer.sailpoint.com/idn/api/beta/create-source-schema) before updating the `isGroup` flag.  For example, here is the `group` account attribute referencing a schema that defines the group: ```json {     \"name\": \"groups\",     \"type\": \"STRING\",     \"schema\": {         \"type\": \"CONNECTOR_SCHEMA\",         \"id\": \"2c9180887671ff8c01767b4671fc7d60\",         \"name\": \"group\"     },     \"description\": \"The groups, roles etc. that reference account group objects\",     \"isMulti\": true,     \"isEntitlement\": true,     \"isGroup\": true } ``` 

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.json_patch_operation import JsonPatchOperation
from sailpoint.beta.models.model_schema import ModelSchema
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.SourcesApi(api_client)
    source_id = '2c9180835d191a86015d28455b4a2329' # str | The Source id.
    schema_id = '2c9180835d191a86015d28455b4a2329' # str | The Schema id.
    json_patch_operation = [{op=replace, path=/displayAttribute, value={new-display-attribute=null}}] # List[JsonPatchOperation] | The JSONPatch payload used to update the schema.

    try:
        # Update Source Schema (Partial)
        api_response = api_instance.update_source_schema(source_id, schema_id, json_patch_operation)
        print("The response of SourcesApi->update_source_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->update_source_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The Source id. | 
 **schema_id** | **str**| The Schema id. | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| The JSONPatch payload used to update the schema. | 

### Return type

[**ModelSchema**](ModelSchema.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Schema was successfully updated. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


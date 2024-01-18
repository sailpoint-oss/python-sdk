# sailpoint.beta.SPConfigApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_sp_config**](SPConfigApi.md#export_sp_config) | **POST** /sp-config/export | Initiates configuration objects export job
[**get_sp_config_export**](SPConfigApi.md#get_sp_config_export) | **GET** /sp-config/export/{id}/download | Download export job result.
[**get_sp_config_export_status**](SPConfigApi.md#get_sp_config_export_status) | **GET** /sp-config/export/{id} | Get export job status
[**get_sp_config_import**](SPConfigApi.md#get_sp_config_import) | **GET** /sp-config/import/{id}/download | Download import job result
[**get_sp_config_import_status**](SPConfigApi.md#get_sp_config_import_status) | **GET** /sp-config/import/{id} | Get import job status
[**import_sp_config**](SPConfigApi.md#import_sp_config) | **POST** /sp-config/import | Initiates configuration objects import job
[**list_sp_config_objects**](SPConfigApi.md#list_sp_config_objects) | **GET** /sp-config/config-objects | Get config object details


# **export_sp_config**
> SpConfigExportJob export_sp_config(export_payload)

Initiates configuration objects export job

This post will export objects from the tenant to a JSON configuration file. For more information about the object types that currently support export functionality, refer to [SaaS Configuration](https://developer.sailpoint.com/idn/docs/saas-configuration/#supported-objects).

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.export_payload import ExportPayload
from sailpoint.beta.models.sp_config_export_job import SpConfigExportJob
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
    api_instance = sailpoint.beta.SPConfigApi(api_client)
    export_payload = {description=Export all available objects, excludeTypes=[], includeTypes=[ACCESS_PROFILE, ACCESS_REQUEST_CONFIG, ATTR_SYNC_SOURCE_CONFIG, AUTH_ORG, CAMPAIGN_FILTER, FORM_DEFINITION, GOVERNANCE_GROUP, IDENTITY_OBJECT_CONFIG, IDENTITY_PROFILE, LIFECYCLE_STATE, NOTIFICATION_TEMPLATE, PASSWORD_POLICY, PASSWORD_SYNC_GROUP, PUBLIC_IDENTITIES_CONFIG, ROLE, RULE, SEGMENT, SERVICE_DESK_INTEGRATION, SOD_POLICY, SOURCE, TAG, TRANSFORM, TRIGGER_SUBSCRIPTION, WORKFLOW], objectOptions={}} # ExportPayload | Export options control what will be included in the export.

    try:
        # Initiates configuration objects export job
        api_response = api_instance.export_sp_config(export_payload)
        print("The response of SPConfigApi->export_sp_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SPConfigApi->export_sp_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_payload** | [**ExportPayload**](ExportPayload.md)| Export options control what will be included in the export. | 

### Return type

[**SpConfigExportJob**](SpConfigExportJob.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Export job accepted and queued for processing. |  -  |
**400** | Client Error - Returned if the request body is invalid.  |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sp_config_export**
> SpConfigExportResults get_sp_config_export(id)

Download export job result.

This endpoint gets the export file resulting from the export job with the requested `id` and downloads it to a file. The request will need one of the following security scopes: - sp:config:read - sp:config:manage

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.sp_config_export_results import SpConfigExportResults
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
    api_instance = sailpoint.beta.SPConfigApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The ID of the export job whose results will be downloaded.

    try:
        # Download export job result.
        api_response = api_instance.get_sp_config_export(id)
        print("The response of SPConfigApi->get_sp_config_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SPConfigApi->get_sp_config_export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the export job whose results will be downloaded. | 

### Return type

[**SpConfigExportResults**](SpConfigExportResults.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exported JSON objects. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sp_config_export_status**
> SpConfigExportJobStatus get_sp_config_export_status(id)

Get export job status

This gets the status of the export job identified by the `id` parameter. The request will need one of the following security scopes: - sp:config:read - sp:config:manage

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.sp_config_export_job_status import SpConfigExportJobStatus
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
    api_instance = sailpoint.beta.SPConfigApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The ID of the export job whose status will be returned.

    try:
        # Get export job status
        api_response = api_instance.get_sp_config_export_status(id)
        print("The response of SPConfigApi->get_sp_config_export_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SPConfigApi->get_sp_config_export_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the export job whose status will be returned. | 

### Return type

[**SpConfigExportJobStatus**](SpConfigExportJobStatus.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export job status successfully returned. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sp_config_import**
> SpConfigImportResults get_sp_config_import(id)

Download import job result

This gets import file resulting from the import job with the requested id and downloads it to a file. The downloaded file will contain the results of the import operation, including any error, warning or informational messages associated with the import. The request will need the following security scope: - sp:config:manage

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.sp_config_import_results import SpConfigImportResults
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
    api_instance = sailpoint.beta.SPConfigApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The ID of the import job whose results will be downloaded.

    try:
        # Download import job result
        api_response = api_instance.get_sp_config_import(id)
        print("The response of SPConfigApi->get_sp_config_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SPConfigApi->get_sp_config_import: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the import job whose results will be downloaded. | 

### Return type

[**SpConfigImportResults**](SpConfigImportResults.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import results JSON object, containing detailed results of the import operation. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sp_config_import_status**
> SpConfigImportJobStatus get_sp_config_import_status(id)

Get import job status

This gets the status of the import job identified by the `id` parameter. For more information about the object types that currently support import functionality, refer to [SaaS Configuration](https://developer.sailpoint.com/idn/docs/saas-configuration/#supported-objects). The request will need the following security scope: - sp:config:manage

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.sp_config_import_job_status import SpConfigImportJobStatus
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
    api_instance = sailpoint.beta.SPConfigApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The ID of the import job whose status will be returned.

    try:
        # Get import job status
        api_response = api_instance.get_sp_config_import_status(id)
        print("The response of SPConfigApi->get_sp_config_import_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SPConfigApi->get_sp_config_import_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the import job whose status will be returned. | 

### Return type

[**SpConfigImportJobStatus**](SpConfigImportJobStatus.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import job status successfully returned. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_sp_config**
> SpConfigJob import_sp_config(data, preview=preview, options=options)

Initiates configuration objects import job

This post will import objects from a JSON configuration file into a tenant. By default, every import will first export all existing objects supported by sp-config as a backup before the import is attempted. The backup is provided so that the state of the configuration prior to the import is available for inspection or restore if needed. The backup can be skipped by setting \"excludeBackup\" to true in the import options. If a backup is performed, the id of the backup will be provided in the ImportResult as the \"exportJobId\". This can be downloaded  using the /sp-config/export/{exportJobId}/download endpoint. You cannot currently import from the Non-Employee Lifecycle Management (NELM) source. You cannot use this endpoint to back up or store NELM data.  For more information about the object types that currently support import functionality, refer to [SaaS Configuration](https://developer.sailpoint.com/idn/docs/saas-configuration/#supported-objects). The request will need the following security scope: - sp:config:manage

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.import_options import ImportOptions
from sailpoint.beta.models.sp_config_job import SpConfigJob
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
    api_instance = sailpoint.beta.SPConfigApi(api_client)
    data = None # bytearray | JSON file containing the objects to be imported.
    preview = False # bool | This option is intended to give the user information about how an import operation would proceed, without having any effect on the target tenant. If this parameter is \"true\", no objects will be imported. Instead, the import process will pre-process the import file and attempt to resolve references within imported objects. The import result file will contain messages pertaining to how specific references were resolved, any errors associated with the preprocessing, and messages indicating which objects would be imported. (optional) (default to False)
    options = sailpoint.beta.ImportOptions() # ImportOptions |  (optional)

    try:
        # Initiates configuration objects import job
        api_response = api_instance.import_sp_config(data, preview=preview, options=options)
        print("The response of SPConfigApi->import_sp_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SPConfigApi->import_sp_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **bytearray**| JSON file containing the objects to be imported. | 
 **preview** | **bool**| This option is intended to give the user information about how an import operation would proceed, without having any effect on the target tenant. If this parameter is \&quot;true\&quot;, no objects will be imported. Instead, the import process will pre-process the import file and attempt to resolve references within imported objects. The import result file will contain messages pertaining to how specific references were resolved, any errors associated with the preprocessing, and messages indicating which objects would be imported. | [optional] [default to False]
 **options** | [**ImportOptions**](ImportOptions.md)|  | [optional] 

### Return type

[**SpConfigJob**](SpConfigJob.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Import job accepted and queued for processing. |  -  |
**400** | Client Error - Returned if the request body is invalid.  |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sp_config_objects**
> List[SpConfigObject] list_sp_config_objects()

Get config object details

This gets the list of object configurations which are known to the tenant export/import service. Object configurations that contain \"importUrl\" and \"exportUrl\" are available for export/import.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.sp_config_object import SpConfigObject
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
    api_instance = sailpoint.beta.SPConfigApi(api_client)

    try:
        # Get config object details
        api_response = api_instance.list_sp_config_objects()
        print("The response of SPConfigApi->list_sp_config_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SPConfigApi->list_sp_config_objects: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[SpConfigObject]**](SpConfigObject.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object configurations returned successfully. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


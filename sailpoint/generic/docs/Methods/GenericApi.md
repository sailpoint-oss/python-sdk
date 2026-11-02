---
id: generic
title: Generic
pagination_label: Generic
sidebar_label: Generic
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Generic', 'Generic'] 
slug: /tools/sdk/python/generic/methods/generic
tags: ['SDK', 'Software Development Kit', 'Generic', 'Generic']
---

# sailpoint.generic.GenericApi
  Call any SailPoint Identity Security versioned API by its path. The path includes the API version, for example &#x60;sources/v1&#x60; or &#x60;sources/v2/{sourceId}/provisioning-policies&#x60;. 
All URIs are relative to *https://sailpoint.api.identitynow.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generic-delete**](#generic-delete) | **DELETE** `/{path}` | Generic DELETE request
[**generic-get**](#generic-get) | **GET** `/{path}` | Generic GET request
[**generic-patch**](#generic-patch) | **PATCH** `/{path}` | Generic PATCH request
[**generic-post**](#generic-post) | **POST** `/{path}` | Generic POST request
[**generic-put**](#generic-put) | **PUT** `/{path}` | Generic PUT request


## generic-delete
:::warning experimental 
This API is currently in an experimental state. The API is subject to change based on feedback and further testing. You must include the X-SailPoint-Experimental header and set it to `true` to use this endpoint.
:::
:::tip setting x-sailpoint-experimental header
 on the configuration object you can set the `x-sailpoint-experimental` header to `true' to enable all experimantl endpoints within the SDK.
 Example:
 ```python
   configuration = Configuration()
   configuration.experimental = True
 ```
:::
Generic DELETE request
Sends a DELETE request to any versioned API path.

[API Spec](https://developer.sailpoint.com/docs/api/generic-delete)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | path | **str** | True  | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`.
   | x_sail_point_experimental | **str** |   (optional) | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs.

### Return type
**object**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Successful response. The body is the JSON returned by the API. | object |  -  |
204 | No content. |  |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.generic.api.generic_api import GenericApi
from sailpoint.generic.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    path = 'accounts/v1' # str | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`. # str | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`.
    x_sail_point_experimental = 'true' # str | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs. (optional) # str | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs. (optional)

    try:
        # Generic DELETE request
        
        results = GenericApi(api_client).generic_delete(path=path)
        # Below is a request that includes all optional parameters
        # results = GenericApi(api_client).generic_delete(path, x_sail_point_experimental)
        print("The response of GenericApi->generic_delete:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling GenericApi->generic_delete: %s\n" % e)
```



[[Back to top]](#) 

## generic-get
:::warning experimental 
This API is currently in an experimental state. The API is subject to change based on feedback and further testing. You must include the X-SailPoint-Experimental header and set it to `true` to use this endpoint.
:::
:::tip setting x-sailpoint-experimental header
 on the configuration object you can set the `x-sailpoint-experimental` header to `true' to enable all experimantl endpoints within the SDK.
 Example:
 ```python
   configuration = Configuration()
   configuration.experimental = True
 ```
:::
Generic GET request
Sends a GET request to any versioned API path, for example `sources/v1/{id}/schemas` or `sources/v2/{sourceId}/provisioning-policies`.

[API Spec](https://developer.sailpoint.com/docs/api/generic-get)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | path | **str** | True  | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`.
  Query | limit | **int** |   (optional) | Max number of results to return. See [Standard Collection Parameters](https://developer.sailpoint.com/docs/standard-collection-parameters) for more information.
  Query | offset | **int** |   (optional) | Offset into the full result set. Usually specified with *limit* to paginate through the results.
  Query | count | **bool** |   (optional) | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.
  Query | filters | **str** |   (optional) | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/docs/standard-collection-parameters#filtering-results).
  Query | sorters | **str** |   (optional) | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/docs/standard-collection-parameters#sorting-results).
   | x_sail_point_experimental | **str** |   (optional) | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs.

### Return type
**object**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Successful response. The body is the JSON returned by the API. | object |  -  |
204 | No content. |  |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.generic.api.generic_api import GenericApi
from sailpoint.generic.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    path = 'accounts/v1' # str | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`. # str | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`.
    limit = 250 # int | Max number of results to return. See [Standard Collection Parameters](https://developer.sailpoint.com/docs/standard-collection-parameters) for more information. (optional) # int | Max number of results to return. See [Standard Collection Parameters](https://developer.sailpoint.com/docs/standard-collection-parameters) for more information. (optional)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. (optional) # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. (optional)
    count = true # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored. (optional) # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored. (optional)
    filters = 'name eq \"Example\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/docs/standard-collection-parameters#filtering-results). (optional) # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/docs/standard-collection-parameters#filtering-results). (optional)
    sorters = 'name,-created' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/docs/standard-collection-parameters#sorting-results). (optional) # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/docs/standard-collection-parameters#sorting-results). (optional)
    x_sail_point_experimental = 'true' # str | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs. (optional) # str | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs. (optional)

    try:
        # Generic GET request
        
        results = GenericApi(api_client).generic_get(path=path)
        # Below is a request that includes all optional parameters
        # results = GenericApi(api_client).generic_get(path, limit, offset, count, filters, sorters, x_sail_point_experimental)
        print("The response of GenericApi->generic_get:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling GenericApi->generic_get: %s\n" % e)
```



[[Back to top]](#) 

## generic-patch
:::warning experimental 
This API is currently in an experimental state. The API is subject to change based on feedback and further testing. You must include the X-SailPoint-Experimental header and set it to `true` to use this endpoint.
:::
:::tip setting x-sailpoint-experimental header
 on the configuration object you can set the `x-sailpoint-experimental` header to `true' to enable all experimantl endpoints within the SDK.
 Example:
 ```python
   configuration = Configuration()
   configuration.experimental = True
 ```
:::
Generic PATCH request
Sends a PATCH request to any versioned API path. The body is a JSON Patch document (RFC 6902): a list of operations such as `[{"op": "replace", "path": "/description", "value": "New description"}]`.

[API Spec](https://developer.sailpoint.com/docs/api/generic-patch)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | path | **str** | True  | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`.
   | x_sail_point_experimental | **str** |   (optional) | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs.
 Body  | request_body | **object** |   (optional) | 

### Return type
**object**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Successful response. The body is the JSON returned by the API. | object |  -  |
204 | No content. |  |  -  |

### HTTP request headers
 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### Example

```python
from sailpoint.generic.api.generic_api import GenericApi
from sailpoint.generic.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    path = 'accounts/v1' # str | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`. # str | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`.
    x_sail_point_experimental = 'true' # str | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs. (optional) # str | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs. (optional)
    request_body = None # object |  (optional) # object |  (optional)

    try:
        # Generic PATCH request
        
        results = GenericApi(api_client).generic_patch(path=path)
        # Below is a request that includes all optional parameters
        # results = GenericApi(api_client).generic_patch(path, x_sail_point_experimental, new_request_body)
        print("The response of GenericApi->generic_patch:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling GenericApi->generic_patch: %s\n" % e)
```



[[Back to top]](#) 

## generic-post
:::warning experimental 
This API is currently in an experimental state. The API is subject to change based on feedback and further testing. You must include the X-SailPoint-Experimental header and set it to `true` to use this endpoint.
:::
:::tip setting x-sailpoint-experimental header
 on the configuration object you can set the `x-sailpoint-experimental` header to `true' to enable all experimantl endpoints within the SDK.
 Example:
 ```python
   configuration = Configuration()
   configuration.experimental = True
 ```
:::
Generic POST request
Sends a POST request with a JSON body to any versioned API path.

[API Spec](https://developer.sailpoint.com/docs/api/generic-post)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | path | **str** | True  | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`.
   | x_sail_point_experimental | **str** |   (optional) | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs.
 Body  | request_body | **object** |   (optional) | 

### Return type
**object**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Successful response. The body is the JSON returned by the API. | object |  -  |
204 | No content. |  |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.generic.api.generic_api import GenericApi
from sailpoint.generic.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    path = 'accounts/v1' # str | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`. # str | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`.
    x_sail_point_experimental = 'true' # str | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs. (optional) # str | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs. (optional)
    request_body = None # object |  (optional) # object |  (optional)

    try:
        # Generic POST request
        
        results = GenericApi(api_client).generic_post(path=path)
        # Below is a request that includes all optional parameters
        # results = GenericApi(api_client).generic_post(path, x_sail_point_experimental, new_request_body)
        print("The response of GenericApi->generic_post:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling GenericApi->generic_post: %s\n" % e)
```



[[Back to top]](#) 

## generic-put
:::warning experimental 
This API is currently in an experimental state. The API is subject to change based on feedback and further testing. You must include the X-SailPoint-Experimental header and set it to `true` to use this endpoint.
:::
:::tip setting x-sailpoint-experimental header
 on the configuration object you can set the `x-sailpoint-experimental` header to `true' to enable all experimantl endpoints within the SDK.
 Example:
 ```python
   configuration = Configuration()
   configuration.experimental = True
 ```
:::
Generic PUT request
Sends a PUT request with a JSON body to any versioned API path.

[API Spec](https://developer.sailpoint.com/docs/api/generic-put)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | path | **str** | True  | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`.
   | x_sail_point_experimental | **str** |   (optional) | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs.
 Body  | request_body | **object** |   (optional) | 

### Return type
**object**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Successful response. The body is the JSON returned by the API. | object |  -  |
204 | No content. |  |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.generic.api.generic_api import GenericApi
from sailpoint.generic.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    path = 'accounts/v1' # str | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`. # str | API path relative to the tenant base URL, including the API version, for example `accounts/v1`, `sources/v1/2c9180835d2e5168015d32f890ca1581` or `sources/v2/2c9180835d2e5168015d32f890ca1581/provisioning-policies`. Use whichever version the endpoint has. A leading slash is optional. Slashes separate path segments, and the SDK URL-encodes each segment, so pass the segments unencoded. Anything after a `?` is sent as query parameters, for example `accounts/v1?detailLevel=SLIM`.
    x_sail_point_experimental = 'true' # str | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs. (optional) # str | Set this header to `true` to call an experimental API. The SDK configuration must also enable experimental APIs. (optional)
    request_body = None # object |  (optional) # object |  (optional)

    try:
        # Generic PUT request
        
        results = GenericApi(api_client).generic_put(path=path)
        # Below is a request that includes all optional parameters
        # results = GenericApi(api_client).generic_put(path, x_sail_point_experimental, new_request_body)
        print("The response of GenericApi->generic_put:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling GenericApi->generic_put: %s\n" % e)
```



[[Back to top]](#) 




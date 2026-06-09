---
id: icons
title: Icons
pagination_label: Icons
sidebar_label: Icons
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Icons', 'Icons'] 
slug: /tools/sdk/python/v1/methods/icons
tags: ['SDK', 'Software Development Kit', 'Icons', 'Icons']
---

# sailpoint.icons_v1.IconsV1Api
  Use this API to implement functionality related to object icons (application icons for example). 
With this functionality in place, administrators can set or remove an icon for specific object type for use throughout Identity Security Cloud.
 
All URIs are relative to *https://sailpoint.api.identitynow.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete-icon-v1**](#delete-icon-v1) | **DELETE** `/icons/v1/{objectType}/{objectId}` | Delete an icon
[**set-icon-v1**](#set-icon-v1) | **PUT** `/icons/v1/{objectType}/{objectId}` | Update an icon


## delete-icon-v1
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
Delete an icon
This API endpoint delete an icon by object type and object id. A token with ORG_ADMIN authority is required to call this API.

[API Spec](https://developer.sailpoint.com/docs/api/v1/delete-icon-v1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | object_type | **str** | True  | Object type. Available options ['application']
Path   | object_id | **str** | True  | Object id.
   | x_sail_point_experimental | **str** |   (optional) (default to 'true') | Use this header to enable this experimental API.

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No content - indicates the request was successful but there is no content to be returned in the response. |  |  -  |
400 | Client Error - Returned if the request body is invalid. | Errorresponsedto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | SetIconV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | Errorresponsedto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | Errorresponsedto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | SetIconV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | Errorresponsedto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.icons_v1.api.icons_v1_api import IconsV1Api
from sailpoint.icons_v1.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    object_type = 'application' # str | Object type. Available options ['application'] # str | Object type. Available options ['application']
    object_id = 'a291e870-48c3-4953-b656-fb5ce2a93169' # str | Object id. # str | Object id.
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (optional) (default to 'true') # str | Use this header to enable this experimental API. (optional) (default to 'true')

    try:
        # Delete an icon
        
        IconsV1Api(api_client).delete_icon_v1(object_type=object_type, object_id=object_id)
        # Below is a request that includes all optional parameters
        # IconsV1Api(api_client).delete_icon_v1(object_type, object_id, x_sail_point_experimental)
    except Exception as e:
        print("Exception when calling IconsV1Api->delete_icon_v1: %s\n" % e)
```



[[Back to top]](#) 

## set-icon-v1
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
Update an icon
This API endpoint updates an icon by object type and object id. A token with ORG_ADMIN authority is required to call this API.

[API Spec](https://developer.sailpoint.com/docs/api/v1/set-icon-v1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | object_type | **str** | True  | Object type. Available options ['application']
Path   | object_id | **str** | True  | Object id.
   | image | **bytearray** | True  | file with icon. Allowed mime-types ['image/png', 'image/jpeg']
   | x_sail_point_experimental | **str** |   (optional) (default to 'true') | Use this header to enable this experimental API.

### Return type
[**SetIconV1200Response**](../models/set-icon-v1200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Icon updated | SetIconV1200Response |  -  |
400 | Client Error - Returned if the request body is invalid. | Errorresponsedto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | SetIconV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | Errorresponsedto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | Errorresponsedto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | SetIconV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | Errorresponsedto |  -  |

### HTTP request headers
 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### Example

```python
from sailpoint.icons_v1.api.icons_v1_api import IconsV1Api
from sailpoint.icons_v1.api_client import ApiClient
from sailpoint.icons_v1.models.set_icon_v1200_response import SetIconV1200Response
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    object_type = 'application' # str | Object type. Available options ['application'] # str | Object type. Available options ['application']
    object_id = 'a291e870-48c3-4953-b656-fb5ce2a93169' # str | Object id. # str | Object id.
    image = None # bytearray | file with icon. Allowed mime-types ['image/png', 'image/jpeg'] # bytearray | file with icon. Allowed mime-types ['image/png', 'image/jpeg']
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (optional) (default to 'true') # str | Use this header to enable this experimental API. (optional) (default to 'true')

    try:
        # Update an icon
        
        results = IconsV1Api(api_client).set_icon_v1(object_type=object_type, object_id=object_id, image=image)
        # Below is a request that includes all optional parameters
        # results = IconsV1Api(api_client).set_icon_v1(object_type, object_id, image, x_sail_point_experimental)
        print("The response of IconsV1Api->set_icon_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IconsV1Api->set_icon_v1: %s\n" % e)
```



[[Back to top]](#) 




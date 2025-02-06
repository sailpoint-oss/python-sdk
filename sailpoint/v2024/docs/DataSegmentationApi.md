# sailpoint.v2024.DataSegmentationApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_segment**](DataSegmentationApi.md#create_data_segment) | **POST** /data-segments | Create Segment
[**delete_data_segment**](DataSegmentationApi.md#delete_data_segment) | **DELETE** /data-segments/{segmentId} | Delete Segment by ID
[**get_data_segment**](DataSegmentationApi.md#get_data_segment) | **GET** /data-segments/{segmentId} | Get Segment by ID
[**get_data_segment_identity_membership**](DataSegmentationApi.md#get_data_segment_identity_membership) | **GET** /data-segments/membership/{identityId} | Get SegmentMembership by Identity ID
[**get_data_segmentation_enabled_for_user**](DataSegmentationApi.md#get_data_segmentation_enabled_for_user) | **GET** /data-segments/user-enabled/{identityId} | Is Segmentation enabled by Identity
[**list_data_segments**](DataSegmentationApi.md#list_data_segments) | **GET** /data-segments | Get Segments
[**patch_data_segment**](DataSegmentationApi.md#patch_data_segment) | **PATCH** /data-segments/{segmentId} | Update Segment
[**publish_data_segment**](DataSegmentationApi.md#publish_data_segment) | **POST** /data-segments/{segmentId} | Publish segment by ID


# **create_data_segment**
> DataSegment create_data_segment(data_segment)

Create Segment

This API creates a segment.  >**Note:** Segment definitions may take time to propagate to all identities.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.data_segment import DataSegment
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.DataSegmentationApi(api_client)
    data_segment = sailpoint.v2024.DataSegment() # DataSegment | 

    try:
        # Create Segment
        api_response = api_instance.create_data_segment(data_segment)
        print("The response of DataSegmentationApi->create_data_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSegmentationApi->create_data_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_segment** | [**DataSegment**](DataSegment.md)|  | 

### Return type

[**DataSegment**](DataSegment.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Segment created |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_segment**
> delete_data_segment(id, x_sail_point_experimental, published=published)

Delete Segment by ID

This API deletes the segment specified by the given ID.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.DataSegmentationApi(api_client)
    id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The segment ID to delete.
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    published = False # bool | This determines which version of the segment to delete (optional) (default to False)

    try:
        # Delete Segment by ID
        api_instance.delete_data_segment(id, x_sail_point_experimental, published=published)
    except Exception as e:
        print("Exception when calling DataSegmentationApi->delete_data_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The segment ID to delete. | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **published** | **bool**| This determines which version of the segment to delete | [optional] [default to False]

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
**204** | No content. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_segment**
> DataSegment get_data_segment(id, x_sail_point_experimental)

Get Segment by ID

This API returns the segment specified by the given ID.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.data_segment import DataSegment
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.DataSegmentationApi(api_client)
    id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The segment ID to retrieve.
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')

    try:
        # Get Segment by ID
        api_response = api_instance.get_data_segment(id, x_sail_point_experimental)
        print("The response of DataSegmentationApi->get_data_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSegmentationApi->get_data_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The segment ID to retrieve. | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]

### Return type

[**DataSegment**](DataSegment.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segment |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_segment_identity_membership**
> object get_data_segment_identity_membership(identity_id, x_sail_point_experimental)

Get SegmentMembership by Identity ID

This API returns the segment membership specified by the given identity ID.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.DataSegmentationApi(api_client)
    identity_id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The identity ID to retrieve the segments they are in.
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')

    try:
        # Get SegmentMembership by Identity ID
        api_response = api_instance.get_data_segment_identity_membership(identity_id, x_sail_point_experimental)
        print("The response of DataSegmentationApi->get_data_segment_identity_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSegmentationApi->get_data_segment_identity_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_id** | **str**| The identity ID to retrieve the segments they are in. | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]

### Return type

**object**

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segment Memberships for specified identity |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_segmentation_enabled_for_user**
> bool get_data_segmentation_enabled_for_user(identity_id, x_sail_point_experimental)

Is Segmentation enabled by Identity

This API returns whether or not segmentation is enabled for the identity.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.DataSegmentationApi(api_client)
    identity_id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The identity ID to retrieve if segmentation is enabled for the identity.
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')

    try:
        # Is Segmentation enabled by Identity
        api_response = api_instance.get_data_segmentation_enabled_for_user(identity_id, x_sail_point_experimental)
        print("The response of DataSegmentationApi->get_data_segmentation_enabled_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSegmentationApi->get_data_segmentation_enabled_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_id** | **str**| The identity ID to retrieve if segmentation is enabled for the identity. | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]

### Return type

**bool**

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns if segmentation is enabled for a specified User |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_segments**
> List[DataSegment] list_data_segments(x_sail_point_experimental, enabled=enabled, unique=unique, published=published, limit=limit, offset=offset, count=count, filters=filters)

Get Segments

This API returns the segment specified by the given ID.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.data_segment import DataSegment
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.DataSegmentationApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    enabled = True # bool | This boolean indicates whether the segment is currently active. Inactive segments have no effect. (optional) (default to True)
    unique = False # bool | This returns only one record if set to true and that would be the published record if exists. (optional) (default to False)
    published = True # bool | This boolean indicates whether the segment is being applied to the accounts. If unpublished its being actively modified until published (optional) (default to True)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'name eq \"\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in, sw*  **name**: *eq, in, sw* (optional)

    try:
        # Get Segments
        api_response = api_instance.list_data_segments(x_sail_point_experimental, enabled=enabled, unique=unique, published=published, limit=limit, offset=offset, count=count, filters=filters)
        print("The response of DataSegmentationApi->list_data_segments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSegmentationApi->list_data_segments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **enabled** | **bool**| This boolean indicates whether the segment is currently active. Inactive segments have no effect. | [optional] [default to True]
 **unique** | **bool**| This returns only one record if set to true and that would be the published record if exists. | [optional] [default to False]
 **published** | **bool**| This boolean indicates whether the segment is being applied to the accounts. If unpublished its being actively modified until published | [optional] [default to True]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in, sw*  **name**: *eq, in, sw* | [optional] 

### Return type

[**List[DataSegment]**](DataSegment.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all segments |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_data_segment**
> DataSegment patch_data_segment(id, x_sail_point_experimental, request_body)

Update Segment

Use this API to update segment fields by using the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.data_segment import DataSegment
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.DataSegmentationApi(api_client)
    id = 'ef38f943-47e9-4562-b5bb-8424a56397d8' # str | The segment ID to modify.
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    request_body = [{op=replace, path=/memberFilter, value={expression={operator=AND, children=[{operator=EQUALS, attribute=location, value={type=STRING, value=Philadelphia}}, {operator=EQUALS, attribute=department, value={type=STRING, value=HR}}]}}}] # List[object] | A list of segment update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields are patchable: * name * description * membership * memberFilter * memberSelection * scopes * enabled 

    try:
        # Update Segment
        api_response = api_instance.patch_data_segment(id, x_sail_point_experimental, request_body)
        print("The response of DataSegmentationApi->patch_data_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSegmentationApi->patch_data_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The segment ID to modify. | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **request_body** | [**List[object]**](object.md)| A list of segment update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields are patchable: * name * description * membership * memberFilter * memberSelection * scopes * enabled  | 

### Return type

[**DataSegment**](DataSegment.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Indicates the PATCH operation succeeded, and returns the segment&#39;s new representation. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_data_segment**
> publish_data_segment(x_sail_point_experimental, request_body, publish_all=publish_all)

Publish segment by ID

This will publish the segment so that it starts applying the segmentation to the desired users if enabled

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.DataSegmentationApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    request_body = ['request_body_example'] # List[str] | A list of segment ids that you wish to publish
    publish_all = True # bool | This flag decides whether you want to publish all unpublished or a list of specific segment ids (optional) (default to True)

    try:
        # Publish segment by ID
        api_instance.publish_data_segment(x_sail_point_experimental, request_body, publish_all=publish_all)
    except Exception as e:
        print("Exception when calling DataSegmentationApi->publish_data_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **request_body** | [**List[str]**](str.md)| A list of segment ids that you wish to publish | 
 **publish_all** | **bool**| This flag decides whether you want to publish all unpublished or a list of specific segment ids | [optional] [default to True]

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segments published |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


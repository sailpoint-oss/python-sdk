# sailpoint.cc.SystemApi

All URIs are relative to *https://sailpoint.api.identitynow.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refresh_identities**](SystemApi.md#refresh_identities) | **POST** /cc/api/system/refreshIdentities | Refresh Identities


# **refresh_identities**
> Dict[str, object] refresh_identities(content_type=content_type, refresh_identities_request=refresh_identities_request)

Refresh Identities

This kicks off an identity refresh for a specified set of identity attributes.  This can be a long running process.  IdentityNow has pre-scheduled versions of this task at set intervals and events already, so only run this when directed by SailPoint.  _Note: If the identities specified by the filter do not exist, a full identity refresh will be run.  Use with caution._  Refresh Arguments:  | Key                   | Description                                        | |-----------------------|----------------------------------------------------| | correlateEntitlements | Analyzes entitlements, access profiles, and roles. | | promoteAttributes     | Calculates identity attributes.                    | | refreshManagerStatus  | Calculates manager correlation and manager status. | | synchronizeAttributes | Performs attribute sync provisioning.              | | pruneIdentities       | Removes any identities which don't have accounts.  | | provision             | Provisions any assigned roles or access profiles.  |

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.cc
from sailpoint.cc.models.refresh_identities_request import RefreshIdentitiesRequest
from sailpoint.cc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.cc.Configuration(
    host = "https://sailpoint.api.identitynow.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.cc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.cc.SystemApi(api_client)
    content_type = 'application/json' # str |  (optional)
    refresh_identities_request = sailpoint.cc.RefreshIdentitiesRequest() # RefreshIdentitiesRequest |  (optional)

    try:
        # Refresh Identities
        api_response = api_instance.refresh_identities(content_type=content_type, refresh_identities_request=refresh_identities_request)
        print("The response of SystemApi->refresh_identities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->refresh_identities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] 
 **refresh_identities_request** | [**RefreshIdentitiesRequest**](RefreshIdentitiesRequest.md)|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


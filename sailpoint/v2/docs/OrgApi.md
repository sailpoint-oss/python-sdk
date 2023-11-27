# sailpoint.v2.OrgApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org_settings**](OrgApi.md#get_org_settings) | **GET** /org | Retrieves your org settings.
[**update_org_settings**](OrgApi.md#update_org_settings) | **PATCH** /org | Updates one or more org attributes.


# **get_org_settings**
> GetOrgSettings200Response get_org_settings()

Retrieves your org settings.

Retrieves information and operational settings for your org (as determined by the URL domain).

### Example

```python
import time
import os
import sailpoint.v2
from sailpoint.v2.models.get_org_settings200_response import GetOrgSettings200Response
from sailpoint.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2"
)


# Enter a context with an instance of the API client
with sailpoint.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2.OrgApi(api_client)

    try:
        # Retrieves your org settings.
        api_response = api_instance.get_org_settings()
        print("The response of OrgApi->get_org_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgApi->get_org_settings: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetOrgSettings200Response**](GetOrgSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  * ETag - Entity tag. <br>  * Last-Modified - Last modified date. <br>  * Link - Links to alternate or related resources. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_settings**
> GetOrgSettings200Response update_org_settings(update_org_settings_request)

Updates one or more org attributes.

Updates one or more attributes for your org.

### Example

```python
import time
import os
import sailpoint.v2
from sailpoint.v2.models.get_org_settings200_response import GetOrgSettings200Response
from sailpoint.v2.models.update_org_settings_request import UpdateOrgSettingsRequest
from sailpoint.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2"
)


# Enter a context with an instance of the API client
with sailpoint.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2.OrgApi(api_client)
    update_org_settings_request = sailpoint.v2.UpdateOrgSettingsRequest() # UpdateOrgSettingsRequest | Org settings to update.

    try:
        # Updates one or more org attributes.
        api_response = api_instance.update_org_settings(update_org_settings_request)
        print("The response of OrgApi->update_org_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgApi->update_org_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_org_settings_request** | [**UpdateOrgSettingsRequest**](UpdateOrgSettingsRequest.md)| Org settings to update. | 

### Return type

[**GetOrgSettings200Response**](GetOrgSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  * ETag - Entity tag. <br>  * Last-Modified - Last modified date. <br>  * Link - Links to alternate or related resources. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


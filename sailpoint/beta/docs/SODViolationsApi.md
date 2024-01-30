# sailpoint.beta.SODViolationsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**start_predict_sod_violations**](SODViolationsApi.md#start_predict_sod_violations) | **POST** /sod-violations/predict | Predict SOD violations for identity.


# **start_predict_sod_violations**
> ViolationPrediction start_predict_sod_violations(identity_with_new_access)

Predict SOD violations for identity.

This API is used to check if granting some additional accesses would cause the subject to be in violation of any SOD policies. Returns the violations that would be caused.  A token with ORG_ADMIN or API authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.identity_with_new_access import IdentityWithNewAccess
from sailpoint.beta.models.violation_prediction import ViolationPrediction
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
    api_instance = sailpoint.beta.SODViolationsApi(api_client)
    identity_with_new_access = {identityId=2c91808568c529c60168cca6f90c1313, accessRefs=[{type=ENTITLEMENT, id=2c918087682f9a86016839c050861ab1, name=CN=Information Access,OU=test,OU=test-service,DC=TestAD,DC=local}, {type=ENTITLEMENT, id=2c918087682f9a86016839c0509c1ab2, name=CN=Information Technology,OU=test,OU=test-service,DC=TestAD,DC=local}]} # IdentityWithNewAccess | 

    try:
        # Predict SOD violations for identity.
        api_response = api_instance.start_predict_sod_violations(identity_with_new_access)
        print("The response of SODViolationsApi->start_predict_sod_violations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SODViolationsApi->start_predict_sod_violations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_with_new_access** | [**IdentityWithNewAccess**](IdentityWithNewAccess.md)|  | 

### Return type

[**ViolationPrediction**](ViolationPrediction.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Violation Contexts |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


---
id: v2026-machine-account-deletion-approval-config
title: Machine_Account_Deletion_Approval_Config
pagination_label: Machine_Account_Deletion_Approval_Config
sidebar_label: Machine_Account_Deletion_Approval_Config
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Machine_Account_Deletion_Approval_Config', 'V2026Machine_Account_Deletion_Approval_Config'] 
slug: /tools/sdk/python/v2026/methods/machine-account-deletion-approval-config
tags: ['SDK', 'Software Development Kit', 'Machine_Account_Deletion_Approval_Config', 'V2026Machine_Account_Deletion_Approval_Config']
---

# sailpoint.v2026.MachineAccountDeletionApprovalConfigApi
   
All URIs are relative to *https://sailpoint.api.identitynow.com/v2026*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-machine-account-deletion-approval-config-by-source**](#get-machine-account-deletion-approval-config-by-source) | **GET** `/sources/{sourceId}/approval-config/machine-account-delete` | Machine Account Deletion Approval Config
[**update-machine-account-deletion-approval-config**](#update-machine-account-deletion-approval-config) | **PATCH** `/sources/{sourceId}/approval-config/machine-account-delete` | Machine Account Deletion Approval Config


## get-machine-account-deletion-approval-config-by-source
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
Machine Account Deletion Approval Config
Retrieves the machine account deletion approval configuration for a specific source. This endpoint returns details about the approval requirements, approvers, and comment settings that govern the deletion of machine accounts associated with the given source ID.

[API Spec](https://developer.sailpoint.com/docs/api/v2026/get-machine-account-deletion-approval-config-by-source)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
   | x_sail_point_experimental | **str** | True  (default to 'true') | Use this header to enable this experimental API.
Path   | source_id | **str** | True  | source id.

### Return type
[**AccountDeleteConfigDto**](../models/account-delete-config-dto)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Responds with a AccountDeleteConfigDto for machine account deletion approval config by sourceId. | AccountDeleteConfigDto |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetAccessRequestConfig401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetAccessRequestConfig429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.machine_account_deletion_approval_config_api import MachineAccountDeletionApprovalConfigApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.account_delete_config_dto import AccountDeleteConfigDto
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true') # str | Use this header to enable this experimental API. (default to 'true')
    source_id = 'gt38f94347e94562b5bb8424a56498d8' # str | source id. # str | source id.

    try:
        # Machine Account Deletion Approval Config
        
        results = MachineAccountDeletionApprovalConfigApi(api_client).get_machine_account_deletion_approval_config_by_source(x_sail_point_experimental=x_sail_point_experimental, source_id=source_id)
        # Below is a request that includes all optional parameters
        # results = MachineAccountDeletionApprovalConfigApi(api_client).get_machine_account_deletion_approval_config_by_source(x_sail_point_experimental, source_id)
        print("The response of MachineAccountDeletionApprovalConfigApi->get_machine_account_deletion_approval_config_by_source:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling MachineAccountDeletionApprovalConfigApi->get_machine_account_deletion_approval_config_by_source: %s\n" % e)
```



[[Back to top]](#) 

## update-machine-account-deletion-approval-config
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
Machine Account Deletion Approval Config
Use this endpoint to update the machine account deletion approval configuration for a specific source.
The update is performed using a JSON Patch payload, which allows partial modifications to the approval config.
This operation is typically used to change approval requirements, approvers, or comments settings for machine account deletion.
The endpoint expects the source ID as a path parameter and a valid JSON Patch array in the request body.


[API Spec](https://developer.sailpoint.com/docs/api/v2026/update-machine-account-deletion-approval-config)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
   | x_sail_point_experimental | **str** | True  (default to 'true') | Use this header to enable this experimental API.
Path   | source_id | **str** | True  | machine account source ID.
 Body  | json_patch_operation | [**[]JsonPatchOperation**](../models/json-patch-operation) | True  | The JSONPatch payload used to update the object.

### Return type
[**AccountDeleteConfigDto**](../models/account-delete-config-dto)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | This response indicates the PATCH operation succeeded and the API returns the updated AccountDeleteConfigDto object. | AccountDeleteConfigDto |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetAccessRequestConfig401Response |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetAccessRequestConfig429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.machine_account_deletion_approval_config_api import MachineAccountDeletionApprovalConfigApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.account_delete_config_dto import AccountDeleteConfigDto
from sailpoint.v2026.models.json_patch_operation import JsonPatchOperation
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true') # str | Use this header to enable this experimental API. (default to 'true')
    source_id = '00eebcf881994e419d72e757fd30dc0e' # str | machine account source ID. # str | machine account source ID.
    json_patch_operation = '''[sailpoint.v2026.JsonPatchOperation()]''' # List[JsonPatchOperation] | The JSONPatch payload used to update the object.

    try:
        # Machine Account Deletion Approval Config
        new_json_patch_operation = JsonPatchOperation.from_json(json_patch_operation)
        results = MachineAccountDeletionApprovalConfigApi(api_client).update_machine_account_deletion_approval_config(x_sail_point_experimental=x_sail_point_experimental, source_id=source_id, json_patch_operation=new_json_patch_operation)
        # Below is a request that includes all optional parameters
        # results = MachineAccountDeletionApprovalConfigApi(api_client).update_machine_account_deletion_approval_config(x_sail_point_experimental, source_id, new_json_patch_operation)
        print("The response of MachineAccountDeletionApprovalConfigApi->update_machine_account_deletion_approval_config:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling MachineAccountDeletionApprovalConfigApi->update_machine_account_deletion_approval_config: %s\n" % e)
```



[[Back to top]](#) 




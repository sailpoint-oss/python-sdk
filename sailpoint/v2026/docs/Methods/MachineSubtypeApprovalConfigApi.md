---
id: v2026-machine-subtype-approval-config
title: Machine_Subtype_Approval_Config
pagination_label: Machine_Subtype_Approval_Config
sidebar_label: Machine_Subtype_Approval_Config
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Machine_Subtype_Approval_Config', 'V2026Machine_Subtype_Approval_Config'] 
slug: /tools/sdk/python/v2026/methods/machine-subtype-approval-config
tags: ['SDK', 'Software Development Kit', 'Machine_Subtype_Approval_Config', 'V2026Machine_Subtype_Approval_Config']
---

# sailpoint.v2026.MachineSubtypeApprovalConfigApi
   
All URIs are relative to *https://sailpoint.api.identitynow.com/v2026*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-machine-account-deletion-sub-type-approval-config**](#get-machine-account-deletion-sub-type-approval-config) | **GET** `/source-subtypes/{subtypeId}/machine-config` | Machine Subtype Approval Config
[**update-machine-account-deletion-by-sub-type-approval-config**](#update-machine-account-deletion-by-sub-type-approval-config) | **PATCH** `/source-subtypes/{subtypeId}/machine-config` | Machine Subtype Approval Config


## get-machine-account-deletion-sub-type-approval-config
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
Machine Subtype Approval Config
This endpoint retrieves the approval configuration for machine account deletion at the machine subtype level. By providing a specific subtypeId in the path, clients can fetch the approval rules and settings (such as required approvers and comments policy) that govern account deletion for that particular machine subtype. The response includes a MachineAccountSubtypeConfigDto object detailing these configurations, enabling clients to understand or display the approval workflow required for deleting machine accounts of the given subtype. Use this endpoint to get machine subtype level approval config for account deletion.

[API Spec](https://developer.sailpoint.com/docs/api/v2026/get-machine-account-deletion-sub-type-approval-config)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
   | x_sail_point_experimental | **str** | True  (default to 'true') | Use this header to enable this experimental API.
Path   | subtype_id | **str** | True  | machine subtype id.

### Return type
[**MachineAccountSubTypeConfigDto**](../models/machine-account-sub-type-config-dto)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Responds with a MachineAccountSubtypeConfigDto for machine account deletion approval config by subtypeId. | MachineAccountSubTypeConfigDto |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTaskStatus401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTaskStatus429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.machine_subtype_approval_config_api import MachineSubtypeApprovalConfigApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.machine_account_sub_type_config_dto import MachineAccountSubTypeConfigDto
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true') # str | Use this header to enable this experimental API. (default to 'true')
    subtype_id = 'ef38f94347e94562b5bb8424a56498d8' # str | machine subtype id. # str | machine subtype id.

    try:
        # Machine Subtype Approval Config
        
        results = MachineSubtypeApprovalConfigApi(api_client).get_machine_account_deletion_sub_type_approval_config(x_sail_point_experimental=x_sail_point_experimental, subtype_id=subtype_id)
        # Below is a request that includes all optional parameters
        # results = MachineSubtypeApprovalConfigApi(api_client).get_machine_account_deletion_sub_type_approval_config(x_sail_point_experimental, subtype_id)
        print("The response of MachineSubtypeApprovalConfigApi->get_machine_account_deletion_sub_type_approval_config:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling MachineSubtypeApprovalConfigApi->get_machine_account_deletion_sub_type_approval_config: %s\n" % e)
```



[[Back to top]](#) 

## update-machine-account-deletion-by-sub-type-approval-config
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
Machine Subtype Approval Config
Updates the approval configuration for machine account deletion at the specified machine subtype level. This endpoint allows clients to modify approval rules and settings (such as required approvers and comments policy) for account deletion workflows associated with a given subtypeId. Use this to customize or enforce approval requirements for deleting machine accounts of a particular subtype.

[API Spec](https://developer.sailpoint.com/docs/api/v2026/update-machine-account-deletion-by-sub-type-approval-config)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
   | x_sail_point_experimental | **str** | True  (default to 'true') | Use this header to enable this experimental API.
Path   | subtype_id | **str** | True  | machine account subtype ID.
 Body  | json_patch_operation | [**[]JsonPatchOperation**](../models/json-patch-operation) | True  | The JSONPatch payload used to update the object.

### Return type
[**MachineAccountSubTypeConfigDto**](../models/machine-account-sub-type-config-dto)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | This response indicates the PATCH operation succeeded and the API returns the updated MachineAccountSubtypeConfigDto object. | MachineAccountSubTypeConfigDto |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTaskStatus401Response |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTaskStatus429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.machine_subtype_approval_config_api import MachineSubtypeApprovalConfigApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.json_patch_operation import JsonPatchOperation
from sailpoint.v2026.models.machine_account_sub_type_config_dto import MachineAccountSubTypeConfigDto
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true') # str | Use this header to enable this experimental API. (default to 'true')
    subtype_id = '00eebcf881994e419d72e757fd30dc0e' # str | machine account subtype ID. # str | machine account subtype ID.
    json_patch_operation = '''[sailpoint.v2026.JsonPatchOperation()]''' # List[JsonPatchOperation] | The JSONPatch payload used to update the object.

    try:
        # Machine Subtype Approval Config
        new_json_patch_operation = JsonPatchOperation.from_json(json_patch_operation)
        results = MachineSubtypeApprovalConfigApi(api_client).update_machine_account_deletion_by_sub_type_approval_config(x_sail_point_experimental=x_sail_point_experimental, subtype_id=subtype_id, json_patch_operation=new_json_patch_operation)
        # Below is a request that includes all optional parameters
        # results = MachineSubtypeApprovalConfigApi(api_client).update_machine_account_deletion_by_sub_type_approval_config(x_sail_point_experimental, subtype_id, new_json_patch_operation)
        print("The response of MachineSubtypeApprovalConfigApi->update_machine_account_deletion_by_sub_type_approval_config:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling MachineSubtypeApprovalConfigApi->update_machine_account_deletion_by_sub_type_approval_config: %s\n" % e)
```



[[Back to top]](#) 




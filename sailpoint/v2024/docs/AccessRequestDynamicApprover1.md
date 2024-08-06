# AccessRequestDynamicApprover1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the identity to add to the approver list for the access request. | 
**name** | **str** | The name of the identity to add to the approver list for the access request. | 
**type** | **object** | The type of object being referenced. | 

## Example

```python
from sailpoint.v2024.models.access_request_dynamic_approver1 import AccessRequestDynamicApprover1

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestDynamicApprover1 from a JSON string
access_request_dynamic_approver1_instance = AccessRequestDynamicApprover1.from_json(json)
# print the JSON string representation of the object
print AccessRequestDynamicApprover1.to_json()

# convert the object into a dict
access_request_dynamic_approver1_dict = access_request_dynamic_approver1_instance.to_dict()
# create an instance of AccessRequestDynamicApprover1 from a dict
access_request_dynamic_approver1_form_dict = access_request_dynamic_approver1.from_dict(access_request_dynamic_approver1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



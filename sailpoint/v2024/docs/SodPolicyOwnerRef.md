# SodPolicyOwnerRef

The owner of the SOD policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Owner type. | [optional] 
**id** | **str** | Owner&#39;s ID. | [optional] 
**name** | **str** | Owner&#39;s name. | [optional] 

## Example

```python
from sailpoint.v2024.models.sod_policy_owner_ref import SodPolicyOwnerRef

# TODO update the JSON string below
json = "{}"
# create an instance of SodPolicyOwnerRef from a JSON string
sod_policy_owner_ref_instance = SodPolicyOwnerRef.from_json(json)
# print the JSON string representation of the object
print(SodPolicyOwnerRef.to_json())

# convert the object into a dict
sod_policy_owner_ref_dict = sod_policy_owner_ref_instance.to_dict()
# create an instance of SodPolicyOwnerRef from a dict
sod_policy_owner_ref_from_dict = SodPolicyOwnerRef.from_dict(sod_policy_owner_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



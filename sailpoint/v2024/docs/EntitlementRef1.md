# EntitlementRef1

Entitlement including a specific set of access.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Entitlement&#39;s DTO type. | [optional] 
**id** | **str** | Entitlement&#39;s ID. | [optional] 
**name** | **str** | Entitlement&#39;s display name. | [optional] 

## Example

```python
from sailpoint.v2024.models.entitlement_ref1 import EntitlementRef1

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementRef1 from a JSON string
entitlement_ref1_instance = EntitlementRef1.from_json(json)
# print the JSON string representation of the object
print(EntitlementRef1.to_json())

# convert the object into a dict
entitlement_ref1_dict = entitlement_ref1_instance.to_dict()
# create an instance of EntitlementRef1 from a dict
entitlement_ref1_from_dict = EntitlementRef1.from_dict(entitlement_ref1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



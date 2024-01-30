# EntitlementRef

Entitlement including a specific set of access.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Entitlement&#39;s DTO type. | [optional] 
**id** | **str** | Entitlement&#39;s ID. | [optional] 
**name** | **str** | Entitlement&#39;s display name. | [optional] 

## Example

```python
from sailpoint.v3.models.entitlement_ref import EntitlementRef

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementRef from a JSON string
entitlement_ref_instance = EntitlementRef.from_json(json)
# print the JSON string representation of the object
print EntitlementRef.to_json()

# convert the object into a dict
entitlement_ref_dict = entitlement_ref_instance.to_dict()
# create an instance of EntitlementRef from a dict
entitlement_ref_form_dict = entitlement_ref.from_dict(entitlement_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



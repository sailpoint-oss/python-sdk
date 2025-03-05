# EntitlementOwner

The identity that owns the entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identity ID | [optional] 
**type** | **str** | The type of object | [optional] 
**name** | **str** | The display name of the identity | [optional] 

## Example

```python
from sailpoint.v2024.models.entitlement_owner import EntitlementOwner

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementOwner from a JSON string
entitlement_owner_instance = EntitlementOwner.from_json(json)
# print the JSON string representation of the object
print(EntitlementOwner.to_json())

# convert the object into a dict
entitlement_owner_dict = entitlement_owner_instance.to_dict()
# create an instance of EntitlementOwner from a dict
entitlement_owner_from_dict = EntitlementOwner.from_dict(entitlement_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



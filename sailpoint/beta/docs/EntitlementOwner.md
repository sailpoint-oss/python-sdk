# EntitlementOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The owner id for the entitlement | [optional] 
**name** | **str** | The owner name for the entitlement | [optional] 
**type** | **str** | The type of the owner. Initially only type IDENTITY is supported | [optional] 

## Example

```python
from sailpoint.beta.models.entitlement_owner import EntitlementOwner

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



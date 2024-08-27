# Entitlement1Owner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The owner id for the entitlement | [optional] 
**name** | **str** | The owner name for the entitlement | [optional] 
**type** | **str** | The type of the owner. Initially only type IDENTITY is supported | [optional] 

## Example

```python
from sailpoint.v2024.models.entitlement1_owner import Entitlement1Owner

# TODO update the JSON string below
json = "{}"
# create an instance of Entitlement1Owner from a JSON string
entitlement1_owner_instance = Entitlement1Owner.from_json(json)
# print the JSON string representation of the object
print(Entitlement1Owner.to_json())

# convert the object into a dict
entitlement1_owner_dict = entitlement1_owner_instance.to_dict()
# create an instance of Entitlement1Owner from a dict
entitlement1_owner_from_dict = Entitlement1Owner.from_dict(entitlement1_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



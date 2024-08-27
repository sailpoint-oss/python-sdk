# IdentityAttribute1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The attribute key | [optional] 
**name** | **str** | Human-readable display name of the attribute | [optional] 
**value** | **str** | The attribute value | [optional] 

## Example

```python
from sailpoint.v2024.models.identity_attribute1 import IdentityAttribute1

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttribute1 from a JSON string
identity_attribute1_instance = IdentityAttribute1.from_json(json)
# print the JSON string representation of the object
print(IdentityAttribute1.to_json())

# convert the object into a dict
identity_attribute1_dict = identity_attribute1_instance.to_dict()
# create an instance of IdentityAttribute1 from a dict
identity_attribute1_from_dict = IdentityAttribute1.from_dict(identity_attribute1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



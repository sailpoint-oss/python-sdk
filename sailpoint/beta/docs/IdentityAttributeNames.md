# IdentityAttributeNames

Identity attribute IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | List of identity attributes&#39; technical names. | [optional] 

## Example

```python
from sailpoint.beta.models.identity_attribute_names import IdentityAttributeNames

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttributeNames from a JSON string
identity_attribute_names_instance = IdentityAttributeNames.from_json(json)
# print the JSON string representation of the object
print(IdentityAttributeNames.to_json())

# convert the object into a dict
identity_attribute_names_dict = identity_attribute_names_instance.to_dict()
# create an instance of IdentityAttributeNames from a dict
identity_attribute_names_from_dict = IdentityAttributeNames.from_dict(identity_attribute_names_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



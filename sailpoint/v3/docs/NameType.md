# NameType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the actor or target name | [optional] 
**type** | [**DtoType**](DtoType.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.name_type import NameType

# TODO update the JSON string below
json = "{}"
# create an instance of NameType from a JSON string
name_type_instance = NameType.from_json(json)
# print the JSON string representation of the object
print NameType.to_json()

# convert the object into a dict
name_type_dict = name_type_instance.to_dict()
# create an instance of NameType from a dict
name_type_form_dict = name_type.from_dict(name_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



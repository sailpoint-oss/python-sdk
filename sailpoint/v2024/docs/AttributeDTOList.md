# AttributeDTOList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[AttributeDTO]**](AttributeDTO.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.attribute_dto_list import AttributeDTOList

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeDTOList from a JSON string
attribute_dto_list_instance = AttributeDTOList.from_json(json)
# print the JSON string representation of the object
print(AttributeDTOList.to_json())

# convert the object into a dict
attribute_dto_list_dict = attribute_dto_list_instance.to_dict()
# create an instance of AttributeDTOList from a dict
attribute_dto_list_from_dict = AttributeDTOList.from_dict(attribute_dto_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



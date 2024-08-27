# BaseCommonDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the Object | [optional] [readonly] 
**name** | **str** | Name of the Object | 
**created** | **datetime** | Creation date of the Object | [optional] [readonly] 
**modified** | **datetime** | Last modification date of the Object | [optional] [readonly] 

## Example

```python
from sailpoint.v2024.models.base_common_dto import BaseCommonDto

# TODO update the JSON string below
json = "{}"
# create an instance of BaseCommonDto from a JSON string
base_common_dto_instance = BaseCommonDto.from_json(json)
# print the JSON string representation of the object
print(BaseCommonDto.to_json())

# convert the object into a dict
base_common_dto_dict = base_common_dto_instance.to_dict()
# create an instance of BaseCommonDto from a dict
base_common_dto_from_dict = BaseCommonDto.from_dict(base_common_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



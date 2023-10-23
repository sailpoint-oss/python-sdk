# BaseCommonDto1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the Object | [optional] [readonly] 
**name** | **str** | Name of the Object | 
**created** | **datetime** | Creation date of the Object | [optional] [readonly] 
**modified** | **datetime** | Last modification date of the Object | [optional] [readonly] 

## Example

```python
from beta.models.base_common_dto1 import BaseCommonDto1

# TODO update the JSON string below
json = "{}"
# create an instance of BaseCommonDto1 from a JSON string
base_common_dto1_instance = BaseCommonDto1.from_json(json)
# print the JSON string representation of the object
print BaseCommonDto1.to_json()

# convert the object into a dict
base_common_dto1_dict = base_common_dto1_instance.to_dict()
# create an instance of BaseCommonDto1 from a dict
base_common_dto1_form_dict = base_common_dto1.from_dict(base_common_dto1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



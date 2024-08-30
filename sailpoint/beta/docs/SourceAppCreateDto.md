# SourceAppCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The source app name | 
**description** | **str** | The description of the source app | 
**match_all_accounts** | **bool** | True if the source app match all accounts | [optional] [default to False]
**account_source** | [**SourceAppCreateDtoAccountSource**](SourceAppCreateDtoAccountSource.md) |  | 

## Example

```python
from sailpoint.beta.models.source_app_create_dto import SourceAppCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SourceAppCreateDto from a JSON string
source_app_create_dto_instance = SourceAppCreateDto.from_json(json)
# print the JSON string representation of the object
print(SourceAppCreateDto.to_json())

# convert the object into a dict
source_app_create_dto_dict = source_app_create_dto_instance.to_dict()
# create an instance of SourceAppCreateDto from a dict
source_app_create_dto_from_dict = SourceAppCreateDto.from_dict(source_app_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



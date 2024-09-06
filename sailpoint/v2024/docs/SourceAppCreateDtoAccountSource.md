# SourceAppCreateDtoAccountSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The source ID | 
**type** | **str** | The source type, will always be \&quot;SOURCE\&quot; | [optional] 
**name** | **str** | The source name | [optional] 

## Example

```python
from sailpoint.v2024.models.source_app_create_dto_account_source import SourceAppCreateDtoAccountSource

# TODO update the JSON string below
json = "{}"
# create an instance of SourceAppCreateDtoAccountSource from a JSON string
source_app_create_dto_account_source_instance = SourceAppCreateDtoAccountSource.from_json(json)
# print the JSON string representation of the object
print(SourceAppCreateDtoAccountSource.to_json())

# convert the object into a dict
source_app_create_dto_account_source_dict = source_app_create_dto_account_source_instance.to_dict()
# create an instance of SourceAppCreateDtoAccountSource from a dict
source_app_create_dto_account_source_from_dict = SourceAppCreateDtoAccountSource.from_dict(source_app_create_dto_account_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



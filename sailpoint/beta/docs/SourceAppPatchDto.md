# SourceAppPatchDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The source app id | [optional] 
**cloud_app_id** | **str** | The deprecated source app id | [optional] 
**name** | **str** | The source app name | [optional] 
**created** | **datetime** | Time when the source app was created | [optional] 
**modified** | **datetime** | Time when the source app was last modified | [optional] 
**enabled** | **bool** | True if the source app is enabled | [optional] [default to False]
**provision_request_enabled** | **bool** | True if the source app is provision request enabled | [optional] [default to False]
**description** | **str** | The description of the source app | [optional] 
**match_all_accounts** | **bool** | True if the source app match all accounts | [optional] [default to False]
**app_center_enabled** | **bool** | True if the source app is shown in the app center | [optional] [default to True]
**access_profiles** | **List[str]** | List of IDs of access profiles | [optional] 
**account_source** | [**SourceAppAccountSource**](SourceAppAccountSource.md) |  | [optional] 
**owner** | [**BaseReferenceDto**](BaseReferenceDto.md) | The owner of source app | [optional] 

## Example

```python
from sailpoint.beta.models.source_app_patch_dto import SourceAppPatchDto

# TODO update the JSON string below
json = "{}"
# create an instance of SourceAppPatchDto from a JSON string
source_app_patch_dto_instance = SourceAppPatchDto.from_json(json)
# print the JSON string representation of the object
print(SourceAppPatchDto.to_json())

# convert the object into a dict
source_app_patch_dto_dict = source_app_patch_dto_instance.to_dict()
# create an instance of SourceAppPatchDto from a dict
source_app_patch_dto_from_dict = SourceAppPatchDto.from_dict(source_app_patch_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



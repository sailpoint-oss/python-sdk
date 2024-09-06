# SourceApp


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
**account_source** | [**SourceAppAccountSource**](SourceAppAccountSource.md) |  | [optional] 
**owner** | [**BaseReferenceDto**](BaseReferenceDto.md) | The owner of source app | [optional] 

## Example

```python
from sailpoint.v2024.models.source_app import SourceApp

# TODO update the JSON string below
json = "{}"
# create an instance of SourceApp from a JSON string
source_app_instance = SourceApp.from_json(json)
# print the JSON string representation of the object
print(SourceApp.to_json())

# convert the object into a dict
source_app_dict = source_app_instance.to_dict()
# create an instance of SourceApp from a dict
source_app_from_dict = SourceApp.from_dict(source_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



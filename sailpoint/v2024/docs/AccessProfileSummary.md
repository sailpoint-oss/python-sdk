# AccessProfileSummary

This is a summary representation of an access profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** | Description of access item. | [optional] 
**type** | **str** | Type of the access item. | [optional] 
**source** | [**Reference**](Reference.md) |  | [optional] 
**owner** | [**DisplayReference**](DisplayReference.md) |  | [optional] 
**revocable** | **bool** |  | [optional] 

## Example

```python
from sailpoint.v2024.models.access_profile_summary import AccessProfileSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileSummary from a JSON string
access_profile_summary_instance = AccessProfileSummary.from_json(json)
# print the JSON string representation of the object
print(AccessProfileSummary.to_json())

# convert the object into a dict
access_profile_summary_dict = access_profile_summary_instance.to_dict()
# create an instance of AccessProfileSummary from a dict
access_profile_summary_from_dict = AccessProfileSummary.from_dict(access_profile_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



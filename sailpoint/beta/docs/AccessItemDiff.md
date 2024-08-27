# AccessItemDiff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the id of the access item | [optional] 
**event_type** | **str** |  | [optional] 
**display_name** | **str** | the display name of the access item | [optional] 
**source_name** | **str** | the source name of the access item | [optional] 

## Example

```python
from sailpoint.beta.models.access_item_diff import AccessItemDiff

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemDiff from a JSON string
access_item_diff_instance = AccessItemDiff.from_json(json)
# print the JSON string representation of the object
print(AccessItemDiff.to_json())

# convert the object into a dict
access_item_diff_dict = access_item_diff_instance.to_dict()
# create an instance of AccessItemDiff from a dict
access_item_diff_from_dict = AccessItemDiff.from_dict(access_item_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



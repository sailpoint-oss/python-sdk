# AccessSummaryAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | The ID of the item being certified | [optional] 
**name** | **str** | The name of the item being certified | [optional] 

## Example

```python
from sailpoint.v3.models.access_summary_access import AccessSummaryAccess

# TODO update the JSON string below
json = "{}"
# create an instance of AccessSummaryAccess from a JSON string
access_summary_access_instance = AccessSummaryAccess.from_json(json)
# print the JSON string representation of the object
print(AccessSummaryAccess.to_json())

# convert the object into a dict
access_summary_access_dict = access_summary_access_instance.to_dict()
# create an instance of AccessSummaryAccess from a dict
access_summary_access_from_dict = AccessSummaryAccess.from_dict(access_summary_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



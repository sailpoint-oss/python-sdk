# CommonAccessItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Common Access Item ID | [optional] 
**access** | [**CommonAccessItemAccess**](CommonAccessItemAccess.md) |  | [optional] 
**status** | [**CommonAccessItemState**](CommonAccessItemState.md) |  | [optional] 
**last_updated** | **str** |  | [optional] 
**reviewed_by_user** | **bool** |  | [optional] 
**last_reviewed** | **str** |  | [optional] 
**created_by_user** | **str** |  | [optional] 

## Example

```python
from sailpoint.v2024.models.common_access_item_response import CommonAccessItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommonAccessItemResponse from a JSON string
common_access_item_response_instance = CommonAccessItemResponse.from_json(json)
# print the JSON string representation of the object
print(CommonAccessItemResponse.to_json())

# convert the object into a dict
common_access_item_response_dict = common_access_item_response_instance.to_dict()
# create an instance of CommonAccessItemResponse from a dict
common_access_item_response_from_dict = CommonAccessItemResponse.from_dict(common_access_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



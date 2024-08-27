# CommonAccessItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**CommonAccessItemAccess**](CommonAccessItemAccess.md) |  | [optional] 
**status** | [**CommonAccessItemState**](CommonAccessItemState.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.common_access_item_request import CommonAccessItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommonAccessItemRequest from a JSON string
common_access_item_request_instance = CommonAccessItemRequest.from_json(json)
# print the JSON string representation of the object
print(CommonAccessItemRequest.to_json())

# convert the object into a dict
common_access_item_request_dict = common_access_item_request_instance.to_dict()
# create an instance of CommonAccessItemRequest from a dict
common_access_item_request_from_dict = CommonAccessItemRequest.from_dict(common_access_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CommonAccessItemAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Common access ID | [optional] 
**type** | [**CommonAccessType**](CommonAccessType.md) |  | [optional] 
**name** | **str** | Common access name | [optional] 
**description** | **str** | Common access description | [optional] 
**owner_name** | **str** | Common access owner name | [optional] 
**owner_id** | **str** | Common access owner ID | [optional] 

## Example

```python
from sailpoint.beta.models.common_access_item_access import CommonAccessItemAccess

# TODO update the JSON string below
json = "{}"
# create an instance of CommonAccessItemAccess from a JSON string
common_access_item_access_instance = CommonAccessItemAccess.from_json(json)
# print the JSON string representation of the object
print(CommonAccessItemAccess.to_json())

# convert the object into a dict
common_access_item_access_dict = common_access_item_access_instance.to_dict()
# create an instance of CommonAccessItemAccess from a dict
common_access_item_access_from_dict = CommonAccessItemAccess.from_dict(common_access_item_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



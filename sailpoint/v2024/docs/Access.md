# Access


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**display_name** | **str** |  | [optional] 
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from sailpoint.v2024.models.access import Access

# TODO update the JSON string below
json = "{}"
# create an instance of Access from a JSON string
access_instance = Access.from_json(json)
# print the JSON string representation of the object
print(Access.to_json())

# convert the object into a dict
access_dict = access_instance.to_dict()
# create an instance of Access from a dict
access_from_dict = Access.from_dict(access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



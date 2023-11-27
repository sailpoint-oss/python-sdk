# BaseAccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**description** | **str** | The description of the access item | [optional] 
**created** | **datetime** | A date-time in ISO-8601 format | [optional] 
**modified** | **datetime** | A date-time in ISO-8601 format | [optional] 
**synced** | **datetime** | A date-time in ISO-8601 format | [optional] 
**enabled** | **bool** |  | [optional] 
**requestable** | **bool** | Indicates if the access can be requested | [optional] 
**request_comments_required** | **bool** | Indicates if comments are required when requesting access | [optional] 
**owner** | [**Owner**](Owner.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.base_access import BaseAccess

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAccess from a JSON string
base_access_instance = BaseAccess.from_json(json)
# print the JSON string representation of the object
print BaseAccess.to_json()

# convert the object into a dict
base_access_dict = base_access_instance.to_dict()
# create an instance of BaseAccess from a dict
base_access_form_dict = base_access.from_dict(base_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



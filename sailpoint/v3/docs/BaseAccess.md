# BaseAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Access item&#39;s description. | [optional] 
**created** | **datetime** | ISO-8601 date-time referring to the time when the object was created. | [optional] 
**modified** | **datetime** | ISO-8601 date-time referring to the time when the object was last modified. | [optional] 
**synced** | **datetime** | ISO-8601 date-time referring to the date-time when object was queued to be synced into search database for use in the search API.   This date-time changes anytime there is an update to the object, which triggers a synchronization event being sent to the search database.  There may be some delay between the &#x60;synced&#x60; time and the time when the updated data is actually available in the search API.  | [optional] 
**enabled** | **bool** | Indicates whether the access item is currently enabled. | [optional] [default to False]
**requestable** | **bool** | Indicates whether the access item can be requested. | [optional] [default to True]
**request_comments_required** | **bool** | Indicates whether comments are required for requests to access the item. | [optional] [default to False]
**owner** | [**BaseAccessOwner**](BaseAccessOwner.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.base_access import BaseAccess

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAccess from a JSON string
base_access_instance = BaseAccess.from_json(json)
# print the JSON string representation of the object
print(BaseAccess.to_json())

# convert the object into a dict
base_access_dict = base_access_instance.to_dict()
# create an instance of BaseAccess from a dict
base_access_from_dict = BaseAccess.from_dict(base_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



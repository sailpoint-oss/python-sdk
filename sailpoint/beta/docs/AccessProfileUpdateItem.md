# AccessProfileUpdateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of Access Profile in bulk update request. | 
**requestable** | **bool** | Access Profile requestable or not. | 
**status** | **str** |  The HTTP response status code returned for an individual Access Profile that is requested for update during a bulk update operation.  &gt; 201   - Access profile is updated successfully.  &gt; 404   - Access profile not found.  | 
**description** | **str** | Human readable status description and containing additional context information about success or failures etc.  | [optional] 

## Example

```python
from sailpoint.beta.models.access_profile_update_item import AccessProfileUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileUpdateItem from a JSON string
access_profile_update_item_instance = AccessProfileUpdateItem.from_json(json)
# print the JSON string representation of the object
print(AccessProfileUpdateItem.to_json())

# convert the object into a dict
access_profile_update_item_dict = access_profile_update_item_instance.to_dict()
# create an instance of AccessProfileUpdateItem from a dict
access_profile_update_item_from_dict = AccessProfileUpdateItem.from_dict(access_profile_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



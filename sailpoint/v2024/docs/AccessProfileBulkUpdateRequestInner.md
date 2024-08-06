# AccessProfileBulkUpdateRequestInner

Access Profile's basic details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Access Profile ID. | [optional] 
**requestable** | **bool** | Access Profile is requestable or not. | [optional] 

## Example

```python
from sailpoint.v2024.models.access_profile_bulk_update_request_inner import AccessProfileBulkUpdateRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileBulkUpdateRequestInner from a JSON string
access_profile_bulk_update_request_inner_instance = AccessProfileBulkUpdateRequestInner.from_json(json)
# print the JSON string representation of the object
print AccessProfileBulkUpdateRequestInner.to_json()

# convert the object into a dict
access_profile_bulk_update_request_inner_dict = access_profile_bulk_update_request_inner_instance.to_dict()
# create an instance of AccessProfileBulkUpdateRequestInner from a dict
access_profile_bulk_update_request_inner_form_dict = access_profile_bulk_update_request_inner.from_dict(access_profile_bulk_update_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



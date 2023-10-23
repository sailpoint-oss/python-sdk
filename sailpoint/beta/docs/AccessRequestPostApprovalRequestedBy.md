# AccessRequestPostApprovalRequestedBy

The identity that initiated the access request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of the object to which this reference applies | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.access_request_post_approval_requested_by import AccessRequestPostApprovalRequestedBy

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestPostApprovalRequestedBy from a JSON string
access_request_post_approval_requested_by_instance = AccessRequestPostApprovalRequestedBy.from_json(json)
# print the JSON string representation of the object
print AccessRequestPostApprovalRequestedBy.to_json()

# convert the object into a dict
access_request_post_approval_requested_by_dict = access_request_post_approval_requested_by_instance.to_dict()
# create an instance of AccessRequestPostApprovalRequestedBy from a dict
access_request_post_approval_requested_by_form_dict = access_request_post_approval_requested_by.from_dict(access_request_post_approval_requested_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



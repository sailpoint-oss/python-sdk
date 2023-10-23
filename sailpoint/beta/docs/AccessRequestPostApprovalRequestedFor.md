# AccessRequestPostApprovalRequestedFor

The identity who the access request is for.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of the object to which this reference applies | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.access_request_post_approval_requested_for import AccessRequestPostApprovalRequestedFor

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestPostApprovalRequestedFor from a JSON string
access_request_post_approval_requested_for_instance = AccessRequestPostApprovalRequestedFor.from_json(json)
# print the JSON string representation of the object
print AccessRequestPostApprovalRequestedFor.to_json()

# convert the object into a dict
access_request_post_approval_requested_for_dict = access_request_post_approval_requested_for_instance.to_dict()
# create an instance of AccessRequestPostApprovalRequestedFor from a dict
access_request_post_approval_requested_for_form_dict = access_request_post_approval_requested_for.from_dict(access_request_post_approval_requested_for_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AccessRequestDynamicApprover


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_id** | **str** | The unique ID of the access request object. Can be used with the [access request status endpoint](https://developer.sailpoint.com/idn/api/beta/list-access-request-status) to get the status of the request.  | 
**requested_for** | [**AccessRequestDynamicApproverRequestedFor**](AccessRequestDynamicApproverRequestedFor.md) |  | 
**requested_items** | [**List[AccessRequestDynamicApproverRequestedItemsInner]**](AccessRequestDynamicApproverRequestedItemsInner.md) | The access items that are being requested. | 
**requested_by** | [**AccessRequestDynamicApproverRequestedBy**](AccessRequestDynamicApproverRequestedBy.md) |  | 

## Example

```python
from beta.models.access_request_dynamic_approver import AccessRequestDynamicApprover

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestDynamicApprover from a JSON string
access_request_dynamic_approver_instance = AccessRequestDynamicApprover.from_json(json)
# print the JSON string representation of the object
print AccessRequestDynamicApprover.to_json()

# convert the object into a dict
access_request_dynamic_approver_dict = access_request_dynamic_approver_instance.to_dict()
# create an instance of AccessRequestDynamicApprover from a dict
access_request_dynamic_approver_form_dict = access_request_dynamic_approver.from_dict(access_request_dynamic_approver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



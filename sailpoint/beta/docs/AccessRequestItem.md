# AccessRequestItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the item being requested. | 
**id** | **str** | ID of Role, Access Profile or Entitlement being requested. | 
**comment** | **str** | Comment provided by requester. * Comment is required when the request is of type Revoke Access.  | [optional] 
**client_metadata** | **Dict[str, str]** | Arbitrary key-value pairs. They will never be processed by the IdentityNow system but will be returned on associated APIs such as /account-activities and /access-request-status. | [optional] 
**remove_date** | **datetime** | The date the role or access profile is no longer assigned to the specified identity. * Specify a date in the future. * The current SLA for the deprovisioning is 24 hours. * This date can be modified to either extend or decrease the duration of access item assignments for the specified identity. * Currently it is not supported for entitlements.  | [optional] 

## Example

```python
from beta.models.access_request_item import AccessRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestItem from a JSON string
access_request_item_instance = AccessRequestItem.from_json(json)
# print the JSON string representation of the object
print AccessRequestItem.to_json()

# convert the object into a dict
access_request_item_dict = access_request_item_instance.to_dict()
# create an instance of AccessRequestItem from a dict
access_request_item_form_dict = access_request_item.from_dict(access_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



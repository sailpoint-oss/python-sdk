# RequestableObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the requestable object itself | [optional] 
**name** | **str** | Human-readable display name of the requestable object | [optional] 
**created** | **datetime** | The time when the requestable object was created | [optional] 
**modified** | **datetime** | The time when the requestable object was last modified | [optional] 
**description** | **str** | Description of the requestable object. | [optional] 
**type** | [**RequestableObjectType**](RequestableObjectType.md) |  | [optional] 
**request_status** | [**RequestableObjectRequestStatus**](RequestableObjectRequestStatus.md) |  | [optional] 
**identity_request_id** | **str** | If *requestStatus* is *PENDING*, indicates the id of the associated account activity. | [optional] 
**owner_ref** | [**IdentityReferenceWithNameAndEmail**](IdentityReferenceWithNameAndEmail.md) |  | [optional] 
**request_comments_required** | **bool** | Whether the requester must provide comments when requesting the object. | [optional] 

## Example

```python
from sailpoint.beta.models.requestable_object import RequestableObject

# TODO update the JSON string below
json = "{}"
# create an instance of RequestableObject from a JSON string
requestable_object_instance = RequestableObject.from_json(json)
# print the JSON string representation of the object
print RequestableObject.to_json()

# convert the object into a dict
requestable_object_dict = requestable_object_instance.to_dict()
# create an instance of RequestableObject from a dict
requestable_object_form_dict = requestable_object.from_dict(requestable_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



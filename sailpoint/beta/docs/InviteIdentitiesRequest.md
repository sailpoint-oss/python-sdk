# InviteIdentitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The list of Identities IDs to invite - required when &#39;uninvited&#39; is false | [optional] 
**uninvited** | **bool** | indicator (optional) to invite all unregistered identities in the system within a limit 1000. This parameter makes sense only when &#39;ids&#39; is empty. | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.invite_identities_request import InviteIdentitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InviteIdentitiesRequest from a JSON string
invite_identities_request_instance = InviteIdentitiesRequest.from_json(json)
# print the JSON string representation of the object
print InviteIdentitiesRequest.to_json()

# convert the object into a dict
invite_identities_request_dict = invite_identities_request_instance.to_dict()
# create an instance of InviteIdentitiesRequest from a dict
invite_identities_request_form_dict = invite_identities_request.from_dict(invite_identities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PeerGroupMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the peer group member. | [optional] 
**type** | **str** | The type of the peer group member. | [optional] 
**peer_group_id** | **str** | The ID of the peer group. | [optional] 
**attributes** | **Dict[str, object]** | Arbitrary key-value pairs, belonging to the peer group member. | [optional] 

## Example

```python
from sailpoint.v2024.models.peer_group_member import PeerGroupMember

# TODO update the JSON string below
json = "{}"
# create an instance of PeerGroupMember from a JSON string
peer_group_member_instance = PeerGroupMember.from_json(json)
# print the JSON string representation of the object
print PeerGroupMember.to_json()

# convert the object into a dict
peer_group_member_dict = peer_group_member_instance.to_dict()
# create an instance of PeerGroupMember from a dict
peer_group_member_form_dict = peer_group_member.from_dict(peer_group_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# IdentityProfileAllOfOwner

Identity profile's owner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Owner&#39;s object type. | [optional] 
**id** | **str** | Owner&#39;s ID. | [optional] 
**name** | **str** | Owner&#39;s name. | [optional] 

## Example

```python
from sailpoint.v3.models.identity_profile_all_of_owner import IdentityProfileAllOfOwner

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProfileAllOfOwner from a JSON string
identity_profile_all_of_owner_instance = IdentityProfileAllOfOwner.from_json(json)
# print the JSON string representation of the object
print(IdentityProfileAllOfOwner.to_json())

# convert the object into a dict
identity_profile_all_of_owner_dict = identity_profile_all_of_owner_instance.to_dict()
# create an instance of IdentityProfileAllOfOwner from a dict
identity_profile_all_of_owner_from_dict = IdentityProfileAllOfOwner.from_dict(identity_profile_all_of_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



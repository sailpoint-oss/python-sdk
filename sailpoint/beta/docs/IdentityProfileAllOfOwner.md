# IdentityProfileAllOfOwner

The owner of the Identity Profile.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the object to which this reference applies | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 

## Example

```python
from beta.models.identity_profile_all_of_owner import IdentityProfileAllOfOwner

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProfileAllOfOwner from a JSON string
identity_profile_all_of_owner_instance = IdentityProfileAllOfOwner.from_json(json)
# print the JSON string representation of the object
print IdentityProfileAllOfOwner.to_json()

# convert the object into a dict
identity_profile_all_of_owner_dict = identity_profile_all_of_owner_instance.to_dict()
# create an instance of IdentityProfileAllOfOwner from a dict
identity_profile_all_of_owner_form_dict = identity_profile_all_of_owner.from_dict(identity_profile_all_of_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



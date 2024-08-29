# IdentityProfilesConnections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the IdentityProfile this reference applies | [optional] 
**name** | **str** | Human-readable display name of the IdentityProfile to which this reference applies | [optional] 
**identity_count** | **int** | The Number of Identities managed by this IdentityProfile | [optional] 

## Example

```python
from sailpoint.v3.models.identity_profiles_connections import IdentityProfilesConnections

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProfilesConnections from a JSON string
identity_profiles_connections_instance = IdentityProfilesConnections.from_json(json)
# print the JSON string representation of the object
print(IdentityProfilesConnections.to_json())

# convert the object into a dict
identity_profiles_connections_dict = identity_profiles_connections_instance.to_dict()
# create an instance of IdentityProfilesConnections from a dict
identity_profiles_connections_from_dict = IdentityProfilesConnections.from_dict(identity_profiles_connections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SourceConnectionsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_profiles** | [**List[IdentityProfilesConnections]**](IdentityProfilesConnections.md) | The IdentityProfile attached to this source | [optional] 
**credential_profiles** | **List[str]** | Name of the CredentialProfile attached to this source | [optional] 
**source_attributes** | **List[str]** | The attributes attached to this source | [optional] 
**mapping_profiles** | **List[str]** | The profiles attached to this source | [optional] 
**dependent_custom_transforms** | [**List[Transform]**](Transform.md) |  | [optional] 
**dependent_apps** | [**List[DependantAppConnections]**](DependantAppConnections.md) |  | [optional] 
**missing_dependents** | [**List[DependantConnectionsMissingDto]**](DependantConnectionsMissingDto.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.source_connections_dto import SourceConnectionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SourceConnectionsDto from a JSON string
source_connections_dto_instance = SourceConnectionsDto.from_json(json)
# print the JSON string representation of the object
print(SourceConnectionsDto.to_json())

# convert the object into a dict
source_connections_dto_dict = source_connections_dto_instance.to_dict()
# create an instance of SourceConnectionsDto from a dict
source_connections_dto_from_dict = SourceConnectionsDto.from_dict(source_connections_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



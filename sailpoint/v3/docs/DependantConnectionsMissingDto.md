# DependantConnectionsMissingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependency_type** | **str** | The type of dependency type that is missing in the SourceConnections | [optional] 
**reason** | **str** | The reason why this dependency is missing | [optional] 

## Example

```python
from sailpoint.v3.models.dependant_connections_missing_dto import DependantConnectionsMissingDto

# TODO update the JSON string below
json = "{}"
# create an instance of DependantConnectionsMissingDto from a JSON string
dependant_connections_missing_dto_instance = DependantConnectionsMissingDto.from_json(json)
# print the JSON string representation of the object
print(DependantConnectionsMissingDto.to_json())

# convert the object into a dict
dependant_connections_missing_dto_dict = dependant_connections_missing_dto_instance.to_dict()
# create an instance of DependantConnectionsMissingDto from a dict
dependant_connections_missing_dto_from_dict = DependantConnectionsMissingDto.from_dict(dependant_connections_missing_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



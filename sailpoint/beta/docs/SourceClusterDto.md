# SourceClusterDto

Source cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Source cluster DTO type. | [optional] 
**id** | **str** | Source cluster ID. | [optional] 
**name** | **str** | Source cluster display name. | [optional] 

## Example

```python
from sailpoint.beta.models.source_cluster_dto import SourceClusterDto

# TODO update the JSON string below
json = "{}"
# create an instance of SourceClusterDto from a JSON string
source_cluster_dto_instance = SourceClusterDto.from_json(json)
# print the JSON string representation of the object
print SourceClusterDto.to_json()

# convert the object into a dict
source_cluster_dto_dict = source_cluster_dto_instance.to_dict()
# create an instance of SourceClusterDto from a dict
source_cluster_dto_form_dict = source_cluster_dto.from_dict(source_cluster_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



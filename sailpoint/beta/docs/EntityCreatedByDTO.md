# EntityCreatedByDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the creator | [optional] 
**display_name** | **str** | The display name of the creator | [optional] 

## Example

```python
from sailpoint.beta.models.entity_created_by_dto import EntityCreatedByDTO

# TODO update the JSON string below
json = "{}"
# create an instance of EntityCreatedByDTO from a JSON string
entity_created_by_dto_instance = EntityCreatedByDTO.from_json(json)
# print the JSON string representation of the object
print EntityCreatedByDTO.to_json()

# convert the object into a dict
entity_created_by_dto_dict = entity_created_by_dto_instance.to_dict()
# create an instance of EntityCreatedByDTO from a dict
entity_created_by_dto_form_dict = entity_created_by_dto.from_dict(entity_created_by_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# IdentityEntitiesIdentityEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the resource to which the identity is associated | [optional] 
**name** | **str** | name of the resource to which the identity is associated | [optional] 
**type** | **str** | type of the resource to which the identity is associated | [optional] 

## Example

```python
from beta.models.identity_entities_identity_entity import IdentityEntitiesIdentityEntity

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityEntitiesIdentityEntity from a JSON string
identity_entities_identity_entity_instance = IdentityEntitiesIdentityEntity.from_json(json)
# print the JSON string representation of the object
print IdentityEntitiesIdentityEntity.to_json()

# convert the object into a dict
identity_entities_identity_entity_dict = identity_entities_identity_entity_instance.to_dict()
# create an instance of IdentityEntitiesIdentityEntity from a dict
identity_entities_identity_entity_form_dict = identity_entities_identity_entity.from_dict(identity_entities_identity_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



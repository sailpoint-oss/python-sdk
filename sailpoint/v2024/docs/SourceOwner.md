# SourceOwner

Reference to identity object who owns the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Owner identity&#39;s ID. | [optional] 
**name** | **str** | Owner identity&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.v2024.models.source_owner import SourceOwner

# TODO update the JSON string below
json = "{}"
# create an instance of SourceOwner from a JSON string
source_owner_instance = SourceOwner.from_json(json)
# print the JSON string representation of the object
print SourceOwner.to_json()

# convert the object into a dict
source_owner_dict = source_owner_instance.to_dict()
# create an instance of SourceOwner from a dict
source_owner_form_dict = source_owner.from_dict(source_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



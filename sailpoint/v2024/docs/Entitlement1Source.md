# Entitlement1Source


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The source ID | [optional] 
**type** | **str** | The source type, will always be \&quot;SOURCE\&quot; | [optional] 
**name** | **str** | The source name | [optional] 

## Example

```python
from sailpoint.v2024.models.entitlement1_source import Entitlement1Source

# TODO update the JSON string below
json = "{}"
# create an instance of Entitlement1Source from a JSON string
entitlement1_source_instance = Entitlement1Source.from_json(json)
# print the JSON string representation of the object
print(Entitlement1Source.to_json())

# convert the object into a dict
entitlement1_source_dict = entitlement1_source_instance.to_dict()
# create an instance of Entitlement1Source from a dict
entitlement1_source_from_dict = Entitlement1Source.from_dict(entitlement1_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



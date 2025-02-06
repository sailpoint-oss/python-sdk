# Scope

This defines what access the segment is giving

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**ScopeType**](ScopeType.md) |  | [optional] 
**visibility** | [**ScopeVisibilityType**](ScopeVisibilityType.md) |  | [optional] 
**scope_filter** | [**VisibilityCriteria**](VisibilityCriteria.md) |  | [optional] 
**scope_selection** | [**List[Ref]**](Ref.md) | List of Identities that are assigned to the segment | [optional] 

## Example

```python
from sailpoint.v2024.models.scope import Scope

# TODO update the JSON string below
json = "{}"
# create an instance of Scope from a JSON string
scope_instance = Scope.from_json(json)
# print the JSON string representation of the object
print(Scope.to_json())

# convert the object into a dict
scope_dict = scope_instance.to_dict()
# create an instance of Scope from a dict
scope_from_dict = Scope.from_dict(scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



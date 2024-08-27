# ExpressionChildrenInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** | Operator for the expression | [optional] 
**attribute** | **str** | Name for the attribute | [optional] 
**value** | [**Value**](Value.md) |  | [optional] 
**children** | **str** | There cannot be anymore nested children. This will always be null. | [optional] 

## Example

```python
from sailpoint.v3.models.expression_children_inner import ExpressionChildrenInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionChildrenInner from a JSON string
expression_children_inner_instance = ExpressionChildrenInner.from_json(json)
# print the JSON string representation of the object
print(ExpressionChildrenInner.to_json())

# convert the object into a dict
expression_children_inner_dict = expression_children_inner_instance.to_dict()
# create an instance of ExpressionChildrenInner from a dict
expression_children_inner_from_dict = ExpressionChildrenInner.from_dict(expression_children_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SelectorAccountMatchConfigMatchExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_terms** | [**List[MatchTerm]**](MatchTerm.md) |  | [optional] 
**var_and** | **bool** | If it is AND operators for match terms | [optional] [default to True]

## Example

```python
from sailpoint.v2024.models.selector_account_match_config_match_expression import SelectorAccountMatchConfigMatchExpression

# TODO update the JSON string below
json = "{}"
# create an instance of SelectorAccountMatchConfigMatchExpression from a JSON string
selector_account_match_config_match_expression_instance = SelectorAccountMatchConfigMatchExpression.from_json(json)
# print the JSON string representation of the object
print(SelectorAccountMatchConfigMatchExpression.to_json())

# convert the object into a dict
selector_account_match_config_match_expression_dict = selector_account_match_config_match_expression_instance.to_dict()
# create an instance of SelectorAccountMatchConfigMatchExpression from a dict
selector_account_match_config_match_expression_from_dict = SelectorAccountMatchConfigMatchExpression.from_dict(selector_account_match_config_match_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



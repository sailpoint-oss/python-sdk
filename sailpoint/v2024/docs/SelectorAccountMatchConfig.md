# SelectorAccountMatchConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_expression** | [**SelectorAccountMatchConfigMatchExpression**](SelectorAccountMatchConfigMatchExpression.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.selector_account_match_config import SelectorAccountMatchConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SelectorAccountMatchConfig from a JSON string
selector_account_match_config_instance = SelectorAccountMatchConfig.from_json(json)
# print the JSON string representation of the object
print(SelectorAccountMatchConfig.to_json())

# convert the object into a dict
selector_account_match_config_dict = selector_account_match_config_instance.to_dict()
# create an instance of SelectorAccountMatchConfig from a dict
selector_account_match_config_from_dict = SelectorAccountMatchConfig.from_dict(selector_account_match_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



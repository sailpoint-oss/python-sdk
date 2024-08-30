# Selector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The application id | [optional] 
**account_match_config** | [**SelectorAccountMatchConfig**](SelectorAccountMatchConfig.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.selector import Selector

# TODO update the JSON string below
json = "{}"
# create an instance of Selector from a JSON string
selector_instance = Selector.from_json(json)
# print the JSON string representation of the object
print(Selector.to_json())

# convert the object into a dict
selector_dict = selector_instance.to_dict()
# create an instance of Selector from a dict
selector_from_dict = Selector.from_dict(selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Argument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the name of the argument | 
**description** | **str** | the description of the argument | [optional] 
**type** | **str** | the programmatic type of the argument | [optional] 

## Example

```python
from sailpoint.beta.models.argument import Argument

# TODO update the JSON string below
json = "{}"
# create an instance of Argument from a JSON string
argument_instance = Argument.from_json(json)
# print the JSON string representation of the object
print Argument.to_json()

# convert the object into a dict
argument_dict = argument_instance.to_dict()
# create an instance of Argument from a dict
argument_form_dict = argument.from_dict(argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



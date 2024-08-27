# AttributeChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the attribute name | [optional] 
**previous_value** | **str** | the old value of attribute | [optional] 
**new_value** | **str** | the new value of attribute | [optional] 

## Example

```python
from sailpoint.v2024.models.attribute_change import AttributeChange

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeChange from a JSON string
attribute_change_instance = AttributeChange.from_json(json)
# print the JSON string representation of the object
print(AttributeChange.to_json())

# convert the object into a dict
attribute_change_dict = attribute_change_instance.to_dict()
# create an instance of AttributeChange from a dict
attribute_change_from_dict = AttributeChange.from_dict(attribute_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



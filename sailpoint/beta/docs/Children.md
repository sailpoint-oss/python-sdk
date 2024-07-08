# Children


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | [optional] 
**attribute** | **str** |  | [optional] 
**value** | [**Value**](Value.md) |  | [optional] 
**children** | **str** |  | [optional] 

## Example

```python
from sailpoint.beta.models.children import Children

# TODO update the JSON string below
json = "{}"
# create an instance of Children from a JSON string
children_instance = Children.from_json(json)
# print the JSON string representation of the object
print Children.to_json()

# convert the object into a dict
children_dict = children_instance.to_dict()
# create an instance of Children from a dict
children_form_dict = children.from_dict(children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



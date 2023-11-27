# FormItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the FormItem | [optional] 

## Example

```python
from sailpoint.beta.models.form_item import FormItem

# TODO update the JSON string below
json = "{}"
# create an instance of FormItem from a JSON string
form_item_instance = FormItem.from_json(json)
# print the JSON string representation of the object
print FormItem.to_json()

# convert the object into a dict
form_item_dict = form_item_instance.to_dict()
# create an instance of FormItem from a dict
form_item_form_dict = form_item.from_dict(form_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FormItemDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the FormItem | [optional] 

## Example

```python
from sailpoint.v3.models.form_item_details import FormItemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FormItemDetails from a JSON string
form_item_details_instance = FormItemDetails.from_json(json)
# print the JSON string representation of the object
print(FormItemDetails.to_json())

# convert the object into a dict
form_item_details_dict = form_item_details_instance.to_dict()
# create an instance of FormItemDetails from a dict
form_item_details_from_dict = FormItemDetails.from_dict(form_item_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



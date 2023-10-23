# FormUsedBy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is a unique identifier | [optional] 
**type** | **str** | Type is a FormUsedByType value WORKFLOW FormUsedByTypeWorkflow SOURCE FormUsedByTypeSource | [optional] 

## Example

```python
from beta.models.form_used_by import FormUsedBy

# TODO update the JSON string below
json = "{}"
# create an instance of FormUsedBy from a JSON string
form_used_by_instance = FormUsedBy.from_json(json)
# print the JSON string representation of the object
print FormUsedBy.to_json()

# convert the object into a dict
form_used_by_dict = form_used_by_instance.to_dict()
# create an instance of FormUsedBy from a dict
form_used_by_form_dict = form_used_by.from_dict(form_used_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



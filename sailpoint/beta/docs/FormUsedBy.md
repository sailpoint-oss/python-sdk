# FormUsedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | FormUsedByType value.  WORKFLOW FormUsedByTypeWorkflow SOURCE FormUsedByTypeSource MySailPoint FormUsedByType | [optional] 
**id** | **str** | Unique identifier of the system using the form. | [optional] 
**name** | **str** | Name of the system using the form. | [optional] 

## Example

```python
from sailpoint.beta.models.form_used_by import FormUsedBy

# TODO update the JSON string below
json = "{}"
# create an instance of FormUsedBy from a JSON string
form_used_by_instance = FormUsedBy.from_json(json)
# print the JSON string representation of the object
print(FormUsedBy.to_json())

# convert the object into a dict
form_used_by_dict = form_used_by_instance.to_dict()
# create an instance of FormUsedBy from a dict
form_used_by_from_dict = FormUsedBy.from_dict(form_used_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



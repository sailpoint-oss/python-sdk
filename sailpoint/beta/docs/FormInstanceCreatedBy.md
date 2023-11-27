# FormInstanceCreatedBy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is a unique identifier | [optional] 
**type** | **str** | Type is a form instance created by type enum value WORKFLOW_EXECUTION FormInstanceCreatedByTypeWorkflowExecution SOURCE FormInstanceCreatedByTypeSource | [optional] 

## Example

```python
from sailpoint.beta.models.form_instance_created_by import FormInstanceCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of FormInstanceCreatedBy from a JSON string
form_instance_created_by_instance = FormInstanceCreatedBy.from_json(json)
# print the JSON string representation of the object
print FormInstanceCreatedBy.to_json()

# convert the object into a dict
form_instance_created_by_dict = form_instance_created_by_instance.to_dict()
# create an instance of FormInstanceCreatedBy from a dict
form_instance_created_by_form_dict = form_instance_created_by.from_dict(form_instance_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



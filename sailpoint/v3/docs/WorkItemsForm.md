# WorkItemsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the form | [optional] 
**name** | **str** | Name of the form | [optional] 
**title** | **str** | The form title | [optional] 
**subtitle** | **str** | The form subtitle. | [optional] 
**target_user** | **str** | The name of the user that should be shown this form | [optional] 
**sections** | [**List[SectionDetails]**](SectionDetails.md) | Sections of the form | [optional] 

## Example

```python
from sailpoint.v3.models.work_items_form import WorkItemsForm

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemsForm from a JSON string
work_items_form_instance = WorkItemsForm.from_json(json)
# print the JSON string representation of the object
print(WorkItemsForm.to_json())

# convert the object into a dict
work_items_form_dict = work_items_form_instance.to_dict()
# create an instance of WorkItemsForm from a dict
work_items_form_from_dict = WorkItemsForm.from_dict(work_items_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# WorkflowBodyOwner

The identity that owns the workflow.  The owner's permissions in IDN will determine what actions the workflow is allowed to perform.  Ownership can be changed by updating the owner in a PUT or PATCH request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object that is referenced | [optional] 
**id** | **str** | The unique ID of the object | [optional] 
**name** | **str** | The name of the object | [optional] 

## Example

```python
from sailpoint.beta.models.workflow_body_owner import WorkflowBodyOwner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowBodyOwner from a JSON string
workflow_body_owner_instance = WorkflowBodyOwner.from_json(json)
# print the JSON string representation of the object
print WorkflowBodyOwner.to_json()

# convert the object into a dict
workflow_body_owner_dict = workflow_body_owner_instance.to_dict()
# create an instance of WorkflowBodyOwner from a dict
workflow_body_owner_form_dict = workflow_body_owner.from_dict(workflow_body_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



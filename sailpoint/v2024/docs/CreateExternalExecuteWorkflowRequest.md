# CreateExternalExecuteWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **object** | The input for the workflow | [optional] 

## Example

```python
from sailpoint.v2024.models.create_external_execute_workflow_request import CreateExternalExecuteWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExternalExecuteWorkflowRequest from a JSON string
create_external_execute_workflow_request_instance = CreateExternalExecuteWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print(CreateExternalExecuteWorkflowRequest.to_json())

# convert the object into a dict
create_external_execute_workflow_request_dict = create_external_execute_workflow_request_instance.to_dict()
# create an instance of CreateExternalExecuteWorkflowRequest from a dict
create_external_execute_workflow_request_from_dict = CreateExternalExecuteWorkflowRequest.from_dict(create_external_execute_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



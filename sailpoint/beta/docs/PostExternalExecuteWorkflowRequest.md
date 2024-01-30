# PostExternalExecuteWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **object** | The input for the workflow | [optional] 

## Example

```python
from sailpoint.beta.models.post_external_execute_workflow_request import PostExternalExecuteWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostExternalExecuteWorkflowRequest from a JSON string
post_external_execute_workflow_request_instance = PostExternalExecuteWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print PostExternalExecuteWorkflowRequest.to_json()

# convert the object into a dict
post_external_execute_workflow_request_dict = post_external_execute_workflow_request_instance.to_dict()
# create an instance of PostExternalExecuteWorkflowRequest from a dict
post_external_execute_workflow_request_form_dict = post_external_execute_workflow_request.from_dict(post_external_execute_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



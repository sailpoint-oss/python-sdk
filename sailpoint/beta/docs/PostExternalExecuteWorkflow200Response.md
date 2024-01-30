# PostExternalExecuteWorkflow200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_execution_id** | **str** | The workflow execution id | [optional] 
**message** | **str** | An error message if any errors occurred | [optional] 

## Example

```python
from sailpoint.beta.models.post_external_execute_workflow200_response import PostExternalExecuteWorkflow200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostExternalExecuteWorkflow200Response from a JSON string
post_external_execute_workflow200_response_instance = PostExternalExecuteWorkflow200Response.from_json(json)
# print the JSON string representation of the object
print PostExternalExecuteWorkflow200Response.to_json()

# convert the object into a dict
post_external_execute_workflow200_response_dict = post_external_execute_workflow200_response_instance.to_dict()
# create an instance of PostExternalExecuteWorkflow200Response from a dict
post_external_execute_workflow200_response_form_dict = post_external_execute_workflow200_response.from_dict(post_external_execute_workflow200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



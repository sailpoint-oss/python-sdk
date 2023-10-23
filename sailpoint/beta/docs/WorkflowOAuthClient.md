# WorkflowOAuthClient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | OAuth client ID for the trigger. This is a UUID generated upon creation. | [optional] 
**secret** | **str** | OAuthClient secret. | [optional] 
**url** | **str** | URL for the external trigger to invoke | [optional] 

## Example

```python
from beta.models.workflow_o_auth_client import WorkflowOAuthClient

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowOAuthClient from a JSON string
workflow_o_auth_client_instance = WorkflowOAuthClient.from_json(json)
# print the JSON string representation of the object
print WorkflowOAuthClient.to_json()

# convert the object into a dict
workflow_o_auth_client_dict = workflow_o_auth_client_instance.to_dict()
# create an instance of WorkflowOAuthClient from a dict
workflow_o_auth_client_form_dict = workflow_o_auth_client.from_dict(workflow_o_auth_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateFormInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | [**FormInstanceCreatedBy**](FormInstanceCreatedBy.md) |  | 
**expire** | **str** | Expire is required | 
**form_definition_id** | **str** | FormDefinitionID is the id of the form definition that created this form | 
**form_input** | **Dict[str, object]** | FormInput is an object of form input labels to value | [optional] 
**recipients** | [**List[FormInstanceRecipient]**](FormInstanceRecipient.md) | Recipients is required | 
**stand_alone_form** | **bool** | StandAloneForm is a boolean flag to indicate if this form should be available for users to complete via the standalone form UI or should this only be available to be completed by as an embedded form | [optional] [default to False]
**state** | **str** | State is required, if not present initial state is FormInstanceStateAssigned ASSIGNED FormInstanceStateAssigned IN_PROGRESS FormInstanceStateInProgress SUBMITTED FormInstanceStateSubmitted COMPLETED FormInstanceStateCompleted CANCELLED FormInstanceStateCancelled | [optional] 
**ttl** | **int** | TTL an epoch timestamp in seconds, it most be in seconds or dynamodb will ignore it SEE: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/time-to-live-ttl-before-you-start.html | [optional] 

## Example

```python
from sailpoint.beta.models.create_form_instance_request import CreateFormInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFormInstanceRequest from a JSON string
create_form_instance_request_instance = CreateFormInstanceRequest.from_json(json)
# print the JSON string representation of the object
print CreateFormInstanceRequest.to_json()

# convert the object into a dict
create_form_instance_request_dict = create_form_instance_request_instance.to_dict()
# create an instance of CreateFormInstanceRequest from a dict
create_form_instance_request_form_dict = create_form_instance_request.from_dict(create_form_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



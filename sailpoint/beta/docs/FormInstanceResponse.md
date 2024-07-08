# FormInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Created is the date the form instance was assigned | [optional] 
**created_by** | [**FormInstanceCreatedBy**](FormInstanceCreatedBy.md) |  | [optional] 
**expire** | **str** | Expire is the maximum amount of time that a form can be in progress. After this time is reached then the form will be moved to a CANCELED state automatically. The user will no longer be able to complete the submission. When a form instance is expires an audit log will be generated for that record | [optional] 
**form_conditions** | [**List[FormCondition]**](FormCondition.md) | FormConditions is the conditional logic that modify the form dynamically modify the form as the recipient is interacting out the form | [optional] 
**form_data** | **Dict[str, object]** | FormData is the data provided by the form on submit. The data is in a key -&gt; value map | [optional] 
**form_definition_id** | **str** | FormDefinitionID is the id of the form definition that created this form | [optional] 
**form_elements** | [**List[FormElement]**](FormElement.md) | FormElements is the configuration of the form, this would be a repeat of the fields from the form-config | [optional] 
**form_errors** | [**List[FormError]**](FormError.md) | FormErrors is an array of form validation errors from the last time the form instance was transitioned to the SUBMITTED state. If the form instance had validation errors then it would be moved to the IN PROGRESS state where the client can retrieve these errors | [optional] 
**form_input** | **Dict[str, object]** | FormInput is an object of form input labels to value | [optional] 
**id** | **str** | Unique guid identifying this form instance | [optional] 
**modified** | **datetime** | Modified is the last date the form instance was modified | [optional] 
**recipients** | [**List[FormInstanceRecipient]**](FormInstanceRecipient.md) | Recipients references to the recipient of a form. The recipients are those who are responsible for filling out a form and completing it | [optional] 
**stand_alone_form** | **bool** | StandAloneForm is a boolean flag to indicate if this form should be available for users to complete via the standalone form UI or should this only be available to be completed by as an embedded form | [optional] [default to False]
**stand_alone_form_url** | **str** | StandAloneFormURL is the URL where this form may be completed by the designated recipients using the standalone form UI | [optional] 
**state** | **str** | State the state of the form instance ASSIGNED FormInstanceStateAssigned IN_PROGRESS FormInstanceStateInProgress SUBMITTED FormInstanceStateSubmitted COMPLETED FormInstanceStateCompleted CANCELLED FormInstanceStateCancelled | [optional] 

## Example

```python
from sailpoint.beta.models.form_instance_response import FormInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FormInstanceResponse from a JSON string
form_instance_response_instance = FormInstanceResponse.from_json(json)
# print the JSON string representation of the object
print FormInstanceResponse.to_json()

# convert the object into a dict
form_instance_response_dict = form_instance_response_instance.to_dict()
# create an instance of FormInstanceResponse from a dict
form_instance_response_form_dict = form_instance_response.from_dict(form_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



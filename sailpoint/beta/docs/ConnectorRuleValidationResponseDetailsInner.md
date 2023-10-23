# ConnectorRuleValidationResponseDetailsInner

CodeErrorDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | **int** | The line number where the issue occurred | 
**column** | **int** | the column number where the issue occurred | 
**messsage** | **str** | a description of the issue in the code | [optional] 

## Example

```python
from beta.models.connector_rule_validation_response_details_inner import ConnectorRuleValidationResponseDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorRuleValidationResponseDetailsInner from a JSON string
connector_rule_validation_response_details_inner_instance = ConnectorRuleValidationResponseDetailsInner.from_json(json)
# print the JSON string representation of the object
print ConnectorRuleValidationResponseDetailsInner.to_json()

# convert the object into a dict
connector_rule_validation_response_details_inner_dict = connector_rule_validation_response_details_inner_instance.to_dict()
# create an instance of ConnectorRuleValidationResponseDetailsInner from a dict
connector_rule_validation_response_details_inner_form_dict = connector_rule_validation_response_details_inner.from_dict(connector_rule_validation_response_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ConnectorRuleValidationResponse

ConnectorRuleValidationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**details** | [**List[ConnectorRuleValidationResponseDetailsInner]**](ConnectorRuleValidationResponseDetailsInner.md) |  | 

## Example

```python
from sailpoint.v2024.models.connector_rule_validation_response import ConnectorRuleValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorRuleValidationResponse from a JSON string
connector_rule_validation_response_instance = ConnectorRuleValidationResponse.from_json(json)
# print the JSON string representation of the object
print ConnectorRuleValidationResponse.to_json()

# convert the object into a dict
connector_rule_validation_response_dict = connector_rule_validation_response_instance.to_dict()
# create an instance of ConnectorRuleValidationResponse from a dict
connector_rule_validation_response_form_dict = connector_rule_validation_response.from_dict(connector_rule_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



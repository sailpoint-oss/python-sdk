# ConnectorRuleResponse

ConnectorRuleResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the name of the rule | 
**description** | **str** | a description of the rule&#39;s purpose | [optional] 
**type** | **str** | the type of rule | 
**signature** | [**ConnectorRuleCreateRequestSignature**](ConnectorRuleCreateRequestSignature.md) |  | [optional] 
**source_code** | [**SourceCode**](SourceCode.md) |  | 
**attributes** | **object** | a map of string to objects | [optional] 
**id** | **str** | the ID of the rule | 
**created** | **str** | an ISO 8601 UTC timestamp when this rule was created | 
**modified** | **str** | an ISO 8601 UTC timestamp when this rule was last modified | [optional] 

## Example

```python
from sailpoint.v2024.models.connector_rule_response import ConnectorRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorRuleResponse from a JSON string
connector_rule_response_instance = ConnectorRuleResponse.from_json(json)
# print the JSON string representation of the object
print ConnectorRuleResponse.to_json()

# convert the object into a dict
connector_rule_response_dict = connector_rule_response_instance.to_dict()
# create an instance of ConnectorRuleResponse from a dict
connector_rule_response_form_dict = connector_rule_response.from_dict(connector_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



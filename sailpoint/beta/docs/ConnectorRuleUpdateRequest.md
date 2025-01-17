# ConnectorRuleUpdateRequest

ConnectorRuleUpdateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the name of the rule | 
**description** | **str** | a description of the rule&#39;s purpose | [optional] 
**type** | **str** | the type of rule | 
**signature** | [**ConnectorRuleCreateRequestSignature**](ConnectorRuleCreateRequestSignature.md) |  | [optional] 
**source_code** | [**SourceCode**](SourceCode.md) |  | 
**attributes** | **object** | a map of string to objects | [optional] 
**id** | **str** | the ID of the rule to update | 

## Example

```python
from sailpoint.beta.models.connector_rule_update_request import ConnectorRuleUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorRuleUpdateRequest from a JSON string
connector_rule_update_request_instance = ConnectorRuleUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ConnectorRuleUpdateRequest.to_json())

# convert the object into a dict
connector_rule_update_request_dict = connector_rule_update_request_instance.to_dict()
# create an instance of ConnectorRuleUpdateRequest from a dict
connector_rule_update_request_from_dict = ConnectorRuleUpdateRequest.from_dict(connector_rule_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



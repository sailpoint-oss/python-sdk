# ConnectorRuleCreateRequestSignature

The rule's function signature. Describes the rule's input arguments and output (if any)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**List[Argument]**](Argument.md) |  | 
**output** | [**Argument**](Argument.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.connector_rule_create_request_signature import ConnectorRuleCreateRequestSignature

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorRuleCreateRequestSignature from a JSON string
connector_rule_create_request_signature_instance = ConnectorRuleCreateRequestSignature.from_json(json)
# print the JSON string representation of the object
print(ConnectorRuleCreateRequestSignature.to_json())

# convert the object into a dict
connector_rule_create_request_signature_dict = connector_rule_create_request_signature_instance.to_dict()
# create an instance of ConnectorRuleCreateRequestSignature from a dict
connector_rule_create_request_signature_from_dict = ConnectorRuleCreateRequestSignature.from_dict(connector_rule_create_request_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



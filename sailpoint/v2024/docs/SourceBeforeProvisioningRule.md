# SourceBeforeProvisioningRule

Rule that runs on the CCG and allows for customization of provisioning plans before the API calls the connector. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Rule ID. | [optional] 
**name** | **str** | Rule&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.v2024.models.source_before_provisioning_rule import SourceBeforeProvisioningRule

# TODO update the JSON string below
json = "{}"
# create an instance of SourceBeforeProvisioningRule from a JSON string
source_before_provisioning_rule_instance = SourceBeforeProvisioningRule.from_json(json)
# print the JSON string representation of the object
print(SourceBeforeProvisioningRule.to_json())

# convert the object into a dict
source_before_provisioning_rule_dict = source_before_provisioning_rule_instance.to_dict()
# create an instance of SourceBeforeProvisioningRule from a dict
source_before_provisioning_rule_from_dict = SourceBeforeProvisioningRule.from_dict(source_before_provisioning_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



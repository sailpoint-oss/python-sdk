# MultiHostSourcesBeforeProvisioningRule

Rule that runs on the CCG and allows for customization of provisioning plans before the API calls the connector. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Rule ID. | [optional] 
**name** | **str** | Rule&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_sources_before_provisioning_rule import MultiHostSourcesBeforeProvisioningRule

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostSourcesBeforeProvisioningRule from a JSON string
multi_host_sources_before_provisioning_rule_instance = MultiHostSourcesBeforeProvisioningRule.from_json(json)
# print the JSON string representation of the object
print(MultiHostSourcesBeforeProvisioningRule.to_json())

# convert the object into a dict
multi_host_sources_before_provisioning_rule_dict = multi_host_sources_before_provisioning_rule_instance.to_dict()
# create an instance of MultiHostSourcesBeforeProvisioningRule from a dict
multi_host_sources_before_provisioning_rule_from_dict = MultiHostSourcesBeforeProvisioningRule.from_dict(multi_host_sources_before_provisioning_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



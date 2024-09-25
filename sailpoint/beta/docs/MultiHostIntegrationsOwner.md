# MultiHostIntegrationsOwner

Reference to identity object who owns the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Owner identity&#39;s ID. | [optional] 
**name** | **str** | Owner identity&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_integrations_owner import MultiHostIntegrationsOwner

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostIntegrationsOwner from a JSON string
multi_host_integrations_owner_instance = MultiHostIntegrationsOwner.from_json(json)
# print the JSON string representation of the object
print(MultiHostIntegrationsOwner.to_json())

# convert the object into a dict
multi_host_integrations_owner_dict = multi_host_integrations_owner_instance.to_dict()
# create an instance of MultiHostIntegrationsOwner from a dict
multi_host_integrations_owner_from_dict = MultiHostIntegrationsOwner.from_dict(multi_host_integrations_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



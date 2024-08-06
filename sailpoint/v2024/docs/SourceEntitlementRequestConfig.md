# SourceEntitlementRequestConfig

Entitlement Request Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_config** | [**EntitlementAccessRequestConfig**](EntitlementAccessRequestConfig.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.source_entitlement_request_config import SourceEntitlementRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SourceEntitlementRequestConfig from a JSON string
source_entitlement_request_config_instance = SourceEntitlementRequestConfig.from_json(json)
# print the JSON string representation of the object
print SourceEntitlementRequestConfig.to_json()

# convert the object into a dict
source_entitlement_request_config_dict = source_entitlement_request_config_instance.to_dict()
# create an instance of SourceEntitlementRequestConfig from a dict
source_entitlement_request_config_form_dict = source_entitlement_request_config.from_dict(source_entitlement_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# EntitlementRequestConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_config** | [**EntitlementAccessRequestConfig**](EntitlementAccessRequestConfig.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.entitlement_request_config import EntitlementRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementRequestConfig from a JSON string
entitlement_request_config_instance = EntitlementRequestConfig.from_json(json)
# print the JSON string representation of the object
print EntitlementRequestConfig.to_json()

# convert the object into a dict
entitlement_request_config_dict = entitlement_request_config_instance.to_dict()
# create an instance of EntitlementRequestConfig from a dict
entitlement_request_config_form_dict = entitlement_request_config.from_dict(entitlement_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



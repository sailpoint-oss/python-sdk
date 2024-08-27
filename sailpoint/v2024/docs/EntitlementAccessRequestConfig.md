# EntitlementAccessRequestConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_schemes** | [**List[EntitlementApprovalScheme]**](EntitlementApprovalScheme.md) | Ordered list of approval steps for the access request. Empty when no approval is required. | [optional] 
**request_comment_required** | **bool** | If the requester must provide a comment during access request. | [optional] [default to False]
**denial_comment_required** | **bool** | If the reviewer must provide a comment when denying the access request. | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.entitlement_access_request_config import EntitlementAccessRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementAccessRequestConfig from a JSON string
entitlement_access_request_config_instance = EntitlementAccessRequestConfig.from_json(json)
# print the JSON string representation of the object
print(EntitlementAccessRequestConfig.to_json())

# convert the object into a dict
entitlement_access_request_config_dict = entitlement_access_request_config_instance.to_dict()
# create an instance of EntitlementAccessRequestConfig from a dict
entitlement_access_request_config_from_dict = EntitlementAccessRequestConfig.from_dict(entitlement_access_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



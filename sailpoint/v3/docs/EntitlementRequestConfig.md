# EntitlementRequestConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_entitlement_request** | **bool** | If this is true, entitlement requests are allowed. | [optional] [default to False]
**request_comments_required** | **bool** | If this is true, comments are required to submit entitlement requests. | [optional] [default to False]
**denied_comments_required** | **bool** | If this is true, comments are required to reject entitlement requests. | [optional] [default to False]
**grant_request_approval_schemes** | **str** | Approval schemes for granting entitlement request. This can be empty if no approval is needed. Multiple schemes must be comma-separated. The valid schemes are \&quot;entitlementOwner\&quot;, \&quot;sourceOwner\&quot;, \&quot;manager\&quot; and \&quot;&#x60;workgroup:{id}&#x60;\&quot;. You can use multiple governance groups (workgroups).  | [optional] [default to 'sourceOwner']

## Example

```python
from sailpoint.v3.models.entitlement_request_config import EntitlementRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementRequestConfig from a JSON string
entitlement_request_config_instance = EntitlementRequestConfig.from_json(json)
# print the JSON string representation of the object
print(EntitlementRequestConfig.to_json())

# convert the object into a dict
entitlement_request_config_dict = entitlement_request_config_instance.to_dict()
# create an instance of EntitlementRequestConfig from a dict
entitlement_request_config_from_dict = EntitlementRequestConfig.from_dict(entitlement_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



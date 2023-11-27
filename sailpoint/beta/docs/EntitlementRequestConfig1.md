# EntitlementRequestConfig1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_entitlement_request** | **bool** | Flag for allowing entitlement request. | [optional] 
**request_comments_required** | **bool** | Flag for requiring comments while submitting an entitlement request. | [optional] [default to False]
**denied_comments_required** | **bool** | Flag for requiring comments while rejecting an entitlement request. | [optional] [default to False]
**grant_request_approval_schemes** | **str** | Approval schemes for granting entitlement request. This can be empty if no approval is needed. Multiple schemes must be comma-separated. The valid schemes are \&quot;entitlementOwner\&quot;, \&quot;sourceOwner\&quot;, \&quot;manager\&quot; and \&quot;workgroup:{id}\&quot;. Multiple workgroups (governance groups) can be used.  | [optional] [default to 'sourceOwner']

## Example

```python
from sailpoint.beta.models.entitlement_request_config1 import EntitlementRequestConfig1

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementRequestConfig1 from a JSON string
entitlement_request_config1_instance = EntitlementRequestConfig1.from_json(json)
# print the JSON string representation of the object
print EntitlementRequestConfig1.to_json()

# convert the object into a dict
entitlement_request_config1_dict = entitlement_request_config1_instance.to_dict()
# create an instance of EntitlementRequestConfig1 from a dict
entitlement_request_config1_form_dict = entitlement_request_config1.from_dict(entitlement_request_config1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MultiHostSourcesPasswordPoliciesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Policy ID. | [optional] 
**name** | **str** | Policy&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_sources_password_policies_inner import MultiHostSourcesPasswordPoliciesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostSourcesPasswordPoliciesInner from a JSON string
multi_host_sources_password_policies_inner_instance = MultiHostSourcesPasswordPoliciesInner.from_json(json)
# print the JSON string representation of the object
print(MultiHostSourcesPasswordPoliciesInner.to_json())

# convert the object into a dict
multi_host_sources_password_policies_inner_dict = multi_host_sources_password_policies_inner_instance.to_dict()
# create an instance of MultiHostSourcesPasswordPoliciesInner from a dict
multi_host_sources_password_policies_inner_from_dict = MultiHostSourcesPasswordPoliciesInner.from_dict(multi_host_sources_password_policies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SourcePasswordPoliciesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Policy ID. | [optional] 
**name** | **str** | Policy&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.v3.models.source_password_policies_inner import SourcePasswordPoliciesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SourcePasswordPoliciesInner from a JSON string
source_password_policies_inner_instance = SourcePasswordPoliciesInner.from_json(json)
# print the JSON string representation of the object
print SourcePasswordPoliciesInner.to_json()

# convert the object into a dict
source_password_policies_inner_dict = source_password_policies_inner_instance.to_dict()
# create an instance of SourcePasswordPoliciesInner from a dict
source_password_policies_inner_form_dict = source_password_policies_inner.from_dict(source_password_policies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



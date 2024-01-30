# IdentityAttributesChangedChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | The name of the identity attribute that changed. | 
**old_value** | [**IdentityAttributesChangedChangesInnerOldValue**](IdentityAttributesChangedChangesInnerOldValue.md) |  | [optional] 
**new_value** | [**IdentityAttributesChangedChangesInnerNewValue**](IdentityAttributesChangedChangesInnerNewValue.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.identity_attributes_changed_changes_inner import IdentityAttributesChangedChangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttributesChangedChangesInner from a JSON string
identity_attributes_changed_changes_inner_instance = IdentityAttributesChangedChangesInner.from_json(json)
# print the JSON string representation of the object
print IdentityAttributesChangedChangesInner.to_json()

# convert the object into a dict
identity_attributes_changed_changes_inner_dict = identity_attributes_changed_changes_inner_instance.to_dict()
# create an instance of IdentityAttributesChangedChangesInner from a dict
identity_attributes_changed_changes_inner_form_dict = identity_attributes_changed_changes_inner.from_dict(identity_attributes_changed_changes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



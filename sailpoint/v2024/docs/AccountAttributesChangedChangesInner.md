# AccountAttributesChangedChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | The name of the attribute. | 
**old_value** | [**AccountAttributesChangedChangesInnerOldValue**](AccountAttributesChangedChangesInnerOldValue.md) |  | 
**new_value** | [**AccountAttributesChangedChangesInnerNewValue**](AccountAttributesChangedChangesInnerNewValue.md) |  | 

## Example

```python
from sailpoint.v2024.models.account_attributes_changed_changes_inner import AccountAttributesChangedChangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAttributesChangedChangesInner from a JSON string
account_attributes_changed_changes_inner_instance = AccountAttributesChangedChangesInner.from_json(json)
# print the JSON string representation of the object
print(AccountAttributesChangedChangesInner.to_json())

# convert the object into a dict
account_attributes_changed_changes_inner_dict = account_attributes_changed_changes_inner_instance.to_dict()
# create an instance of AccountAttributesChangedChangesInner from a dict
account_attributes_changed_changes_inner_from_dict = AccountAttributesChangedChangesInner.from_dict(account_attributes_changed_changes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



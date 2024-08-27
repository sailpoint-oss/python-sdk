# AccountAttributesChangedSource

The source that contains the account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the object to which this reference applies | 
**type** | **str** | The type of object that is referenced | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from sailpoint.beta.models.account_attributes_changed_source import AccountAttributesChangedSource

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAttributesChangedSource from a JSON string
account_attributes_changed_source_instance = AccountAttributesChangedSource.from_json(json)
# print the JSON string representation of the object
print(AccountAttributesChangedSource.to_json())

# convert the object into a dict
account_attributes_changed_source_dict = account_attributes_changed_source_instance.to_dict()
# create an instance of AccountAttributesChangedSource from a dict
account_attributes_changed_source_from_dict = AccountAttributesChangedSource.from_dict(account_attributes_changed_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



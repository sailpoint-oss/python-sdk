# AccountAttributesCreateAttributes

The schema attribute values for the account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | Target source to create an account | 

## Example

```python
from sailpoint.beta.models.account_attributes_create_attributes import AccountAttributesCreateAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAttributesCreateAttributes from a JSON string
account_attributes_create_attributes_instance = AccountAttributesCreateAttributes.from_json(json)
# print the JSON string representation of the object
print AccountAttributesCreateAttributes.to_json()

# convert the object into a dict
account_attributes_create_attributes_dict = account_attributes_create_attributes_instance.to_dict()
# create an instance of AccountAttributesCreateAttributes from a dict
account_attributes_create_attributes_form_dict = account_attributes_create_attributes.from_dict(account_attributes_create_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AccountAttributesCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**AccountAttributesCreateAttributes**](AccountAttributesCreateAttributes.md) |  | 

## Example

```python
from sailpoint.beta.models.account_attributes_create import AccountAttributesCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAttributesCreate from a JSON string
account_attributes_create_instance = AccountAttributesCreate.from_json(json)
# print the JSON string representation of the object
print(AccountAttributesCreate.to_json())

# convert the object into a dict
account_attributes_create_dict = account_attributes_create_instance.to_dict()
# create an instance of AccountAttributesCreate from a dict
account_attributes_create_from_dict = AccountAttributesCreate.from_dict(account_attributes_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



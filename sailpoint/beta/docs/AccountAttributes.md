# AccountAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** | The schema attribute values for the account | 

## Example

```python
from sailpoint.beta.models.account_attributes import AccountAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAttributes from a JSON string
account_attributes_instance = AccountAttributes.from_json(json)
# print the JSON string representation of the object
print(AccountAttributes.to_json())

# convert the object into a dict
account_attributes_dict = account_attributes_instance.to_dict()
# create an instance of AccountAttributes from a dict
account_attributes_from_dict = AccountAttributes.from_dict(account_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



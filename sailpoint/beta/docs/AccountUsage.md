# AccountUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The first day of the month for which activity is aggregated. | [optional] 
**count** | **int** | The number of days within the month that the account was active in a source. | [optional] 

## Example

```python
from sailpoint.beta.models.account_usage import AccountUsage

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUsage from a JSON string
account_usage_instance = AccountUsage.from_json(json)
# print the JSON string representation of the object
print(AccountUsage.to_json())

# convert the object into a dict
account_usage_dict = account_usage_instance.to_dict()
# create an instance of AccountUsage from a dict
account_usage_from_dict = AccountUsage.from_dict(account_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AccessProfileDetailsAccountSelector

How to select account when there are multiple accounts for the user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selectors** | [**List[Selector]**](Selector.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.access_profile_details_account_selector import AccessProfileDetailsAccountSelector

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileDetailsAccountSelector from a JSON string
access_profile_details_account_selector_instance = AccessProfileDetailsAccountSelector.from_json(json)
# print the JSON string representation of the object
print(AccessProfileDetailsAccountSelector.to_json())

# convert the object into a dict
access_profile_details_account_selector_dict = access_profile_details_account_selector_instance.to_dict()
# create an instance of AccessProfileDetailsAccountSelector from a dict
access_profile_details_account_selector_from_dict = AccessProfileDetailsAccountSelector.from_dict(access_profile_details_account_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



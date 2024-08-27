# AccountAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Describes if action will be enabled or disabled | [optional] 
**source_ids** | **List[str]** | List of source IDs. The sources must have the ENABLE feature or flat file source. See \&quot;/sources\&quot; endpoint for source features. | [optional] 

## Example

```python
from sailpoint.beta.models.account_action import AccountAction

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAction from a JSON string
account_action_instance = AccountAction.from_json(json)
# print the JSON string representation of the object
print(AccountAction.to_json())

# convert the object into a dict
account_action_dict = account_action_instance.to_dict()
# create an instance of AccountAction from a dict
account_action_from_dict = AccountAction.from_dict(account_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



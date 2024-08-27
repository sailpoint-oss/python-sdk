# LifecycleState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Lifecycle state ID. | [optional] [readonly] 
**name** | **str** | Lifecycle state name. | [optional] [readonly] 
**technical_name** | **str** | Lifecycle state technical name. This is for internal use. | [optional] [readonly] 
**description** | **str** | Lifecycle state description. | [optional] 
**created** | **datetime** | Lifecycle state created date. | [optional] [readonly] 
**modified** | **datetime** | Lifecycle state modified date. | [optional] [readonly] 
**enabled** | **bool** | Indicates whether the lifecycle state is enabled or disabled. | [optional] [default to False]
**identity_count** | **int** | Number of identities that have the lifecycle state. | [optional] [readonly] 
**email_notification_option** | [**EmailNotificationOption**](EmailNotificationOption.md) |  | [optional] 
**account_actions** | [**List[AccountAction]**](AccountAction.md) |  | [optional] 
**access_profile_ids** | **List[str]** | List of access-profile IDs that are associated with the lifecycle state. | [optional] 

## Example

```python
from sailpoint.beta.models.lifecycle_state import LifecycleState

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleState from a JSON string
lifecycle_state_instance = LifecycleState.from_json(json)
# print the JSON string representation of the object
print(LifecycleState.to_json())

# convert the object into a dict
lifecycle_state_dict = lifecycle_state_instance.to_dict()
# create an instance of LifecycleState from a dict
lifecycle_state_from_dict = LifecycleState.from_dict(lifecycle_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



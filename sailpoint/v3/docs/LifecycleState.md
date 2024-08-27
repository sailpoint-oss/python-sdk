# LifecycleState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the Object | [optional] [readonly] 
**name** | **str** | Name of the Object | 
**created** | **datetime** | Creation date of the Object | [optional] [readonly] 
**modified** | **datetime** | Last modification date of the Object | [optional] [readonly] 
**enabled** | **bool** | Indicates whether the lifecycle state is enabled or disabled. | [optional] [default to False]
**technical_name** | **str** | The lifecycle state&#39;s technical name. This is for internal use. | 
**description** | **str** | Lifecycle state&#39;s description. | [optional] 
**identity_count** | **int** | Number of identities that have the lifecycle state. | [optional] [readonly] 
**email_notification_option** | [**EmailNotificationOption**](EmailNotificationOption.md) |  | [optional] 
**account_actions** | [**List[AccountAction]**](AccountAction.md) |  | [optional] 
**access_profile_ids** | **List[str]** | List of unique access-profile IDs that are associated with the lifecycle state. | [optional] 
**identity_state** | **str** | The lifecycle state&#39;s associated identity state. This field is generally &#39;null&#39;. | [optional] 

## Example

```python
from sailpoint.v3.models.lifecycle_state import LifecycleState

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



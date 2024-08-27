# ManagedClientStatus

Managed Client Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **object** | ManagedClientStatus body information | 
**status** | [**ManagedClientStatusEnum**](ManagedClientStatusEnum.md) |  | 
**type** | [**ManagedClientType**](ManagedClientType.md) |  | 
**timestamp** | **datetime** | timestamp on the Client Status update | 

## Example

```python
from sailpoint.beta.models.managed_client_status import ManagedClientStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedClientStatus from a JSON string
managed_client_status_instance = ManagedClientStatus.from_json(json)
# print the JSON string representation of the object
print(ManagedClientStatus.to_json())

# convert the object into a dict
managed_client_status_dict = managed_client_status_instance.to_dict()
# create an instance of ManagedClientStatus from a dict
managed_client_status_from_dict = ManagedClientStatus.from_dict(managed_client_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



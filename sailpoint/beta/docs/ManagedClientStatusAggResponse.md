# ManagedClientStatusAggResponse

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
from sailpoint.beta.models.managed_client_status_agg_response import ManagedClientStatusAggResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedClientStatusAggResponse from a JSON string
managed_client_status_agg_response_instance = ManagedClientStatusAggResponse.from_json(json)
# print the JSON string representation of the object
print(ManagedClientStatusAggResponse.to_json())

# convert the object into a dict
managed_client_status_agg_response_dict = managed_client_status_agg_response_instance.to_dict()
# create an instance of ManagedClientStatusAggResponse from a dict
managed_client_status_agg_response_from_dict = ManagedClientStatusAggResponse.from_dict(managed_client_status_agg_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



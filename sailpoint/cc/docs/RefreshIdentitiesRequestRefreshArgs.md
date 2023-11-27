# RefreshIdentitiesRequestRefreshArgs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlate_entitlements** | **bool** | This will refresh entitlement, role, and access profile calculations. | [optional] 
**promote_attributes** | **bool** | This will calculate identity attributes. | [optional] 
**refresh_manager_status** | **bool** | This recalculates manager correlation and manager status. Note: This is computationally expensive to run.  | [optional] 
**synchronize_attributes** | **bool** | Enables attribute synchronization. | [optional] 
**prune_identities** | **bool** | Option that will enable deletion of an identity objects if there are no account objects. Note: This is not typically used in IdentityNow, except by guidance from SailPoint.  | [optional] 
**provision** | **bool** | Enables provisioning of role assignments with entitlements that are not currently fulfilled. | [optional] 

## Example

```python
from sailpoint.cc.models.refresh_identities_request_refresh_args import RefreshIdentitiesRequestRefreshArgs

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshIdentitiesRequestRefreshArgs from a JSON string
refresh_identities_request_refresh_args_instance = RefreshIdentitiesRequestRefreshArgs.from_json(json)
# print the JSON string representation of the object
print RefreshIdentitiesRequestRefreshArgs.to_json()

# convert the object into a dict
refresh_identities_request_refresh_args_dict = refresh_identities_request_refresh_args_instance.to_dict()
# create an instance of RefreshIdentitiesRequestRefreshArgs from a dict
refresh_identities_request_refresh_args_form_dict = refresh_identities_request_refresh_args.from_dict(refresh_identities_request_refresh_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



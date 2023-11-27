# RefreshIdentitiesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Defines the identity or identities which this refresh applies to. The filter must use searchable identity attributes. If the filter cannot be understood or parsed, all identities will be refreshed.  | [optional] 
**refresh_args** | [**RefreshIdentitiesRequestRefreshArgs**](RefreshIdentitiesRequestRefreshArgs.md) |  | [optional] 

## Example

```python
from sailpoint.cc.models.refresh_identities_request import RefreshIdentitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshIdentitiesRequest from a JSON string
refresh_identities_request_instance = RefreshIdentitiesRequest.from_json(json)
# print the JSON string representation of the object
print RefreshIdentitiesRequest.to_json()

# convert the object into a dict
refresh_identities_request_dict = refresh_identities_request_instance.to_dict()
# create an instance of RefreshIdentitiesRequest from a dict
refresh_identities_request_form_dict = refresh_identities_request.from_dict(refresh_identities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



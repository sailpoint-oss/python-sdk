# IdentitiesAccountsBulkRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_ids** | **List[str]** | The ids of the identities for which enable/disable accounts. | [optional] 

## Example

```python
from beta.models.identities_accounts_bulk_request import IdentitiesAccountsBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentitiesAccountsBulkRequest from a JSON string
identities_accounts_bulk_request_instance = IdentitiesAccountsBulkRequest.from_json(json)
# print the JSON string representation of the object
print IdentitiesAccountsBulkRequest.to_json()

# convert the object into a dict
identities_accounts_bulk_request_dict = identities_accounts_bulk_request_instance.to_dict()
# create an instance of IdentitiesAccountsBulkRequest from a dict
identities_accounts_bulk_request_form_dict = identities_accounts_bulk_request.from_dict(identities_accounts_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



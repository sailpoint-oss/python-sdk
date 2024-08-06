# BulkIdentitiesAccountsResponse

Bulk response object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of bulk request item. | [optional] 
**status_code** | **int** | Response status value. | [optional] 
**message** | **str** | Status containing additional context information about failures. | [optional] 

## Example

```python
from sailpoint.v2024.models.bulk_identities_accounts_response import BulkIdentitiesAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkIdentitiesAccountsResponse from a JSON string
bulk_identities_accounts_response_instance = BulkIdentitiesAccountsResponse.from_json(json)
# print the JSON string representation of the object
print BulkIdentitiesAccountsResponse.to_json()

# convert the object into a dict
bulk_identities_accounts_response_dict = bulk_identities_accounts_response_instance.to_dict()
# create an instance of BulkIdentitiesAccountsResponse from a dict
bulk_identities_accounts_response_form_dict = bulk_identities_accounts_response.from_dict(bulk_identities_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ImportAccountsRequest1

This content type is provided for compatibility with services that don't support multipart/form-data, such as SailPoint Workflows. This content type does not support files, so it can only be used for direct connect sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_optimization** | **str** | Use this flag to reprocess every account whether or not the data has changed. | [optional] 

## Example

```python
from sailpoint.beta.models.import_accounts_request1 import ImportAccountsRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of ImportAccountsRequest1 from a JSON string
import_accounts_request1_instance = ImportAccountsRequest1.from_json(json)
# print the JSON string representation of the object
print ImportAccountsRequest1.to_json()

# convert the object into a dict
import_accounts_request1_dict = import_accounts_request1_instance.to_dict()
# create an instance of ImportAccountsRequest1 from a dict
import_accounts_request1_form_dict = import_accounts_request1.from_dict(import_accounts_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



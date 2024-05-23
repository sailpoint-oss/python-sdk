# ImportAccountsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | The CSV file containing the source accounts to aggregate. | [optional] 
**disable_optimization** | **str** | Use this flag to reprocess every account whether or not the data has changed. | [optional] 

## Example

```python
from sailpoint.beta.models.import_accounts_request import ImportAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportAccountsRequest from a JSON string
import_accounts_request_instance = ImportAccountsRequest.from_json(json)
# print the JSON string representation of the object
print ImportAccountsRequest.to_json()

# convert the object into a dict
import_accounts_request_dict = import_accounts_request_instance.to_dict()
# create an instance of ImportAccountsRequest from a dict
import_accounts_request_form_dict = import_accounts_request.from_dict(import_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



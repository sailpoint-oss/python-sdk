# ImportEntitlementCsvRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bytearray** |  | [optional] 

## Example

```python
from sailpoint.beta.models.import_entitlement_csv_request import ImportEntitlementCsvRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportEntitlementCsvRequest from a JSON string
import_entitlement_csv_request_instance = ImportEntitlementCsvRequest.from_json(json)
# print the JSON string representation of the object
print ImportEntitlementCsvRequest.to_json()

# convert the object into a dict
import_entitlement_csv_request_dict = import_entitlement_csv_request_instance.to_dict()
# create an instance of ImportEntitlementCsvRequest from a dict
import_entitlement_csv_request_form_dict = import_entitlement_csv_request.from_dict(import_entitlement_csv_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



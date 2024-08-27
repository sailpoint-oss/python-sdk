# ImportEntitlementsBySourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csv_file** | **bytearray** | The CSV file containing the source entitlements to aggregate. | [optional] 

## Example

```python
from sailpoint.beta.models.import_entitlements_by_source_request import ImportEntitlementsBySourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportEntitlementsBySourceRequest from a JSON string
import_entitlements_by_source_request_instance = ImportEntitlementsBySourceRequest.from_json(json)
# print the JSON string representation of the object
print(ImportEntitlementsBySourceRequest.to_json())

# convert the object into a dict
import_entitlements_by_source_request_dict = import_entitlements_by_source_request_instance.to_dict()
# create an instance of ImportEntitlementsBySourceRequest from a dict
import_entitlements_by_source_request_from_dict = ImportEntitlementsBySourceRequest.from_dict(import_entitlements_by_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ImportEntitlementsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | The CSV file containing the source entitlements to aggregate. | [optional] 

## Example

```python
from sailpoint.beta.models.import_entitlements_request import ImportEntitlementsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportEntitlementsRequest from a JSON string
import_entitlements_request_instance = ImportEntitlementsRequest.from_json(json)
# print the JSON string representation of the object
print ImportEntitlementsRequest.to_json()

# convert the object into a dict
import_entitlements_request_dict = import_entitlements_request_instance.to_dict()
# create an instance of ImportEntitlementsRequest from a dict
import_entitlements_request_form_dict = import_entitlements_request.from_dict(import_entitlements_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



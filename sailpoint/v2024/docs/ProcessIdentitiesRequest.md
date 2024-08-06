# ProcessIdentitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_ids** | **List[str]** | List of up to 250 identity IDs to process. | [optional] 

## Example

```python
from sailpoint.v2024.models.process_identities_request import ProcessIdentitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessIdentitiesRequest from a JSON string
process_identities_request_instance = ProcessIdentitiesRequest.from_json(json)
# print the JSON string representation of the object
print ProcessIdentitiesRequest.to_json()

# convert the object into a dict
process_identities_request_dict = process_identities_request_instance.to_dict()
# create an instance of ProcessIdentitiesRequest from a dict
process_identities_request_form_dict = process_identities_request.from_dict(process_identities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



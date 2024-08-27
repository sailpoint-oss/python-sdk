# AccessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_for** | **List[str]** | A list of Identity IDs for whom the Access is requested. If it&#39;s a Revoke request, there can only be one Identity ID. | 
**request_type** | [**AccessRequestType**](AccessRequestType.md) |  | [optional] 
**requested_items** | [**List[AccessRequestItem]**](AccessRequestItem.md) |  | 
**client_metadata** | **Dict[str, str]** | Arbitrary key-value pairs. They will never be processed by the IdentityNow system but will be returned on associated APIs such as /account-activities. | [optional] 

## Example

```python
from sailpoint.v2024.models.access_request import AccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequest from a JSON string
access_request_instance = AccessRequest.from_json(json)
# print the JSON string representation of the object
print(AccessRequest.to_json())

# convert the object into a dict
access_request_dict = access_request_instance.to_dict()
# create an instance of AccessRequest from a dict
access_request_from_dict = AccessRequest.from_dict(access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



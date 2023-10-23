# CloseAccessRequest

Request body payload for close access requests endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_ids** | **List[str]** | Access Request IDs for the requests to be closed. Accepts 1-500 Identity Request IDs per request. | 
**message** | **str** | Reason for closing the access request. Displayed under Warnings in IdentityNow. | [optional] [default to 'The IdentityNow Administrator manually closed this request.']
**execution_status** | **str** | The request&#39;s provisioning status. Displayed as Stage in IdentityNow. | [optional] [default to 'Terminated']
**completion_status** | **str** | The request&#39;s overall status. Displayed as Status in IdentityNow. | [optional] [default to 'Failure']

## Example

```python
from beta.models.close_access_request import CloseAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloseAccessRequest from a JSON string
close_access_request_instance = CloseAccessRequest.from_json(json)
# print the JSON string representation of the object
print CloseAccessRequest.to_json()

# convert the object into a dict
close_access_request_dict = close_access_request_instance.to_dict()
# create an instance of CloseAccessRequest from a dict
close_access_request_form_dict = close_access_request.from_dict(close_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AccessRequested


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request** | [**AccessRequestResponse**](AccessRequestResponse.md) |  | [optional] 
**identity_id** | **str** | the identity id | [optional] 
**event_type** | **str** | the event type | [optional] 
**dt** | **str** | the date of event | [optional] 

## Example

```python
from beta.models.access_requested import AccessRequested

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequested from a JSON string
access_requested_instance = AccessRequested.from_json(json)
# print the JSON string representation of the object
print AccessRequested.to_json()

# convert the object into a dict
access_requested_dict = access_requested_instance.to_dict()
# create an instance of AccessRequested from a dict
access_requested_form_dict = access_requested.from_dict(access_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



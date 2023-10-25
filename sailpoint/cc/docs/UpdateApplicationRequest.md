# UpdateApplicationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 

## Example

```python
from cc.models.update_application_request import UpdateApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApplicationRequest from a JSON string
update_application_request_instance = UpdateApplicationRequest.from_json(json)
# print the JSON string representation of the object
print UpdateApplicationRequest.to_json()

# convert the object into a dict
update_application_request_dict = update_application_request_instance.to_dict()
# create an instance of UpdateApplicationRequest from a dict
update_application_request_form_dict = update_application_request.from_dict(update_application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateApplicationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from sailpoint.cc.models.create_application_request import CreateApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApplicationRequest from a JSON string
create_application_request_instance = CreateApplicationRequest.from_json(json)
# print the JSON string representation of the object
print CreateApplicationRequest.to_json()

# convert the object into a dict
create_application_request_dict = create_application_request_instance.to_dict()
# create an instance of CreateApplicationRequest from a dict
create_application_request_form_dict = create_application_request.from_dict(create_application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



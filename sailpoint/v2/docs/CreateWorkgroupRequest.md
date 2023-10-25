# CreateWorkgroupRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**owner** | [**CreateWorkgroupRequestOwner**](CreateWorkgroupRequestOwner.md) |  | [optional] 

## Example

```python
from v2.models.create_workgroup_request import CreateWorkgroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkgroupRequest from a JSON string
create_workgroup_request_instance = CreateWorkgroupRequest.from_json(json)
# print the JSON string representation of the object
print CreateWorkgroupRequest.to_json()

# convert the object into a dict
create_workgroup_request_dict = create_workgroup_request_instance.to_dict()
# create an instance of CreateWorkgroupRequest from a dict
create_workgroup_request_form_dict = create_workgroup_request.from_dict(create_workgroup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



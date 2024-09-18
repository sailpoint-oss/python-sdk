# CreateUploadedConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bytearray** | JSON file containing the objects to be imported. | 
**name** | **str** | Name that will be assigned to the uploaded configuration file. | 

## Example

```python
from sailpoint.v2024.models.create_uploaded_configuration_request import CreateUploadedConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUploadedConfigurationRequest from a JSON string
create_uploaded_configuration_request_instance = CreateUploadedConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUploadedConfigurationRequest.to_json())

# convert the object into a dict
create_uploaded_configuration_request_dict = create_uploaded_configuration_request_instance.to_dict()
# create an instance of CreateUploadedConfigurationRequest from a dict
create_uploaded_configuration_request_from_dict = CreateUploadedConfigurationRequest.from_dict(create_uploaded_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ManualDiscoverApplications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | The CSV file to upload containing &#x60;application_name&#x60; and &#x60;description&#x60; columns. Each row represents an application to be discovered. | 

## Example

```python
from sailpoint.v3.models.manual_discover_applications import ManualDiscoverApplications

# TODO update the JSON string below
json = "{}"
# create an instance of ManualDiscoverApplications from a JSON string
manual_discover_applications_instance = ManualDiscoverApplications.from_json(json)
# print the JSON string representation of the object
print ManualDiscoverApplications.to_json()

# convert the object into a dict
manual_discover_applications_dict = manual_discover_applications_instance.to_dict()
# create an instance of ManualDiscoverApplications from a dict
manual_discover_applications_form_dict = manual_discover_applications.from_dict(manual_discover_applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



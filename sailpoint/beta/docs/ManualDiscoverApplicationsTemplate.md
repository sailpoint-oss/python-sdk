# ManualDiscoverApplicationsTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | Name of the example application. | [optional] 
**domain** | **str** | Description of the example application&#39;s domain. | [optional] 

## Example

```python
from sailpoint.beta.models.manual_discover_applications_template import ManualDiscoverApplicationsTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ManualDiscoverApplicationsTemplate from a JSON string
manual_discover_applications_template_instance = ManualDiscoverApplicationsTemplate.from_json(json)
# print the JSON string representation of the object
print ManualDiscoverApplicationsTemplate.to_json()

# convert the object into a dict
manual_discover_applications_template_dict = manual_discover_applications_template_instance.to_dict()
# create an instance of ManualDiscoverApplicationsTemplate from a dict
manual_discover_applications_template_form_dict = manual_discover_applications_template.from_dict(manual_discover_applications_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



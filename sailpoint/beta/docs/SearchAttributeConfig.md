# SearchAttributeConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the new attribute | [optional] 
**display_name** | **str** | The display name of the new attribute | [optional] 
**application_attributes** | **object** | Map of application id and their associated attribute. | [optional] 

## Example

```python
from sailpoint.beta.models.search_attribute_config import SearchAttributeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SearchAttributeConfig from a JSON string
search_attribute_config_instance = SearchAttributeConfig.from_json(json)
# print the JSON string representation of the object
print SearchAttributeConfig.to_json()

# convert the object into a dict
search_attribute_config_dict = search_attribute_config_instance.to_dict()
# create an instance of SearchAttributeConfig from a dict
search_attribute_config_form_dict = search_attribute_config.from_dict(search_attribute_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



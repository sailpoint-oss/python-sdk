# FormElementDynamicDataSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**FormElementDynamicDataSourceConfig**](FormElementDynamicDataSourceConfig.md) |  | [optional] 
**data_source_type** | **str** | DataSourceType is a FormElementDataSourceType value STATIC FormElementDataSourceTypeStatic INTERNAL FormElementDataSourceTypeInternal SEARCH FormElementDataSourceTypeSearch FORM_INPUT FormElementDataSourceTypeFormInput | [optional] 

## Example

```python
from sailpoint.beta.models.form_element_dynamic_data_source import FormElementDynamicDataSource

# TODO update the JSON string below
json = "{}"
# create an instance of FormElementDynamicDataSource from a JSON string
form_element_dynamic_data_source_instance = FormElementDynamicDataSource.from_json(json)
# print the JSON string representation of the object
print(FormElementDynamicDataSource.to_json())

# convert the object into a dict
form_element_dynamic_data_source_dict = form_element_dynamic_data_source_instance.to_dict()
# create an instance of FormElementDynamicDataSource from a dict
form_element_dynamic_data_source_from_dict = FormElementDynamicDataSource.from_dict(form_element_dynamic_data_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



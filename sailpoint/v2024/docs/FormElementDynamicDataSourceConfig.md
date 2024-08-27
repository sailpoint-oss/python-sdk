# FormElementDynamicDataSourceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_bucket_field** | **str** | AggregationBucketField is the aggregation bucket field name | [optional] 
**indices** | **List[str]** | Indices is a list of indices to use | [optional] 
**object_type** | **str** | ObjectType is a PreDefinedSelectOption value IDENTITY PreDefinedSelectOptionIdentity ACCESS_PROFILE PreDefinedSelectOptionAccessProfile SOURCES PreDefinedSelectOptionSources ROLE PreDefinedSelectOptionRole ENTITLEMENT PreDefinedSelectOptionEntitlement | [optional] 
**query** | **str** | Query is a text | [optional] 

## Example

```python
from sailpoint.v2024.models.form_element_dynamic_data_source_config import FormElementDynamicDataSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FormElementDynamicDataSourceConfig from a JSON string
form_element_dynamic_data_source_config_instance = FormElementDynamicDataSourceConfig.from_json(json)
# print the JSON string representation of the object
print(FormElementDynamicDataSourceConfig.to_json())

# convert the object into a dict
form_element_dynamic_data_source_config_dict = form_element_dynamic_data_source_config_instance.to_dict()
# create an instance of FormElementDynamicDataSourceConfig from a dict
form_element_dynamic_data_source_config_from_dict = FormElementDynamicDataSourceConfig.from_dict(form_element_dynamic_data_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



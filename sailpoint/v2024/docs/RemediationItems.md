# RemediationItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the certification | [optional] 
**target_id** | **str** | The ID of the certification target | [optional] 
**target_name** | **str** | The name of the certification target | [optional] 
**target_display_name** | **str** | The display name of the certification target | [optional] 
**application_name** | **str** | The name of the application/source | [optional] 
**attribute_name** | **str** | The name of the attribute being certified | [optional] 
**attribute_operation** | **str** | The operation of the certification on the attribute | [optional] 
**attribute_value** | **str** | The value of the attribute being certified | [optional] 
**native_identity** | **str** | The native identity of the target | [optional] 

## Example

```python
from sailpoint.v2024.models.remediation_items import RemediationItems

# TODO update the JSON string below
json = "{}"
# create an instance of RemediationItems from a JSON string
remediation_items_instance = RemediationItems.from_json(json)
# print the JSON string representation of the object
print(RemediationItems.to_json())

# convert the object into a dict
remediation_items_dict = remediation_items_instance.to_dict()
# create an instance of RemediationItems from a dict
remediation_items_from_dict = RemediationItems.from_dict(remediation_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



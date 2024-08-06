# NativeChangeDetectionConfig

Source configuration information for Native Change Detection that is read and used by account aggregation process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | A flag indicating if Native Change Detection is enabled for a source. | [optional] [default to False]
**operations** | **List[str]** | Operation types for which Native Change Detection is enabled for a source. | [optional] 
**all_entitlements** | **bool** | A flag indicating that all entitlements participate in Native Change Detection. | [optional] [default to False]
**all_non_entitlement_attributes** | **bool** | A flag indicating that all non-entitlement account attributes participate in Native Change Detection. | [optional] [default to False]
**selected_entitlements** | **List[str]** | If allEntitlements flag is off this field lists entitlements that participate in Native Change Detection. | [optional] 
**selected_non_entitlement_attributes** | **List[str]** | If allNonEntitlementAttributes flag is off this field lists non-entitlement account attributes that participate in Native Change Detection. | [optional] 

## Example

```python
from sailpoint.v2024.models.native_change_detection_config import NativeChangeDetectionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NativeChangeDetectionConfig from a JSON string
native_change_detection_config_instance = NativeChangeDetectionConfig.from_json(json)
# print the JSON string representation of the object
print NativeChangeDetectionConfig.to_json()

# convert the object into a dict
native_change_detection_config_dict = native_change_detection_config_instance.to_dict()
# create an instance of NativeChangeDetectionConfig from a dict
native_change_detection_config_form_dict = native_change_detection_config.from_dict(native_change_detection_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



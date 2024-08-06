# Sed

Suggested Entitlement Description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the entitlement | [optional] 
**approved_by** | **str** | entitlement approved by | [optional] 
**approved_type** | **str** | entitlement approved type | [optional] 
**approved_when** | **datetime** | entitlement approved then | [optional] 
**attribute** | **str** | entitlement attribute | [optional] 
**description** | **str** | description of entitlement | [optional] 
**display_name** | **str** | entitlement display name | [optional] 
**id** | **str** | sed id | [optional] 
**source_id** | **str** | entitlement source id | [optional] 
**source_name** | **str** | entitlement source name | [optional] 
**status** | **str** | entitlement status | [optional] 
**suggested_description** | **str** | llm suggested entitlement description | [optional] 
**type** | **str** | entitlement type | [optional] 
**value** | **str** | entitlement value | [optional] 

## Example

```python
from sailpoint.v2024.models.sed import Sed

# TODO update the JSON string below
json = "{}"
# create an instance of Sed from a JSON string
sed_instance = Sed.from_json(json)
# print the JSON string representation of the object
print Sed.to_json()

# convert the object into a dict
sed_dict = sed_instance.to_dict()
# create an instance of Sed from a dict
sed_form_dict = sed.from_dict(sed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



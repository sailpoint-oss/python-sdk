# ConditionEffectConfig

Arbitrary map containing a configuration based on the EffectType.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_value_label** | **str** | Effect type&#39;s label. | [optional] 
**element** | **str** | Element&#39;s identifier. | [optional] 

## Example

```python
from sailpoint.beta.models.condition_effect_config import ConditionEffectConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionEffectConfig from a JSON string
condition_effect_config_instance = ConditionEffectConfig.from_json(json)
# print the JSON string representation of the object
print ConditionEffectConfig.to_json()

# convert the object into a dict
condition_effect_config_dict = condition_effect_config_instance.to_dict()
# create an instance of ConditionEffectConfig from a dict
condition_effect_config_form_dict = condition_effect_config.from_dict(condition_effect_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



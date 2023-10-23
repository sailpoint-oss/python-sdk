# ConditionEffect

ConditionEffect is the effect produced by a condition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **Dict[str, object]** | Config is a arbitrary map that holds a configuration based on EffectType | [optional] 
**effect_type** | **str** | EffectType is the type of effect to perform when the conditions are evaluated for this logic block HIDE ConditionEffectTypeHide  ConditionEffectTypeHide disables validations SHOW ConditionEffectTypeShow  ConditionEffectTypeShow enables validations DISABLE ConditionEffectTypeDisable  ConditionEffectTypeDisable disables validations ENABLE ConditionEffectTypeEnable  ConditionEffectTypeEnable enables validations REQUIRE ConditionEffectTypeRequire OPTIONAL ConditionEffectTypeOptional SUBMIT_MESSAGE ConditionEffectTypeSubmitMessage SUBMIT_NOTIFICATION ConditionEffectTypeSubmitNotification SET_DEFAULT_VALUE ConditionEffectTypeSetDefaultValue  ConditionEffectTypeSetDefaultValue is ignored on purpose | [optional] 

## Example

```python
from beta.models.condition_effect import ConditionEffect

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionEffect from a JSON string
condition_effect_instance = ConditionEffect.from_json(json)
# print the JSON string representation of the object
print ConditionEffect.to_json()

# convert the object into a dict
condition_effect_dict = condition_effect_instance.to_dict()
# create an instance of ConditionEffect from a dict
condition_effect_form_dict = condition_effect.from_dict(condition_effect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



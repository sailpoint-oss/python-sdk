# PreferencesDto

Maps an Identity's attribute key to a list of preferred notification mediums.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The template notification key. | [optional] 
**mediums** | [**List[Medium]**](Medium.md) | List of preferred notification mediums, i.e., the mediums (or method) for which notifications are enabled. More mediums may be added in the future. | [optional] 
**modified** | **datetime** | Modified date of preference | [optional] 

## Example

```python
from beta.models.preferences_dto import PreferencesDto

# TODO update the JSON string below
json = "{}"
# create an instance of PreferencesDto from a JSON string
preferences_dto_instance = PreferencesDto.from_json(json)
# print the JSON string representation of the object
print PreferencesDto.to_json()

# convert the object into a dict
preferences_dto_dict = preferences_dto_instance.to_dict()
# create an instance of PreferencesDto from a dict
preferences_dto_form_dict = preferences_dto.from_dict(preferences_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



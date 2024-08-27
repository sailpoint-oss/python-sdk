# OutlierFeatureTranslation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | [**TranslationMessage**](TranslationMessage.md) |  | [optional] 
**description** | [**TranslationMessage**](TranslationMessage.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.outlier_feature_translation import OutlierFeatureTranslation

# TODO update the JSON string below
json = "{}"
# create an instance of OutlierFeatureTranslation from a JSON string
outlier_feature_translation_instance = OutlierFeatureTranslation.from_json(json)
# print the JSON string representation of the object
print(OutlierFeatureTranslation.to_json())

# convert the object into a dict
outlier_feature_translation_dict = outlier_feature_translation_instance.to_dict()
# create an instance of OutlierFeatureTranslation from a dict
outlier_feature_translation_from_dict = OutlierFeatureTranslation.from_dict(outlier_feature_translation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



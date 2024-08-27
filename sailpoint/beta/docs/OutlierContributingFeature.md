# OutlierContributingFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Contributing feature id | [optional] 
**name** | **str** | The name of the feature | [optional] 
**value_type** | **str** | The data type of the value field | [optional] 
**value** | [**OutlierContributingFeatureValue**](OutlierContributingFeatureValue.md) |  | [optional] 
**importance** | **float** | The importance of the feature. This can also be a negative value | [optional] 
**display_name** | **str** | The (translated if header is passed) displayName for the feature | [optional] 
**description** | **str** | The (translated if header is passed) description for the feature | [optional] 
**translation_messages** | [**OutlierFeatureTranslation**](OutlierFeatureTranslation.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.outlier_contributing_feature import OutlierContributingFeature

# TODO update the JSON string below
json = "{}"
# create an instance of OutlierContributingFeature from a JSON string
outlier_contributing_feature_instance = OutlierContributingFeature.from_json(json)
# print the JSON string representation of the object
print(OutlierContributingFeature.to_json())

# convert the object into a dict
outlier_contributing_feature_dict = outlier_contributing_feature_instance.to_dict()
# create an instance of OutlierContributingFeature from a dict
outlier_contributing_feature_from_dict = OutlierContributingFeature.from_dict(outlier_contributing_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FeatureValueDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **str** | The type of feature | [optional] 
**numerator** | **int** | The number of identities that have access to the feature | [optional] 
**denominator** | **int** | The number of identities with the corresponding feature | [optional] 

## Example

```python
from beta.models.feature_value_dto import FeatureValueDto

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureValueDto from a JSON string
feature_value_dto_instance = FeatureValueDto.from_json(json)
# print the JSON string representation of the object
print FeatureValueDto.to_json()

# convert the object into a dict
feature_value_dto_dict = feature_value_dto_instance.to_dict()
# create an instance of FeatureValueDto from a dict
feature_value_dto_form_dict = feature_value_dto.from_dict(feature_value_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



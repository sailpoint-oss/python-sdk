# Outlier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identity&#39;s unique identifier for the outlier record | [optional] 
**identity_id** | **str** | The ID of the identity that is detected as an outlier | [optional] 
**type** | **str** | The type of outlier summary | [optional] 
**first_detection_date** | **datetime** | The first date the outlier was detected | [optional] 
**latest_detection_date** | **datetime** | The most recent date the outlier was detected | [optional] 
**ignored** | **bool** | Flag whether or not the outlier has been ignored | [optional] 
**attributes** | **object** | Object containing mapped identity attributes | [optional] 
**score** | **float** | The outlier score determined by the detection engine ranging from 0..1 | [optional] 
**unignore_type** | **str** | Enum value of if the outlier manually or automatically un-ignored. Will be NULL if outlier is not ignored | [optional] 
**unignore_date** | **datetime** | shows date when last time has been unignored outlier | [optional] 
**ignore_date** | **datetime** | shows date when last time has been ignored outlier | [optional] 

## Example

```python
from sailpoint.beta.models.outlier import Outlier

# TODO update the JSON string below
json = "{}"
# create an instance of Outlier from a JSON string
outlier_instance = Outlier.from_json(json)
# print the JSON string representation of the object
print(Outlier.to_json())

# convert the object into a dict
outlier_dict = outlier_instance.to_dict()
# create an instance of Outlier from a dict
outlier_from_dict = Outlier.from_dict(outlier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



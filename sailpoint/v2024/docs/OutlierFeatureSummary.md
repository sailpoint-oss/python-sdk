# OutlierFeatureSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contributing_feature_name** | **str** | Contributing feature name | [optional] 
**identity_outlier_display_name** | **str** | Identity display name | [optional] 
**outlier_feature_display_values** | [**List[OutlierFeatureSummaryOutlierFeatureDisplayValuesInner]**](OutlierFeatureSummaryOutlierFeatureDisplayValuesInner.md) |  | [optional] 
**feature_definition** | **str** | Definition of the feature | [optional] 
**feature_explanation** | **str** | Detailed explanation of the feature | [optional] 
**peer_display_name** | **str** | outlier&#39;s peer identity display name | [optional] 
**peer_identity_id** | **str** | outlier&#39;s peer identity id | [optional] 
**access_item_reference** | **object** | Access Item reference | [optional] 

## Example

```python
from sailpoint.v2024.models.outlier_feature_summary import OutlierFeatureSummary

# TODO update the JSON string below
json = "{}"
# create an instance of OutlierFeatureSummary from a JSON string
outlier_feature_summary_instance = OutlierFeatureSummary.from_json(json)
# print the JSON string representation of the object
print(OutlierFeatureSummary.to_json())

# convert the object into a dict
outlier_feature_summary_dict = outlier_feature_summary_instance.to_dict()
# create an instance of OutlierFeatureSummary from a dict
outlier_feature_summary_from_dict = OutlierFeatureSummary.from_dict(outlier_feature_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



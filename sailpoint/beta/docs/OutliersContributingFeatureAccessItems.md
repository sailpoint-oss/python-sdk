# OutliersContributingFeatureAccessItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the access item | [optional] 
**display_name** | **str** | the display name of the access item | [optional] 
**description** | **str** | Description of the access item. | [optional] 
**access_type** | **str** | The type of the access item. | [optional] 
**source_name** | **str** | the associated source name if it exists | [optional] 
**extremely_rare** | **bool** | rarest access | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.outliers_contributing_feature_access_items import OutliersContributingFeatureAccessItems

# TODO update the JSON string below
json = "{}"
# create an instance of OutliersContributingFeatureAccessItems from a JSON string
outliers_contributing_feature_access_items_instance = OutliersContributingFeatureAccessItems.from_json(json)
# print the JSON string representation of the object
print(OutliersContributingFeatureAccessItems.to_json())

# convert the object into a dict
outliers_contributing_feature_access_items_dict = outliers_contributing_feature_access_items_instance.to_dict()
# create an instance of OutliersContributingFeatureAccessItems from a dict
outliers_contributing_feature_access_items_from_dict = OutliersContributingFeatureAccessItems.from_dict(outliers_contributing_feature_access_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



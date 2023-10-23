# OutlierSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of outlier summary | [optional] 
**snapshot_date** | **datetime** | The date the bulk outlier detection ran/snapshot was created | [optional] 
**total_outliers** | **int** | Total number of outliers for the customer making the request | [optional] 
**total_identities** | **int** | Total number of identities for the customer making the request | [optional] 

## Example

```python
from beta.models.outlier_summary import OutlierSummary

# TODO update the JSON string below
json = "{}"
# create an instance of OutlierSummary from a JSON string
outlier_summary_instance = OutlierSummary.from_json(json)
# print the JSON string representation of the object
print OutlierSummary.to_json()

# convert the object into a dict
outlier_summary_dict = outlier_summary_instance.to_dict()
# create an instance of OutlierSummary from a dict
outlier_summary_form_dict = outlier_summary.from_dict(outlier_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



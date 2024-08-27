# LatestOutlierSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of outlier summary | [optional] 
**snapshot_date** | **datetime** | The date the bulk outlier detection ran/snapshot was created | [optional] 
**total_outliers** | **int** | Total number of outliers for the customer making the request | [optional] 
**total_identities** | **int** | Total number of identities for the customer making the request | [optional] 
**total_ignored** | **int** | Total number of ignored outliers | [optional] 

## Example

```python
from sailpoint.v2024.models.latest_outlier_summary import LatestOutlierSummary

# TODO update the JSON string below
json = "{}"
# create an instance of LatestOutlierSummary from a JSON string
latest_outlier_summary_instance = LatestOutlierSummary.from_json(json)
# print the JSON string representation of the object
print(LatestOutlierSummary.to_json())

# convert the object into a dict
latest_outlier_summary_dict = latest_outlier_summary_instance.to_dict()
# create an instance of LatestOutlierSummary from a dict
latest_outlier_summary_from_dict = LatestOutlierSummary.from_dict(latest_outlier_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



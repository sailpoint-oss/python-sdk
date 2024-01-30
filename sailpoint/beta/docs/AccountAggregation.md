# AccountAggregation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** | When the aggregation started. | [optional] 
**status** | **str** | STARTED - Aggregation started, but source account iteration has not completed.  ACCOUNTS_COLLECTED - Source account iteration completed, but all accounts have not yet been processed.  COMPLETED - Aggregation completed (*possibly with errors*).  CANCELLED - Aggregation cancelled by user.  RETRIED - Aggregation retried because of connectivity issues with the Virtual Appliance.  TERMINATED - Aggregation marked as failed after 3 tries after connectivity issues with the Virtual Appliance.  | [optional] 
**total_accounts** | **int** | The total number of *NEW, CHANGED and DELETED* accounts that need to be processed for this aggregation. This does not include accounts that were unchanged since the previous aggregation. This can be zero if there were no new, changed or deleted accounts since the previous aggregation. *Only available when status is ACCOUNTS_COLLECTED or COMPLETED.* | [optional] 
**processed_accounts** | **int** | The number of *NEW, CHANGED and DELETED* accounts that have been processed so far. This reflects the number of accounts that have been processed at the time of the API call, and may increase on subsequent API calls while the status is ACCOUNTS_COLLECTED. *Only available when status is ACCOUNTS_COLLECTED or COMPLETED.* | [optional] 

## Example

```python
from sailpoint.beta.models.account_aggregation import AccountAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAggregation from a JSON string
account_aggregation_instance = AccountAggregation.from_json(json)
# print the JSON string representation of the object
print AccountAggregation.to_json()

# convert the object into a dict
account_aggregation_dict = account_aggregation_instance.to_dict()
# create an instance of AccountAggregation from a dict
account_aggregation_form_dict = account_aggregation.from_dict(account_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



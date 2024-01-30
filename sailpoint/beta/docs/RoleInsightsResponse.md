# RoleInsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Request Id for a role insight generation request | [optional] 
**created_date** | **datetime** | The date-time role insights request was created. | [optional] 
**last_generated** | **datetime** | The date-time role insights request was completed. | [optional] 
**number_of_updates** | **int** | Total number of updates for this request. Starts with 0 and will have correct number when request is COMPLETED. | [optional] 
**role_ids** | **List[str]** | The role IDs that are in this request. | [optional] 
**status** | **str** | Request status | [optional] 

## Example

```python
from sailpoint.beta.models.role_insights_response import RoleInsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleInsightsResponse from a JSON string
role_insights_response_instance = RoleInsightsResponse.from_json(json)
# print the JSON string representation of the object
print RoleInsightsResponse.to_json()

# convert the object into a dict
role_insights_response_dict = role_insights_response_instance.to_dict()
# create an instance of RoleInsightsResponse from a dict
role_insights_response_form_dict = role_insights_response.from_dict(role_insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



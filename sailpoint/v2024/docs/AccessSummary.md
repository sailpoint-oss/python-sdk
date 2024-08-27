# AccessSummary

An object holding the access that is being reviewed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**AccessSummaryAccess**](AccessSummaryAccess.md) |  | [optional] 
**entitlement** | [**ReviewableEntitlement**](ReviewableEntitlement.md) |  | [optional] 
**access_profile** | [**ReviewableAccessProfile**](ReviewableAccessProfile.md) |  | [optional] 
**role** | [**ReviewableRole**](ReviewableRole.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.access_summary import AccessSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AccessSummary from a JSON string
access_summary_instance = AccessSummary.from_json(json)
# print the JSON string representation of the object
print(AccessSummary.to_json())

# convert the object into a dict
access_summary_dict = access_summary_instance.to_dict()
# create an instance of AccessSummary from a dict
access_summary_from_dict = AccessSummary.from_dict(access_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



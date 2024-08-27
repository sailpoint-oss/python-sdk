# AuthProfileSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | **str** | Tenant name. | [optional] 
**id** | **str** | Identity ID. | [optional] 

## Example

```python
from sailpoint.v2024.models.auth_profile_summary import AuthProfileSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AuthProfileSummary from a JSON string
auth_profile_summary_instance = AuthProfileSummary.from_json(json)
# print the JSON string representation of the object
print(AuthProfileSummary.to_json())

# convert the object into a dict
auth_profile_summary_dict = auth_profile_summary_instance.to_dict()
# create an instance of AuthProfileSummary from a dict
auth_profile_summary_from_dict = AuthProfileSummary.from_dict(auth_profile_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RoleInsightsIdentities


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id for identity | [optional] 
**name** | **str** | Name for identity | [optional] 
**attributes** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sailpoint.beta.models.role_insights_identities import RoleInsightsIdentities

# TODO update the JSON string below
json = "{}"
# create an instance of RoleInsightsIdentities from a JSON string
role_insights_identities_instance = RoleInsightsIdentities.from_json(json)
# print the JSON string representation of the object
print RoleInsightsIdentities.to_json()

# convert the object into a dict
role_insights_identities_dict = role_insights_identities_instance.to_dict()
# create an instance of RoleInsightsIdentities from a dict
role_insights_identities_form_dict = role_insights_identities.from_dict(role_insights_identities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



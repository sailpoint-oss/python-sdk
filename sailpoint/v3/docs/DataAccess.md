# DataAccess

DAS data for the entitlement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[DataAccessPoliciesInner]**](DataAccessPoliciesInner.md) | List of classification policies that apply to resources the entitlement \\ groups has access to | [optional] 
**categories** | [**List[DataAccessCategoriesInner]**](DataAccessCategoriesInner.md) | List of classification categories that apply to resources the entitlement \\ groups has access to | [optional] 
**impact_score** | [**DataAccessImpactScore**](DataAccessImpactScore.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.data_access import DataAccess

# TODO update the JSON string below
json = "{}"
# create an instance of DataAccess from a JSON string
data_access_instance = DataAccess.from_json(json)
# print the JSON string representation of the object
print DataAccess.to_json()

# convert the object into a dict
data_access_dict = data_access_instance.to_dict()
# create an instance of DataAccess from a dict
data_access_form_dict = data_access.from_dict(data_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



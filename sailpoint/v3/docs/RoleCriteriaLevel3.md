# RoleCriteriaLevel3

Defines STANDARD type Role membership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**RoleCriteriaOperation**](RoleCriteriaOperation.md) |  | [optional] 
**key** | [**RoleCriteriaKey**](RoleCriteriaKey.md) |  | [optional] 
**string_value** | **str** | String value to test the Identity attribute, Account attribute, or Entitlement specified in the key w/r/t the specified operation. If this criteria is a leaf node, that is, if the operation is one of EQUALS, NOT_EQUALS, CONTAINS, STARTS_WITH, or ENDS_WITH, this field is required. Otherwise, specifying it is an error. | [optional] 

## Example

```python
from sailpoint.v3.models.role_criteria_level3 import RoleCriteriaLevel3

# TODO update the JSON string below
json = "{}"
# create an instance of RoleCriteriaLevel3 from a JSON string
role_criteria_level3_instance = RoleCriteriaLevel3.from_json(json)
# print the JSON string representation of the object
print RoleCriteriaLevel3.to_json()

# convert the object into a dict
role_criteria_level3_dict = role_criteria_level3_instance.to_dict()
# create an instance of RoleCriteriaLevel3 from a dict
role_criteria_level3_form_dict = role_criteria_level3.from_dict(role_criteria_level3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RoleCriteriaLevel2

Defines STANDARD type Role membership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**RoleCriteriaOperation**](RoleCriteriaOperation.md) |  | [optional] 
**key** | [**RoleCriteriaKey**](RoleCriteriaKey.md) |  | [optional] 
**string_value** | **str** | String value to test the Identity attribute, Account attribute, or Entitlement specified in the key w/r/t the specified operation. If this criteria is a leaf node, that is, if the operation is one of EQUALS, NOT_EQUALS, CONTAINS, STARTS_WITH, or ENDS_WITH, this field is required. Otherwise, specifying it is an error. | [optional] 
**children** | [**List[RoleCriteriaLevel3]**](RoleCriteriaLevel3.md) | Array of child criteria. Required if the operation is AND or OR, otherwise it must be left null. A maximum of three levels of criteria are supported, including leaf nodes. Additionally, AND nodes can only be children or OR nodes and vice-versa. | [optional] 

## Example

```python
from sailpoint.beta.models.role_criteria_level2 import RoleCriteriaLevel2

# TODO update the JSON string below
json = "{}"
# create an instance of RoleCriteriaLevel2 from a JSON string
role_criteria_level2_instance = RoleCriteriaLevel2.from_json(json)
# print the JSON string representation of the object
print(RoleCriteriaLevel2.to_json())

# convert the object into a dict
role_criteria_level2_dict = role_criteria_level2_instance.to_dict()
# create an instance of RoleCriteriaLevel2 from a dict
role_criteria_level2_from_dict = RoleCriteriaLevel2.from_dict(role_criteria_level2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



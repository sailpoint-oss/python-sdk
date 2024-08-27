# ProvisioningCriteriaLevel3

Defines matching criteria for an Account to be provisioned with a specific Access Profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**ProvisioningCriteriaOperation**](ProvisioningCriteriaOperation.md) |  | [optional] 
**attribute** | **str** | Name of the Account attribute to be tested. If **operation** is one of EQUALS, NOT_EQUALS, CONTAINS, or HAS, this field is required. Otherwise, specifying it is an error. | [optional] 
**value** | **str** | String value to test the Account attribute w/r/t the specified operation. If the operation is one of EQUALS, NOT_EQUALS, or CONTAINS, this field is required. Otherwise, specifying it is an error. If the Attribute is not String-typed, it will be converted to the appropriate type. | [optional] 
**children** | **str** | Array of child criteria. Required if the operation is AND or OR, otherwise it must be left null. A maximum of three levels of criteria are supported, including leaf nodes. | [optional] 

## Example

```python
from sailpoint.v3.models.provisioning_criteria_level3 import ProvisioningCriteriaLevel3

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningCriteriaLevel3 from a JSON string
provisioning_criteria_level3_instance = ProvisioningCriteriaLevel3.from_json(json)
# print the JSON string representation of the object
print(ProvisioningCriteriaLevel3.to_json())

# convert the object into a dict
provisioning_criteria_level3_dict = provisioning_criteria_level3_instance.to_dict()
# create an instance of ProvisioningCriteriaLevel3 from a dict
provisioning_criteria_level3_from_dict = ProvisioningCriteriaLevel3.from_dict(provisioning_criteria_level3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



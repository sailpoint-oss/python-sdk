# AccessConstraint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of Access | 
**ids** | **List[str]** | Must be set only if operator is SELECTED. | [optional] 
**operator** | **str** | Used to determine whether the scope of the campaign should be reduced for selected ids or all. | 

## Example

```python
from sailpoint.v3.models.access_constraint import AccessConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of AccessConstraint from a JSON string
access_constraint_instance = AccessConstraint.from_json(json)
# print the JSON string representation of the object
print AccessConstraint.to_json()

# convert the object into a dict
access_constraint_dict = access_constraint_instance.to_dict()
# create an instance of AccessConstraint from a dict
access_constraint_form_dict = access_constraint.from_dict(access_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



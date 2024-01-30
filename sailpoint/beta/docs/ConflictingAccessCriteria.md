# ConflictingAccessCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_criteria** | [**AccessCriteria**](AccessCriteria.md) |  | [optional] 
**right_criteria** | [**AccessCriteria**](AccessCriteria.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.conflicting_access_criteria import ConflictingAccessCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of ConflictingAccessCriteria from a JSON string
conflicting_access_criteria_instance = ConflictingAccessCriteria.from_json(json)
# print the JSON string representation of the object
print ConflictingAccessCriteria.to_json()

# convert the object into a dict
conflicting_access_criteria_dict = conflicting_access_criteria_instance.to_dict()
# create an instance of ConflictingAccessCriteria from a dict
conflicting_access_criteria_form_dict = conflicting_access_criteria.from_dict(conflicting_access_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



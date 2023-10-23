# AccessCriteria


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Business name for the access construct list | [optional] 
**criteria_list** | [**List[AccessCriteriaCriteriaListInner]**](AccessCriteriaCriteriaListInner.md) | List of criteria. There is a min of 1 and max of 50 items in the list. | [optional] 

## Example

```python
from v3.models.access_criteria import AccessCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of AccessCriteria from a JSON string
access_criteria_instance = AccessCriteria.from_json(json)
# print the JSON string representation of the object
print AccessCriteria.to_json()

# convert the object into a dict
access_criteria_dict = access_criteria_instance.to_dict()
# create an instance of AccessCriteria from a dict
access_criteria_form_dict = access_criteria.from_dict(access_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



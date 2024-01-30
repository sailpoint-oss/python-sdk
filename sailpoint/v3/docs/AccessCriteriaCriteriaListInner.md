# AccessCriteriaCriteriaListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the propery to which this reference applies to | [optional] 
**id** | **str** | ID of the object to which this reference applies to | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies to | [optional] 

## Example

```python
from sailpoint.v3.models.access_criteria_criteria_list_inner import AccessCriteriaCriteriaListInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessCriteriaCriteriaListInner from a JSON string
access_criteria_criteria_list_inner_instance = AccessCriteriaCriteriaListInner.from_json(json)
# print the JSON string representation of the object
print AccessCriteriaCriteriaListInner.to_json()

# convert the object into a dict
access_criteria_criteria_list_inner_dict = access_criteria_criteria_list_inner_instance.to_dict()
# create an instance of AccessCriteriaCriteriaListInner from a dict
access_criteria_criteria_list_inner_form_dict = access_criteria_criteria_list_inner.from_dict(access_criteria_criteria_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



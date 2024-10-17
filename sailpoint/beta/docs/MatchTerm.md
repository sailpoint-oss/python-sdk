# MatchTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The attribute name | [optional] 
**value** | **str** | The attribute value | [optional] 
**op** | **str** | The operator between name and value | [optional] 
**container** | **bool** | If it is a container or a real match term | [optional] [default to False]
**var_and** | **bool** | If it is AND logical operator for the children match terms | [optional] [default to False]
**children** | **List[Dict[str, object]]** | The children under this match term | [optional] 

## Example

```python
from sailpoint.beta.models.match_term import MatchTerm

# TODO update the JSON string below
json = "{}"
# create an instance of MatchTerm from a JSON string
match_term_instance = MatchTerm.from_json(json)
# print the JSON string representation of the object
print(MatchTerm.to_json())

# convert the object into a dict
match_term_dict = match_term_instance.to_dict()
# create an instance of MatchTerm from a dict
match_term_from_dict = MatchTerm.from_dict(match_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



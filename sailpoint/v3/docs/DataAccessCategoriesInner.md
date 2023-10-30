# DataAccessCategoriesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the category | [optional] 
**match_count** | **int** | Number of matched for each category | [optional] 

## Example

```python
from v3.models.data_access_categories_inner import DataAccessCategoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataAccessCategoriesInner from a JSON string
data_access_categories_inner_instance = DataAccessCategoriesInner.from_json(json)
# print the JSON string representation of the object
print DataAccessCategoriesInner.to_json()

# convert the object into a dict
data_access_categories_inner_dict = data_access_categories_inner_instance.to_dict()
# create an instance of DataAccessCategoriesInner from a dict
data_access_categories_inner_form_dict = data_access_categories_inner.from_dict(data_access_categories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



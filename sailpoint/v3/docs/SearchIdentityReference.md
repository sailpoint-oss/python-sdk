# SearchIdentityReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**type** | [**DtoType**](DtoType.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.search_identity_reference import SearchIdentityReference

# TODO update the JSON string below
json = "{}"
# create an instance of SearchIdentityReference from a JSON string
search_identity_reference_instance = SearchIdentityReference.from_json(json)
# print the JSON string representation of the object
print SearchIdentityReference.to_json()

# convert the object into a dict
search_identity_reference_dict = search_identity_reference_instance.to_dict()
# create an instance of SearchIdentityReference from a dict
search_identity_reference_form_dict = search_identity_reference.from_dict(search_identity_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Reassignment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**CertificationReference**](CertificationReference.md) |  | [optional] 
**comment** | **str** | Comments from the previous reviewer. | [optional] 

## Example

```python
from sailpoint.beta.models.reassignment import Reassignment

# TODO update the JSON string below
json = "{}"
# create an instance of Reassignment from a JSON string
reassignment_instance = Reassignment.from_json(json)
# print the JSON string representation of the object
print Reassignment.to_json()

# convert the object into a dict
reassignment_dict = reassignment_instance.to_dict()
# create an instance of Reassignment from a dict
reassignment_form_dict = reassignment.from_dict(reassignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Reassignment1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**CertificationReference1**](CertificationReference1.md) |  | [optional] 
**comment** | **str** | Comments from the previous reviewer. | [optional] 

## Example

```python
from sailpoint.v2024.models.reassignment1 import Reassignment1

# TODO update the JSON string below
json = "{}"
# create an instance of Reassignment1 from a JSON string
reassignment1_instance = Reassignment1.from_json(json)
# print the JSON string representation of the object
print Reassignment1.to_json()

# convert the object into a dict
reassignment1_dict = reassignment1_instance.to_dict()
# create an instance of Reassignment1 from a dict
reassignment1_form_dict = reassignment1.from_dict(reassignment1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



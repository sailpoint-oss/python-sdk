# NonEmployeeIdentityReferenceWithId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NonEmployeeIdentityDtoType**](NonEmployeeIdentityDtoType.md) |  | [optional] 
**id** | **str** | Identity id | [optional] 

## Example

```python
from v3.models.non_employee_identity_reference_with_id import NonEmployeeIdentityReferenceWithId

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeIdentityReferenceWithId from a JSON string
non_employee_identity_reference_with_id_instance = NonEmployeeIdentityReferenceWithId.from_json(json)
# print the JSON string representation of the object
print NonEmployeeIdentityReferenceWithId.to_json()

# convert the object into a dict
non_employee_identity_reference_with_id_dict = non_employee_identity_reference_with_id_instance.to_dict()
# create an instance of NonEmployeeIdentityReferenceWithId from a dict
non_employee_identity_reference_with_id_form_dict = non_employee_identity_reference_with_id.from_dict(non_employee_identity_reference_with_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



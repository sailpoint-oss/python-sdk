# AuditDetails

Audit details for the reassignment configuration of an identity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Initial date and time when the record was created | [optional] 
**created_by** | [**Identity1**](Identity1.md) |  | [optional] 
**modified** | **datetime** | Last modified date and time for the record | [optional] 
**modified_by** | [**Identity1**](Identity1.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.audit_details import AuditDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AuditDetails from a JSON string
audit_details_instance = AuditDetails.from_json(json)
# print the JSON string representation of the object
print AuditDetails.to_json()

# convert the object into a dict
audit_details_dict = audit_details_instance.to_dict()
# create an instance of AuditDetails from a dict
audit_details_form_dict = audit_details.from_dict(audit_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# NonEmployeeSourceWithCloudExternalId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Non-Employee source id. | [optional] 
**source_id** | **str** | Source Id associated with this non-employee source. | [optional] 
**name** | **str** | Source name associated with this non-employee source. | [optional] 
**description** | **str** | Source description associated with this non-employee source. | [optional] 
**approvers** | [**List[IdentityReferenceWithId]**](IdentityReferenceWithId.md) | List of approvers | [optional] 
**account_managers** | [**List[IdentityReferenceWithId]**](IdentityReferenceWithId.md) | List of account managers | [optional] 
**modified** | **datetime** | When the request was last modified. | [optional] 
**created** | **datetime** | When the request was created. | [optional] 
**non_employee_count** | **int** | The number of non-employee records on all sources that *requested-for* user manages. | [optional] 
**cloud_external_id** | **str** | Legacy ID used for sources from the V1 API. This attribute will be removed from a future version of the API and will not be considered a breaking change. No clients should rely on this ID always being present. | [optional] 

## Example

```python
from sailpoint.beta.models.non_employee_source_with_cloud_external_id import NonEmployeeSourceWithCloudExternalId

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeSourceWithCloudExternalId from a JSON string
non_employee_source_with_cloud_external_id_instance = NonEmployeeSourceWithCloudExternalId.from_json(json)
# print the JSON string representation of the object
print NonEmployeeSourceWithCloudExternalId.to_json()

# convert the object into a dict
non_employee_source_with_cloud_external_id_dict = non_employee_source_with_cloud_external_id_instance.to_dict()
# create an instance of NonEmployeeSourceWithCloudExternalId from a dict
non_employee_source_with_cloud_external_id_form_dict = non_employee_source_with_cloud_external_id.from_dict(non_employee_source_with_cloud_external_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CertificationIdentitySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the identity summary | [optional] 
**name** | **str** | Name of the linked identity | [optional] 
**identity_id** | **str** | The ID of the identity being certified | [optional] 
**completed** | **bool** | Indicates whether the review items for the linked identity&#39;s certification have been completed | [optional] 

## Example

```python
from sailpoint.v2024.models.certification_identity_summary import CertificationIdentitySummary

# TODO update the JSON string below
json = "{}"
# create an instance of CertificationIdentitySummary from a JSON string
certification_identity_summary_instance = CertificationIdentitySummary.from_json(json)
# print the JSON string representation of the object
print(CertificationIdentitySummary.to_json())

# convert the object into a dict
certification_identity_summary_dict = certification_identity_summary_instance.to_dict()
# create an instance of CertificationIdentitySummary from a dict
certification_identity_summary_from_dict = CertificationIdentitySummary.from_dict(certification_identity_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



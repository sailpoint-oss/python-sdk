# CertificationSignedOffCertification

The certification campaign that was signed off on.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the certification. | 
**name** | **str** | The name of the certification. | 
**created** | **datetime** | The date and time the certification was created. | 
**modified** | **datetime** | The date and time the certification was last modified. | [optional] 
**campaign_ref** | [**CampaignReference**](CampaignReference.md) |  | 
**phase** | [**CertificationPhase**](CertificationPhase.md) |  | 
**due** | **datetime** | The due date of the certification. | 
**signed** | **datetime** | The date the reviewer signed off on the certification. | 
**reviewer** | [**Reviewer**](Reviewer.md) |  | 
**reassignment** | [**Reassignment**](Reassignment.md) |  | [optional] 
**has_errors** | **bool** | Indicates it the certification has any errors. | 
**error_message** | **str** | A message indicating what the error is. | [optional] 
**completed** | **bool** | Indicates if all certification decisions have been made. | 
**decisions_made** | **int** | The number of approve/revoke/acknowledge decisions that have been made by the reviewer. | 
**decisions_total** | **int** | The total number of approve/revoke/acknowledge decisions for the certification. | 
**entities_completed** | **int** | The number of entities (identities, access profiles, roles, etc.) for which all decisions have been made and are complete. | 
**entities_total** | **int** | The total number of entities (identities, access profiles, roles, etc.) in the certification, both complete and incomplete. | 

## Example

```python
from beta.models.certification_signed_off_certification import CertificationSignedOffCertification

# TODO update the JSON string below
json = "{}"
# create an instance of CertificationSignedOffCertification from a JSON string
certification_signed_off_certification_instance = CertificationSignedOffCertification.from_json(json)
# print the JSON string representation of the object
print CertificationSignedOffCertification.to_json()

# convert the object into a dict
certification_signed_off_certification_dict = certification_signed_off_certification_instance.to_dict()
# create an instance of CertificationSignedOffCertification from a dict
certification_signed_off_certification_form_dict = certification_signed_off_certification.from_dict(certification_signed_off_certification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



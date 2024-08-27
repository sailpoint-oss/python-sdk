# Certification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the certification | [optional] 
**name** | **str** | name of the certification | [optional] 
**campaign** | [**CampaignReference**](CampaignReference.md) |  | [optional] 
**completed** | **bool** | Have all decisions been made? | [optional] 
**identities_completed** | **int** | The number of identities for whom all decisions have been made and are complete. | [optional] 
**identities_total** | **int** | The total number of identities in the Certification, both complete and incomplete. | [optional] 
**created** | **datetime** | created date | [optional] 
**modified** | **datetime** | modified date | [optional] 
**decisions_made** | **int** | The number of approve/revoke/acknowledge decisions that have been made. | [optional] 
**decisions_total** | **int** | The total number of approve/revoke/acknowledge decisions. | [optional] 
**due** | **datetime** | The due date of the certification. | [optional] 
**signed** | **datetime** | The date the reviewer signed off on the Certification. | [optional] 
**reviewer** | [**Reviewer**](Reviewer.md) |  | [optional] 
**reassignment** | [**Reassignment**](Reassignment.md) |  | [optional] 
**has_errors** | **bool** | Identifies if the certification has an error | [optional] 
**error_message** | **str** | Description of the certification error | [optional] 
**phase** | [**CertificationPhase**](CertificationPhase.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.certification import Certification

# TODO update the JSON string below
json = "{}"
# create an instance of Certification from a JSON string
certification_instance = Certification.from_json(json)
# print the JSON string representation of the object
print(Certification.to_json())

# convert the object into a dict
certification_dict = certification_instance.to_dict()
# create an instance of Certification from a dict
certification_from_dict = Certification.from_dict(certification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



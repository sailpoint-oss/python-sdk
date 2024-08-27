# IdentityCertDecisionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_decisions_made** | **int** | Number of entitlement decisions that have been made | [optional] 
**access_profile_decisions_made** | **int** | Number of access profile decisions that have been made | [optional] 
**role_decisions_made** | **int** | Number of role decisions that have been made | [optional] 
**account_decisions_made** | **int** | Number of account decisions that have been made | [optional] 
**entitlement_decisions_total** | **int** | The total number of entitlement decisions on the certification, both complete and incomplete | [optional] 
**access_profile_decisions_total** | **int** | The total number of access profile decisions on the certification, both complete and incomplete | [optional] 
**role_decisions_total** | **int** | The total number of role decisions on the certification, both complete and incomplete | [optional] 
**account_decisions_total** | **int** | The total number of account decisions on the certification, both complete and incomplete | [optional] 
**entitlements_approved** | **int** | The number of entitlement decisions that have been made which were approved | [optional] 
**entitlements_revoked** | **int** | The number of entitlement decisions that have been made which were revoked | [optional] 
**access_profiles_approved** | **int** | The number of access profile decisions that have been made which were approved | [optional] 
**access_profiles_revoked** | **int** | The number of access profile decisions that have been made which were revoked | [optional] 
**roles_approved** | **int** | The number of role decisions that have been made which were approved | [optional] 
**roles_revoked** | **int** | The number of role decisions that have been made which were revoked | [optional] 
**accounts_approved** | **int** | The number of account decisions that have been made which were approved | [optional] 
**accounts_revoked** | **int** | The number of account decisions that have been made which were revoked | [optional] 

## Example

```python
from sailpoint.v2024.models.identity_cert_decision_summary import IdentityCertDecisionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityCertDecisionSummary from a JSON string
identity_cert_decision_summary_instance = IdentityCertDecisionSummary.from_json(json)
# print the JSON string representation of the object
print(IdentityCertDecisionSummary.to_json())

# convert the object into a dict
identity_cert_decision_summary_dict = identity_cert_decision_summary_instance.to_dict()
# create an instance of IdentityCertDecisionSummary from a dict
identity_cert_decision_summary_from_dict = IdentityCertDecisionSummary.from_dict(identity_cert_decision_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# IdentitySnapshotSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot** | **str** | the date when the identity record was created | [optional] 

## Example

```python
from sailpoint.v2024.models.identity_snapshot_summary_response import IdentitySnapshotSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IdentitySnapshotSummaryResponse from a JSON string
identity_snapshot_summary_response_instance = IdentitySnapshotSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(IdentitySnapshotSummaryResponse.to_json())

# convert the object into a dict
identity_snapshot_summary_response_dict = identity_snapshot_summary_response_instance.to_dict()
# create an instance of IdentitySnapshotSummaryResponse from a dict
identity_snapshot_summary_response_from_dict = IdentitySnapshotSummaryResponse.from_dict(identity_snapshot_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



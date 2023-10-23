# RequestableObjectRequestStatus

Status indicating the ability of an access request for the object to be made by or on behalf of the identity specified by *identity-id*. *AVAILABLE* indicates the object is available to request. *PENDING* indicates the object is unavailable because the identity has a pending request in flight. *ASSIGNED* indicates the object is unavailable because the identity already has the indicated role or access profile. If *identity-id* is not specified (allowed only for admin users), then status will be *AVAILABLE* for all results.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



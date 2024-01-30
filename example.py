# import sailpoint
# import sailpoint.v3
# import sailpoint.beta
# from sailpoint.configuration import Configuration
# from sailpoint.paginator import Paginator
# from sailpoint.v3.models.search import Search
# from pprint import pprint

# configuration = Configuration()
    
# # Enter a context with an instance of the API client
# with sailpoint.v3.ApiClient(configuration) as api_client:
#     # Create an instance of the API class
#     api_instance = sailpoint.v3.TransformsApi(api_client)

#     # List transforms
#     try:
#         # List transforms
#         api_response = api_instance.list_transforms()
#         print("The response of TransformsApi->list_transforms:\n")
#         for transform in api_response:
#             pprint(transform.name)
#     except Exception as e:
#         print("Exception when calling TransformsApi->list_transforms: %s\n" % e)

#     # List Access Profiles
#     api_instance = sailpoint.v3.AccessProfilesApi(api_client)

#     try:
#         api_response = api_instance.list_access_profiles()
#         print("The response of AccessProfilesApi->list_access_profiles:\n")
#         for access_profile in api_response:
#             pprint(access_profile.name)
#     except Exception as e:
#         print(
#             "Exception when calling AccessProfilesApi->list_access_profiles: %s\n" % e
#         )
    
#     # Use the paginator with search

#     search = Search()
#     search.indices = ['identities']
#     search.query = { 'query': '*' }
#     search.sort = ['-name']

#     identities = Paginator.paginate_search(sailpoint.v3.SearchApi(api_client),search, 250, 1000)
#     for identity in identities:
#         print(identity['name'])
    


#     # Use the paginator to paginate 1000 accounts 100 at a time
#     accounts = Paginator.paginate(sailpoint.v3.AccountsApi(api_client).list_accounts, 1000, limit=100)
#     print(len(accounts))
#     for account in accounts:
#         print(account.name)


#     workgroups = sailpoint.beta.GovernanceGroupsApi(api_client).list_workgroups()
#     for workgroup in workgroups:
#         print(workgroup.name)


import sailpoint
import sailpoint.v3
import sailpoint.beta
from sailpoint.beta.models.workgroup_dto import WorkgroupDto
from sailpoint.beta.models.usage_type import UsageType
from sailpoint.beta.models.owner_dto import OwnerDto
from sailpoint.beta.models.json_patch_operation import JsonPatchOperation
from sailpoint.beta.models.json_patch_operation_value import JsonPatchOperationValue
from sailpoint.configuration import Configuration

configuration = Configuration()

api_client = sailpoint.v3.ApiClient(configuration)
api_client_beta = sailpoint.beta.ApiClient(configuration)

identities_api_instance = sailpoint.v3.PublicIdentitiesApi(api_client)
workgroups_api_instance = sailpoint.beta.GovernanceGroupsApi(api_client_beta)

workgroup = workgroups_api_instance.list_workgroups(filters='name eq "DB Access Governance Group"')[0]

json_patch_operation = [JsonPatchOperation(op='replace', path='/description', value=JsonPatchOperationValue('Description was updated by API'))]

try:
    workgroupResponse = workgroups_api_instance.patch_workgroup(workgroup.id,json_patch_operation=json_patch_operation)
    print("The response of GovernanceGroupsApi->patch_workgroup:\n")
    print(workgroupResponse)
except Exception as e:
    print("Exception when calling GovernanceGroupsApi->patch_workgroup: %s\n" % e)


# sources_instance = sailpoint.beta.SourcesApi(api_client_beta)

# new_field = { 'name': 'full_name', 'transform': None, 'attributes': {}, 'isRequired': False, 'type': None, 'isMultiValued': False }

# json_patch_operation=[JsonPatchOperation(op='add', path='/fields/-', value=JsonPatchOperationValue(new_field))]

# try:
#     create_provisioning_policy = sources_instance.update_provisioning_policy(source_id='df038ccd74834db1ae15546cfac56008', usage_type=UsageType.CREATE, json_patch_operation=json_patch_operation)
#     print("The response of GovernanceGroupsApi->patch_workgroup:\n")
#     print(create_provisioning_policy)
# except Exception as e:
#     print("Exception when calling GovernanceGroupsApi->patch_workgroup: %s\n" % e)

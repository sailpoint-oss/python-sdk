import time
import os
import sailpoint
from sailpoint.configuration import Configuration
from sailpoint.v3.models.transform_read import TransformRead
from sailpoint.v3.rest import ApiException
from pprint import pprint

configuration = Configuration()

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.TransformsApi(api_client)

    try:
        # List transforms
        api_response = api_instance.list_transforms()
        print("The response of TransformsApi->list_transforms:\n")
        for transform in api_response:
            pprint(transform.name)
    except Exception as e:
        print("Exception when calling TransformsApi->list_transforms: %s\n" % e)

    api_instance = sailpoint.v3.AccessProfilesApi(api_client)

    try:
        api_response = api_instance.list_access_profiles()
        print("The response of AccessProfilesApi->list_access_profiles:\n")
        for access_profile in api_response:
            pprint(access_profile.name)
    except Exception as e:
        print(
            "Exception when calling AccessProfilesApi->list_access_profiles: %s\n" % e
        )

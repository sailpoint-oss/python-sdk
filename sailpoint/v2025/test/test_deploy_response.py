# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.deploy_response import DeployResponse

class TestDeployResponse(unittest.TestCase):
    """DeployResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeployResponse:
        """Test DeployResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeployResponse`
        """
        model = DeployResponse()
        if include_optional:
            return DeployResponse(
                job_id = '07659d7d-2cce-47c0-9e49-185787ee565a',
                status = 'COMPLETE',
                type = 'CONFIG_DEPLOY_DRAFT',
                message = 'Deploy creation message',
                requester_name = 'requester.name',
                file_exists = True,
                created = '2021-05-11T22:23:16Z',
                modified = '2021-05-11T22:23:16Z',
                completed = '2021-05-11T22:23:16Z',
                draft_id = '07659d7d-2cce-47c0-9e49-185787ee565a',
                draft_name = 'Draft Name',
                cloud_storage_status = 'SYNCED'
            )
        else:
            return DeployResponse(
        )
        """

    def testDeployResponse(self):
        """Test DeployResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

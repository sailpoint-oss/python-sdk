# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.update_detail import UpdateDetail

class TestUpdateDetail(unittest.TestCase):
    """UpdateDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateDetail:
        """Test UpdateDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateDetail`
        """
        model = UpdateDetail()
        if include_optional:
            return UpdateDetail(
                message = 'unsupported xsd version, please ensure latest xsd version http://www.sailpoint.com/xsd/sailpoint_form_2_0.xsd is used for source config',
                script_name = 'servicenow',
                updated_files = [pod/org/connectorFiles/testconnector/test1.jar],
                status = 'ERROR'
            )
        else:
            return UpdateDetail(
        )
        """

    def testUpdateDetail(self):
        """Test UpdateDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

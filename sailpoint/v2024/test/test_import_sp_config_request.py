# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v2024.models.import_sp_config_request import ImportSpConfigRequest

class TestImportSpConfigRequest(unittest.TestCase):
    """ImportSpConfigRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportSpConfigRequest:
        """Test ImportSpConfigRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportSpConfigRequest`
        """
        model = ImportSpConfigRequest()
        if include_optional:
            return ImportSpConfigRequest(
                data = bytes(b'blah'),
                options = sailpoint.v2024.models.import_options.ImportOptions(
                    exclude_types = [
                        'SOURCE'
                        ], 
                    include_types = [
                        'TRIGGER_SUBSCRIPTION'
                        ], 
                    object_options = {TRIGGER_SUBSCRIPTION={includedIds=[be9e116d-08e1-49fc-ab7f-fa585e96c9e4], includedNames=[Test 2]}}, 
                    default_references = [
                        'TRIGGER_SUBSCRIPTION'
                        ], 
                    exclude_backup = False, )
            )
        else:
            return ImportSpConfigRequest(
                data = bytes(b'blah'),
        )
        """

    def testImportSpConfigRequest(self):
        """Test ImportSpConfigRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
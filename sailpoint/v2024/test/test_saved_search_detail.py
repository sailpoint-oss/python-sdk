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

from sailpoint.v2024.models.saved_search_detail import SavedSearchDetail

class TestSavedSearchDetail(unittest.TestCase):
    """SavedSearchDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SavedSearchDetail:
        """Test SavedSearchDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SavedSearchDetail`
        """
        model = SavedSearchDetail()
        if include_optional:
            return SavedSearchDetail(
                created = '2018-06-25T20:22:28.104Z',
                modified = '2018-06-25T20:22:28.104Z',
                indices = [identities],
                columns = {identity=[{field=displayName, header=Display Name}, {field=e-mail, header=Work Email}]},
                query = '@accounts(disabled:true)',
                fields = [disabled],
                order_by = {identity=[lastName, firstName], role=[name]},
                sort = [displayName],
                filters = None
            )
        else:
            return SavedSearchDetail(
                indices = [identities],
                query = '@accounts(disabled:true)',
        )
        """

    def testSavedSearchDetail(self):
        """Test SavedSearchDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
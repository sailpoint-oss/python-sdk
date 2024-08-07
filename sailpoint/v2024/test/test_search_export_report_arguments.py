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

from sailpoint.v2024.models.search_export_report_arguments import SearchExportReportArguments

class TestSearchExportReportArguments(unittest.TestCase):
    """SearchExportReportArguments unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchExportReportArguments:
        """Test SearchExportReportArguments
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchExportReportArguments`
        """
        model = SearchExportReportArguments()
        if include_optional:
            return SearchExportReportArguments(
                indices = [entitlements],
                filters = {source.id={type=TERMS, terms=[2c9180897termsId780bd2920576]}, source.name.exact={type=TERMS, terms=[IdentityNow], exclude=true}},
                query = sailpoint.v2024.models.query.Query(
                    query = 'name:a*', 
                    fields = '[firstName,lastName,email]', 
                    time_zone = 'America/Chicago', 
                    inner_hit = sailpoint.v2024.models.inner_hit.InnerHit(
                        query = 'source.name:\"Active Directory\"', 
                        type = 'access', ), ),
                include_nested = True,
                sort = [displayName, +id]
            )
        else:
            return SearchExportReportArguments(
                query = sailpoint.v2024.models.query.Query(
                    query = 'name:a*', 
                    fields = '[firstName,lastName,email]', 
                    time_zone = 'America/Chicago', 
                    inner_hit = sailpoint.v2024.models.inner_hit.InnerHit(
                        query = 'source.name:\"Active Directory\"', 
                        type = 'access', ), ),
        )
        """

    def testSearchExportReportArguments(self):
        """Test SearchExportReportArguments"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2024.models.cluster_manual_upgrade_jobs_inner_managed_process_configuration_ccg import ClusterManualUpgradeJobsInnerManagedProcessConfigurationCcg

class TestClusterManualUpgradeJobsInnerManagedProcessConfigurationCcg(unittest.TestCase):
    """ClusterManualUpgradeJobsInnerManagedProcessConfigurationCcg unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClusterManualUpgradeJobsInnerManagedProcessConfigurationCcg:
        """Test ClusterManualUpgradeJobsInnerManagedProcessConfigurationCcg
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClusterManualUpgradeJobsInnerManagedProcessConfigurationCcg`
        """
        model = ClusterManualUpgradeJobsInnerManagedProcessConfigurationCcg()
        if include_optional:
            return ClusterManualUpgradeJobsInnerManagedProcessConfigurationCcg(
                version = '1798_1054_241.0.0',
                path = 'sailpoint/ccg',
                description = 'CCG Deployment through ops-cli',
                restart_needed = True,
                dependencies = {IQService=743/IQService-743.zip, connector-bundle-jdbc=432/connector-bundle-jdbc-432.zip, connector-bundle-misc=437/connector-bundle-misc-437.zip, connector-bundle-unix=242/connector-bundle-unix-242.zip, connector-common-config=208/connector-common-config-208.zip, connector-bundle-filebased=222/connector-bundle-filebased-222.zip, connector-bundle-imprivata=3/connector-bundle-imprivata-3.zip, connector-bundle-mainframe=211/connector-bundle-mainframe-211.zip, connector-bundle-directories=681/connector-bundle-directories-681.zip, connector-bundle-sap-on-prem=196/connector-bundle-sap-on-prem-196.zip, connector-bundle-webservices=1535/connector-bundle-webservices-1535.zip, connector-bundle-sap-cloud-app=175/connector-bundle-sap-cloud-app-175.zip, connector-bundle-healthcare-epic=302/connector-bundle-healthcare-epic-302.zip, connector-bundle-hrms-oraclefusionhcm=166/connector-bundle-hrms-oraclefusionhcm-166.zip, connector-bundle-collaboration-connectors=246/connector-bundle-collaboration-connectors-246.zip}
            )
        else:
            return ClusterManualUpgradeJobsInnerManagedProcessConfigurationCcg(
                version = '1798_1054_241.0.0',
                path = 'sailpoint/ccg',
                description = 'CCG Deployment through ops-cli',
                restart_needed = True,
                dependencies = {IQService=743/IQService-743.zip, connector-bundle-jdbc=432/connector-bundle-jdbc-432.zip, connector-bundle-misc=437/connector-bundle-misc-437.zip, connector-bundle-unix=242/connector-bundle-unix-242.zip, connector-common-config=208/connector-common-config-208.zip, connector-bundle-filebased=222/connector-bundle-filebased-222.zip, connector-bundle-imprivata=3/connector-bundle-imprivata-3.zip, connector-bundle-mainframe=211/connector-bundle-mainframe-211.zip, connector-bundle-directories=681/connector-bundle-directories-681.zip, connector-bundle-sap-on-prem=196/connector-bundle-sap-on-prem-196.zip, connector-bundle-webservices=1535/connector-bundle-webservices-1535.zip, connector-bundle-sap-cloud-app=175/connector-bundle-sap-cloud-app-175.zip, connector-bundle-healthcare-epic=302/connector-bundle-healthcare-epic-302.zip, connector-bundle-hrms-oraclefusionhcm=166/connector-bundle-hrms-oraclefusionhcm-166.zip, connector-bundle-collaboration-connectors=246/connector-bundle-collaboration-connectors-246.zip},
        )
        """

    def testClusterManualUpgradeJobsInnerManagedProcessConfigurationCcg(self):
        """Test ClusterManualUpgradeJobsInnerManagedProcessConfigurationCcg"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

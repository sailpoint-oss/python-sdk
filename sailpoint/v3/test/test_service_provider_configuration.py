# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v3.models.service_provider_configuration import ServiceProviderConfiguration

class TestServiceProviderConfiguration(unittest.TestCase):
    """ServiceProviderConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceProviderConfiguration:
        """Test ServiceProviderConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceProviderConfiguration`
        """
        model = ServiceProviderConfiguration()
        if include_optional:
            return ServiceProviderConfiguration(
                enabled = True,
                bypass_idp = True,
                saml_configuration_valid = True,
                federation_protocol_details = [{role=SAML_IDP, entityId=http://www.okta.com/exktq4o24bmQA4fr60h7, cert=MIIDpDCCAoygAwIBAgIGAYhZ+b29MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5jaXNjbzENMAsGA1UECgwET2t0YTEUMBIGA1UECwwLU1NPUHJvdmlkZXIxEzARBgNVBAMMCmRldi0yMDY0NDUxHDAaBgkqhkiG9w0BCQEWDWluZm9Ab2t0YS5jb20wHhcNMjMwNTI2MjEzMDU5WhcNMzMwNTI2MjEzMTU5WjCBkjELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExFjAUBgNVBAcMDVNhbiBGcmFuY2lzY28xDTALBgNVBAoMBE9rdGExFDASBgNVBAsMC1NTT1Byb3ZpZGVyMRMwEQYDVQQDDApkZXYtMjA2NDQ1MRwwGgYJKoZIhvcNAQkBFg1pbmZvQG9rdGEuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwvi1+WbF2ceGlLCrLl5PrG1lpj04IsrHX6OE666ObC2WFh+Nxvpxy+Vmzon9c9+akhK3bTv+9ifEoVc6tA1qWuCfXISAn9g81JqI68I1PGUbe6eF8pmOA18rjOrt7x94k4QukpR3+I8DfPJ+TynatltB51laLb8H4jchMafA4rDTjV/ZiYPxV0LMEIbprVyGuvBEhiEWha3wwVdDuJq996okX36YNS8PcGH+5CJ8c3YWZp/wrspgJmfCooMXeV+6zBpZfXqPpMWlUo0gcZqDOFgy3r4vkXehJdVYRlInMfDv04Lvy8VI1YAZClG/duO/6o9YVUFLjD9s+mQfhgaF5wIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQB1CTrA/pTHkarbhMHsdSFAjVoYWwdAfrssG99rIjwwr/CW9tavTC3keaoUmUeddcnLY4V/TfL07+xgQGHCBR88cnzG9h6rC9qWxt6C3nug3YDVQfkdCDgnW9A8QEvLeq/KVLoRccpJNEENb2Y5ESUXHi1+PtjkFBtvfSgZ4eEhVggirL0bJdWVm700hCnjb2iCGSbSX7WflfPi0GSmjht983caG9OwZDnDzNFt8qGWCxo4bNSThT00JnWEN/6f1BWNOt9YDrxqEyNclqhLL+RDqFsPBFIrQlsoXzqpWqCL8oS9UMNxbGATK2v3d5ueE9+SswBAFBhirCuqZw19Ri2W, loginUrlPost=https://dev-206445.oktapreview.com/app/tivolidev206445_acmeidntest_1/exktq4o24bmQA4fr60h7/sso/saml, loginUrlRedirect=https://dev-206445.oktapreview.com/app/tivolidev206445_acmeidntest_1/exktq4o24bmQA4fr60h7/sso/saml, logoutUrl=https://dev-206445.oktapreview.com/login/signout, nameId=urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress, binding=urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST, authnContext=urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport, includeAuthnContext=true, mappingAttribute=email, jitConfiguration={enabled=true, sourceId=2c9180897427f3a501745042afc83144, sourceAttributeMappings={firstName=okta.firstName, lastName=okta.lastName, email=okta.email}}, certificateExpirationDate=Thu May 26 21:31:59 GMT 2033, certificateName=EMAILADDRESS=info@okta.com, CN=dev-206445, OU=SSOProvider, O=Okta, L=San Francisco, ST=California, C=US}, {role=SAML_SP, entityId=https://acme.identitysoon.com/sp, alias=acme-sp, callbackUrl=https://acme.test-login.sailpoint.com/saml/SSO/alias/acme-sp, legacyAcsUrl=https://megapod-useast1-sso.identitysoon.com/sso/Consumer/metaAlias/acme/sp}]
            )
        else:
            return ServiceProviderConfiguration(
        )
        """

    def testServiceProviderConfiguration(self):
        """Test ServiceProviderConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
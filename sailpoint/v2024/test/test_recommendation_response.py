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

from sailpoint.v2024.models.recommendation_response import RecommendationResponse

class TestRecommendationResponse(unittest.TestCase):
    """RecommendationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecommendationResponse:
        """Test RecommendationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecommendationResponse`
        """
        model = RecommendationResponse()
        if include_optional:
            return RecommendationResponse(
                request = sailpoint.v2024.models.recommendation_request.RecommendationRequest(
                    identity_id = '2c938083633d259901633d25c68c00fa', 
                    item = sailpoint.v2024.models.access_item_ref.AccessItemRef(
                        id = '2c938083633d259901633d2623ec0375', 
                        type = 'ENTITLEMENT', ), ),
                recommendation = 'true',
                interpretations = [75% of identities with the same department have this access. This information had a high impact on the overall score., 67% of identities with the same peer group have this access. This information had a low impact on the overall score., 42% of identities with the same location have this access. This information had a low impact on the overall score.],
                translation_messages = [{key=recommender-api.V2_WEIGHT_FEATURE_PRODUCT_INTERPRETATION_HIGH, values=[75, department]}],
                recommender_calculations = sailpoint.v2024.models.recommender_calculations.RecommenderCalculations(
                    identity_id = '2c91808457d8f3ab0157e3e62cb4213c', 
                    entitlement_id = '2c91809050db617d0150e0bf3215385e', 
                    recommendation = 'YES', 
                    overall_weighted_score = 1.337, 
                    feature_weighted_scores = {
                        'key' : 1.337
                        }, 
                    threshold = 1.337, 
                    identity_attributes = {
                        'key' : sailpoint.v2024.models.recommender_calculations_identity_attributes_value.RecommenderCalculations_identityAttributes_value(
                            value = '', )
                        }, 
                    feature_values = sailpoint.v2024.models.feature_value_dto.FeatureValueDto(
                        feature = 'department', 
                        numerator = 14, 
                        denominator = 14, ), )
            )
        else:
            return RecommendationResponse(
        )
        """

    def testRecommendationResponse(self):
        """Test RecommendationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
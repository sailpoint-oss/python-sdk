# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.api.workflows_api import WorkflowsApi


class TestWorkflowsApi(unittest.TestCase):
    """WorkflowsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WorkflowsApi()

    def tearDown(self) -> None:
        pass

    def test_cancel_workflow_execution(self) -> None:
        """Test case for cancel_workflow_execution

        Cancel Workflow Execution by ID
        """
        pass

    def test_create_workflow(self) -> None:
        """Test case for create_workflow

        Create Workflow
        """
        pass

    def test_delete_workflow(self) -> None:
        """Test case for delete_workflow

        Delete Workflow By Id
        """
        pass

    def test_get_workflow(self) -> None:
        """Test case for get_workflow

        Get Workflow By Id
        """
        pass

    def test_get_workflow_execution(self) -> None:
        """Test case for get_workflow_execution

        Get Workflow Execution
        """
        pass

    def test_get_workflow_execution_history(self) -> None:
        """Test case for get_workflow_execution_history

        Get Workflow Execution History
        """
        pass

    def test_get_workflow_executions(self) -> None:
        """Test case for get_workflow_executions

        List Workflow Executions
        """
        pass

    def test_list_complete_workflow_library(self) -> None:
        """Test case for list_complete_workflow_library

        List Complete Workflow Library
        """
        pass

    def test_list_workflow_library_actions(self) -> None:
        """Test case for list_workflow_library_actions

        List Workflow Library Actions
        """
        pass

    def test_list_workflow_library_operators(self) -> None:
        """Test case for list_workflow_library_operators

        List Workflow Library Operators
        """
        pass

    def test_list_workflow_library_triggers(self) -> None:
        """Test case for list_workflow_library_triggers

        List Workflow Library Triggers
        """
        pass

    def test_list_workflows(self) -> None:
        """Test case for list_workflows

        List Workflows
        """
        pass

    def test_patch_workflow(self) -> None:
        """Test case for patch_workflow

        Patch Workflow
        """
        pass

    def test_post_external_execute_workflow(self) -> None:
        """Test case for post_external_execute_workflow

        Execute Workflow via External Trigger
        """
        pass

    def test_post_workflow_external_trigger(self) -> None:
        """Test case for post_workflow_external_trigger

        Generate External Trigger OAuth Client
        """
        pass

    def test_put_workflow(self) -> None:
        """Test case for put_workflow

        Update Workflow
        """
        pass

    def test_test_external_execute_workflow(self) -> None:
        """Test case for test_external_execute_workflow

        Test Workflow via External Trigger
        """
        pass

    def test_test_workflow(self) -> None:
        """Test case for test_workflow

        Test Workflow By Id
        """
        pass


if __name__ == '__main__':
    unittest.main()

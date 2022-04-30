from unittest import TestCase

from jira import JIRAError

from jira_client import JiraClient


class TestJira(TestCase):
    def setUp(self) -> None:
        host = "https://issues.apache.org/jira/"
        self.jira = JiraClient(host)

    def test_01_get_issue(self):
        issue = self.jira.get_issue("AIRFLOW-1")
        self.assertEqual(issue.fields.summary, "Migrate GitHub code to Apache git")

    def test_02_get_non_exist_issue(self):
        with self.assertRaises(JIRAError) as e:     # pylint: disable=invalid-name
            self.jira.get_issue("AIRFLOWW-1")

        self.assertEqual(e.exception.status_code, 404)

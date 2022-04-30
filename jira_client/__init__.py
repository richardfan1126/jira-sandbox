from jira import JIRA, Issue


class JiraClient:   # pylint: disable=too-few-public-methods
    def __init__(self, host: str, username: str = None, password: str = None) -> None:
        auth = None
        if username and password:
            auth = (username, password)

        self.jira = JIRA(host, basic_auth = auth)

    def get_issue(self, key: str) -> Issue:
        return self.jira.issue(key)

from jira_client import JiraClient


def main():
    host = "https://issues.apache.org/jira/"

    jira = JiraClient(host)
    issue = jira.get_issue("AC-1")

    print(issue.fields.summary)

if __name__ == "__main__":
    main()

# Automating Data Pipeline Workflow using github actions 

This GitHub Actions workflow automates the execution of a data pipeline that fetches data from Reddit using credentials stored in GitHub Secrets, processes it, and pushes any changes back to the repository.

## Workflow Overview

The workflow runs either on a scheduled basis (daily) or manually via a dispatch event. It checks out the repository content, sets up a Python environment, installs dependencies, runs the data pipeline, and commits and pushes any changes made to the repository.

## Workflow Trigger

- **Scheduled Trigger**: The workflow is scheduled to run daily at 12:35 AM UTC.
  ```yaml
  cron: "48 15 * * *"
- **Manual Trigger**: The workflow can also be triggered manually using GitHub's workflow_dispatch event.
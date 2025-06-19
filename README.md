# 🔐 Brute Force Login Detection with Flask on Azure

## 🧪 Lab Overview

This project demonstrates how to deploy a Python Flask application to Azure App Service and detect brute-force login behavior using Azure Log Analytics and Azure Monitor Alerts.

The application includes a `/login` endpoint that logs both successful and failed login attempts. The logs are sent to Azure Monitor via Diagnostic Settings, and a KQL query is used to detect potential brute-force login attacks. An alert rule is configured to notify via email when more than 5 failed login attempts occur within a 5-minute window.

### Youtube link- https://youtu.be/B99fBld-olI

---

## 📦 Project Structure

├── app.py # Flask application with login route

├── requirements.txt # Python dependencies

├── test-app.http # Test file for REST Client (VS Code)

├── README.md # This file


---

## 🚀 What I Learned

- Deploying Python Flask apps to Azure App Services
- Setting up Diagnostic Settings to connect logs to Log Analytics Workspace
- Writing KQL queries to filter specific log events
- Creating Azure Monitor alert rules and email notifications
- Debugging app logging and ingestion issues in a cloud environment

---

## ⚠️ Challenges Faced

- Logs from `app.logger.warning()` were not showing up in Log Analytics due to stdout not being captured as expected by Azure.
- AppServiceConsoleLogs were capturing system logs, but not custom application logs consistently.
- To address this, logging was redirected to stdout using Python's `StreamHandler`, and a fallback query strategy was planned.

---

## 🔎 KQL Query Used

This query is intended to detect failed login attempts based on log output:

```kql
AppServiceConsoleLogs
| where TimeGenerated > ago(10m)
| where ResultDescription has "Failed login attempt"

Note: Due to ingestion issues, logs from the app did not consistently appear. However, the detection logic and alert rule were successfully configured.

.

 Azure Monitor Alert Configuration
Signal type: Log (Custom Log Search)

Scope: Log Analytics Workspace

Query: See above

Threshold: More than 5 table rows in 5 minutes

Evaluation frequency: Every 1 minute

Action Group: Email notification to the student

Severity: 2 (High)


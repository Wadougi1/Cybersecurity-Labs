# Log Analysis and Insider Threat Detection

This module contains scripts and reports focused on analyzing system access logs to detect unauthorized or anomalous activity within an organization's network.

## Research Context

Access log analysis is a foundational skill in cybersecurity operations. Organizations generate thousands of access events daily, and manually reviewing them is impractical. Automated log analysis enables security teams to quickly identify **cross-departmental access violations**, **privilege misuse**, and **insider threats** before they escalate into data breaches.

This module demonstrates the ability to programmatically parse, normalize, and analyze access logs using Python, producing structured outputs that can feed directly into a Security Information and Event Management (SIEM) pipeline or incident response workflow.

## Project Overview

**Project:** Cross-Departmental Resource Access Detection  
**Course:** Graduate Cybersecurity Lab — UNC Charlotte  
**Objective:** Identify employees who accessed resources belonging to departments other than their own, flagging potential insider threats or policy violations.

## Methodology

1. **Data Ingestion:** Loaded access logs, employee records, and department-resource mappings from CSV files.
2. **Normalization:** Standardized employee IDs, department names, and resource identifiers to ensure consistent matching across datasets.
3. **Cross-Reference Analysis:** Merged datasets to map each access event to the employee's department and the resource's owning department.
4. **Anomaly Flagging:** Identified and extracted all events where the employee's department did not match the resource's department.
5. **Output Generation:** Exported flagged events to a structured CSV report for further review.

## Files

| File | Description |
| :--- | :--- |
| `access_log_analyzer.py` | Python script that parses and analyzes access logs to detect cross-departmental access violations. |
| `reports/Access_Log_Analysis_Summary.pdf` | Full project report including methodology, findings, and sample output. |

## Key Findings

- Multiple employees from the **Finance** and **HR** departments were flagged for accessing **IT-owned resources** (e.g., AuthServer).
- The script successfully identified **cross-departmental access patterns** that could indicate unauthorized privilege use or misconfigured access controls.
- All flagged events were exported to `cross_dept_accesses.csv` for further investigation.

## Skills Demonstrated

- Python scripting for security data analysis
- Log normalization and data cleaning using Pandas
- Insider threat detection logic
- Structured reporting of security findings
- Access control auditing and policy enforcement analysis

## Tools Used

| Tool | Purpose |
| :--- | :--- |
| Python 3 | Scripting and automation |
| Pandas | Data loading, normalization, and analysis |
| CSV | Input/output data format |
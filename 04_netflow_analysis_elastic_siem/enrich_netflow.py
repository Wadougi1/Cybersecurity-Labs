"""
Netflow Enrichment Script
Author: Douglas Kwarteng
Date: 2026-03-25

This script enriches netflow logs by adding:
- src_ip_internal
- des_ip_internal
- des_ip_company
- total_bytes
"""

import json
import ipaddress
import pandas as pd
import requests

INPUT_FILE = "nf-log.json"
OUTPUT_FILE = "enriched_netflow.json"


def is_internal_ip(ip):
    """Return 1 if the IP is private/internal, otherwise 0."""
    try:
        return 1 if ipaddress.ip_address(str(ip).strip()).is_private else 0
    except ValueError:
        return 0


def lookup_asn_org(ip):
    """Get ASN organization name for a public IP from ipinfo.io."""
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=3)
        response.raise_for_status()
        return response.json().get("org", "")
    except requests.RequestException:
        return ""


def map_company(org):
    """Map ASN organization name to the required company categories."""
    org = org.lower()
    if "microsoft" in org:
        return "Microsoft"
    if "google" in org:
        return "Google"
    if "amazon" in org or "aws" in org:
        return "Amazon"
    if "facebook" in org or "meta" in org:
        return "Facebook"
    return "None"


def load_json_records(file_path):
    """Load records from NDJSON or JSON array format."""
    records = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read().strip()

    for line in content.splitlines():
        try:
            record = json.loads(line)
            if isinstance(record, dict):
                records.append(record)
        except json.JSONDecodeError:
            continue

    if records:
        return records

    try:
        data = json.loads(content)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return [data]
    except json.JSONDecodeError:
        pass

    return []


def main():
    records = load_json_records(INPUT_FILE)
    if not records:
        raise ValueError("No valid JSON records found in the input file.")

    df = pd.DataFrame(records)

    df["src_ip_internal"] = df["src_ip"].apply(is_internal_ip)
    df["des_ip_internal"] = df["dest_ip"].apply(is_internal_ip)

    ip_cache = {}

    def classify_dest_ip(dest_ip):
        dest_ip = str(dest_ip).strip()
        if is_internal_ip(dest_ip) == 1:
            return "None"
        if dest_ip in ip_cache:
            return ip_cache[dest_ip]
        org = lookup_asn_org(dest_ip)
        company = map_company(org)
        ip_cache[dest_ip] = company
        return company

    df["des_ip_company"] = df["dest_ip"].apply(classify_dest_ip)

    df["total_bytes"] = (
        pd.to_numeric(df["bytes_toserver"], errors="coerce").fillna(0) +
        pd.to_numeric(df["bytes_toclient"], errors="coerce").fillna(0)
    )

    df.to_json(OUTPUT_FILE, orient="records", lines=True)

    print(f"Enriched dataset saved to {OUTPUT_FILE}")
    print("\nCompany distribution:")
    print(df["des_ip_company"].value_counts())


if __name__ == "__main__":
    main()
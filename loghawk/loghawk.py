import re

# === Load each log file ===
with open("access.log") as f:
    access_log = f.readlines()
with open("app.log") as f:
    app_log = f.readlines()
with open("auth.log") as f:
    auth_log = f.readlines()
with open("system.log") as f:
    system_log = f.readlines()

# === Define patterns and labels ===
patterns = {
    "access.log": {
        "Too Many 401 Errors (Access Denied)": r'401',
        "Repeated Access to /admin": r'/admin',
        "Blocked wp-login Attempts": r'/wp-login\.php',
    },
    "app.log": {
        "CRITICAL Errors in App": r'CRITICAL:',
        "ERROR Messages in App": r'ERROR:',
        "WARNINGs in App": r'WARNING:',
        "Repeated Access to /admin": r'/admin',
    },
    "auth.log": {
        "Failed SSH Logins": r'Failed password',
        "Invalid User Logins": r'invalid user',
    },
    "system.log": {
        "WARNINGs in App": r'WARNING:',
        "Suspicious Script Execution (CRON)": r'(malware\.py|malicious\.py|security_check\.py)',
        "Firewall Blocking": r'Firewall: blocked connection',
        "Unusual Traffic or CPU": r'(Suspicious activity|High CPU usage|Unusual number of connections)',
    }
}

# === Function to extract IP from a log line ===
def extract_ip(line):
    match = re.search(r'(\d{1,3}(?:\.\d{1,3}){3})', line)
    return match.group(1) if match else "No IP"

# === Function to scan log content ===
def scan_log(file_name, log_lines, rule_set):
    print(f"\n===== Scanning {file_name} =====")
    for label, pattern in rule_set.items():
        regex = re.compile(pattern)
        for line in log_lines:
            if regex.search(line):
                ip = extract_ip(line)
                print(f"[{file_name}] {label} ⚠️ Line: {line.strip()} | IP: {ip}")

# === Run the scans ===
scan_log("access.log", access_log, patterns["access.log"])
scan_log("app.log", app_log, patterns["app.log"])
scan_log("auth.log", auth_log, patterns["auth.log"])
scan_log("system.log", system_log, patterns["system.log"])

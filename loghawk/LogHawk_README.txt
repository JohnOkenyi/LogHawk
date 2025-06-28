LogHawk - README 

LogHawk is a lightweight, open-source tool that helps security teams automatically monitor and analyze log files for suspicious activity such as failed login attempts, unauthorized access, critical application errors, and more.

Installation
------------
Make sure Python 3 is installed on your system. You can install it with:

    sudo apt-get install python3

Usage
-----
Run the LogHawk tool on your log files using the command below:

    python3 loghawk.py

Make sure 'loghawk.py' and the log files (access.log, auth.log, app.log, system.log) are in the same directory.

Example Output:
    [app.log] CRITICAL Errors in App ⚠ Line: CRITICAL: Something broke | IP: 192.168.0.12
    [access.log] Repeated Access to /admin ⚠ Line: GET /admin HTTP/1.1 | IP: 192.168.0.10

Automating with Cron
---------------------
To make LogHawk run automatically every 10 minutes, follow these steps:

1. Open the crontab editor:

    crontab -e

2. Add the following line (replace with the actual path to your script):

    */10 * * * * /usr/bin/python3 /path/to/loghawk.py >> /path/to/log_output.log 2>&1

This command will run the script every 10 minutes and log output to log_output.log.

Log Files Supported
-------------------
LogHawk supports monitoring the following log files 
- access.log
- auth.log
- app.log
- system.log

Contributing
------------
Contributions are welcome! Feel free to open an issue or submit a pull request.

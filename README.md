# Verihash

Python script for validating hashes of files on Linux systems

Note: example.csv can be used to test this tool, the first 3 test files should show up as good but the last test should fail

# Systemd Service
The verihash.service file is provided to easily setup a systemd service to run verihash at a timed interval, by default 15 minutes
By default, the default.csv file is used as the csv file to check
To enable the service, simply place verihash.service and verihash.timer in the /lib/systemd/system directory and run the following commands:
    sudo systemctl daemon-reload
    sudo systemctl enable verihash.timer
    sudo systemctl start verihash.timer


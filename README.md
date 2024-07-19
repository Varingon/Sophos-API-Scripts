# Sophos Endpoint Management Scripts

This repository contains two Python scripts designed to interact with the Sophos API. These scripts allow you to convert computer hostnames to endpoint IDs and subsequently delete endpoints based on those IDs.

## Requirements

1) A Sophos environment
2) Sophos Client ID and Secret
3) Python
4) Requests library: ```pip install requests```


# Scripts

## convertHostnameToEndpointID.py

This script authenticates with the Sophos API using provided client credentials, retrieves the tenant ID and data region, reads a list of computer names from a file (computers.txt), and finds the corresponding endpoint IDs. The IDs are then exported to a file (new_computers.txt).

1) Ensure you have the requests library installed:  ```pip install requests```
2) Create a file named computers.txt in the same directory as your script. List the computer names (one per line) that you want to query.
3) Replace "YOUR_CLIENT_ID" with your actual client ID.
4) Execute the script and input your client secret when prompted:


## deleteSophosByEndpointID.py

This script authenticates with the Sophos API, reads a list of endpoint IDs from a file (new_computers.txt), and deletes these endpoints.

1) Replace "YOUR_CLIENT_ID" with your actual client ID.
2) Execute the script and input your client secret when prompted.



### Notes
1) Ensure you handle and store your client secret securely.
2) Both scripts assume that the computer names in computers.txt are formatted correctly for the API. Adjust the formatting as necessary based on your actual computer name formats.
3) Ensure you have the necessary permissions to execute these operations in your Sophos environment

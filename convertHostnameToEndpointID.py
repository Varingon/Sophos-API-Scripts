import os
import requests

def authenticate(client_id, client_secret):
    url = "https://id.sophos.com/api/v2/oauth2/token"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'token'
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        auth_response = response.json()
        jwt_token = auth_response['access_token']
        print("Authentication successful. JWT token acquired.")
        return jwt_token
    else:
        print("Authentication failed.")
        return None

def find_tenant_id(jwt_token):
    url = "https://api.central.sophos.com/whoami/v1"
    headers = {
        'Authorization': f'Bearer {jwt_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tenant_id = response.json()['id']
        data_region = response.json()['apiHosts']['dataRegion']
        print("Tenant ID found:", tenant_id)
        print("Data region found:", data_region)
        return tenant_id, data_region
    else:
        print("Failed to find Tenant ID.")
        return None, None
    
def read_computer_names(file_path):
    with open(file_path, 'r') as file:
        computer_names = file.readlines()
    computer_names = [computer_name.strip() for computer_name in computer_names]
    return computer_names

def find_endpoint_id(computer_name, token, data_region, tenant_id):
    url = f"{data_region}/endpoint/v1/endpoints?hostnameContains={computer_name[3:]}"
    headers = {
        'Authorization': f'Bearer {token}',
        'X-Tenant-ID': tenant_id
    }
    response = requests.get(url, headers=headers)
    print(computer_name)
    if response.status_code == 200:
        response_data = response.json()
        num_entries = len(response_data.get('items', []))
        # Assuming the JSON data is stored in a variable named 'data'
        if num_entries == 1:
            if 'items' in response_data:
                for item in response_data['items']:
                    if 'id' in item:              
                        f = open(export_path, "a")
                        f.write(item['id'] + "\n")
                        f.close
                        print(item['id'])
        else:
            print("More than one result for: " + computer_name)
            f = open("failed_computers.txt", "a")
            f.write(computer_name + "\n")
            f.close


client_id = "CLIENT ID HERE"
client_secret = input("Enter CLIENT_SECRET: ")  
file_path = "computers.txt"
export_path = "new_computers.txt"

# Authenticate and obtain JWT token
jwt_token = authenticate(client_id, client_secret)

if jwt_token:
    tenant_id, data_region = find_tenant_id(jwt_token)
    
    if tenant_id and data_region:
        endpoint_ids = read_computer_names(file_path)

        for endpoint_id in endpoint_ids:
            find_endpoint_id(endpoint_id, jwt_token, data_region, tenant_id)
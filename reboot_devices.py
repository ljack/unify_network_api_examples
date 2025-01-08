import requests
import time

# Replace these with actual values
host = "https://api.example.com"
auth_token = "your_auth_token"  # Replace with a valid authentication token

# Headers for all requests
headers = {
    "Authorization": f"Bearer {auth_token}",
    "Content-Type": "application/json",
}

def get_info():
    """
    Retrieves basic API information.
    """
    url = f"{host}/v1/info"
    response = requests.get(url, headers=headers)
    return response.json()

def get_sites():
    """
    Retrieves all sites.
    """
    url = f"{host}/v1/sites"
    response = requests.get(url, headers=headers)
    return response.json()

def get_devices(site_id):
    """
    Retrieves devices for a specific site.
    """
    url = f"{host}/v1/sites/{site_id}/devices"
    response = requests.get(url, headers=headers)
    return response.json()

def reboot_device(site_id, device_id):
    """
    Sends a POST request to reboot a device.
    """
    url = f"{host}/v1/sites/{site_id}/devices/{device_id}/actions"
    payload = {"action": "RESTART"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def loop_through_devices(site_id, devices):
    """
    Loops through all devices and reboots them, skipping specific ones.
    """
    for device in devices:
        print(f"Processing Device ID: {device['id']}, Name: {device['name']}")
        
        # Skip if the device name is 'Dream Machine SE'
        if device['name'] == "Dream Machine SE":
            print(f"Skipping {device['name']}")
            continue

        # Reboot the device
        print(f"Rebooting Device ID: {device['id']}")
        response = reboot_device(site_id, device['id'])
        print(f"Reboot response: {response}")

        # Sleep for 50 seconds before the next request
        print("Sleeping for 50 seconds...")
        time.sleep(50)

    print("All devices processed.")

# Main program logic
def main():
    print("Fetching API Info...")
    info = get_info()
    print("API Info:", info)

    print("\nFetching Sites...")
    sites = get_sites()
    print("Sites:", sites)

    # Assuming we process the first site
    if not sites:
        print("No sites found. Exiting.")
        return
    
    site_id = sites[0]['id']  # Replace with logic to choose a site if needed
    print(f"\nProcessing Site ID: {site_id}")

    print("\nFetching Devices...")
    devices = get_devices(site_id)
    print(f"Devices for Site {site_id}:", devices)

    print("\nLooping Through Devices...")
    loop_through_devices(site_id, devices)

if __name__ == "__main__":
    main()

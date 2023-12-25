import requests
import json
import logging

api_key = 'fsq3hWTfV6RzWgYpedrH+1UYPwzhrUaG8DhNIN0eOqKcGUc='

def setup_logging():
    logging.basicConfig(filename='checkin_log.log', level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_latest_checkin(api_key):
    try:
        # Replace with the actual API endpoint and parameters
        url = f"https://api.foursquare.com/v2/checkins/recent?oauth_token={api_key}&v=20231225"
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from Foursquare: {e}")
        return None

def write_to_json(data, filename='latest_checkin.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info("Data written to JSON file successfully.")
    except Exception as e:
        logging.error(f"Error writing data to JSON file: {e}")

def main():
    setup_logging()
    data = fetch_latest_checkin(api_key)
    if data:
        write_to_json(data)
    else:
        logging.info("No new data to write.")

if __name__ == "__main__":
    main()

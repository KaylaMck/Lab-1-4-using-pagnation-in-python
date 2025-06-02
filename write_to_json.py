import requests
import json

# Get the token first
api_url = 'https://developyr-api.azurewebsites.net/api'
credentials = {
    "username": "admin",
    "password": "password123"
}

auth_response = requests.post(api_url + "/auth", json=credentials)

if auth_response.status_code == 200:
    token = auth_response.json()
    bearer_token = token.get("token")
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "accept": "application/json"
    }
    
    # Now get the people data
    offset = 0
    
    while True:
        # Ask for 10 people
        url = f'https://developyr-api.azurewebsites.net/api/people?offset={offset}&limit=10'
        response = requests.get(url, headers=headers)
        
        # Get the whole response
        full_response = response.json()
        
        # Pull out just the people
        people = full_response["data"]
        
        print(f"Got {len(people)} people")
        
        # If no people, stop
        if len(people) == 0:
            break
        
        # Save each person
        with open('people.json', 'a') as file:
            for person in people:
                json.dump(person, file)
                file.write('\n')
        
        # Ask for the next 10
        offset = offset + 10
    
    print("Done!")
    
else:
    print(f"Login failed: {auth_response.status_code}")
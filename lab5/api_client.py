import os
import json
import requests

API_URL = "https://jsonplaceholder.typicode.com/todos"
OUTPUT_FILE = "frontend_feed.json"

def fetch_and_transform():
    token = os.getenv("API_TOKEN", "dev_token")
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "B1-AI-Pipeline/1.0"
    }

    try:
        # TODO 1: Send GET request with headers and 5-second timeout
        response = requests.get(headers=headers, url=API_URL, timeout=5)

        # TODO 2: Verify HTTP status code (raise exception on 4xx/5xx)
        response.raise_for_status()
        # https://www.geeksforgeeks.org/python/response-raise_for_status-python-requests/

        raw_data = response.json()
        '''
        liste de dictionnaire de forme 
        [
            {
                "userId": 10,
                "id": 200,
                "title": "ipsam aperiam voluptates qui",
                "completed": false
            }
        ]
        '''

        # TODO 3: Validate payload type and filter/transform records for userId == 1
        # on aura la même forme mais uniquement avec les user dont l'ID = 1 
        cleaned_records = []
        if raw_data and type(raw_data) is list :
            for user_infos in raw_data:
                if user_infos["userId"] == 1:
                    cleaned_records.append({
                        "task_id": user_infos["id"],
                        "label": user_infos["title"],
                        "is_done": user_infos["completed"]
                    })

        # TODO 4: Write cleaned_records to OUTPUT_FILE with indent=2
        '''
        https://docs.python.org/3/library/json.html?

        with -> pour gérer l'ouverture / la fermeture du fichier automatiquement 
        https://www.docstring.fr/glossaire/with/

        'w' -> écrire dans le fichier
        https://www.geeksforgeeks.org/python/with-statement-in-python/

        '''
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(cleaned_records, f, indent=2, ensure_ascii=False)
        print(f"Successfully exported {len(cleaned_records)} records to {OUTPUT_FILE}.")

    except requests.exceptions.Timeout:
        print("ERROR: Request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP ERROR: {e}")
    except Exception as e:
        print(f"UNEXPECTED ERROR: {e}")

if __name__ == "__main__":
    fetch_and_transform()
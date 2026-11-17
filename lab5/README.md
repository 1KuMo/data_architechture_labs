# API Contract
> **Note:**I used AI to improve the visual presentation of this readme, but the work is mine.

## JSON schema

The backend sends this JSON structure to the Front-End:

```json
{
  "task_id": 1,
  "label": "delectus aut autem",
  "is_done": false
}
```

- `task_id`: integer
- `label`: string
- `is_done`: boolean

The data is sent as a JSON list in `frontend_feed.json`.

## Architecture

```text
[External API]
     |
     | HTTPS - Port 443 - JSON
     | GET /todos
     v
[Python Backend]
     |
     | Write JSON
     v
[frontend_feed.json]
     |
     v
[Local HTTP Server - Port 8080]
     |
     | HTTP GET - JSON
     v
[Front-End Client]
```


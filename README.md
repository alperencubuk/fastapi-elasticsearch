# FastAPI Elasticsearch

---
### Summary:

```
Basic FastAPI, Elasticsearch example.
```

### Requirements:

```
docker
```

### Run:

```
cp config/.env.example config/.env
docker compose up --build -d
```

### Docs:

```
localhost:8000/docs
```

### Endpoints:

```http request
POST   /books                            # book add
GET    /books                            # book search

GET    /                                 # health check
```

### Example Requests/Responses:

#### Request:
```http request
POST /books

Body:
{
    "title": "hello",
    "detail": "world"
}
```

#### Response:
```json
{
    "title": "hello",
    "detail": "world"
}
```

#### Request:
```http request
GET /books?query=hello&fields=title

Query:
query: str = Search string (required)
fields: str = Search fields (optional) (default=title, detail)
```

#### Response:
```json
[
  {
    "title": "hello",
    "detail": "world"
  }
]

```

---

# Kurz Flask

A simple URL shortening tool in Flask, Postgres and Docker


# Underlying Stack 
* Flask
* Postgres

# Requirements
* Docker
* Docker-compose

# Commands
```
```bash
docker-compose -f docker-compose.yml up --build

# Create a shortened URL
curl -d '{"url":"http://google.com"}' -H "Content-Type: application/json" -X POST http://localhost:5001/shortner     

# Response
{
  "digest": "c7b920", 
  "status": "success"
}


# Retrive a URL from digest
curl -X GET http://localhost:5001/shortner/c7b920

# Response
{
  "data": {
    "digest": "c7b920", 
    "url": "http://google.com"
  }, 
  "status": "success"
}


# Retrive a list of URLs and digest
curl -X GET http://localhost:5001/shortner

# Response
{
  "data": {
    "shortner": [
      {
        "digest": "c7b920", 
        "url": "http://google.com"
      }, 
      {
        "digest": "873c87", 
        "url": "http://yahoo.com"
      }
    ]
  }, 
  "status": "success"
}
```

# License
MIT
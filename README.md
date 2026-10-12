# SEC101 Lab: Python API Client in Docker

A small Python client that sends GET and POST requests to an echo API,
uses custom headers, parses JSON responses, and runs inside a Docker container.

Built as the final lab for **SEC 101** in my AI Security & AI Red Teaming learning path.

## What it does

- Sends a **GET** request with custom headers and query parameters
- Sends a **POST** request with a JSON payload
- Prints what the server actually received (headers, params, JSON)

## Run it

Requires Docker.

```bash
docker build -t sec101-lab .
docker run --rm sec101-lab
```

## Security choices

- Runs as a **non-root user** (`appuser`) inside the container
- Uses a minimal base image (`python:3.12-slim`)
- Sets a request **timeout** so the script doesn't hang on slow servers

## Next steps

This is the foundation for future AI red teaming tools: the same pattern
(POST + JSON + headers) is how you talk to LLM APIs. Planned next:
a script that sends a list of test prompts to a model and logs the responses.
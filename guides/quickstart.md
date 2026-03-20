# Quickstart Guide

## Step 1: Authentication

Obtain your API token from the dashboard.

## Step 2: Make Your First Request

```bash
curl -X POST https://api.example.com/orders \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{ ... }'
```

## Step 3: Handle Response
Check for success or error codes and handle accordingly.

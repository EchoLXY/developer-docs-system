# Create Order

Creates a new order in the system.

## Endpoint

POST /api/orders

## Request Headers

| Header        | Type   | Required | Description              |
|---------------|--------|----------|--------------------------|
| Authorization | String | Yes      | Bearer token (JWT)       |
| Content-Type  | String | Yes      | application/json         |

## Request Body

```json
{
  "user_id": "12345",
  "items": [
    {
      "product_id": "A001",
      "quantity": 2
    }
  ],
  "total_price": 49.99
}

## Response

### Success (200)

```json
{
  "order_id": "ORD-001",
  "status": "created"
}

### Error (400)

```json
{
  "error": "Invalid request parameters"
}

## Notes

- Ensure the user is authenticated before making this request  
- Validate item availability before submission

---

## Example Request

```bash
curl -X POST https://api.example.com/orders \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{ ... }'

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

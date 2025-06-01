# 🛒 Orders App - API Documentation

This app manages customer orders within the e-commerce system. Each order can contain multiple products and is associated with a specific user.

## 📦 Models

### `Order`
Represents a user's order.

- `id`: Auto-incremented primary key.
- `user`: The user who placed the order (automatically assigned).
- `status`: The current state of the order (`pending`, `paid`, `shipped`, `cancelled`, etc.).
- `total_price`: Automatically calculated based on the items.
- `created_at`: Timestamp of when the order was created.
- `updated_at`: Timestamp of when the order was updated.

### `OrderItem`
Represents a product in a specific order.

- `id`: Auto-incremented primary key.
- `order`: Reference to the related order.
- `product`: Reference to the product being ordered.
- `quantity`: Number of units ordered.
- `price`: Total price for the quantity of this product.

---

## 📡 API Endpoints

### List / Create Orders

`GET /api/orders/`  
`POST /api/orders/`

- **Authentication required** ✅
- **Permissions**:
  - Normal users: List **their own** orders.
  - Admins: List **all** orders.
- `POST` creates a new order with one or more items.

**Example POST body:**

```json
{
  "items": [
    {
      "product": 1,
      "quantity": 2
    },
    {
      "product": 3,
      "quantity": 1
    }
  ]
}
```
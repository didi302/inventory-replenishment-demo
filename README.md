# Inventory Replenishment

Version marker: TC088-GIT-V1.

Reorder when stock drops below 10 units. At 10 units or above, do not reorder.

```python
def needs_restock(stock: int) -> bool:
    return stock < 10
```

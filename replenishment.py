"""Inventory replenishment rules for the V2 demo."""

from dataclasses import dataclass

REORDER_POINT = 25


@dataclass(frozen=True)
class WarehouseStock:
    warehouse: str
    sku: str
    on_hand: int
    reserved: int = 0
    inbound: int = 0

    def __post_init__(self) -> None:
        if not self.warehouse or not self.sku:
            raise ValueError("Warehouse and SKU are required")
        if min(self.on_hand, self.reserved, self.inbound) < 0:
            raise ValueError("Stock counts cannot be negative")

    @property
    def available(self) -> int:
        return self.on_hand - self.reserved


@dataclass(frozen=True)
class ReplenishmentDecision:
    warehouse: str
    sku: str
    projected_stock: int
    order_quantity: int
    reason: str


def plan_replenishment(
    stock: WarehouseStock, *, safety_stock: int = 5, case_size: int = 6
) -> ReplenishmentDecision:
    """Plan one SKU independently at each warehouse.

    Order only below the reorder point after counting inbound stock.
    Round orders up to a full case to reach reorder point plus safety stock.
    """
    if safety_stock < 0 or case_size <= 0:
        raise ValueError("Safety stock must be nonnegative and case size positive")

    projected = stock.available + stock.inbound
    if projected >= REORDER_POINT:
        return ReplenishmentDecision(
            stock.warehouse, stock.sku, projected, 0, "Stock meets reorder point"
        )

    deficit = REORDER_POINT + safety_stock - projected
    cases = (deficit + case_size - 1) // case_size
    return ReplenishmentDecision(
        stock.warehouse, stock.sku, projected, cases * case_size,
        "Projected stock is below reorder point",
    )

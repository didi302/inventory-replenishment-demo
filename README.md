# Inventory Replenishment

Version marker: TC088-GIT-V2.

For each warehouse and SKU, projected stock equals on-hand stock minus reservations plus inbound stock. Reorder when projected stock drops below 25 units. At 25 units or above, do not reorder.

The default target is 30 units, including 5 units of safety stock. Order quantities are rounded up to full cases of 6 units. For example, projected stock of 23 units requires an order of 12 units.

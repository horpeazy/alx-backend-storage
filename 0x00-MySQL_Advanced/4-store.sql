-- SQL script that creates a trigger that decreases the
-- quantity of an item after adding a new order.


-- drop trigger if exists
DROP TRIGGER IF EXISTS update_item_quantity;

-- trigger declaration
CREATE TRIGGER update_item_quantity
AFTER INSERT
ON orders
FOR EACH ROW
-- Trigger actions
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;

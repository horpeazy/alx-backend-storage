-- SQL script that creates a trigger that resets the
-- attribute valid_email only when the email has been changed.

-- drop trigger if exists
DROP TRIGGER IF EXISTS reset_valid_email;

-- create the trigger
DELIMITER $$
CREATE TRIGGER reset_valid_email
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
	-- Trigger body
	IF OLD.email != NEW.email THEN
		SET NEW.valid_email = 0;
	END IF;
END$$
DELIMITER ;

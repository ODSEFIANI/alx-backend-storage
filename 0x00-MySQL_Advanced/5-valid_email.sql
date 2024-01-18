-- Each time the email changes the script
-- runs and check if it's match the prev one
DELIMITER $$ ;
CREATE TRIGGER mail_checker BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;$$
delimiter ;
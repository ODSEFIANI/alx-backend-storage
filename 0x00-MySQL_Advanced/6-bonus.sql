-- Addbonus procedure that adds new corections
DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN user_id INTEGER,
    IN project_name VARCHAR(255),
    IN score INTEGER
)
BEGIN
    -- Insert the project if it doesn't exist
    INSERT IGNORE INTO projects (name) VALUES (project_name);

    -- Get the project_id (existing or newly inserted)
    SET @project_id := (SELECT id FROM projects WHERE name = project_name);

    -- Insert the correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, @project_id, score);
END;

$$

DELIMITER ;
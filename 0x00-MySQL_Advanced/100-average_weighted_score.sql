-- calculate average weighted score

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (in_user_id INT)
BEGIN
    DECLARE v_total_weighted_score INT DEFAULT 0;
    DECLARE v_total_weight INT DEFAULT 0;

    SELECT SUM(c.score * p.weight)
        INTO v_total_weighted_score
        FROM corrections c
        INNER JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = in_user_id;

    SELECT SUM(p.weight)
        INTO v_total_weight
        FROM corrections c
        INNER JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = in_user_id;

    IF v_total_weight = 0 THEN
        UPDATE users u
        SET u.average_score = 0
        WHERE u.id = in_user_id;
    ELSE
        UPDATE users u
        SET u.average_score = v_total_weighted_score / v_total_weight
        WHERE u.id = in_user_id;
    END IF;
END $$

DELIMITER ;

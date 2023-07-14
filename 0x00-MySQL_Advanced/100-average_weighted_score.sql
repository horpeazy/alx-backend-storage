-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.


-- drop stored procedure
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- create the stored procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE weighted_avg FLOAT DEFAULT 0;

	SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight) INTO weighted_avg
	FROM corrections
	JOIN projects
	ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;

	UPDATE users
	SET average_score = weighted_avg
	WHERE id = user_id;
END$$
DELIMITER ;

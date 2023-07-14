-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student


-- drop procedure if exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- stored procedure declarations
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score INT DEFAULT 0;
	DECLARE u_id INT DEFAULT 0;

	SET u_id = user_id;
	-- calculate the sum 
	SELECT AVG(score) INTO @avg_score
	FROM corrections
	WHERE user_id = u_id;
	-- update the users table
	UPDATE users
	SET average_score = @avg_score
	WHERE id = u_id;
END$$
DELIMITER ;

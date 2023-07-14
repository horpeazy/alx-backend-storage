-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.


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

-- drop procedure if exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- create the procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE done INT DEFAULT FALSE;
	DECLARE id_value INT;
	DECLARE query_cursor CURSOR FOR SELECT id FROM users;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

	OPEN query_cursor;
	read_loop: LOOP
		FETCH query_cursor INTO id_value;
		IF done THEN
			LEAVE read_loop;
		END IF;
		-- call ComputeAverageWeightedScoreForUser
		CALL ComputeAverageWeightedScoreForUser(id_value);
	END LOOP;

	CLOSE query_cursor;
END $$
DELIMITER ;

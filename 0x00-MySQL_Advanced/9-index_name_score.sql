--  SQL script that creates an index idx_name_first on the table names and the first letter of name and score


-- drop the index
DROP INDEX IF EXISTS idx_name_first_score;

-- Index declaration
CREATE INDEX idx_name_first_score ON names (name(1), score);

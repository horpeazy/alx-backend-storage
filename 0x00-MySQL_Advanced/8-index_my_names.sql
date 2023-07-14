--  SQL script that creates an index idx_name_first on the table names and the first letter of name


-- drop index if exists
DROP INDEX IF EXISTS idx_name_first;

-- Index declaration
CREATE INDEX idx_name_first ON names (name(1));

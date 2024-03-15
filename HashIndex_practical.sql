create Database Practice;
use Practice;

CREATE TABLE your_table (
    id INT auto_increment PRIMARY KEY,
    hash_indexed_column INT
);

-- Drop the stored procedure once done
DROP PROCEDURE IF EXISTS insert_records;

-- Create a stored procedure to insert records
DELIMITER $$
CREATE PROCEDURE insert_records()
BEGIN
    DECLARE counter INT DEFAULT 1;
    
    WHILE counter <= 10000 DO
        -- Generate random values for columns
        SET @hash_index_value = FLOOR(RAND() * 1000);
        
        -- Insert record into the table
        INSERT INTO your_table (hash_indexed_column) VALUES (@hash_index_value);
        
        -- Increment counter
        SET counter = counter + 1;
    END WHILE;
END$$
DELIMITER ;

-- Call the stored procedure to insert records
CALL insert_records();

SET profiling = 1;

SELECT * FROM your_table WHERE hash_indexed_column = 889;
SELECT * FROM your_table WHERE hash_indexed_column = 746;
SELECT * FROM your_table WHERE hash_indexed_column = 634;

CREATE INDEX hash_index ON your_table (hash_indexed_column) USING HASH;

SELECT * FROM your_table WHERE hash_indexed_column = 889;
SELECT * FROM your_table WHERE hash_indexed_column = 746;
SELECT * FROM your_table WHERE hash_indexed_column = 634;

SHOW PROFILES;



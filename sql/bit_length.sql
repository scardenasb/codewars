-- Given a demographics table in the following format:
--
-- ** demographics table schema **
--
-- id
-- name
-- birthday
-- race
-- you need to return the same table where all text fields (name & race) are changed to 
-- the bit length of the string.


select *, length(name)*8 as name, length(race)*8 as race
from demographics


-- ###################################
-- WITH BIT_LENGTH() BUILT-IN FUNCTION
-- ###################################
select *, bit_length(name) as name, bit_length(race) as race
from demographics

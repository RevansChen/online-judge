-- MySQL

CREATE PROCEDURE mostExpensive()
    SELECT
        name
    FROM
        `Products`
    ORDER BY
        price * quantity DESC,
        name
    LIMIT
        1
    ;

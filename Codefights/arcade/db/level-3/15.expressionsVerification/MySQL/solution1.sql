-- MySQL

CREATE PROCEDURE expressionsVerification()
    SELECT
        *
    FROM
        `expressions`
    WHERE
        CASE
            WHEN operation = '+' THEN c = (a + b)
            WHEN operation = '-' THEN c = (a - b)
            WHEN operation = '*' THEN c = (a * b)
            ELSE                      c = (a / b)
        END
    ;

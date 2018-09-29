-- MySQL

CREATE PROCEDURE volleyballResults()
    SELECT
        *
    FROM
        `results`
    ORDER BY
        wins
    ;

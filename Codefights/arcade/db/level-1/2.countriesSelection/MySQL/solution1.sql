-- MySQL

CREATE PROCEDURE countriesSelection()
    SELECT
        *
    FROM
        `countries`
    WHERE
        continent = "Africa"
    ;

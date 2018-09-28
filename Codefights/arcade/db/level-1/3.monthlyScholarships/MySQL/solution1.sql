-- MySQL

CREATE PROCEDURE monthlyScholarships()
    SELECT
        id,
        scholarship / 12 AS scholarship
    FROM
        `scholarships`
    ;

-- MySQL

CREATE PROCEDURE projectsTeam()
    SELECT
        name
    FROM
        `projectLog`
    GROUP BY
        name
    ;

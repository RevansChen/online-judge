-- MySQL

CREATE PROCEDURE projectList()
    SELECT
        project_name,
        team_lead,
        income
    FROM
        `Projects`
    ORDER BY
        internal_id
    ;

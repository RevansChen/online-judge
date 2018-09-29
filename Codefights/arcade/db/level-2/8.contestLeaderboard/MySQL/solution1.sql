-- MySQL

CREATE PROCEDURE contestLeaderboard()
    SELECT
        name
    FROM
        `leaderboard`
    ORDER BY
        score DESC
    LIMIT
        3, 5
    ;

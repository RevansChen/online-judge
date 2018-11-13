-- MySQL

CREATE PROCEDURE newsSubscribers()
    SELECT
        *
    FROM (
        SELECT
            subscriber
        FROM
            `full_year`
        WHERE
            newspaper LIKE '%Daily%'
        UNION
        SELECT
            subscriber
        FROM
            `half_year`
        WHERE
            newspaper LIKE '%Daily%'
    ) AS tmp
    ORDER BY
        subscriber
    ;

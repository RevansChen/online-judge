-- MySQL

CREATE PROCEDURE mischievousNephews()
    SELECT
        WEEKDAY(mischief_date) AS weekday,
        mischief_date,
        author,
        title
    FROM
        `mischief`
    ORDER BY
        weekday,
        FIELD(author, "Huey", "Dewey", "Louie"),
        mischief_date,
        title
    ;

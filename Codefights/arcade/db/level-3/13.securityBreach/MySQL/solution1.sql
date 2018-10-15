-- MySQL

CREATE PROCEDURE securityBreach()
    SELECT
        *
    FROM
        `users`
    WHERE
        attribute REGEXP BINARY CONCAT('.+%', first_name, '_', second_name, '%.*')
    ;

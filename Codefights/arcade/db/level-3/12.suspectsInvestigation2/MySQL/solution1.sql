-- MySQL

CREATE PROCEDURE suspectsInvestigation2()
    SELECT
        id,
        name,
        surname
    FROM
        `Suspect`
    WHERE
        (height <= 170) OR
        (name NOT LIKE "B%") OR
        (surname NOT LIKE "Gre_n")
    ;

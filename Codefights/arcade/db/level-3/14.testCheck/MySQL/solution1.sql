-- MySQL

-- 有限制修改區域
CREATE PROCEDURE testCheck()
    SELECT id, IF (
        correct_answer = given_answer,
        'correct',
        IF (
            ISNULL(given_answer),
            'no answer',
            'incorrect'
        )
    ) AS checks
    FROM answers
    ORDER BY id;

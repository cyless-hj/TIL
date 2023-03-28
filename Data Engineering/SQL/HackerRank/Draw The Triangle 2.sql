SELECT
    RPAD('*',(2 * LEVEL), ' *')
FROM
    DUAL
CONNECT BY
    LEVEL <= 20;
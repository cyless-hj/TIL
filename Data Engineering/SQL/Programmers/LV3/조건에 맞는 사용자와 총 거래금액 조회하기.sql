SELECT U.USER_ID, U.NICKNAME,
       U.CITY || ' ' || U.STREET_ADDRESS1 || ' ' || STREET_ADDRESS2 AS 전체주소,
       SUBSTR(U.TLNO, 0, 3) || '-' || SUBSTR(U.TLNO, 4, 4) || '-' || SUBSTR(U.TLNO, 8) AS 전화번호
FROM USED_GOODS_USER U
JOIN
      (
          SELECT  WRITER_ID, COUNT(*) AS CNT
          FROM    USED_GOODS_BOARD
          GROUP BY WRITER_ID
          HAVING  COUNT(*) >= 3
      ) B
ON B.WRITER_ID = U.USER_ID
ORDER BY U.USER_ID DESC;
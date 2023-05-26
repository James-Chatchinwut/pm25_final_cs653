SELECT "glue_2022"."date",
  AVG("02t") as "1015",
  AVG("05t") as "1047",
  AVG("10t") as "1006",
  AVG("11t") as "1026",
  AVG("12t") as "1012",
  AVG("59t") as "1014",
  AVG("61t") as "1045",
  AVG("03t") as "1021",
  AVG("50t") as "1007",
  AVG("52t") as "1016"
FROM "new_test_pm25"."glue_2022" 
WHERE "glue_2022"."date" >= TIMESTAMP '2022-01-01 00:00:00'
  AND "glue_2022"."date" <= TIMESTAMP '2022-01-31 00:00:00'
GROUP BY "glue_2022"."date";

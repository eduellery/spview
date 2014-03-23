COPY(

SELECT t.lat, t.lon, t.semana,
  (2*TRIM(SUBSTR(t.horamin, 0, 3))::int + TRIM(SUBSTR(t.horamin, 4))::int/30) AS hora,
  SUM(t.extensaolentidao) as extensao
  FROM (
    SELECT lat, lon,
      EXTRACT(DOW FROM SUBSTR(datahora, 0, 11)::date) as semana,
      TRIM(SUBSTR(datahora, 11)) AS horamin,
      extensaolentidao
    FROM lentidao) t
  GROUP BY t.lat, t.lon, t.semana, t.horamin
  ORDER BY t.semana, t.horamin

) TO '/home/eltermann/dados/Lentidao.zip.d/lentidao_sumario_semanal3.csv' WITH CSV;
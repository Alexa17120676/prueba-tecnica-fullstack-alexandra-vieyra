-- Pregunta A

SELECT
    m.title,
    AVG(s.tickets_sold * 100.0 / s.capacity) AS avg_occupancy
FROM showtimes s
JOIN movies m
    ON s.id_movie = m.id_movie
JOIN cinemas c
    ON s.id_cine = c.id_cine
WHERE c.brand = 'VIP'
  AND s.show_date >= CURRENT_DATE - INTERVAL '7 days'
GROUP BY m.id_movie, m.title
ORDER BY avg_occupancy DESC
LIMIT 5;

-- Pregunta B

SELECT
    c.id_cine,
    c.name
FROM cinemas c
LEFT JOIN showtimes s
    ON c.id_cine = s.id_cine
    AND s.show_date = CURRENT_DATE - 1
WHERE s.id IS NULL;

-- Pregunta C

-- Ayuda a optimizar consultas que filtran funciones por fecha,
-- como la Pregunta A, donde se consulta un rango de días.
CREATE INDEX idx_showtimes_date
ON showtimes (show_date);


-- Ayuda a buscar funciones de un cine en una fecha específica,
-- como en la Pregunta B.
CREATE INDEX idx_showtimes_cine_date
ON showtimes (id_cine, show_date);
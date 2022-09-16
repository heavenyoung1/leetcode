create table fine (
    fine_id int primary key AUTO_INCREMENT,
    name varchar(40),
    number_plate varchar(6),
    violation varchar(50),
    sum_fine decimal(8,2),
    date_violation date,
    date_payment date
                  )
                  
insert into fine  (name, number_plate, violation, sum_fine, date_violation, date_payment) values 
('Баранов П.Е.', 'Р523ВТ', 'Превышение скорости(от 40 до 60)', NULL, '2020-02-14', NULL),
('Абрамова К.А.', 'О111АВ', 'Проезд на запрещающий сигнал', NULL, '2020-02-23', NULL),
('Яковлев Г.Р.', 'Т330ТТ', 'Проезд на запрещающий сигнал', NULL, '2020-03-03',NULL)       

CREATE TABLE book (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    author_id INT NOT NULL,
    genre_id INT,
    price DECIMAL(8,2),
    amount INT,
    FOREIGN KEY (author_id) REFERENCES author (author_id),
    FOREIGN KEY (genre_id) REFERENCES genre (genre_id)
);
    
    
SELECT * FROM book

SELECT b.title, g.name_genre, b.price
from book b
join genre g 
on b.genre_id = g.genre_id
where b.amount > 8
order by b.price desc

-- отработка  cross join на MySQL
SELECT c.name_city, a.name_author, (DATE_ADD('2020-01-01', INTERVAL FLOOR(RAND() * 365) DAY)) as Дата
from city c CROSS JOIN author a
order by c.name_city, Дата desc

--Запрос на выборку из нескольких страниц
select  g.name_genre, b.title, a.name_author
from book b
inner join genre g on b.genre_id = g.genre_id
inner join author a on b.author_id = a.author_id
where g.name_genre like 'роман'
order by b.title

SELECT a.name_author, SUM(b.amount) AS Количество
FROM author a
LEFT JOIN book b
ON a.author_id = b.author_id 
GROUP BY a.name_author
HAVING Количество < 10 OR Количество IS Null
ORDER BY count(b.amount)

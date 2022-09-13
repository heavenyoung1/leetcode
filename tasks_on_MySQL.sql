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

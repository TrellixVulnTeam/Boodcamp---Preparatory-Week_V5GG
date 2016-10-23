SELECT * FROM bootcamp.students
WHERE BirthDate < date_sub(curdate(), interval 17 year);
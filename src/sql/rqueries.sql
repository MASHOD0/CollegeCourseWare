select class_id,course_id, "link", "time"
from classes
where section_id = 21;



INSERT INTO classes(class_id, time, day, link, course_id, section_id ) 
values(DEFAULT, '{}', '{}', '{}', '19CH2ICCHY', 21);

SELECT teacher_id
FROM teachers
WHERE name = '{}'
limit 1;
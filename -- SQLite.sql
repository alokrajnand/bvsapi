-- SQLite
select * from userprofile_profile;

DELETE from userprofile_profile where user_email_address_id = 'alok@gmail.com'


INSERT INTO 
userprofile_profile ( user_email_address_id, user_name,user_date_of_birth,user_class)
   VALUES
   ( 'alok@gmail.com', 'Alok kumar','1987-12-12','Ten');


INSERT INTO 
course_course ( course_header, course_name,course_category)
   VALUES
   ( 'Type-Script', 'Type Script','Computer Science');

   select * from course_course;

INSERT INTO 
course_lesson ( course_header_id, lesson_name)
   VALUES
   ( 'Type-Script', 'Lesson Two');

   select * from course_lesson;
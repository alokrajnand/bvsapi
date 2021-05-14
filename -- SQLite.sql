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


INSERT INTO 
course_ratings ( course_header_id, rated_by,rating,rating_comment)
   VALUES
   ( 'angular', 'alok@gmail.com','5','good');

   select * from course_ratings;

   DELETE from course_ratings where course_header_id = 'angular'



create table userauth_varification(
   user_email_address VARCHAR(100) NOT NULL,
   email_varification VARCHAR(100) NULL,
   phone_varification VARCHAR(40) NULL,
   PRIMARY KEY (user_email_address)
);

drop TABLE userauth_varification;
INSERT INTO 
userauth_varification ( email_address_id, email_varification)
   VALUES
   ( 'alok@gmail.com','Done');


    DELETE from userauth_varification where email_varification = 'done'
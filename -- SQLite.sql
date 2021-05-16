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
   ( 'type-script', 'Type Script','Computer Science');

   select * from course_course;
DELETE from course_lesson where course_header_id = 'Type-Script'
INSERT INTO 
course_lesson ( course_header_id, lesson_name)
   VALUES
   ( 'type-script', 'Lesson Four');

   select * from course_lesson;

INSERT INTO 
course_lesson ( course_header_id, lesson_name)
   VALUES
   ( 'Type-Script', 'Lesson Four');


INSERT INTO 
quiz_quiz ( course_header_id, quiz_name,quiz_desc)
   VALUES
   ( 'angular', 'Quiz two' ,'quiz to test');



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

INSERT INTO 
discussion_discussion ( course_header_id, discussion_header,discussion_name, discussion_desc)
   VALUES
   ( 'type-script', 'question-number-four' ,'Question Number Four' , "Some early exploration of the dashboard/overview for an eLearning platform I'm working on. This past month I've been working on some exciting stuff and can't wait to share more in the future!");


update course_lesson set lesson_id =4 where id =8
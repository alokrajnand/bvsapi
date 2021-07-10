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


update course_course set course_short_desc = "Master Typescript by learning popular design patterns and building complex projects. Includes React and Express! complex projects. Includes React and Express!"
   
   select * from course_course;
DELETE from django_migrations 

where course_header_id = 'Type-Script'

INSERT INTO 
course_lesson ( 
   course_header_id,
   course_name,
   lesson_header, 
   lesson_name,
   lesson_id,
   lesson_video_link,
   lesson_video_minute)
   VALUES
   ( 'type-script', 'Type Script',
   'type-script-lesson-four','Lesson Four' ,
   1,'https://www.youtube.com/embed/tZrpoSUQCJ0',
   20);

   select * from course_lesson;

INSERT INTO 
course_lesson ( course_header_id, lesson_name)
   VALUES
   ( 'Type-Script', 'Lesson Four');


INSERT INTO 
quiz_quiz ( course_header_id, quiz_header, quiz_name,quiz_desc)
   VALUES
   ( 'type-script', 'type-script-quiz-two' ,'type Script Quiz Two' ,'quiz to test');



   select * from course_ratings;

   DELETE from course_ratings where course_header_id = 'angular'



create table userauth_varification(
   user_email_address VARCHAR(100) NOT NULL,
   email_varification VARCHAR(100) NULL,
   phone_varification VARCHAR(40) NULL,
   PRIMARY KEY (user_email_address)
);

drop TABLE quiz_quiz;
INSERT INTO 
userauth_varification ( email_address_id, email_varification)
   VALUES
   ( 'alok@gmail.com','Done');


    DELETE from userauth_varification where email_varification = 'done'

INSERT INTO 
discussion_discussion ( course_header_id, discussion_header,discussion_name, discussion_desc)
   VALUES
   ( 'type-script', 'question-number-four' ,'Question Number Four' , "Some early exploration of the dashboard/overview for an eLearning platform I'm working on. This past month I've been working on some exciting stuff and can't wait to share more in the future!");

DELETE from django_migrations where id = 49;


delete from django_migrations;
drop table discussion_discussion


insert INTO course_lesson(
    lesson_header,
    lesson_id,
    course_header_id,
    course_name,
    lesson_name,
    lesson_description ,
    lesson_video_link,
    lesson_video_minute
) VALUES (
   'type-script-getting-startted-with-type-script',2,'type-script','Type Script','Getting Started With Type Sctript',
   'This is first lesson of the course and it will guide you how the basics of type script and it will setup the differet tool need to start learning',
   'https://www.youtube.com/embed/OtwHJwP-juo',30
);

update course_lesson set lesson_about = "<h1>London is the capital city of England.</h1><p>This is a specific challenge overview inside the trackTraining platform I've been working on for the last couple of months.</p><p>The aim of the overview is to have a general picture of the overall material progress. While the emphasis is on overall progress—we also wanted to highlight specific trainee scores and grading.</p>" 


INSERT INTO discussion_discussion(
    discussion_header,
    course_header_id ,
    course_name,
    lesson_header_id,
    lesson_name ,
    discussion_name,
    discussion_desc,
    discussion_views,
    discussion_ans_count
) VALUES(
'how-to-setup-type-script-on-mac' , 
'type-script',
'Type Script',
'type-script-basics-of-type-script',
'Getting Started with Type Script',
'How to setup type Script On mac',
'I am very new to type script just started to setup the process of learnign. please help me to understand hoe to start ',
100,
10
)
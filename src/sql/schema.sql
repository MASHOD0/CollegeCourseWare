CREATE TABLE "student" (
  "student_id" SERIAL PRIMARY KEY,
  "section_id" int,
  "USN" varchar(10),
  "Name" varchar(60),
  "password" varchar,
  "email" varchar(64),
  "branch" varchar
);

CREATE TABLE "teachers" (
  "teacher_id" SERIAL PRIMARY KEY,
  "name" varchar(60),
  "password" varchar,
  "email" varchar(64),
  "department" varchar
);

CREATE TABLE "sections" (
  "section_id" SERIAL PRIMARY KEY,
  "section" varchar,
  "semester" int
);

CREATE TABLE "courses" (
  "course_id" SERIAL PRIMARY KEY,
  "department" varchar,
  "course_code" varchar(10)
);

CREATE TABLE "classes" (
  "section_id" int,
  "course_id" int,
  "link" varchar,
  "day" varchar(10),
  "time" time,
  "class_id" SERIAL PRIMARY KEY,
  "teacher_id" integer
);

CREATE TABLE "grades" (
  "student_id" int,
  "course_id" int,
  "semester" int,
  "CIE_1" int,
  "CIE_2" int,
  "CIE_3" int,
  "AAT" int,
  "SEE" int,
  "section_id" int
);

CREATE TABLE "Attendance" (
  "student_id" int,
  "course_id" int,
  "missed" int,
  "total" int,
  "section_id" int
);

ALTER TABLE "classes" ADD FOREIGN KEY ("section_id") REFERENCES "sections" ("section_id");

ALTER TABLE "classes" ADD FOREIGN KEY ("course_id") REFERENCES "courses" ("course_id");

ALTER TABLE "classes" ADD FOREIGN KEY ("teacher_id") REFERENCES "teachers" ("teacher_id");

ALTER TABLE "grades" ADD FOREIGN KEY ("student_id") REFERENCES "student" ("student_id");

ALTER TABLE "grades" ADD FOREIGN KEY ("course_id") REFERENCES "courses" ("course_id");

ALTER TABLE "grades" ADD FOREIGN KEY ("section_id") REFERENCES "sections" ("section_id");

ALTER TABLE "Attendance" ADD FOREIGN KEY ("student_id") REFERENCES "student" ("student_id");

ALTER TABLE "Attendance" ADD FOREIGN KEY ("course_id") REFERENCES "courses" ("course_id");

ALTER TABLE "Attendance" ADD FOREIGN KEY ("section_id") REFERENCES "sections" ("section_id");

ALTER TABLE "student" ADD FOREIGN KEY ("section_id") REFERENCES "sections" ("section_id");

ALTER TABLE "teachers" ADD FOREIGN KEY ("department") REFERENCES "courses" ("department");

-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(*)
FROM assignments
WHERE teacher_id = ? AND grade = 'A';

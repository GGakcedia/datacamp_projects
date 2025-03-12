"""-- This query ranks students based on their exam scores, including other factors like attendance, study hours, sleep hours, and tutoring sessions.
SELECT 
    Attendance, 
    Hours_Studied, 
    Sleep_Hours, 
    Tutoring_Sessions, 
    -- Assigns a rank to each student based on their exam score, with the highest score ranked first.
    DENSE_RANK() OVER (ORDER BY Exam_Score DESC) AS exam_rank
-- Specifies the source of the data.
FROM student_performance
-- Orders the result by exam rank in ascending order so the highest-ranked students come first.
ORDER BY exam_rank ASC
-- Limits the result to the top 30 students.
LIMIT 30;
"""
-- avg_exam_score_by_study_and_extracurricular
-- Edit the query below as needed
-- This query calculates the average exam score of students who studied more than 10 hours and participated in extracurricular activities.
SELECT Hours_Studied, AVG(Exam_Score) AS avg_exam_score
FROM student_performance
-- Filters the data to include only those who studied more than 10 hours and participated in extracurricular activities.
WHERE Hours_Studied > 10
  AND Extracurricular_Activities = 'Yes'
-- Groups the results by the number of hours studied to calculate the average exam score for each study group.
GROUP BY Hours_Studied
-- Orders the results by the number of hours studied in descending order.
ORDER BY Hours_Studied DESC;

-- avg_exam_score_by_hours_studied_range
-- Add solution code below 
-- This query groups students by ranges of hours studied and calculates the average exam score for each group.
SELECT
    CASE
        -- Categorizes hours studied into specific ranges: 1-5, 6-10, 11-15, and 16+ hours.
        WHEN Hours_Studied BETWEEN 1 AND 5 THEN '1-5 hours'
        WHEN Hours_Studied BETWEEN 6 AND 10 THEN '6-10 hours'
        WHEN Hours_Studied BETWEEN 11 AND 15 THEN '11-15 hours'
        ELSE '16+ hours'
    END AS hours_studied_range,
    -- Calculates the average exam score for each range of hours studied.
    AVG(Exam_Score) AS avg_exam_score
-- Specifies the source of the data.
FROM student_performance
-- Groups the data by the newly created study ranges.
GROUP BY hours_studied_range
-- Orders the result by average exam score in descending order to see which range performs best.
ORDER BY avg_exam_score DESC;

-- student_exam_ranking
-- Add solution code below 
-- This query ranks students based on their exam scores, including other factors like attendance, study hours, sleep hours, and tutoring sessions.
SELECT 
    Attendance, 
    Hours_Studied, 
    Sleep_Hours, 
    Tutoring_Sessions, 
    -- Assigns a rank to each student based on their exam score, with the highest score ranked first.
    DENSE_RANK() OVER (ORDER BY Exam_Score DESC) AS exam_rank
-- Specifies the source of the data.
FROM student_performance
-- Orders the result by exam rank in ascending order so the highest-ranked students come first.
ORDER BY exam_rank ASC
-- Limits the result to the top 30 students.
LIMIT 30;
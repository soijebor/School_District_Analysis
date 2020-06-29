# School_District_Analysis
PyCitySchools with Panda

## *Project Overview*

* A high-level snapshot of the district's key metrics, presented in a table format
* An overview of the key metrics for each school, presented in a table format
* Tables presenting each of the following metrics:
  * Top 5 and bottom 5 performing schools, based on the overall passing rate
  * The average math score received by students in each grade level at each school
  * The average reading score received by students in each grade level at each school
  * School performance based on the budget per student
  * School performance based on the school size 
  * School performance based on the type of school

## *Challenge Overview*

A cheif data scientist for a city school has given me the following tasks to complete After replacing the reading and math scores for the Thomas High School with NaN
* A high-level snapshot of the district's key metrics, presented in a table format
* An overview of the key metrics for each school, presented in a table format
* Tables presenting each of the following metrics:
  * Top 5 and bottom 5 performing schools, based on the overall passing rate
  * The average math score received by students in each grade level at each school
  * The average reading score received by students in each grade level at each school
  * School performance based on the budget per student
  * School performance based on the school size 
  * School performance based on the type of school
  
Recreate the district and school summa

  * Data Source: 
      * schools_complete.csv
      * students_complete.csv
  
  * Software: Python 3.7.6, Anaconda 4.8.3, Jupyter Notebook 6.0.3
  
  ## *Summary*
  
  The analysis of the school district show that:
  * After recreating the district and school summary DataFrames that in both summary the average math score went down from 79.0 to 78.9 and the percentage of passing math, reading and the overall percentage all went down by 1% each
  * Replacing the ninth graders’ math and reading scores affect Thomas High School’s performance, relative to the other schools by dropping from 2nd place in top performing school to 8th place
  * After recalculating the scores by grade, scores by school spending, scores by school size, and scores by school type, replacing the ninth-grade scores affects the following by:
  * Math and Reading Scores by Grade - it only affected the 9th grade for Thomas high school by replacing the grade with NaN for both math and  reading
  * Scores by School Spending - the spending range $630 -644 per student scores percentage for passing math, reading snd overall percentage dropped by 6%, 7% and 7% respecrtively due to the replacement of the ninth grade sccores for Thomas high school
  * Scores by School Size - the medium(1000-2000)school size percentage for passing math, reading snd overall percentage all dropped by 6% each  due to the replacement of the ninth grade sccores for Thomas high school
  * Scores by School Type - the Charter school type percentage for passing math, reading snd overall percentage dropped 4%,4% and 3% respectively due to the replacement of the ninth grade sccores for Thomas high school.

### Traffic Prediction based on Weather Conditions

This project encompasses the utilization of two open datasets from Kaggle. Our primary objectives involve data acquisition, data cleansing, and subsequent storage of the cleaned data in .sqlite format using a structured data pipeline. Throughout this process, we've conducted in-depth analysis and exploratory data analysis (EDA). Prior to commencing, ensure Python is installed as we'll be working within Jupyter Notebooks.

### Project Overview

1. Data Pipeline Creation: Initially, our focus was on building a robust data pipeline that facilitated the extraction of Kaggle data, enabling its transformation and storage in the .sqlite format.

2. Test File Creation: To ensure the efficacy of our data pipeline, we developed a test file for verifying the successful creation and storage of data within the .sqlite directory.

3. Final Report: Our final report encompasses several crucial steps:

	- Data Cleaning: We meticulously examined the datasets for any occurrences of missing or empty values (NaN), promptly addressing and removing them to ensure data integrity. Additionally, we identified and rectified any data type inconsistencies within our dataset.

	- Exploratory Data Analysis (EDA): After completing the data cleansing process, we delved into an extensive exploration of the dataset. This involved statistical analysis and descriptive insights to better comprehend the underlying patterns and trends.

	- Data Visualization: To gain comprehensive insights and facilitate a better understanding of the dataset, we employed various data visualization techniques. Visual representations such as plots, graphs, and charts were utilized to highlight significant trends, correlations, and anomalies within the data.

We emphasize that each phase of this project was undertaken individually, ensuring dedicated attention to detail and comprehensive exploration of the dataset. Our work focused on maintaining a high standard of accuracy, adhering to best practices in data analysis, and striving for a cohesive and structured project execution.
     

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises, sometimes using [Python](https://www.python.org/), sometimes using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.<jv or py>`.

In regular intervalls, exercises will be given as homework to complete during the semester. We will divide you into two groups, one completing an exercise in Jayvee, the other in Python, switching each exercise. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv` or `./exercises/exercise1.py`
2. `./exercises/exercise2.jv` or `./exercises/exercise2.py`
3. `./exercises/exercise3.jv` or `./exercises/exercise3.py`
4. `./exercises/exercise4.jv` or `./exercises/exercise4.py`
5. `./exercises/exercise5.jv` or `./exercises/exercise5.py`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```

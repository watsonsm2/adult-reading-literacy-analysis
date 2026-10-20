# college-reading-literacy-analysis
A data science research project analyzing factors associated with reading fluency and comprehension among college students using statistical analysis and machine learning.
# Reading Fluency and Comprehension Among College Students

### An Educational Data Science & Machine Learning Research Project

## Project Overview

This project investigates the linguistic, cognitive, behavioral, and educational factors associated with reading fluency and reading comprehension among college and university students.

Using statistical analysis, data visualization, and machine learning, the research aims to identify patterns in reading performance and determine which measurable factors are most strongly associated with students' ability to read efficiently and understand complex academic texts.

The long-term objective is to contribute to evidence-based educational research and explore how data science can support academic literacy and student success in higher education.

**Project Status:** Phase 1 — Research Problem Definition

**Research Domain:** Educational Data Science | Learning Analytics | Machine Learning | Literacy Research

---

## Research Problem

Reading fluency and reading comprehension are closely related but distinct dimensions of literacy.

- **Reading Fluency:** The ability to read text accurately, at an appropriate rate, and with suitable expression.
- **Reading Comprehension:** The ability to understand, interpret, integrate, and evaluate information presented in written text.

College students may demonstrate strong reading fluency while still experiencing difficulty comprehending complex academic material.

This project seeks to understand which factors are most strongly associated with differences in these reading outcomes.

## Research Objectives

1. Identify factors associated with reading fluency among college and university students.
2. Identify factors associated with reading comprehension.
3. Examine the relationship between reading fluency and comprehension.
4. Investigate how linguistic, cognitive, behavioral, and educational characteristics relate to reading performance.
5. Develop and evaluate statistical and machine learning models to examine the predictive value of these factors.
6. Communicate findings that may inform future educational research and academic support initiatives.

## Research Questions

**Primary Research Question:**

Which linguistic, cognitive, behavioral, and educational factors are most strongly associated with differences in reading fluency and reading comprehension among college and university students?

**Supporting Questions:**

- RQ1: Which factors are most strongly associated with reading fluency?
- RQ2: Which factors are most strongly associated with reading comprehension?
- RQ3: What is the relationship between reading fluency and comprehension?
- RQ4: Do reading habits, motivation, vocabulary knowledge, and academic experiences explain additional variation in reading outcomes?
- RQ5: Can statistical and machine learning models identify the most informative predictors of reading performance?

## Research Hypotheses

| ID | Hypothesis |
|---|---|
| H1 | Vocabulary knowledge is positively associated with reading comprehension. |
| H2 | Word recognition and decoding accuracy are positively associated with reading fluency. |
| H3 | Reading fluency and comprehension are positively correlated but remain distinct outcomes. |
| H4 | Reading habits and motivation explain additional variation in reading performance. |
| H5 | Background knowledge and reasoning ability contribute to differences in comprehension. |

These hypotheses will be evaluated using available research data.

## Potential Research Variables

The following variables are candidates for investigation, subject to dataset availability and measurement validity.

| Category | Potential Variables |
|---|---|
| Linguistic | Vocabulary knowledge, decoding accuracy, syntactic knowledge |
| Cognitive | Working memory, attention, reasoning ability |
| Behavioral | Reading frequency, motivation, reading strategies |
| Educational | Academic preparation, prior instruction, educational resources |
| Contextual | Text difficulty, subject familiarity, language background |

**Primary Outcome Variables:**
- Reading fluency assessment scores
- Reading comprehension assessment scores

The final variable definitions and measurement methods will be determined during the data collection phase.

---

## Research Methodology

The project will follow an extended data science life cycle informed by the CRISP-DM framework.

### Phase 1: Problem Definition
- Establish the research problem.
- Identify the target population.
- Develop research questions and hypotheses.
- Define potential outcome and predictor variables.

### Phase 2: Data Collection
- Identify credible educational research datasets.
- Evaluate data quality and availability.
- Verify that assessments are appropriate for college students.
- Review dataset permissions, limitations, and documentation.

### Phase 3: Data Cleaning and Preparation
- Examine missing values.
- Identify duplicates and inconsistencies.
- Assess outliers and data distributions.
- Prepare reproducible data-processing pipelines.

### Phase 4: Exploratory Data Analysis
- Analyze descriptive statistics.
- Visualize reading performance distributions.
- Investigate relationships between variables.
- Identify potential patterns and confounding factors.

### Phase 5: Feature Engineering
- Select and transform relevant predictors.
- Encode categorical features.
- Standardize numerical variables when appropriate.
- Prevent data leakage.

### Phase 6: Statistical Analysis and Machine Learning
- Perform correlation analysis.
- Develop regression models.
- Compare machine learning approaches.
- Investigate predictive relationships.

Potential models include:
- Linear and regularized regression
- Random Forest
- Gradient Boosting / XGBoost

### Phase 7: Model Evaluation
- Evaluate model performance on held-out data.
- Examine prediction errors.
- Assess model interpretability.
- Investigate bias, uncertainty, and limitations.

### Phase 8: Visualization and Deployment
- Develop research visualizations.
- Create an interactive dashboard if appropriate.
- Present findings in an accessible format.

### Phase 9: Research Communication
- Summarize findings.
- Discuss educational implications.
- Document limitations.
- Identify opportunities for future research.

---

## Proposed Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Manipulation | Pandas, NumPy |
| Statistical Analysis | SciPy, Statsmodels |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Development | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |
| Dashboard (Optional) | Streamlit |

*The technology stack may change as research and dataset requirements become clearer.*

## Repository Structure

The repository will be organized as development progresses.

```text
college-reading-literacy-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── problem_statement.md
│   ├── research_questions.md
│   ├── methodology.md
│   └── data_dictionary.md
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_statistical_analysis.ipynb
│   └── 04_machine_learning.ipynb
│
├── src/
│
├── reports/
│   └── figures/
│
├── tests/
│
├── .gitignore
├── requirements.txt
└── README.md
```

Directories and notebooks listed above are planned and will be added during the relevant development phases.

## Project Roadmap

- [x] Define the research problem.
- [x] Identify the target student population.
- [x] Establish initial research questions.
- [x] Develop preliminary hypotheses.
- [x] Identify potential research variables.
- [ ] Locate and evaluate suitable research datasets.
- [ ] Finalize the data dictionary and methodology.
- [ ] Perform data cleaning and exploratory analysis.
- [ ] Conduct statistical modeling.
- [ ] Develop and compare machine learning models.
- [ ] Evaluate and interpret results.
- [ ] Develop visualizations or a dashboard.
- [ ] Publish the final research report.

## Research Ethics and Limitations

This project will prioritize responsible educational data science practices.

Research considerations include:

- Protecting student privacy and confidentiality.
- Using datasets with appropriate permissions.
- Evaluating the validity of reading assessment instruments.
- Recognizing sampling bias and measurement limitations.
- Assessing model performance across relevant student populations.
- Avoiding unsupported causal conclusions.

**Important:** Statistical associations and machine learning feature importance do not establish causation.

Any predictions or findings will be interpreted within the limitations of the available data.

## Expected Outcomes

The project aims to produce:

1. A reproducible analysis of factors associated with reading fluency and comprehension.
2. Statistical summaries and data visualizations.
3. Evaluated predictive models.
4. An interpretable comparison of influential predictors.
5. A research report describing findings, limitations, and educational implications.
6. A documented portfolio project demonstrating applied educational data science skills.

These are intended deliverables, not completed research findings.

## Future Research Opportunities

Potential future extensions include:

- AI-assisted reading comprehension tools.
- Personalized learning recommendations.
- Academic reading interventions.
- Comparative analysis across educational disciplines.
- Longitudinal research on college-level literacy development.

## Project Author

**Shawn Watson**

Undergraduate researcher interested in educational data science, artificial intelligence, machine learning, and the application of technology to improving student learning outcomes.

## Project Status

**Current Phase:** Phase 1 — Problem Definition

**Next Phase:** Phase 2 — Data Collection and Dataset Evaluation

This repository will be updated throughout the research and development process.

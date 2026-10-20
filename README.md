# Reading Fluency and Comprehension Among Adult Readers

### An Educational Data Science & Machine Learning Research Project

## Project Overview

This project investigates the linguistic, cognitive, behavioral, educational, and contextual factors associated with reading fluency and reading comprehension among adult readers.

Using statistical analysis, data visualization, and machine learning, the research aims to identify patterns in adult reading performance and determine which measurable factors are most strongly associated with individuals' ability to read efficiently and comprehend written information.

The broader objective is to contribute to evidence-based adult literacy research and explore how data science can improve our understanding of reading performance, educational development, and lifelong learning.

**Project Status:** Phase 2 — Dataset Identification and Evaluation

**Research Domain:** Educational Data Science | Learning Analytics | Machine Learning | Adult Literacy Research

**Target Population:** Adult readers aged 18 years and older

---

## Research Problem

Reading fluency and reading comprehension are related but distinct dimensions of literacy.

**Reading Fluency** refers to the ability to read text accurately, at an appropriate rate, and with suitable expression. Reading efficiency and automaticity may also be relevant depending on the assessment.

**Reading Comprehension** refers to the ability to understand, interpret, integrate, and evaluate information presented in written texts.

Adult readers demonstrate varying levels of reading performance, potentially associated with differences in vocabulary knowledge, cognitive abilities, reading behaviors, educational experiences, and reading environments.

Understanding these relationships may help researchers identify factors associated with adult literacy and inform future educational research.

### Primary Research Question

**Which linguistic, cognitive, behavioral, educational, and contextual factors are most strongly associated with reading fluency and reading comprehension among adult readers?**

## Research Objectives

1. Identify measurable factors associated with adult reading fluency.
2. Identify factors associated with adult reading comprehension.
3. Examine the relationship between fluency and comprehension.
4. Investigate associations involving vocabulary knowledge, cognitive abilities, reading behaviors, and educational experiences.
5. Compare the predictive value of selected variables using statistical analysis and machine learning.
6. Interpret findings in the context of adult literacy and educational research.

## Research Questions

**RQ1:** Which factors are most strongly associated with reading fluency among adult readers?

**RQ2:** Which factors are most strongly associated with reading comprehension?

**RQ3:** What is the relationship between reading fluency and reading comprehension in adult populations?

**RQ4:** To what extent do reading behaviors, vocabulary knowledge, cognitive abilities, and educational experiences explain variation in adult reading performance?

**RQ5:** Can statistical and machine learning models identify informative predictors of reading fluency and comprehension?

## Research Hypotheses

| ID | Hypothesis |
|---|---|
| H1 | Vocabulary knowledge will be positively associated with reading comprehension. |
| H2 | Word recognition accuracy and decoding ability will be positively associated with reading fluency. |
| H3 | Reading fluency and comprehension will exhibit a positive statistical association. |
| H4 | Reading behaviors and educational experiences will explain additional variation after accounting for foundational reading skills. |
| H5 | Background knowledge and reasoning abilities will be positively associated with reading comprehension after accounting for relevant reading skills. |

These hypotheses have not yet been tested.

## Research Population

The target population consists of adult readers aged 18 years and older.

Depending on dataset availability, the study may include:

- College and university students
- Working adults
- Adult learners
- Adults with varying educational backgrounds
- Native and nonnative English readers, when supported by the selected dataset

The final sample and generalizability of findings will depend on the selected data source.

## Potential Research Variables

| Category | Candidate Variables |
|---|---|
| Linguistic | Vocabulary knowledge, decoding accuracy, word recognition |
| Cognitive | Working memory, attention, reasoning ability |
| Behavioral | Reading frequency, reading motivation, reading strategies |
| Educational | Educational attainment, literacy instruction, academic background |
| Contextual | Passage difficulty, text genre, language experience |
| Demographic | Age and other ethically appropriate background variables |

### Primary Outcome Variables

1. Reading fluency or a validated adult reading-efficiency measure.
2. Reading comprehension assessment performance.

The final operational definitions will be determined after selecting and evaluating the datasets.

---

## Research Methodology

The project follows a data science life cycle informed by CRISP-DM.

### Phase 1: Problem Definition

- Establish the research problem.
- Identify the target population.
- Develop research questions.
- Establish hypotheses.
- Identify potential variables.

**Status: Completed**

### Phase 2: Data Collection and Evaluation

- Identify credible adult literacy datasets.
- Examine participant demographics and sampling methods.
- Verify available fluency and comprehension measurements.
- Evaluate data quality, access conditions, and licensing.
- Select appropriate datasets for analysis.

**Status: In Progress**

### Phase 3: Data Cleaning and Preparation

- Inspect missing values and duplicates.
- Evaluate data consistency and measurement validity.
- Address data quality issues.
- Prepare reproducible preprocessing pipelines.

### Phase 4: Exploratory Data Analysis

- Analyze reading performance distributions.
- Investigate relationships between variables.
- Develop statistical summaries.
- Produce visualizations.

### Phase 5: Feature Engineering

- Identify relevant predictors.
- Encode categorical variables.
- Transform features where appropriate.
- Prevent data leakage.

### Phase 6: Statistical Analysis and Machine Learning

- Conduct correlation analysis.
- Develop regression models.
- Compare predictive algorithms.
- Investigate feature importance and model interpretation.

Candidate models include linear regression, regularized regression, Random Forest, and gradient boosting.

### Phase 7: Model Evaluation

- Evaluate generalization performance.
- Compare predictions against baseline models.
- Examine prediction errors.
- Investigate uncertainty and potential bias.

### Phase 8: Visualization and Deployment

- Develop research visualizations.
- Create an optional interactive dashboard.
- Document findings and model limitations.

### Phase 9: Research Communication

- Prepare the final research report.
- Summarize statistical findings.
- Discuss implications for adult literacy research.
- Identify directions for future study.

---

## Candidate Research Datasets

The following datasets are being evaluated.

| Dataset | Research Relevance | Selection Status |
|---|---|---|
| OneStop Eye Movements | Adult reading behavior and comprehension | Under evaluation |
| PIAAC | Adult literacy and educational background | Under evaluation |
| GECO | Reading processes and eye movements | Under evaluation |
| CELER | Reading behavior across language backgrounds | Under evaluation |

Dataset inclusion has not been finalized.

A dataset containing eye-tracking measurements will not automatically be considered a direct measure of reading fluency.

## Proposed Technology Stack

| Purpose | Technology |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Statistical Analysis | SciPy, Statsmodels |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Development | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |
| Dashboard (Optional) | Streamlit |

The final technology stack may change according to the analytical requirements.

## Repository Structure

```text
adult-reading-literacy-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── problem_statement.md
│   ├── research_questions.md
│   ├── methodology.md
│   ├── data_dictionary.md
│   └── dataset_sources.md
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_statistical_analysis.ipynb
│   └── 04_machine_learning.ipynb
│
├── src/
├── reports/
│   └── figures/
├── tests/
│
├── .gitignore
├── requirements.txt
└── README.md
```

This is the planned repository structure. Files and directories will be added as the corresponding research phases begin.

## Project Roadmap

- [x] Define the research problem.
- [x] Establish the adult reader population.
- [x] Develop initial research questions.
- [x] Develop preliminary hypotheses.
- [x] Identify candidate research variables.
- [x] Identify initial dataset candidates.
- [ ] Verify dataset access, measurements, and suitability.
- [ ] Select the primary research dataset.
- [ ] Finalize the data dictionary.
- [ ] Perform data cleaning and preparation.
- [ ] Conduct exploratory data analysis.
- [ ] Perform statistical modeling.
- [ ] Develop machine learning models.
- [ ] Evaluate model performance and interpretability.
- [ ] Develop research visualizations or a dashboard.
- [ ] Publish the final research report.

## Research Ethics and Limitations

This research emphasizes responsible data science practices.

Considerations include:

- Protecting participant privacy and confidentiality.
- Following data licensing and access restrictions.
- Using appropriate reading assessment instruments.
- Evaluating sampling bias and measurement limitations.
- Assessing potential disparities in model performance.
- Avoiding unsupported causal conclusions.

**Statistical association does not establish causation. Machine learning feature importance does not establish causal influence.**

## Expected Research Deliverables

The project aims to produce:

1. A documented dataset selection process.
2. Reproducible data preprocessing and analysis.
3. Statistical findings on adult reading performance.
4. Evaluated machine learning models.
5. Research visualizations.
6. A comparison of factors associated with reading fluency and comprehension.
7. A final research report.

These are intended outcomes, not completed findings.

## Future Research Opportunities

Potential future extensions include:

- AI-assisted reading comprehension tools.
- Personalized adult literacy learning systems.
- Reading interventions and literacy support.
- Comparisons across educational backgrounds.
- Longitudinal investigations of adult reading development.

## Project Author

**Shawn Watson**

Undergraduate researcher interested in educational data science, artificial intelligence, machine learning, literacy, and the application of technology to learning and educational outcomes.

## Project Status

**Current Phase:** Phase 2 — Dataset Identification and Evaluation

**Next Milestone:** Verify and select appropriate adult reading research datasets.

This repository will be updated throughout the research process.

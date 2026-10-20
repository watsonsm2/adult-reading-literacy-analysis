# Data Dictionary

**Project:** Reading Fluency and Comprehension Among Adult Readers  
**Research Domain:** Educational Data Science and Machine Learning  
**Target Population:** Adults aged 18 years and older  
**Research Phase:** Phase 2 — Dataset Identification and Evaluation  
**Document Version:** 0.1 — Preliminary  
**Dataset Status:** Not Yet Selected

---

## 1. Purpose

This document defines the proposed variables, data types, measurement methods, and analytical roles for the research project.

The study aims to identify linguistic, cognitive, behavioral, educational, and contextual factors associated with reading fluency and reading comprehension among adult readers.

This dictionary contains conceptual variable definitions. Actual dataset column names, permitted values, missing-value codes, and assessment scoring rules will be documented after a dataset is selected.

## 2. Unit of Analysis

The proposed unit of analysis is an adult participant's reading assessment.

Depending on the dataset, observations may represent:

- Individual adult participants.
- Participant-passage combinations.
- Repeated reading assessments.
- Individual reading trials.

Repeated observations from the same participant will not be treated as independent without an appropriate statistical justification.

Participant and passage identifiers may be required to support valid analysis.

## 3. Dependent Variables

Dependent variables represent the reading outcomes under investigation.

| Variable | Description | Proposed Type |
|---|---|---|
| `reading_fluency_score` | Validated reading fluency or efficiency outcome | Float |
| `reading_comprehension_score` | Performance on a reading comprehension assessment | Float |

### 3.1 Reading Fluency

Reading fluency involves accurate, appropriately paced, and expressive reading.

Potential measurements include:

- Correct words per minute.
- Word recognition accuracy.
- Oral reading prosody.
- Validated adult reading fluency assessments.
- Standardized reading-efficiency scores.

Reading speed, total reading time, and eye-movement measures may be analyzed as distinct reading-process indicators. They must not automatically be labeled as measures of full reading fluency.

### 3.2 Reading Comprehension

Reading comprehension describes an individual's ability to understand, interpret, integrate, and evaluate written information.

Possible measurements include:

- Standardized reading comprehension scores.
- Passage-level comprehension accuracy.
- Literal and inferential question performance.
- Academic or functional literacy assessment results.

The final outcome definition will depend on the scoring procedures of the selected assessment.

## 4. Independent Variables

Independent variables are potential predictors of adult reading performance.

### 4.1 Linguistic Factors

| Variable | Description | Proposed Type |
|---|---|---|
| `vocabulary_score` | Vocabulary knowledge assessment | Float |
| `decoding_accuracy` | Accuracy of word decoding | Float |
| `word_recognition_score` | Word recognition ability | Float |
| `syntactic_knowledge_score` | Understanding of grammatical structures | Float |
| `morphological_awareness` | Understanding of meaningful word components | Float |
| `language_proficiency_score` | Language proficiency assessment | Float |

These factors may help explain differences in word recognition, reading efficiency, and text comprehension.

### 4.2 Cognitive Factors

| Variable | Description | Proposed Type |
|---|---|---|
| `working_memory_score` | Working memory assessment | Float |
| `attention_score` | Attention assessment performance | Float |
| `reasoning_ability_score` | Reasoning assessment performance | Float |
| `metacognitive_awareness` | Awareness of cognitive processes | Float |

These variables represent possible cognitive correlates of reading performance.

The final analysis will use validated measurements where available.

### 4.3 Behavioral Factors

| Variable | Description | Proposed Type |
|---|---|---|
| `reading_frequency` | Reading frequency over a defined period | Integer or Float |
| `reading_duration` | Time spent reading within a defined period | Float |
| `reading_motivation_score` | Reading motivation assessment | Float |
| `reading_strategy_score` | Reported or assessed use of reading strategies | Float |
| `reading_purpose` | Purpose of reading activity | Categorical |

Reading frequency and duration must include a clearly defined reference period and unit.

### 4.4 Educational Factors

| Variable | Description | Proposed Type |
|---|---|---|
| `education_level` | Highest educational attainment | Categorical |
| `years_of_education` | Completed years of formal education | Float |
| `educational_enrollment` | Current education enrollment status | Categorical |
| `prior_literacy_instruction` | Documented literacy instruction experience | Categorical |
| `adult_education_participation` | Participation in adult learning programs | Boolean or Categorical |

Educational background may help explain differences in literacy experiences and assessment performance.

### 4.5 Contextual and Reading-Task Factors

| Variable | Description | Proposed Type |
|---|---|---|
| `background_knowledge_score` | Knowledge of passage subject matter | Float |
| `text_difficulty` | Standardized text complexity | Float or Categorical |
| `text_genre` | Category of reading material | Categorical |
| `reading_format` | Digital or print reading format | Categorical |
| `language_background` | Documented language-learning background | Categorical |
| `passage_id` | Identifier for reading passage | String |

Text characteristics may be important when interpreting performance across different reading tasks.

## 5. Additional Adult Population Variables

Because the target population includes adult readers rather than only university students, the following variables may be relevant.

| Variable | Description | Proposed Type |
|---|---|---|
| `participant_age` | Participant age in years | Integer |
| `employment_status` | Employment category | Categorical |
| `occupation_category` | Occupational classification | Categorical |
| `education_level` | Educational attainment | Categorical |
| `years_of_education` | Formal education duration | Float |
| `language_background` | Language experience | Categorical |
| `adult_learning_status` | Participation in adult education | Categorical |

These variables may function as predictors, controls, or subgroup descriptors depending on the research design.

Sensitive or potentially identifying variables will be used only when justified and permitted.

## 6. Reading-Process Indicators

Some candidate datasets contain behavioral measurements collected during reading.

These measures may help characterize reading processes but should not automatically be interpreted as direct fluency measures.

| Variable | Description | Proposed Type |
|---|---|---|
| `total_reading_time` | Time spent reading a passage | Float |
| `reading_rate` | Words read per unit of time | Float |
| `fixation_duration` | Eye fixation duration | Float |
| `fixation_count` | Number of recorded fixations | Integer |
| `regression_count` | Number of backward eye movements | Integer |
| `rereading_frequency` | Frequency of rereading behavior | Integer or Float |

All time measurements must specify their units.

If reading rate is calculated from passage length and reading time, the derived measurement procedure must be documented.

When analyzing comprehension, reading-process indicators measured during the same task must be distinguished from information available before the task.

## 7. Potential Control Variables

Potential controls include:

- Participant age.
- Language background.
- Educational attainment.
- Text difficulty.
- Passage genre.
- Reading condition.
- Assessment instrument.
- Dataset or research study identifier.

Control variable selection will depend on the research design and a documented rationale.

## 8. Dataset Identification Variables

If multiple research datasets are used, source information must be retained.

| Variable | Description |
|---|---|
| `dataset_id` | Dataset identifier |
| `dataset_source` | Original data source |
| `participant_id` | Deidentified participant identifier |
| `assessment_id` | Reading assessment identifier |
| `passage_id` | Reading passage identifier |
| `assessment_date` | Assessment date, if available and permitted |

Identifiers will support reproducibility and appropriate treatment of repeated measurements.

They must not reveal identifiable participant information in the public repository.

## 9. Data Types and Measurement Standards

The following conventions will guide the final dictionary.

**Integer:** Whole-number values, such as fixation counts.

**Float:** Continuous numerical values, such as assessment scores or reading durations.

**Categorical:** Variables representing defined groups, such as educational attainment.

**Boolean:** Variables containing true/false values.

**String:** Textual identifiers or labels.

All continuous measures must have documented units and valid ranges.

Categorical variables must have documented coding schemes.

## 10. Data Quality Requirements

The selected dataset will be evaluated for:

1. Missing values.
2. Duplicate observations.
3. Inconsistent data types.
4. Invalid or implausible scores.
5. Unclear measurement units.
6. Inconsistent categorical values.
7. Unreliable assessment measures.
8. Sampling and selection bias.
9. Potential data leakage.
10. Incomplete documentation.

Data quality findings will be recorded before formal statistical analysis.

## 11. Missing Data Handling

Missing-value procedures will be selected based on the dataset and research objectives.

Possible approaches include:

- Missingness summaries.
- Complete-case analysis where justified.
- Statistical imputation.
- Missingness indicators.
- Sensitivity analyses.

Missing data will not automatically be replaced with zero or the mean.

For predictive modeling, imputation procedures will be fitted using training data only.

## 12. Dataset Variable Availability

Each proposed variable will be assigned an availability status after dataset selection.

| Status | Definition |
|---|---|
| Available | Directly measured in the dataset |
| Derived | Can be constructed from documented source variables |
| Unavailable | Cannot be measured using the dataset |

Variables marked unavailable will not be fabricated or replaced with unrelated measurements.

Research questions and model specifications may be revised based on variable availability.

## 13. Research Ethics and Privacy

This project will follow responsible data science practices.

The public GitHub repository must not include:

- Personally identifiable participant records.
- Private educational records.
- Restricted research data without redistribution permission.
- Credentials or access tokens.
- Confidential participant-level assessment information.

Participant privacy, licensing requirements, and institutional research obligations will be respected.

## 14. Dictionary Versioning

### Version 0.1 — Preliminary

Conceptual variables and proposed measurements.

**Current version**

### Version 0.2 — Dataset Selection

Verified dataset column names, data types, scoring procedures, source documentation, and variable availability.

### Version 1.0 — Analysis-Ready

Final variable definitions, coding schemes, preprocessing decisions, transformations, and measurement limitations.

## 15. Next Steps

1. Compare candidate adult reading datasets.
2. Verify dataset access and licensing.
3. Identify available reading outcome measures.
4. Determine whether fluency and comprehension can both be analyzed.
5. Review available linguistic, cognitive, behavioral, and educational predictors.
6. Select the primary dataset.
7. Update this dictionary using verified dataset fields.

---

**Current Status:** Preliminary Data Dictionary  
**Research Phase:** Phase 2 — Dataset Identification and Evaluation  
**Next Milestone:** Primary Dataset Selection

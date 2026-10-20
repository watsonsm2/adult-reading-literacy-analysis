# Data Dictionary

**Project:** Reading Fluency and Comprehension Among College and University Students  
**Research Domain:** Educational Data Science and Machine Learning  
**Research Phase:** Phase 1 — Problem Definition  
**Document Status:** Preliminary Data Dictionary  
**Dataset Status:** Not Yet Selected

---

## 1. Purpose

This data dictionary documents the proposed variables, definitions, data types, measurement methods, and intended analytical roles for the research project.

The study aims to identify linguistic, cognitive, behavioral, and educational factors associated with reading fluency and reading comprehension among college and university students.

The dictionary will be updated once an appropriate research dataset has been selected and its actual variables have been verified.

## 2. Unit of Analysis

The proposed unit of analysis is an individual college or university student's reading assessment.

If the selected dataset contains multiple assessments per student, the analysis will account for repeated observations.

No personally identifying student information will be published in this repository.

## 3. Dependent Variables

Dependent variables represent the primary reading outcomes being investigated.

| Variable | Description | Data Type | Measurement |
|---|---|---|---|
| `reading_fluency_score` | Student reading fluency or efficiency | Float | Validated assessment score |
| `reading_comprehension_score` | Student understanding of written material | Float | Validated comprehension assessment |

### Reading Fluency

Reading fluency involves accurate, appropriately paced, and expressive reading.

Potential measurements include:

- Correct words per minute.
- Word-reading accuracy.
- Oral reading prosody.
- Validated adult reading-efficiency scores.

Because this research focuses on college students, the measurement instrument must be appropriate for adult readers.

### Reading Comprehension

Reading comprehension refers to the ability to understand, interpret, integrate, and evaluate written information.

Potential measurements include:

- Standardized comprehension assessment scores.
- Passage-based comprehension performance.
- Inferential question accuracy.
- Academic text interpretation assessments.

Raw scores from different instruments must not be combined without an appropriate measurement justification.

## 4. Independent Variables

Independent variables are candidate predictors whose associations with reading outcomes will be investigated.

### 4.1 Linguistic Factors

| Variable | Description | Data Type |
|---|---|---|
| `vocabulary_score` | Vocabulary knowledge assessment | Float |
| `decoding_accuracy` | Accuracy of word decoding | Float |
| `word_recognition_score` | Word recognition ability | Float |
| `syntactic_knowledge_score` | Understanding of grammatical structures | Float |
| `morphological_awareness` | Ability to recognize meaningful word components | Float |

**Research relevance:** Linguistic abilities may be associated with both reading efficiency and comprehension.

### 4.2 Cognitive Factors

| Variable | Description | Data Type |
|---|---|---|
| `working_memory_score` | Working memory assessment performance | Float |
| `attention_score` | Performance on an attention assessment | Float |
| `reasoning_ability_score` | Reasoning assessment performance | Float |
| `metacognitive_awareness` | Awareness and monitoring of thinking processes | Float |

**Research relevance:** Cognitive processes may contribute to how students process, retain, and interpret written information.

### 4.3 Behavioral Factors

| Variable | Description | Data Type |
|---|---|---|
| `reading_frequency` | Frequency of reading activities | Integer or Float |
| `reading_duration` | Time spent reading during a defined period | Float |
| `reading_motivation_score` | Reading motivation assessment | Float |
| `reading_strategy_score` | Use of reading comprehension strategies | Float |

**Research relevance:** Reading behaviors and motivation may be associated with differences in performance.

### 4.4 Educational Factors

| Variable | Description | Data Type |
|---|---|---|
| `academic_year` | Year or level of university study | Categorical |
| `academic_major` | Student's academic discipline | Categorical |
| `prior_academic_preparation` | Prior educational preparation | Float or Categorical |
| `literacy_support_access` | Access to academic reading support | Boolean or Categorical |
| `institution_type` | Type of postsecondary institution | Categorical |

**Research relevance:** Educational experiences may help explain differences in academic reading development.

### 4.5 Contextual Factors

| Variable | Description | Data Type |
|---|---|---|
| `background_knowledge_score` | Familiarity with passage subject matter | Float |
| `text_difficulty` | Complexity of reading material | Float or Categorical |
| `text_genre` | Type of reading material | Categorical |
| `reading_format` | Digital or printed text | Categorical |
| `language_background` | Documented language-learning background | Categorical |

**Research relevance:** Reading comprehension can depend on both the reader and the characteristics of the text.

## 5. Potential Control Variables

Control variables may help account for alternative explanations of observed relationships.

| Variable | Description |
|---|---|
| `age` | Student age |
| `academic_year` | Educational level |
| `institution_id` | Deidentified institution identifier |
| `language_background` | Relevant language experience |
| `text_difficulty` | Reading passage complexity |

Control variables will be selected according to the research question, theoretical justification, and available data.

A variable may serve as a predictor, control, or moderator in different analyses.

## 6. Variable Measurement Requirements

For every variable included in the final dataset, the following information must be documented:

1. Actual dataset column name.
2. Variable definition.
3. Data type.
4. Unit of measurement.
5. Assessment instrument or data collection method.
6. Valid range or permitted categories.
7. Missing-value representation.
8. Data source.
9. Collection time or assessment period.
10. Relevant limitations.

For questionnaire-based variables, the final dictionary should also record the scale and scoring direction.

For example, higher values should not automatically be interpreted as greater motivation unless the instrument documentation confirms this.

## 7. Data Quality Requirements

The selected dataset will be examined for:

- Missing observations.
- Duplicate records.
- Invalid data types.
- Out-of-range values.
- Inconsistent category labels.
- Implausible assessment scores.
- Measurement reliability.
- Potential selection bias.

Data quality findings will be documented before statistical modeling.

## 8. Missing Data Handling

Missing-value procedures will depend on the selected dataset.

Potential approaches include:

- Describing missingness by variable.
- Examining patterns of missing observations.
- Complete-case analysis where justified.
- Statistical imputation where appropriate.
- Sensitivity analysis.

Missing values will not automatically be replaced with zero or a variable's mean.

For predictive modeling, imputation parameters must be estimated using training data only.

## 9. Data Privacy and Ethical Considerations

The project will follow responsible educational data practices.

The public GitHub repository must not contain:

- Student names.
- Student identification numbers.
- Private educational records.
- Confidential assessment results.
- Credentials or access tokens.
- Restricted datasets without redistribution permission.

Deidentified data will be handled according to the applicable access agreement and institutional requirements.

## 10. Data Dictionary Validation

After choosing a dataset, each proposed variable will be assigned one of three statuses:

| Status | Meaning |
|---|---|
| Available | Variable exists and can be appropriately measured |
| Derived | Variable can be constructed using documented source fields |
| Unavailable | Variable cannot be measured using the selected dataset |

Unavailable variables will not be fabricated or replaced by unrelated proxies.

Any major differences between proposed and available variables will require reconsideration of the research questions.

## 11. Future Updates

This dictionary will evolve through the following stages:

**Version 0.1 — Preliminary**

Initial proposed variables and conceptual definitions.

**Version 0.2 — Dataset Selection**

Actual dataset fields, source information, and availability classifications.

**Version 1.0 — Analysis-Ready**

Final variable definitions, transformations, coding schemes, missing-value rules, and measurement documentation.

## 12. Next Steps

1. Identify datasets containing college-level reading assessments.
2. Evaluate whether both fluency and comprehension are measured.
3. Verify the availability of relevant predictors.
4. Review dataset permissions and assessment validity.
5. Update this dictionary with actual dataset column names and measurement details.

---

**Current Status:** Preliminary — No Dataset Selected  
**Next Phase:** Phase 2 — Data Collection and Dataset Evaluation

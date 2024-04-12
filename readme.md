
---

# Feature Extraction from Software Reviews

## Introduction

This project aims to extract useful feature sets from both positive and negative software reviews using natural language processing techniques. The extracted features can be utilized to gain insights into customer sentiments, identify key aspects of software products that users appreciate or dislike, and inform decision-making processes for product improvement and marketing strategies.

## Approach

### Data Collection

- Survey responses were fetched from the G2 website using their API.
- Responses were saved as JSON files for further processing.

### Data Preprocessing

- Relevant information was extracted from the JSON files, including comments and secondary answers.
- Additional features such as review sources and incentivization status were extracted.
- Text columns were preprocessed to remove unnecessary characters.

### Feature Extraction

- TF-IDF (Term Frequency-Inverse Document Frequency) was used to extract key word pairs from both positive (love and benefits) and negative (hate and recommendations) reviews.
- Top TF-IDF word pairs were selected for further analysis.

### Model Building

- Feature selection was performed using a pre-trained language model (LLM).
- Feature sets were generated based on the top word pairs extracted from the reviews.

## Findings

- Positive reviews highlighted features such as gathering customer feedback, brand awareness, social proof, and efficient marketing as key strengths of the software.
- Negative reviews identified issues related to pricing transparency, customization limitations, insufficient support, and integration difficulties.

### Running the Application

1. Open the Jupyter Notebook file `DaalChawal.ipynb` in your Jupyter environment.

2. Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

3. Execute the cells in the notebook to run each part of the analysis step by step. Make sure to execute them in order.

4. The notebook contains explanations and code for each step of the analysis, including data collection, preprocessing, feature extraction, model building, and visualization.

5. Follow the instructions provided in the notebook to understand the code and the results of each step.

6. The result will be displayed in the notebook and it will also start a streamlit app where you can see the output.

### Files

- `DaalChawal.ipynb`: Jupyter Notebook containing the code and explanations for the analysis.
- `app.py`: Custom module for output using streamlit.
- `responses/`: Directory containing JSON files of survey responses.
- `survey_responses.csv`: CSV file containing preprocessed survey response data.
- `response_positive.txt`: Text file containing feature sets generated for positive reviews.
- `response_negative.txt`: Text file containing feature sets generated for negative reviews.

## Contributors

- Deepak Parmar
- Samar Pratap
- Tushar Pandita

---
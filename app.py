import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file


@st.cache_data
def load_data():
    df = pd.read_csv('survey_responses.csv')
    return df


df = load_data()

# Drop rows where all values are NaN
df = df.dropna(how='all')
st.sidebar.title("DaalChawal 🍲")
# Define colors for the bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Define the list of features with underscores
features = ['meets_requirements', 'ease_of_use', 'quality_of_support',
            'ease_of_setup', 'ease_of_admin', 'ease_of_doing_business_with']

# Define the list of features without underscores for display
feature_names_display = ['Meets Requirements', 'Ease of Use', 'Quality of Support',
                         'Ease of Setup', 'Ease of Admin', 'Ease of Doing Business With']

# Sidebar for selecting feature
selected_feature_index = st.sidebar.selectbox(
    "Select Feature",
    range(len(features)),
    format_func=lambda x: feature_names_display[x]
)

# Button to show text file
if st.sidebar.button('Feature Sets Customer Liked'):
    with open('response_positive.txt', 'r') as file:
        st.write(file.read())

if st.sidebar.button('Customer asks for improvement'):
    with open('response_negative.txt', 'r') as file:
        st.write(file.read())

else:
    selected_feature = features[selected_feature_index]
    # Display bar chart for selected feature
    st.write(f"### {feature_names_display[selected_feature_index]} Ratings")
    ratings_counts = df[selected_feature].value_counts().sort_index()
    st.bar_chart(ratings_counts,
                 color=colors[selected_feature_index % len(colors)])

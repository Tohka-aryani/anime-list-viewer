import pandas as pd
import streamlit as st

# Load the anime review data from CSV file
def load_data():
    data = pd.read_csv("Book1.csv")
    return data

# Save the anime review data to CSV file
def save_data(data):
    data.to_csv("Book1.csv", index=False)

# Add new anime review to the data
def add_review(data, anime_title, animation_studio, status, genre, rating, notes):
    new_row = {'Anime Title': anime_title,
               'Animation Studio': animation_studio,
               'Status': status,
               'Genre': genre,
               'Rating': rating,
               'Notes': notes}
    data = data.append(new_row, ignore_index=True)
    return data

# Filter the data based on status
def filter_data(data, status):
    if status == "All":
        return data
    filtered_data = data[data['Status'] == status]
    return filtered_data

# Main function
def main():
    st.title("Anime Review List")

    # Load data from CSV file
    data = load_data()

    # Add new review form
    st.subheader("Add New Review")
    anime_title = st.text_input("Anime Title")
    animation_studio = st.text_input


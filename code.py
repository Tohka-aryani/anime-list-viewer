import streamlit as st
import pandas as pd

# Function to read the CSV file
def load_data():
    data = pd.read_csv('Book1.csv')
    return data

# Function to save data to the CSV file
def save_data(data):
    data.to_csv('Book1.csv', index=False)

# Function to filter data based on status
def filter_data(data, status):
    if status == 'All':
        return data
    filtered_data = data[data['Status'] == status]
    return filtered_data

# Main function
def main():
    st.title("Anime Review List")
    data = load_data()

    # Display the form page to insert new data
    st.subheader("Insert New Data")
    anime_title = st.text_input("Anime Title")
    animation_studio = st.text_input("Animation Studio")
    status = st.selectbox("Status", ['Watching', 'Completed', 'On Hold', 'Dropped'])
    genre = st.text_input("Genre")
    rating = st.slider("Rating", min_value=0, max_value=10, step=0.5)
    notes = st.text_area("Notes")
    if st.button("Add"):
        new_data = {'Anime Title': anime_title, 'Animation Studio': animation_studio, 'Status': status,
                    'Genre': genre, 'Rating': rating, 'Notes': notes}
        data = data.append(new_data, ignore_index=True)
        save_data(data)
        st.success("New data has been added!")

    # Display search and filter bar
    st.subheader("Search and Filter")
    status_filter = st.selectbox("Filter by Status", ['All', 'Watching', 'Completed', 'On Hold', 'Dropped'])
    filtered_data = filter_data(data, status_filter)

    # Display the filtered data
    st.subheader("Anime Review List")
    st.dataframe(filtered_data)

if __name__ == '__main__':
    main()


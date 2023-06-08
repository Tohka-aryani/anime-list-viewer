import pandas as pd
import streamlit as st

# Define the path to the CSV file
CSV_FILE = "anime_reviews.csv"

# Create a form page for inserting new data
def add_anime_review():
    st.header("Add Anime Review")
    anime_title = st.text_input("Anime Title")
    animation_studio = st.text_input("Animation Studio")
    status = st.selectbox("Status", ["Watching", "Completed", "On Hold", "Dropped"])
    genre = st.text_input("Genre")
    rating = st.slider("Rating", min_value=1, max_value=10, step=1)
    notes = st.text_area("Notes")
    submit = st.button("Submit")

    if submit:
        new_review = {
            "Anime Title": anime_title,
            "Animation Studio": animation_studio,
            "Status": status,
            "Genre": genre,
            "Rating": rating,
            "Notes": notes
        }

        df = pd.read_csv(CSV_FILE)
        df = df.append(new_review, ignore_index=True)
        df.to_csv(CSV_FILE, index=False)

        st.success("Anime review added successfully!")

# Search and filter anime reviews by status
def search_anime_reviews():
    st.header("Search Anime Reviews")
    status_filter = st.selectbox("Filter by Status", ["All", "Watching", "Completed", "On Hold", "Dropped"])

    df = pd.read_csv(CSV_FILE)

    if status_filter != "All":
        df = df[df["Status"] == status_filter]

    st.table(df)

# Main program
def main():
    st.title("Anime Review List")

    # Create the CSV file if it doesn't exist
    try:
        df = pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Anime Title", "Animation Studio", "Status", "Genre", "Rating", "Notes"])
        df.to_csv(CSV_FILE, index=False)

    menu_choice = st.sidebar.selectbox("Menu", ["Add Anime Review", "Search Anime Reviews"])

    if menu_choice == "Add Anime Review":
        add_anime_review()
    elif menu_choice == "Search Anime Reviews":
        search_anime_reviews()

if __name__ == "__main__":
    main()

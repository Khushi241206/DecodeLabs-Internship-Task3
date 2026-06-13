import streamlit as st
from recommendations import recommend

st.title("AI Recommendation System")

options = [
    "coding",
    "python",
    "technology",
    "ai",
    "camera",
    "art",
    "creative",
    "design",
    "health",
    "gym",
    "exercise",
    "mindfulness"
]

user_choices = st.multiselect(
    "Select your interests",
    options
)

if st.button("Get Recommendations"):

    results = recommend(user_choices)

    st.subheader("Recommended Items")

    for item in results:
        if item["score"] > 0:
            st.write(
                f"✅ {item['name']} (Match Score: {item['score']})"
            )
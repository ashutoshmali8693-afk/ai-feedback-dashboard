import streamlit as st
import pandas as pd
from datetime import datetime
import os
import llm_utils

st.title("Customer Feedback")

rating = st.selectbox("Select rating", [1, 2, 3, 4, 5])
review = st.text_area("Write your review")

if st.button("Submit"):
    if review.strip() == "":
        st.error("Review cannot be empty")
    else:
        if not os.path.exists("data"):
            os.makedirs("data")

        file_path = "data/reviews.csv"

        if not os.path.exists(file_path):
            pd.DataFrame(columns=[
                "timestamp",
                "rating",
                "review",
                "ai_response",
                "ai_summary",
                "ai_action"
            ]).to_csv(file_path, index=False)

        ai_response = llm_utils.generate_user_response(review, rating)
        ai_summary = llm_utils.generate_summary(review)
        ai_action = llm_utils.generate_recommended_action(review, rating)

        data = {
            "timestamp": datetime.now(),
            "rating": rating,
            "review": review,
            "ai_response": ai_response,
            "ai_summary": ai_summary,
            "ai_action": ai_action
        }

        pd.DataFrame([data]).to_csv(
            file_path, mode="a", header=False, index=False
        )

        st.success(ai_response)

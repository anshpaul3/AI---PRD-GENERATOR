import streamlit as st
import google.generativeai as genai


genai.configure(api_key="API_key")


model = genai.GenerativeModel("gemini-2.5-flash")


st.header("Product Requirement Document Generator")


product_name = st.text_input("Product Name")
problem_statement = st.text_area("Problem Statement")
target_user = st.text_area("Target Users")
features = st.text_area("Features")
success_metrics = st.text_area("Success Metrics")

generate_button = st.button("Generate PRD")

if generate_button:

    if not product_name:
        st.warning("Please enter a product name")

    else:

        with st.spinner("Analyzing and Generating..."):

            # PRD Prompt
            prompt = f"""
Create a professional Product Requirement Document.

Product Name:
{product_name}

Problem Statement:
{problem_statement}

Target Users:
{target_user}

Features:
{features}

Success Metrics:
{success_metrics}

Generate the PRD in the following format:

# Product Overview

# Problem Statement

# Target Users

# Features

# Success Metrics

# Risks and Assumptions

# Future Enhancements

Use bullet points where appropriate.
"""

            # Generate PRD
            response = model.generate_content(prompt)

            # Store PRD
            prd = response.text

            # Display PRD
            st.subheader("Generated PRD")
            st.write(prd)

            # Download Button
            st.download_button(
                "Download PRD",
                prd,
                file_name=f"{product_name}_PRD.txt"
            )

            # Review Prompt
            review_prompt = f"""
Review the following Product Requirement Document.

Provide:

1. Score out of 10
2. Strengths
3. Missing Areas
4. Improvement Suggestions

PRD:

{prd}
"""

            # Generate Review
            review = model.generate_content(review_prompt)

            # Display Review
            st.subheader("Scope of Improvement")
            st.write(review.text)
import streamlit as st
import google.generativeai as genai

genai.configure(api_key ="api_key")
model = genai.GenerativeModel("gemini-2.5-flash") 

st.header("Product Requirement Document Generator")

product_name = st.text_input ("Product name")

problem_statement =st.text_area("problem statement")

target_user =st.text_area("target user")

success_metrics = st.text_area("success metrics")

features = st.text_area("features")

generate_button = st.button("Click to Generate PRD")

if generate_button:
    
   if not product_name:
      st.warning ("please enter product name")
   else:
      st.write("generating ....") 
      
with st.spinner("Analyzing and Generating...."):

  prompt = f"""
  create a professional product requirement document  
  
  product_name:
  {product_name} 
  
  Target_Users:
  {target_user}

  Features:
  {features}

  Success_Metrics:
  {success_metrics}
  
 Generate the prd in this format:
  
# Product Overview

# Problem Statement

# Target Users

# Features

# Success Metrics

# Risks and Assumptions

# Future Enhancements

Use bullet points where appropriate.

  """
  
  response = model.generate_content(prompt)
  st.write(response.text)

  st.write("##product name")
  st.write(product_name)

  st.write("##problem statement")
  st.write(problem_statement)

  st.write("##target user")
  st.write(target_user)

  st.write("##features")
  st.write(features)

  st.write("##success metrics")
  st.write(success_metrics)

  prd = response.text
  st.write(prd)
  st.download_button("Download prd", prd, file_name=f"{product_name}_prd.txt")

  review_prompt = f"""
  Review the following product requirment document and provide feedback on how to improve it
  be specific and blunt in your feedback and also provide suggestions on how to improve it 
  {prd}

  """
  review = model.generate_content(review_prompt)
  st.subheader("Scope of Improvement")
  st.write(review.text)

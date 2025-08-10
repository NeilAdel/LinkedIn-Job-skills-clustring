import streamlit as st
import pandas as pd
from src.app import load_data, generate_skill_matrix, perform_clustering

def main():
    st.title("LinkedIn Job Skills Clustering")
    
    st.sidebar.header("Upload Job Descriptions")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Load and display the data
        data = load_data(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(data.head())
        
        # Generate the binary skill matrix
        skill_matrix = generate_skill_matrix(data)
        st.write("Binary Skill Matrix:")
        st.dataframe(skill_matrix.head())
        
        # Perform clustering
        clusters = perform_clustering(skill_matrix)
        st.write("Clustering Results:")
        st.dataframe(clusters)

        # Display additional insights or visualizations here
        st.write("Explore the clusters and insights derived from the job descriptions.")
    
if __name__ == "__main__":
    main()
import streamlit as st

def main():
    st.set_page_config(page_title="Churn Prediction", page_icon="🧊", layout="wide",initial_sidebar_state='expanded')
    with st.container():
        st.title("Welcome to Churn Prediction App")
        st.subheader("This app predicts the probability of churn for a telecom company")
        pass

    st.sidebar.header("User Input Features")

    col1 , col2 = st.columns([4,1])
    with col1:
        st.write("This is column 1")
        pass
    with col2:
        st.write("This is column 2")
        pass


if __name__ == "__main__":
    main()
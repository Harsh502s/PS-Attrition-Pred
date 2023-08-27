import streamlit as st

def add_sidebar():
    st.sidebar.header("Churn Prediction Parameters")

    slider_labels = [
        ('Age of Employee', 'Age'),
        ('Business Travel Frequently', 'BusinessTravel_Travel_Frequently'),
        ('Daily Rate', 'DailyRate'),
        ('Department Sales', 'Department_Sales'),
        ('Distance from Home', 'DistanceFromHome'),
        ('Education Field Of Employee', 'EducationField'),
        ('Environment Satisfaction', 'EnvironmentSatisfaction'),
        ('Hourly Rate', 'HourlyRate'),
        ('Job Involvement', 'JobInvolvement'),
        ('Job Level', 'JobLevel'),
        ('Job Role', 'JobRole'),
        ('Monthly Income', 'MonthlyIncome'),
        ('Monthly Rate', 'MonthlyRate'),
        ('Num Companies Worked', 'NumCompaniesWorked'),
        ('Over Time', 'OverTime'),
        ('Percent Salary Hike', 'PercentSalaryHike'),
        ('Performance Rating', 'PerformanceRating'),
        ('Relationship Satisfaction', 'RelationshipSatisfaction'),
        ('Stock Option Level', 'StockOptionLevel'),
        ('Total Working Years', 'TotalWorkingYears'),
        ('Training Times Last Year', 'TrainingTimesLastYear'),
        ('Work Life Balance', 'WorkLifeBalance'),
        ('Years At Company', 'YearsAtCompany'),
        ('Years In Current Role', 'YearsInCurrentRole'),
        ('Years Since Last Promotion', 'YearsSinceLastPromotion'),
        ('Years With Curr Manager', 'YearsWithCurrManager')
        ]
    
    input_key = {}
    
    for label,key in slider_labels:
        if label in ['Age of Employee','Daily Rate','Distance from Home','Hourly Rate','Monthly Income','Monthly Rate','Num Companies Worked','Percent Salary Hike','Total Working Years','Training Times Last Year','Years At Company','Years In Current Role','Years Since Last Promotion','Years With Curr Manager']:
            input_key[key] = st.sidebar.slider(label, 0, 100, 50)
        elif label in ['Business Travel Frequently','Department Sales','Over Time']:
            input_key[key] = st.sidebar.selectbox(label, ['Yes','No'])
        elif label in ['Environment Satisfaction','Job Involvement','Stock Option Level','Work Life Balance']:
            input_key[key] = st.sidebar.selectbox(label, [1,2,3,4,5])

    return input_key

def main():
    st.set_page_config(page_title="Churn Prediction", page_icon="🧊", layout="wide",initial_sidebar_state='expanded')
    with st.container():
        st.title("Welcome to Churn Prediction App")
        st.subheader("This app predicts the probability of churn for a telecom company")
        pass

    inputs = add_sidebar()

    st.write(inputs)

    col1 , col2 = st.columns([4,1])
    with col1:
        st.write("This is column 1")
        pass
    with col2:
        st.write("This is column 2")
        pass


if __name__ == "__main__":
    main()
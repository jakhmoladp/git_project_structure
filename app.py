import streamlit as st
import yaml
import joblib
import numpy as np

def read_config():
    """_summary_
        Read the configuration file.
    Returns:
        configuration yaml data
    """
    with open("config.yaml", 'r+') as f:
        config = yaml.safe_load(f)
    return config


def main():
    st.header("Marks Predictor for Students")
    st.write("Demo application created in Streamlit to predict marks of the students based using LinearRegression model.")
    # Read the number of subjects and average study hours per day.
    number_of_subjects = st.text_input("Number of subjects", 0)
    avg_study_hours_per_day = st.text_input("Average study hours per day", 0)

    validation_error = False
    number_of_subjects = int(number_of_subjects)
    avg_study_hours_per_day = float(avg_study_hours_per_day)

    if st.button("predict"):
        validation_error = False
        if number_of_subjects <=0:
            st.error("You need to provide realistic number of subjects to study.")
            validation_error = True
        elif number_of_subjects > 10:
            st.error("You must be superman but I can't predict for more than 10 subjects")
            validation_error = True

        if avg_study_hours_per_day <0 or avg_study_hours_per_day > 24:
            st.error("Homo sapien can enter between 0 and 24!")
            validation_error = True
                
        if validation_error == False:
            config = read_config()
            loaded_model = joblib.load(config['training']['model']['file_name'])
            predicted_marks = loaded_model.predict([[number_of_subjects, avg_study_hours_per_day]])[0]
            predicted_marks = np.round(predicted_marks, 2)        
            st.markdown("---")
            st.write("Predicted Marks:")
            st.subheader(predicted_marks)
            st.markdown(f"""
            If you study **{avg_study_hours_per_day}** hours on average per day and you have opted for **{number_of_subjects}** subject(s), then I think you will get around **{predicted_marks} marks**.
            """)


if __name__ == '__main__':
    main()
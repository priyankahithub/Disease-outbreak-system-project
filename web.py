import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")
diabetes_model=pickle.load(open(r"C:\Users\ComProWorld\Desktop\Example.txt\disease outbreaks\Training_model\diabetes_model.sav",'rb'))
heart__disease_model=pickle.load(open(r"C:\Users\ComProWorld\Desktop\Example.txt\disease outbreaks\Training_model\heart_model.sav",'rb'))
parkinsons_model=pickle.load(open(r"C:\Users\ComProWorld\Desktop\Example.txt\disease outbreaks\Training_model\parkinsons_model.sav",'rb'))
with st.sidebar:
    selected=option_menu('Prediction of Disease Outbreak System',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Disease Prediction'],
                                                                  menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        pregnancies=st.text_input('number of pregnancies')
    with col2:
        Glucose=st.text_input('Glucose level')
    with col3:
        Bloodpressure=st.text_input('Blood pressure level')
    with col1:
        skinThickness=st.text_input('skin Thickness value')
    with col2:
        Insulin=st.time_input('Insulin level')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function level')
    with col2:
        Age=st.text_input('Age of the person')
    
    diab_diagnosis=''
    if st.button('Diabetes Test Result'):
        user_input=[pregnancies,Glucose,Bloodpressure,skinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        import datetime
        print("user INPUT",user_input)
        print("data Types",[type(X) for X in user_input])

        user_input=[X.hour + X.minute/60 + X.second/3600 if isinstance(X,datetime.time)else float(X) for X in user_input]
        print("processed user input:",user_input)

        diabetes_prediction=diabetes_model.predict([user_input])
        if diabetes_prediction==1:
            diab_diagnosis='The Person is Diabetic'
        else:
            diab_diagnosis='The Person is not a Diabetic'
    st.success(diab_diagnosis)

#heart disease
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        import datetime
        print("user INPUT",user_input)
        print("data Types",[type(X) for X in user_input])

        user_input=[X.hour + X.minute/60 + X.second/3600 if isinstance(X,datetime.time)else float(X) for X in user_input]
        print("processed user input:",user_input)

        heart_prediction = heart__disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart Disease'
        else:
            heart_diagnosis = 'The person does not have any heart Disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Disease Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        import datetime
        print("user INPUT",user_input)
        print("data Types",[type(X) for X in user_input])

        user_input=[X.hour + X.minute/60 + X.second/3600 if isinstance(X,datetime.time)else float(X) for X in user_input]
        print("processed user input:",user_input)

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's Disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's Disease"

    st.success(parkinsons_diagnosis)

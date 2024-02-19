import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import joblib
from PIL import Image
 
def About():
    st.write("# About Brain Stroke project")
    st.caption("This project is a multipage app that shows the EDA analysis in a dynamic dashboard ")
    st.caption("and prediction of the brain stroke occurrence")
    st.title("Stroke is the condition in which the blood supply to the brain is cut")
    st.write("due to blood clot (ischemic stroke) or bursting the blood vessels reaching the brain (hemorrhagic stroke)")
    st.caption("Transient ischaemic attack")
    st.write("it is a mini_stroke that can persist for 24 hours")
    st.write(" and it is a related condition that happens due to temporary interruption of blood supply to the brain")
    st.caption("Certain conditions increase the risk of having a stroke, including:")
    st.write("1-high blood pressure (hypertension)")         
    st.write("2-high cholesterol")        
    st.write("3-irregular heartbeats (atrial fibrillation)")
    st.write("4-diabetes")
    icon = Image.open('b.stroke.jpg')
    st.image(icon, use_column_width= True)


def Bain_stroke_EDA():
    col1, col2 = st.columns(2)
    brain= pd.read_csv("brain_stroke.csv")
    num_cat_vars=brain.groupby("stroke").mean()
#gender
    stroke_gender=brain.groupby("gender")["stroke"].mean()
    stroke_gender = pd.DataFrame({'gender':stroke_gender.index, 'stroke':stroke_gender.values})
    gender_glucose =brain.groupby("gender")["avg_glucose_level"].mean()
    gender_glucose = pd.DataFrame({'gender':gender_glucose.index, 'glucose_levels':gender_glucose.values})
    gender_bmi=brain.groupby("gender")["bmi"].mean()
    gender_bmi = pd.DataFrame({'gender':gender_bmi.index, 'bmi':gender_bmi.values})
#gender uni
    gender_count = brain["gender"].value_counts()
    gender_count = pd.DataFrame({'gender':gender_count.index, 'number':gender_count.values})
    
    
#work type_num
#work_type_stroke
    stroke_vars=brain.groupby("work_type")["stroke"].mean()
    work_type_stroke = pd.DataFrame({'stroke_vars':stroke_vars.index, 'number':stroke_vars.values})
    work_glucose_level=brain.groupby("work_type")["avg_glucose_level"].mean()
    work_glucose_level = pd.DataFrame({'work_type':work_glucose_level.index, 'glucose_level':work_glucose_level.values})
    work_bmi=brain.groupby("work_type")["bmi"].mean()
    work_bmi = pd.DataFrame({'work_type':work_bmi.index, 'bmi':work_bmi.values})
#work type uni
    work_type_count = brain["work_type"].value_counts()
    work_type_count = pd.DataFrame({'work_type':work_type_count.index, 'number':work_type_count.values})
# heart dis_num
    stroke_heart_disease=brain.groupby("heart_disease")["stroke"].mean()
    stroke_heart_disease = pd.DataFrame({'heart_disease':stroke_heart_disease.index, 'stroke':stroke_heart_disease.values})
    heart_disease_glucose =brain.groupby("heart_disease")["avg_glucose_level"].mean()
    heart_disease_glucose = pd.DataFrame({'heart_disease':heart_disease_glucose.index, 'glucose_levels':heart_disease_glucose.values})
    heart_disease_bmi=brain.groupby("heart_disease")["bmi"].mean()
    heart_disease_bmi = pd.DataFrame({'heart_disease':heart_disease_bmi.index, 'bmi':heart_disease_bmi.values})
#heart dis uni
    heart_disease_count=brain["heart_disease"].value_counts()
    heart_disease_count = pd.DataFrame({'heart disease':heart_disease_count.index, 'number':heart_disease_count.values})
#ever_married_count
    ever_married_count=brain["ever_married"].value_counts()
    ever_married_count=pd.DataFrame({'ever_married':ever_married_count.index, 'number':ever_married_count.values})
    stroke_ever_married=brain.groupby("ever_married")["stroke"].mean()
    stroke_ever_married = pd.DataFrame({'ever_married':stroke_ever_married.index, 'stroke':stroke_ever_married.values})
    ever_married_glucose =brain.groupby("ever_married")["avg_glucose_level"].mean()
    ever_married_glucose = pd.DataFrame({'ever_married':ever_married_glucose.index, 'glucose_level':ever_married_glucose.values})
    ever_married_bmi=brain.groupby("ever_married")["bmi"].mean()
    ever_married_bmi = pd.DataFrame({'ever_married':ever_married_bmi.index, 'bmi':ever_married_bmi.values})
#smoking_status_count
    smoking_status_count=brain["smoking_status"].value_counts()
    smoking_status_count=pd.DataFrame({'smoking_status':smoking_status_count.index, 'number':smoking_status_count.values})
#
    stroke_smoking_status=brain.groupby("smoking_status")["stroke"].mean()
    stroke_smoking_status = pd.DataFrame({'smoking_status':stroke_smoking_status.index, 'stroke':stroke_smoking_status.values})
    smoking_status_glucose =brain.groupby("smoking_status")["avg_glucose_level"].mean()
    smoking_status_glucose = pd.DataFrame({'smoking_status':smoking_status_glucose.index, 'glucose_level':smoking_status_glucose.values})
    smoking_status_bmi=brain.groupby("smoking_status")["bmi"].mean()
    smoking_status_bmi = pd.DataFrame({'smoking_status':smoking_status_bmi.index, 'bmi':smoking_status_bmi.values})
#hypertension

    hypertension_count=brain["hypertension"].value_counts()
    hypertension_count=pd.DataFrame({'hypertension':hypertension_count.index, 'number':hypertension_count.values})
    stroke_hypertension=brain.groupby("hypertension")["stroke"].mean()
    stroke_hypertension= pd.DataFrame({'hypertension':stroke_hypertension.index, 'stroke':stroke_hypertension.values})
    hypertension_glucose =brain.groupby("hypertension")["avg_glucose_level"].mean()
    hypertension_glucose = pd.DataFrame({'hypertension':hypertension_glucose.index, 'glucose_level':hypertension_glucose.values})
    hypertension_bmi=brain.groupby("hypertension")["bmi"].mean()
    hypertension_bmi = pd.DataFrame({'hypertension':hypertension_bmi.index, 'bmi':hypertension_bmi.values})
    
    Residence_type_count=brain["Residence_type"].value_counts()
    Residence_type_count=pd.DataFrame({'Residence_type':Residence_type_count.index, 'number':Residence_type_count.values})
    stroke_Residence_type=brain.groupby("Residence_type")["stroke"].mean()
    stroke_Residence_type = pd.DataFrame({'Residence_type':stroke_Residence_type.index, 'stroke':stroke_Residence_type.values})
    Residence_type_glucose =brain.groupby("Residence_type")["avg_glucose_level"].mean()
    Residence_type_glucose = pd.DataFrame({'Residence_type':Residence_type_glucose.index, 'glucose_level':Residence_type_glucose.values})
    Residence_type_bmi=brain.groupby("Residence_type")["bmi"].mean()
    Residence_type_bmi = pd.DataFrame({'Residence_type':Residence_type_bmi.index, 'bmi':Residence_type_bmi.values})

    stroke_prob= brain["stroke"].mean()
 
    with st.sidebar:
        
        st.sidebar.title("Select Visual Charts")
        st.sidebar.markdown("Select the Charts/Plots accordingly:") 
        categorial_vars_option= st.selectbox('Choose categorical variable:',("gender","work_type",'hypertension', 'heart_disease', 'ever_married','smoking_status',
       'Residence_type'))
        numerical_vars= st.selectbox('Choose numerical variable:',("avg_glucose_level", 'bmi','stroke'))
        select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'scatter'], key='1')   
    
    
    with col1:
        st.title("Dynamic Dashboard of brain Stroke EDA ") 
        st.markdown("The dashboard will help the user to get more insights about the given datasets") 
        num_cat_vars
   
        if select=='Bar plot':
            if categorial_vars_option=="work_type":
                fig=px.bar(work_type_count,x="work_type", y = "number")
                st.plotly_chart(fig)        
        if select=='Bar plot':
            if categorial_vars_option=="work_type":
                if numerical_vars=="stroke":
                    fig=px.bar(work_type_stroke,x="stroke_vars", y = "number")
                    st.plotly_chart(fig) 
                            
     
        if select=='Bar plot':
            if categorial_vars_option=="work_type":
                if numerical_vars=="avg_glucose_level":
                    fig=px.bar(work_glucose_level,x="work_type", y = "glucose_level")
                    st.plotly_chart(fig)
        if select=='Bar plot':
            if categorial_vars_option=="work_type":
                if numerical_vars=="bmi":
                    fig=px.bar(work_bmi,x="work_type", y = "bmi")
                    st.plotly_chart(fig) 
 #gender
        if select=='Bar plot':
            if categorial_vars_option=="gender":
                fig=px.bar(gender_count, x="gender", y = "number")
                st.plotly_chart(fig)        
        if select=='Bar plot':
            if categorial_vars_option=="gender":
                if numerical_vars=="stroke":
                    fig=px.bar(stroke_gender,x="gender", y = "stroke")
                    st.plotly_chart(fig) 
                            
     
        if select=='Bar plot':
            if categorial_vars_option=="gender":
                if numerical_vars=="avg_glucose_level":
                    fig=px.bar(gender_glucose ,x="gender", y = "glucose_levels")
                    st.plotly_chart(fig)
        if select=='Bar plot':
            if categorial_vars_option=="gender":
                if numerical_vars=="bmi":
                    fig=px.bar(gender_bmi,x="gender", y = "bmi")
                    st.plotly_chart(fig) 
 #heart_disease input
          
        if select=='Bar plot':
            if categorial_vars_option=="heart_disease":
                fig=px.bar(heart_disease_count,x="heart_disease", y = "number")
                st.plotly_chart(fig)        
        if select=='Bar plot':
            if categorial_vars_option=="heart_disease":
                if numerical_vars=="stroke":
                    fig=px.bar(stroke_heart_disease,x="heart_disease", y = "stroke")
                    st.plotly_chart(fig)        
     
        if select=='Bar plot':
            if categorial_vars_option=="heart_disease":
                if numerical_vars=="avg_glucose_level":
                    fig=px.bar(heart_disease_glucose,x="heart_disease", y = "glucose_levels")
                    st.plotly_chart(fig)
        if select=='Bar plot':
            if categorial_vars_option=="heart_disease":
                if numerical_vars=="bmi":
                    fig=px.bar(heart_disease_bmi, x="heart_disease", y = "bmi")
                    st.plotly_chart(fig)     
                     
#ever married
        if select=='Bar plot':
           if categorial_vars_option=="ever_married":
                fig=px.bar(ever_married_count,x="ever_married", y = "number")
                st.plotly_chart(fig)        
        if select=='Bar plot':
            if categorial_vars_option=="ever_married":
                if numerical_vars=="stroke":
                    fig=px.bar(stroke_ever_married,x="ever_married", y = "stroke")
                    st.plotly_chart(fig)        
     
        if select=='Bar plot':
            if categorial_vars_option=="ever_married":
                if numerical_vars=="avg_glucose_level":
                    fig=px.bar(ever_married_glucose,x="ever_married", y = "glucose_level")
                    st.plotly_chart(fig)
        if select=='Bar plot':
            if categorial_vars_option=="ever_married":
                if numerical_vars=="bmi":
                    fig=px.bar(ever_married_bmi,x="ever_married", y = "bmi")
                    st.plotly_chart(fig)   
                
#smoking
        if select=='Bar plot':
           if categorial_vars_option=="smoking_status":
                fig=px.bar(smoking_status_count,x="smoking_status", y = "number")
                st.plotly_chart(fig)        
        if select=='Bar plot':
            if categorial_vars_option=="smoking_status":
                if numerical_vars=="stroke":
                    fig=px.bar(stroke_smoking_status,x="smoking_status", y = "stroke")
                    st.plotly_chart(fig)        
     
        if select=='Bar plot':
            if categorial_vars_option=="smoking_status":
                if numerical_vars=="avg_glucose_level":
                    fig=px.bar(smoking_status_glucose,x="smoking_status", y = "glucose_level")
                    st.plotly_chart(fig)
        if select=='Bar plot':
            if categorial_vars_option=="smoking_status":
                if numerical_vars=="bmi":
                    fig=px.bar(smoking_status_bmi,x="smoking_status", y = "bmi")
                    st.plotly_chart(fig)
                
#hypertension
        if select=='Bar plot':
            if categorial_vars_option=="hypertension":
                fig=px.bar(hypertension_count,x="hypertension", y = "number")
                st.plotly_chart(fig)        
        if select=='Bar plot':
            if categorial_vars_option=="hypertension":
                if numerical_vars=="stroke":
                    fig=px.bar(stroke_hypertension,x="hypertension", y = "stroke")
                    st.plotly_chart(fig)        
     
        if select=='Bar plot':
            if categorial_vars_option=="hypertension":
                if numerical_vars=="avg_glucose_level":
                    fig=px.bar(hypertension_glucose,x="hypertension", y = "glucose_level")
                    st.plotly_chart(fig)
        if select=='Bar plot':
            if categorial_vars_option=="hypertension":
                if numerical_vars=="bmi":
                    fig=px.bar(hypertension_bmi,x="hypertension", y = "bmi")
                    st.plotly_chart(fig)
#residual_type
        if select=='Bar plot':
            if categorial_vars_option=="Residence_type":
                fig=px.bar(Residence_type_count,x="Residence_type", y = "number")
                st.plotly_chart(fig)        
        if select=='Bar plot':
            if categorial_vars_option=="Residence_type":
                if numerical_vars=="stroke":
                    fig=px.bar(stroke_Residence_type,x="Residence_type", y = "stroke")
                    st.plotly_chart(fig)        
     
        if select=='Bar plot':
            if categorial_vars_option=="Residence_type":
                if numerical_vars=="avg_glucose_level":
                    fig=px.bar(Residence_type_glucose,x="Residence_type", y = "glucose_level")
                    st.plotly_chart(fig)
        if select=='Bar plot':
            if categorial_vars_option=="Residence_type":
                if numerical_vars=="bmi":
                    fig=px.bar(Residence_type_bmi,x="Residence_type", y = "bmi")
                    st.plotly_chart(fig)
def stroke_prediction():
    st.markdown("#stroke_prediction📈")
    st.sidebar.markdown("#stroke_prediction📈")
    clf1 = joblib.load('clf1')
    processor=joblib.load("processor")
    brain= pd.read_csv("D:/brain_stroke.csv")
    st.title("Prediction of brain occurrance")
    st.caption("About the app")
    st.write("""Simple approach of prediction of brain stroke based on some life style features""")

    age= st.slider("age",brain["age"].min(), brain["age"].max())
    bmi= st.slider("bmi",brain["bmi"].min(), brain["bmi"].max())
    avg_glucose_level=st.slider("avg_glucose_level",brain["avg_glucose_level"].min(), brain["avg_glucose_level"].max())
    gender=st.sidebar.selectbox('gender',brain["gender"].unique())
    ever_married= st.sidebar.selectbox("ever_married",("Yes","No"))
    smoking_status= st.sidebar.selectbox("smoking_status",brain["smoking_status"].unique())
    heart_disease= st.sidebar.selectbox('heart_disease', ("Yes","No"))
    hypertension= st.sidebar.selectbox('hypertension', ("Yes","No"))
    work_type=st.sidebar.selectbox('work_type', brain["work_type"].unique())
    Residence_type=st.sidebar.selectbox("Residence_type",("Rural","Urban"))


    def convert_response(response):
        if response=="Yes":
            return  1
        else:
            return  0

#dict
    user_data={
    "gender":gender, 
    "age":age,
    "bmi": bmi,
    "avg_glucose_level": avg_glucose_level,
    "ever_married":ever_married,
    "heart_disease":convert_response(heart_disease),
    "hypertension": convert_response(hypertension),
    "smoking_status":smoking_status,
    "Residence_type": Residence_type,
    "work_type":work_type}
        
         
    brain_parm=pd.DataFrame(user_data, index=[0]) 
    brain_parm_ready=processor.transform(brain_parm)
    brain_pred= clf1.predict_proba(brain_parm_ready)[0][1]*100
 #display
    if st.button("probability"):
        st.markdown("""# {} %""".format(brain_pred))         

        
page_names_to_funcs = {"About": About,"Bain_stroke_EDA": Bain_stroke_EDA, "stroke_prediction": stroke_prediction}
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()               

import pickle
import streamlit as st 
credit_card_fraud=pickle.load(open('Credit Card Fraud Detection.ipynb','rb'))
st.title('Credit Card Fraud Detection Using ML')
col1,col2,col3 = st.columns(3)
with col1:
       Time=st.text_input('Time')
with col2:
        Amount=st.text_input('amount')
with col3:
        Class=st.text_input('class')
Credit_Card_Fraud_Detection=''
if st.button('Credit Card Fraud Detection'):
    if ('Classs==1'):
        Credit_Card_Fraud_Detection='Legit'
    else:
        Credit_Card_Fraud_Detection='Fraud'
st.success(Credit_Card_Fraud_Detection)

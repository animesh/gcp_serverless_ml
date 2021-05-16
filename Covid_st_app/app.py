import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('./covidpred_v1.pkl','rb'))

def main():

    st.title('*Life is Fuzzy, lets try to deFuzzyify, Bit by bIT*')

    st.subheader('Trying to develop an Artificial Intelligence powered system to augment doctors in interpreting symptoms w.r.t. demography backed by data, probabilistic diagnosis, specifically, interpret lab tests and imaging results coming from suspected infectious disease and risk assessment of other conditions e.g. cancer, able to integrate into available health infrastructure via API(s), locally sourced data, predicting an outbreak, aiding resource allocation, add Bhojpuri/Hindi to aid urban and rural health care providers respectively. If you would like to get involved, please contact [animesh@fuzzylife.org]')

    X_signght   = st.text_input('X sign', 0)
    X_symptom    = st.text_input('X symptom', 0)
    Y_signgth   = st.text_input('Y sign', 0)
    Y_symptom    = st.text_input('Y symptom', 0)
    Z_symptom    = st.text_input('Z symptom', 0)


    if st.button('Get Prediction'):

        pred = model.predict(np.array([[float(X_signght),float(X_symptom),float(Y_signgth),float(Y_symptom)]],float(Z_symptom)]]))

        st.text('Predicted Z:' + pred[0])


if __name__ == "__main__":
    main()

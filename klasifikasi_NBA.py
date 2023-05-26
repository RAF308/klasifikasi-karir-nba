import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('nba.sav', 'rb'))

st.markdown("<h2 style='text-align: center; color: white;'>Prediksi Lama Karir Pemain NBA </h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    GP = st.number_input('Game Played')
    MIN = st.number_input('Minutes Played')
    PTS = st.number_input('PointsPerGame')
    FGM = st.number_input('Field Goals Made')
    FGA = st.number_input('Field Goals Attempts')
    FGP = st.number_input('Field Goal Percent')
    TPM = st.number_input('3 Point Made')
    TPA = st.number_input('3 Point Attempts')
    FTM = st.number_input('Free Throw Made')

with col2:
    FTA = st.number_input('Free Throw Attempts')
    FTP = st.number_input('Free Throw Percent')
    OREB = st.number_input('Offensive Rebound')
    DREB = st.number_input('Defensive Rebound')
    REB = st.number_input('Rebounds')
    AST = st.number_input('Assists')
    STL = st.number_input('Steals')
    BLK = st.number_input('Blocks')
    TOV = st.number_input('Turnovers')


prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[GP, MIN, PTS, FGM, FGA, FGP, TPM, TPA, FTM, FTA, FTP, OREB, DREB, REB, AST, STL, BLK, TOV]])

    if(prediksi[0] == 1):
        prediksi = 'Prediksi Karir >=5 Tahun di NBA'
    else:
        prediksi = 'Prediksi Karir <5 Tahun di NBA'
st.success(prediksi)
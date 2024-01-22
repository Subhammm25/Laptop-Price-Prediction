import streamlit as st
import pickle
import sklearn

# importing the model

pipe = pickle.load(open('pipe.pkl', "rb"))
df = pickle.load(open('df.pkl', 'rb'))
st.title("Laptop Price Prediction")

# brand
company = st.selectbox('Brand', df['Company'].unique())

# type of laptop

type = st.selectbox('Type', df['TypeName'].unique())

# ram
ram = st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# weight

weight = st.number_input()

# Touchscreen

Touchscreen = st.selectbox('Touchscreen', ['NO', 'YES'])

#ips

ips = st.selectbox('IPS', ['NO', 'YES'])

# screen size

screen_size = st.number_input('Screen Size')

#resolution

resolution = st.selectbox('screen Resolution', ['1928x1080', '1920x1080', '1366x768', '1600x900',
                                               '1080x1080', '3840x1800', '3200x1800', '2880x1600',
                                               '2560x1440', '2304x1440'])

#cpu

cpu = st.selectbox('Brand',df['Cpu Brand'].unique())

hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])

ssd = st.selectbox('SSD(in GB)', [0, 128, 256, 512, 1024])

gpu = st.selectbox('Brand', df['Gpu Brand'].unique())

os = st.selectbox('OS', df['OS'].unique())

if st.button('Predict Price'):
    pass

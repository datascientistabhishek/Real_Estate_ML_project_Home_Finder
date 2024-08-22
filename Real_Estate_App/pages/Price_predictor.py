import streamlit as st
import pickle
import pandas as pd 
import numpy as np

st.set_page_config(page_title = "Viz Demo")
# st.title('Page 1')

with open('D:\Gurgaon_real_estate_project\Real_Estate_App\df.pkl','rb') as file:
    df = pickle.load(file)

with open('D:\Gurgaon_real_estate_project\Real_Estate_App\pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)
#st.dataframe(df)  

st.header('Enter Input Feature Value:')

#property type
property_type = st.selectbox('property Type' , ['flat','house'])

#sector
sector = st.selectbox('sector',sorted(df['sector'].unique().tolist()))

# BedRoom
BedRoom = float(st.selectbox('No. of BedRoom',sorted(df['bedRoom'].unique().tolist())))

#BathRoom
BathRoom = float(st.selectbox('No. of BathRoom',sorted(df['bathroom'].unique().tolist())))

#Balcony
Balcony = st.selectbox('Total Balcony',sorted(df['balcony'].unique().tolist()))

#Property age
PropertyAge = st.selectbox('property age',sorted(df['agePossession'].unique().tolist()))

#Built up area
Built_Up_Area = float(st.number_input('Built Up Area'))

#servent room
servnt_room = float(st.selectbox('Servant room' , [0.0 , 1.0]))

#store room
store_room = float(st.selectbox('Store Room' , [0.0 , 1.0]))

#furnishing type 
furnishing_type  = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))

#luxury category
Luxury_category = st.selectbox('Luxury_Category',sorted(df['luxury_category'].unique().tolist()))

#floor_category
floor_category = st.selectbox('Floor_Category',sorted(df['floor_category'].unique().tolist()))


if st.button('Predict'):

# forming a dataframe
    data = [ [ property_type , sector , BedRoom , BathRoom , Balcony , PropertyAge , Built_Up_Area , servnt_room , store_room , furnishing_type , Luxury_category , floor_category ]]

    columns = ['property_type', 'sector', 'bedRoom' , 'bathroom' , 'balcony', 'agePossession', 'built_up_area', 'servant room', 'store room', 'furnishing_type', 'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data,columns=columns)
    #st.dataframe(one_df)

# predict 
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    #display
    #st.text("The price of the flat is between {} and {}".format(low,high))
    st.text(f"The price of the property is between {np.round(low,2)} Cr and {np.round(high,2)} cr")
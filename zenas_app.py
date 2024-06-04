# Import python packages
import streamlit as st
import snowflake.connector as con
import pandas as pd


my_cnx = con.connect(**st.secrets["snowflake"]) 
my_cur = my_cnx.cursor() 
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()") 
my_data_row = my_cur.fetchone() 
st.text("Hello from Snowflake:") 
st.text(my_data_row)

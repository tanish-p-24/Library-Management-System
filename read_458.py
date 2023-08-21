import pandas as pd
import streamlit as st
import plotly.express as px
from database_458 import view_all_books,view_all_users,view_issue,view_request


def read():
    result1 = view_all_books()
    # st.write(result)
    df = pd.DataFrame(result1)
    with st.expander("View all Books"):
        st.dataframe(df)

    result2 = view_all_users()
    # st.write(result)
    df = pd.DataFrame(result2)
    with st.expander("View all Users"):
        st.dataframe(df)

    result3 = view_issue()
    # st.write(result)
    df = pd.DataFrame(result3)
    with st.expander("View issued books"):
        st.dataframe(df)
    
    result4 = view_request()
    # st.write(result)
    df = pd.DataFrame(result4)
    with st.expander("View requested books"):
        st.dataframe(df)

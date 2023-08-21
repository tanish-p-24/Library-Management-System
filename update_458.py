import datetime

import pandas as pd
import streamlit as st
from database_458 import view_all_books, get_book, edit_book_data,view_only_books


def update_book():
    result = view_all_books()
    # st.write(result)
    df = pd.DataFrame(result)
    with st.expander("Current Train"):
        st.dataframe(df)
    list_of_books = [i[0] for i in view_only_books()]
    selected_book = st.selectbox("Book to Edit", list_of_books)
    selected_result = get_book(selected_book)
    # st.write(selected_result)
    if selected_result:
        bookprice = selected_result[0][6]
        bookquantity = selected_result[0][7]
       

        # Layout of Create
        price = st.text_input("New price : ")
        quan = st.text_input("New quantity : ")
        
        if st.button("Update Book"):
            edit_book_data(selected_book,price,quan) 
            st.success("Successfully updated book {} from price {} and quantity {} to price {} and quantity {} ".format(selected_book,bookprice,bookquantity,price,quan))

    result2 = view_all_books()
    df2 = pd.DataFrame(result2)
    with st.expander("Updated data"):
        st.dataframe(df2)

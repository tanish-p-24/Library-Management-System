# Importing pakages
import streamlit as st
import mysql.connector

from create_458 import create_book,create_user,issue_book,request_book
from database_458 import create_table
# from delete_458 import delete
from read_458 import read
from update_458 import update_book




def main():
    st.title("Library Management System")
    menu = ["Add book", "Add user","issue book","request book" ,"view", "update", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Add book":
        st.subheader("Add the book:")
        create_book()

    elif choice == "Add user":
        st.subheader("Add a user")
        create_user()
    
    elif choice == "issue book":
        st.subheader("Issue a book")
        issue_book()
    
    elif choice == "request book":
        st.subheader("Requesting for a book")
        request_book()

    elif choice == "view":
        st.subheader("View")
        read()
    
    # elif choice == "request book":
    #     st.subheader("Update created tasks")
    #     update()
    
    # elif choice == "view issued books":
    #     st.subheader("Update created tasks")
    #     update()
    
    elif choice == "update":
        st.subheader("Update Book")
        update_book()

    # elif choice == "Remove":
    #     st.subheader("Delete created tasks")
    #     delete()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()

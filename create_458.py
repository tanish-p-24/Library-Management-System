import streamlit as st
from database_458 import add_data_book,view_only_books,view_only_users,add_data_user,get_user,get_book,add_data_issuebook,add_data_requestbook


def create_book():
    col1, col2,col3,col4= st.columns(4)
    with col1:
        id = st.text_input("id:")
        name = st.text_input("Book Name:")
        det = st.text_input("Book details :")
    with col2:
        auth = st.text_input("Author :")
        pub = st.text_input("Publisher :")
        branch = st.text_input("Branch :")
    with col3:
        price = st.text_input("Price :")
        quan = st.text_input("Quantity : ")
    with col4:
        avail = st.text_input("Enter Availabilty")
        rent = st.text_input("rent :")
    if st.button("Add Book"):
        add_data_book(id,name,det,auth,pub,branch,price,quan,avail,rent)
        st.success("Successfully added Book: {}".format(name))


def create_user():
    col1, col2,col3= st.columns(3)
    with col1:
        id = st.text_input("id:")
        name = st.text_input("Name:")
    with col2:
        email = st.text_input("email :")
        password = st.text_input("Password :")
    with col3:
        type = st.text_input("Type :")
    if st.button("Add user"):
        add_data_user(id,name,email,password,type)
        st.success("Successfully added user: {}".format(name))


def issue_book():
    id = st.text_input("id:")
    days = st.text_input("Number of days:")
    # name = st.selectbox("Name", ["Express", "Mail", "Passenger"])
    list_of_users = [i[0] for i in view_only_users()]
    name = st.selectbox("Name", list_of_users)
    selected_user = get_user(name)
    print(selected_user)
    list_of_books = [i[0] for i in view_only_books()]
    book = st.selectbox("Book", list_of_books)
    selected_book = get_book(book)

    fine = st.text_input("Fine : ")
    st.write(selected_user)
    st.write(selected_book)
    if selected_user:
        userid = selected_user[0][0]
        issuename = selected_user[0][1]
        issuetype = selected_user[0][4]
        issuedate = '19/11/2022'
        issuereturn = '24/11/2022'
    if selected_book:
        issue_book = selected_book[0][1]

    if st.button("Add Book"):
        add_data_issuebook(id,userid,issuename,issue_book,issuetype,days,issuedate,issuereturn,fine)
        st.success("Successfully added issuename: {}".format(name))


def request_book():
    id = st.text_input("id:")
    days = st.text_input("Number of days:")
    # name = st.selectbox("Name", ["Express", "Mail", "Passenger"])
    list_of_users = [i[0] for i in view_only_users()]
    name = st.selectbox("Name", list_of_users)
    selected_user = get_user(name)
    print(selected_user)
    list_of_books = [i[0] for i in view_only_books()]
    book = st.selectbox("Book", list_of_books)
    selected_book = get_book(book)

    st.write(selected_user)
    st.write(selected_book)
    if selected_user:
        userid = selected_user[0][0]
        username = selected_user[0][1]
        usertype = selected_user[0][4]
    if selected_book:
        bookid = selected_book[0][0]
        bookname = selected_book[0][1]

    if st.button("Add user to request book"):
        add_data_requestbook(id,userid,bookid,username,usertype,bookname,days)
        st.success("Successfully added request book: {}".format(name))


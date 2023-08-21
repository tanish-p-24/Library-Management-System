import pandas as pd
import streamlit as st
from database_458 import view_all_books, view_all_users, delete_data,view_only_users


def delete():
    result = view_all_users()
    df = pd.DataFrame(result)
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_users = [i[0] for i in view_only_users()]
    selected_user = st.selectbox("Task to Delete", list_of_users)
    st.warning("Do you want to delete :{}".format(selected_user))
    if st.button("Delete User"):
        delete_data(selected_user)
        st.success("User has been deleted successfully")
    new_result = view_all_users()
    df2 = pd.DataFrame(new_result)
    with st.expander("Updated data"):
        st.dataframe(df2)
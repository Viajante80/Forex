import streamlit as st

ma_cross_pairs = st.Page("MA_Cross_Pairs.py", title="Pairs - MA Cross", icon=":material/analytics:")
create_page = st.Page("MA_Cross.py", title="MA Cross", icon=":material/analytics:")
delete_page = st.Page("page_3.py", title="Delete entry", icon=":material/delete:")

pg = st.navigation([ma_cross_pairs, create_page, delete_page])
st.set_page_config(page_title="Forex", page_icon=":material/show_chart:")
pg.run()

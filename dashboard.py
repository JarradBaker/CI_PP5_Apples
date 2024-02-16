import streamlit as st
from app_dashboard.multi_page import Dashboard

from app_dashboard.page1 import page1_body
from app_dashboard.page2 import page2_body
from app_dashboard.page3 import page3_body
from app_dashboard.page4 import page4_body
from app_dashboard.page5 import page5_body


app = Dashboard(page_name="Predictive Analytics Dashboard")

app.app_page("Page 1", page1_body)
app.app_page("Page 2", page2_body)
app.app_page("Page 3", page3_body)
app.app_page("Page 4", page4_body)
app.app_page("Page 5", page5_body)

app.run()
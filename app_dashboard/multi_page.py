import streamlit as st

class Dashboard:

    def __init__(self, page_name) -> None:
        self.pages = []
        self.page_name = page_name

        st.set_page_config(
            page_title=self.page_name,
            page_icon=""
        )

    
    def app_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    
    def run(self):
        st.title(self.page_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()
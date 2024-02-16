import streamlit as st
import matplotlib.pyplot as plt


def page1_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Apples and Oranges get mixed up when the company is trying to separate them "
        f"ready for juicing and selling.\n"
        f"* The apples and oranges are harvested from the same orchard and "
        f"are often mixed together.\n"
        f"* The data set is made up of many images of apples and oranges for comparing "
        f"and classifying, ready for separation and production.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/JarradBaker/CI_PP5_Apples/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"between apples and oranges.\n"
        f"* 2 - The client is interested to tell whether a given fruit is an apple or an orange. "
        )
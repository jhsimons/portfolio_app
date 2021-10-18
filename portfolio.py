# Assignment 3: My Portfolio
# Janine Simons
# October 16 2021

import streamlit as st
import base64
main_bg = "images/background.png"
main_bg_ext = "png"
side_bg = "images/bg-sidebar.jpeg"
side_bg_ext = "jpeg"
st.title("Janine Simons")
st.header("Data Scientist")
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)
dropdown = st.sidebar.selectbox(" ",["About me","Services", "Blog", "Contact"])
if dropdown == "About me":
    st.subheader("About me")
    st.markdown("Hi, my name is Janine Simons and I am studying to become a Data Scientist. "
                "I have a Master's Degree in Computer Science (Utrecht University). "
                "I have 12 years experience in software testing and test management and now I am making a change in my career to Data Scientist. "
                "I am analytical, accurate and very eager to learn.")

if dropdown == "Services":
    st.subheader("Services")
    st.markdown("As a data scientist, I translate data into valuable and comprehensible insights. "
             "My goal is to communicate clear results that support you understanding the data and making reliable decisions. "
             "I use advanced data visualization techniques to present results. I can help you with: "
             "Data analysis, Data visualization, Identifying opportunities, Organizing workshops decision driven business, and testing of ML algorithms.")
    st.text("Example of data visualization")
    st.image("images/img.png")
if dropdown == "Blog":
    st.subheader("Blog")
    st.info("This site is under construction")
if dropdown == "Contact":
    st.subheader("Contact")
    st.text("Please leave your name and email in the form below and I will get to you soon")
    with st.form(key='my_form'):
        text_input_name = st.text_input(label='Your Name')
        text_input_mail = st.text_input(label='Your E-mail')
        text_input_mess = st.text_area(label='Your Message')
        #submit_button = st.form_submit_button(label="Submit", on_click=True)
        if st.form_submit_button("Submit"):
            message = []
            message.append(text_input_name)
            message.append(text_input_mail)
            message.append(text_input_mess)
            #file_1 = open("C:/Users/simon/PycharmProjects/bootcamp/Assignment3/message","r+")
            #file_1.writelines(text_input_name)
            #file_1.writelines(text_input_mess)
            #file_1.writelines(text_input_mail)
            print(message)
            st.info("You message has been sent succesfully! I will contact you soon!")

st.sidebar.image("images/Mijn_foto.jpg", width = 200)
st.sidebar.title("Janine Simons")
st.sidebar.markdown( "As a data expert I know how to handle large volumes of data and catch critical information for your company. "
                     "I can help you to identify opportunities and identify solutions for your company. "
                     "If you want to work together with me, please contact me with the contact form. "
                     "Location: Utrecht region (the Netherlands) or remote work. ")




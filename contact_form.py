# import streamlit as st
# import streamlit.components.v1 as components
# from streamlit_lottie import st_lottie
# import json

# def contact():
#     col1, col2 = st.columns(2)

#     # col1.markdown("## Experience")
#     with col1:
#         st.markdown("""
#                     <style>
#                     .centered {
#                         display: flex;
#                         align-items: center;
#                         height: 100%;
#                         margin-top: 200px; /* Adjust this value as needed */
#                     }
#                     </style>
#                     <div class="centered">
#                         <h2>📨 Contact Form </h2>
#                     </div>
#                 """, unsafe_allow_html=True)
#     path = "Animation_contact.json"
#     with open(path, "r") as file:
#         url = json.load(file)
#     with col2:
#         st_lottie(url,
#                   reverse=True,
#                   height=400,
#                   width=400,
#                   speed=1,
#                   loop=True,
#                   quality='high',
#                   )

#     # components.html(
#     #     f"""
#     #      <iframe src="https://docs.google.com/forms/d/e/1FAIpQLScLaMWyScjbqoo6I5w5MtoQwfSU-Izghn1y_jsTP-yuf5zZOA/viewform?embedded=true" width="640" height="741" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
#     #     """,
#     #     height=1800,
#     # )
#     components.html(
#         f'<p><a href="mailto:natthaphop.phat@gmail.com">natthaphop.phat@gmail.com</a></p>'
#     )


import streamlit as st


def contact():
    # Set page configuration
    # st.set_page_config(page_title="Let's Talk - Contact Us", layout="centered")

    # Custom CSS to style the page
    st.markdown("""
        <style>
        /* Background and container styling */
        .main-container {
            background-color: #e6e6fa; /* Light purple background */
            border-radius: 20px;
            padding: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: 0 auto;
        }
        /* Heading styling */
        .heading {
            font-size: 48px;
            font-weight: bold;
            color: #4b0082; /* Dark purple */
            margin-bottom: 10px;
        }
        /* Description text */
        .description {
            font-size: 16px;
            color: #666;
            margin-bottom: 30px;
        }
        /* Input field styling */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            border-radius: 10px;
            border: 1px solid #d3d3d3;
            padding: 10px;
            font-size: 16px;
        }
        /* Button styling */
        .stButton > button {
            background-color: #6a5acd; /* Medium purple */
            color: white;
            border: none;
            border-radius: 20px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            width: 100%;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #483d8b; /* Darker purple on hover */
        }
        /* Contact info styling */
        .contact-info {
            margin-top: 30px;
            font-size: 14px;
            color: #666;
            line-height: 1.6;
        }
        /* Social media icons */
        .social-icons img {
            width: 30px;
            margin: 0 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Main container
    st.markdown("""<div class="main-container"> <div style="position: center;"> 
                        <span style="font-size: 60px;">📧💬✈️</span>
                    </div>"""
                , unsafe_allow_html=True)

    # Heading
    st.markdown('<div class="heading">Let’s talk</div>', unsafe_allow_html=True)

    # Description
    st.markdown("""
        <div class="description">
        To request a quote or want to meet up for coffee, contact us directly or fill out the form and we will get back to you promptly.
        </div>
    """, unsafe_allow_html=True)

    # Contact Form
    # with st.form(key="contact_form"):
    #     name = st.text_input("Your Name")
    #     email = st.text_input("Your Email")
    #     message = st.text_area("Your Message", placeholder="Type something if you want...")
    #     submit_button = st.form_submit_button("Send Message")

    #     # Handle form submission
    #     if submit_button:
    #         if name and email and message:
    #             st.success("Thank you for your message! We'll get back to you soon.")
    #         else:
    #             st.error("Please fill out all fields before submitting.")

    # Contact Information
    st.markdown("""
        <div class="contact-info">        
        📞 +66 (203) 302-9545<br>
        ✉️ natthahpop.phat@gmail.com
        </div>
    """, unsafe_allow_html=True)  ## 📍 151 New Park Ave, Hartford, CT 06106, United States<br>

    # Social Media Icons (using emoji placeholders since we can't directly use images in this setup)
    # st.markdown("""
    #     <div class="social-icons" style="margin-top: 20px; text-align: center;">
    #         <a href="https://facebook.com" target="_blank"><img src="https://img.icons8.com/color/48/000000/facebook-new.png"/></a>
    #         <a href="https://twitter.com" target="_blank"><img src="https://img.icons8.com/color/48/000000/twitter--v1.png"/></a>
    #         <a href="https://instagram.com" target="_blank"><img src="https://img.icons8.com/color/48/000000/instagram-new.png"/></a>
    #     </div>
    # """, unsafe_allow_html=True)

    # Close the main container
    st.markdown('</div>', unsafe_allow_html=True)

    # Optional: Add background illustration (simplified, since we can't directly replicate the exact design)
    st.markdown("""
        <div style="position: absolute; top: 50px; right: 50px;">
            <span style="font-size: 50px;">📧💬✈️</span>
        </div>
    """, unsafe_allow_html=True)
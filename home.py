import streamlit as st
from streamlit_option_menu import option_menu
import base64
from streamlit_lottie import st_lottie
import requests
import json
from reume_page import resume
from experience_page import experience
from upwork_page import feedbackRating
from project_page import projects
from contact_form import contact



 # Page setup
st.set_page_config(
    page_title="Natthaphop",
    page_icon="📋",
    layout="wide",
)

# Inject meta tags into the app
# <head>
meta_tags = """

    <title>Natthaphop Portfolio!</title>
    <meta name="title" content="Natthaphop Portfolio!" />
    <meta name="description" content="I'm an Application Engineer with expertise in 2D and 3D Vision System and software development" />

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://metatags.io/" />
    <meta property="og:title" content="Natthaphop Portfolio!" />
    <meta property="og:description" content="I'm an Application Engineer with expertise in 2D and 3D Vision System and software development" />
    <meta property="og:image" content="https://metatags.io/images/meta-tags.png" />

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="https://metatags.io/" />
    <meta property="twitter:title" content="Natthaphop Portfolio!" />
    <meta property="twitter:description" content="I'm an Application Engineer with expertise in 2D and 3D Vision System and software development" />
    <meta property="twitter:image" content="https://metatags.io/images/meta-tags.png" />

"""
# </head>

# Display the meta tags
st.markdown(meta_tags, unsafe_allow_html=True)


def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
                unsafe_allow_html=True)
def aboutMe():
    col1, col2 = st.columns(2)
    # full_name = "Archana"
    # info = {'Intro': "Data scientist"}

    with col1:
        st.markdown("<h2 style='text-align: center; '>Hello! I'm Natthaphop 👋</h2>", unsafe_allow_html=True)

        st.markdown("""
        <style>
        .center-text {
        text-align: justify;
        }
        </style>
        <div class="justify-text">
        I'm an Application Engineer with expertise in 2D vision camera systems, 3D camera,
        machine vision, and industrial automation. Strong background in image
        processing, computer vision, and deep learning with hands-on experience in
        integrating and troubleshooting vision systems in industrial environments.
        Passionate about optimizing automation processes and delivering highperformance solutions.
        </div>
        """, unsafe_allow_html=True)
        c1,c2, c3 =st.columns(3)
        c1.markdown("""**[GitHub](https://github.com/archanags001)**""")
        c2.markdown("""**[LinkedIn](https://www.linkedin.com/in/archanags001)** """)
        c3.markdown("""**[Upwork](https://www.upwork.com/freelancers/~010f3758a004ea64dd?viewMod%20e)**""")


    path = "Animation_blue_robo.json"
    with open(path, "r") as file:
        url = json.load(file)
    with col2:

        st_lottie(url,
                  reverse=True,
                  height=400,
                  width=400,
                  speed=1,
                  loop=True,
                  quality='high',
                  )
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Get the base64 string of the image
# image profile 
logo_base64 = get_base64_image("profile.png")

# Logo styling
logo_html = f"""
    <style>
    .logo-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }}
    .logo {{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
    }}
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
    </div>"""

# Display logo in the sidebar
st.sidebar.markdown(logo_html, unsafe_allow_html=True)
with st.sidebar:
    # Other sidebar elements
    # st.sidebar.image("logo_image.png", width=200, use_column_width=True)
    # Option menu in sidebar
    pages = ["About me", "Resume", "Experience",  "Projects", "Testimonials", "Contact"]
    nav_tab_op = option_menu(
        menu_title="Nathaphop",
        options=pages,
        icons=['person-fill', 'file-text', 'briefcase', 'folder', 'star', 'envelope'],
        menu_icon="cast",
        default_index=0,
    )
# Main content of the app
if nav_tab_op == "About me":
    aboutMe()

elif nav_tab_op == "Resume":
    resume()
elif nav_tab_op == "Experience":
    experience()
elif nav_tab_op == "Testimonials":
    feedbackRating()
elif nav_tab_op == "Projects":
    projects()
elif nav_tab_op == "Contact":
    contact()



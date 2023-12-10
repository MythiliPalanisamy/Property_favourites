import json
import requests
import streamlit as st
from streamlit_option_menu import option_menu
import asset as asset
import time

# Initialize session state variables
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'favorites' not in st.session_state:
    st.session_state.favorites = []
if 'url' not in st.session_state:
    st.session_state.url = ""
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'password' not in st.session_state:
    st.session_state.password = ""

# Function to get favorites using st.cache with a custom cache key
def get_favorites(url, username, password):
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        return response.json()
    else:
        st.header('No Service - Issue loading the page')
        return []

def one_element(favorites):
    for favorite in favorites:
        col1, col2 = st.columns(2)

        with col1:
            st.image(favorite["picture"], use_column_width=True)            

        with col2:        
            st.subheader(favorite['title'])
            st.markdown(f'##### € {favorite["price"]}')
            st.markdown(f'<div style="margin-left: 250px;">{favorite["date"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="line-height: 1.2;">{favorite["full_address"]}</div>', unsafe_allow_html=True)
            st.text(favorite['province'])
  
            st.text_area("Description", value=favorite["description"], height=200)
            
            st.link_button('🔗', favorite['url'])

st.set_page_config(
    page_title="Property Favorites",
    page_icon="🌐",)
st.title('Welcome')

with st.sidebar:        
    app = option_menu(
            menu_title='Favourite Properties',
            options=['Account','Home','Favourites', 'about'],)
    
if app == 'Account':
    with st.form(key='my_form'):
        st.session_state.url = st.text_input('Enter API URL:')
        st.session_state.username = st.text_input('Enter email:')
        st.session_state.password = st.text_input('Enter password:', type='password')
        st.session_state.submitted = st.form_submit_button()
        
elif app == 'Home':
    st.image('asset/pic.jpg')
    st.markdown(f'##### Discover more about the selected properties here!')

elif app == 'Favourites':
    if st.session_state.submitted:
        # Use st.session_state to access variables across reruns
        favorites = get_favorites(st.session_state.url, st.session_state.username, st.session_state.password)
        one_element(favorites)

elif app == 'about':
    st.image('asset/pic1.jpg')

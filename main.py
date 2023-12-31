import requests
import streamlit as st
from streamlit_option_menu import option_menu
import asset as asset

st.set_page_config(
    page_title="Property Favorites",
    page_icon="🌐",)

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

# querying data
def get_favorites(url, username, password):
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        return response.json()
    else:
        st.header('No Service - Issue loading the page')
        return []

# creating columns for visual 
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

# streamlit sidebar and its functions
def main_function():
    with st.sidebar:        
        app = option_menu(
            menu_title='Saved Properties',
                options=['Account','Home','Favourites', 'about'],)
        
    if app == 'Account':
        st.title('Welcome')
        st.text('Please enter the details')
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
        else:
            st.markdown('<div style="text-align: left; font-size: 20px;">Please enter the account details</div>', unsafe_allow_html=True)
            st.image('asset/error.jpg')

    elif app == 'about':
        st.image('asset/pic1.jpg')
        st.markdown('<div style="text-align: right; font-size: 20px;">Thank you for your time</div>', unsafe_allow_html=True)

main_function()


   

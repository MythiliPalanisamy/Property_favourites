import json
import requests
import file as file
import streamlit as st
import asset as asset

def response_check(response):
    if response.status_code == 200:
        favorites = response.json()
    else:
        st.header('No Service - Issue loading the page')
    return favorites

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
    page_icon="🌐",
    
)

with st.sidebar:
    about = st.button('About')
    fav = st.button('Favorites')
    st.image('asset/pic.jpg')

if about:
    st.image('asset/pic1.jpg')
    st.markdown(f'##### Discover more about the selected properties here!')

elif fav:
    url = file.query_api
    response = requests.get(url, auth=(file.username, file.password))

    favorites = response_check(response)
    one_element(favorites)





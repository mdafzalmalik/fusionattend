import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp{
                background: #5865f2 !important
            }
        </style>
                """,unsafe_allow_html=True)

    
def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp{
                background: #e0e3ff !important
            }
        </style>
                """,unsafe_allow_html=True)

    
def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Chewy&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
        
        
            /* Hide Toolbar */
            #MainMeny, footer, header {
                visibility: hidden
            }
            
            .block-container{
                padding-top: 1.5rem
            }
            
            h1 {
                font-family: "Chewy", system-ui;
                font-size: 3.5rem !important;
                line-height: 1.1rem !important;
                marging-bottome: 0rem !important;
            }
            
            h2 {
                font-family: "Chewy", system-ui;
                font-size: 3.5rem !important;
                line-height: 1.1rem !important;
                marging-bottome: 0rem !important;
            }
            
            h3, h4, p {
                font-family: "Outfit", sans-serif !important;
            }
            
            button {
                background: #5865f2;
                border-radius: 1.5rem !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important; 
            }
            
            button[kind="secondary"] {
                background: #eb459e;
                border-radius: 1.5rem !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important; 
            }
            
            button[kind="tertiary"] {
                background: black;
                border-radius: 1.5rem !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important; 
            }
            
            button:hover {
                transform: scale(1.05);
            }
            
        </style>
                """,unsafe_allow_html=True)
    

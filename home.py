import streamlit as st
import time
from gifRender import GifRender
from pageRender import PageRender

st.set_page_config(
	page_title="Welcome",
	initial_sidebar_state="collapsed",
	page_icon="🏠",
)

def center_title(title):
	"""Centers a title type text"""
	st.markdown(f"<h1 style='text-align: center; color: #00ff00; font-size: 38px;'>{title}</h1>", unsafe_allow_html=True)

def center_text(text):
	"""Centers generic text"""
	st.markdown(f"<p style='text-align: center; color: #ffffff; font-size: 15px;'>{text}</p>", unsafe_allow_html=True)	

PageRender.renderHidden()

# Ensures the splash screen is only shown one time
if 'gif_shown' not in st.session_state:
	st.session_state.gif_shown = True

# Boolean for using ai (or not)
if 'use_AI' not in st.session_state:
	st.session_state.use_AI = True


center_title("H U N T * T H E * W U M P U S")
time.sleep(1)
GifRender.create_space(1)
center_text("The hunt is about to begin.")
GifRender.create_space(2)
time.sleep(1)

if st.session_state.gif_shown:
	GifRender.display_gif("splash.gif")
    # Set a timer to hide the GIF after 0.5 seconds
	time.sleep(0.5)
	st.session_state.gif_shown = False
	st.rerun()  # Re-run the script to update the UI without the GIF

center_text("Enter your name:")
buff, col, buff2 = st.columns([1,3,1])
userName = col.text_input("username", label_visibility="collapsed", placeholder="GregoryYob73")

if userName != "":
	entered = True
	GifRender.create_space(2)
	center_text(f"Welcome, {userName}.")
	GifRender.create_space(2)

	st.session_state.userName = userName

	col1, col2, col3, col4 = st.columns([1, 1.3, 1.4, 1.4])
	with col1:
		if st.button("New Game", type = "primary"):
			st.switch_page("pages/help.py")
	with col2:
		if st.button("Player Stats", type = "primary"):
			st.switch_page("pages/stats.py")
	with col3:
		if st.button("Accessibility", help = "TTS/STT-Based Gameplay for Dyslexia and Visual Impairments"):
			st.switch_page("pages/speechGame.py")
	with col4:
		if st.button("Leaderboard", type = "primary"):
			st.switch_page("pages/leaderboard.py")

	GifRender.create_space(3)
	col5, col6 = st.columns([2, 1])

	st.session_state.use_AI = col6.checkbox("Use AI for Trivia", value=True, help="ChatGPT is used to generate Trivia Questions to make them more varied, challenging, and creative. If this is something you would not prefer, uncheck this.")

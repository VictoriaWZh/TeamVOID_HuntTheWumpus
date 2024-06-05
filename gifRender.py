import base64
import streamlit as st

class GifRender:
    @staticmethod
    def setup_gif(path):
        """Returns a data_url based on the contents of a gif."""
        # Reads the data per frame in gif
        with open(path, "rb") as file_:
            contents = file_.read()
        # Rewrites and decodes the data into a usable link
        data_url = base64.b64encode(contents).decode("utf-8")
        return data_url # Returns gif data
    
    @staticmethod
    # Makes space
    def create_space(n):
        """Adding additional blank lines."""
        for count in range(n):
            st.write("")
    
    @staticmethod
    def display_gif(path):
        """Renders a gif based on the data url."""
        # Shows the gif in streamlit using html
        data_url = GifRender.setup_gif(path)
        st.markdown(f'<img src="data:image/gif;base64,{data_url}">', unsafe_allow_html=True)
        GifRender.create_space(3)
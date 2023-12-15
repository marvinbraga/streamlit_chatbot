import base64
import os
from abc import ABCMeta, abstractmethod

import streamlit as st

from apps.settings import IMAGES_DIR, STATIC_DIR


class AbstractLoader(metaclass=ABCMeta):
    def __init__(self, filename: str):
        self._filename = filename

    @abstractmethod
    def load(self):
        pass


class ImageLoader(AbstractLoader):
    def load(self):
        with open(os.path.join(IMAGES_DIR, self._filename), "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')


class CssLoader:
    def __init__(self, filename: str = "styles.css"):
        self._filename = filename

    def load(self):
        with open(os.path.join(STATIC_DIR, self._filename), "r") as f:
            css = f"""
            <style>
            {f.read()}
            </style>
            """
            st.markdown(css, unsafe_allow_html=True)


class HtmlLoader(AbstractLoader):
    def load(self):
        with open(self._filename, "r") as file:
            html_content = file.read()
        return html_content

from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import math
import time
import re
import os
import joblib
import seaborn as sns
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  
from sklearn.metrics import pairwise_distances
from matplotlib import gridspec
from scipy.sparse import hstack
from scipy import sparse
import warnings
warnings.filterwarnings("ignore")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

@st.cache
def text_cleaning(total_text):
    if type(total_text) is not int:
        string = ""
        for words in total_text.split():
            # remove the special chars in review like '"#$@!%^&*()_+-~?>< etc.
            word = ("".join(e for e in words if e.isalnum()))
            word = word.lower()
            if not word in stop_words:
                string += word + " "
        return string

books = pd.read_pickle('books_final.pkl')

@st.cache
def make_prediction(titles):
    row_label = books.index[books['title'] == titles].tolist()
    w2v_title = pd.read_pickle('sent_vect.pkl')    
    pairwise_dist = pairwise_distances(w2v_title, w2v_title[row_label].reshape(1, -1))
    # np.argsort will return indices of 9 smallest distances
    indices = np.argsort(pairwise_dist.flatten())[0:6]
    # pdists will store the 9 smallest distances
    pdists = np.sort(pairwise_dist.flatten())[0:6]
    # data frame indices of the 9 smallest distace's
    df_indices = list(books.index[indices])
    t,photo = [],[]
    for i in range(0, len(indices)):
        t.append(books['title'].loc[df_indices[i]])
        photo.append(books['image_link'].loc[df_indices[i]])
    return t,photo

st.write('### **BOOK RECOMMENDATION SYSTEM BY LUKE CHUGH**')
st.write("##### **This WebApp recommends top 5 books based on your favourite book**")

book_list = books['title'].values
selected_book = st.selectbox("Select a book title from the list of 4000 books",book_list)
    
if st.button('Recommend'):
    ti, im = make_prediction(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(ti[1])
        response = requests.get(im[1])
        img = Image.open(BytesIO(response.content))
        image = np.array(img)
        st.image(image)
    with col2:
        st.text(ti[2])
        response = requests.get(im[2])
        img = Image.open(BytesIO(response.content))
        image = np.array(img)
        st.image(image)
    with col3:
        st.text(ti[3])
        response = requests.get(im[3])
        img = Image.open(BytesIO(response.content))
        image = np.array(img)
        st.image(image)
    with col4:
        st.text(ti[4])
        response = requests.get(im[4])
        img = Image.open(BytesIO(response.content))
        image = np.array(img)
        st.image(image)
    with col5:
        st.text(ti[5])
        response = requests.get(im[5])
        img = Image.open(BytesIO(response.content))
        image = np.array(img)
        st.image(image)















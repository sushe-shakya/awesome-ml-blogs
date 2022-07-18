# import streamlit as st
# st.write("Streamlit is awesome")

import pickle
import streamlit as st

with open("model.pickle",'rb') as fid:
	clf = pickle.load(fid) # load the classifier model
	cv = pickle.load(fid) # load the count vectorizer


user_input = st.text_input(label="Enter your text here")
input_mat = cv.fit_transform([user_input])
prediction = clf.predict(input_mat)

if prediction[0] == 0: 
	st.write("Your sentence is negative.")
else:
	st.write("Your sentence is positive.")
---
layout: posts
title: Explain your machine learning applications with awesome visuals
---

![stout0]({{site.url}}/assets/images/st-out0.png)

**Goal:** <br>
Impress your client / audience with awesome visualization for your machine learning applications

**Problem statement:** <br>
Machine learning engineers don't necessarily have enough frontend experience to build visually appealing websites to demo their machine learning model applications

**Solution:**

Yes, Jupyter notebooks are very good for the machine learning experimentation purpose but when it comes to displaying the output of your ML models, the platform isn't eye catching.<br><br>[Streamlit](https://streamlit.io) is a python package that converts your python scripts into beautiful web application. It is insanely easy to get started with streamlit, thanks to its **magically simple API**.

<script src="https://gist.github.com/sushe-shakya/e77f028e0f77c8dc3616621bfff7cbef.js"></script>

Now let's start the streamlit server by running the following code.
```
streamlit run streamlit-ui.py
```
Enter the displayed **Local URL** in your browser.
![stoutput1]({{site.url}}/assets/images/st-out1.png)

You will see the following output on your screen.
![stoutput2]({{site.url}}/assets/images/st-out2.png)

Sweet!!! 😎 ,Right ?

Now, let's build something that you can actually use to present and explain your machine learning models.


**Demo:**<br>
Let's assume you have trained a model that predicts whether an image is of a dog or not. 
Since its creation, the streamlit community has grown a lot and they have been developing 
many third party plugins to make the development of web apps with streamlit even easier and 
more fun. 



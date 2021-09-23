from joblib import load
import streamlit as st
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

#st.set_page_config(page_title = "Fake News Detector")

st.markdown(
   """
    <style>
    .reportview-container {
        background: url("https://images.app.goo.gl/LFCobouKtT7oZ7Qv7")
    }
   .sidebar .sidebar-content {
        background: url("https://images.app.goo.gl/LFCobouKtT7oZ7Qv7")
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown('<p class="big-font"{font-size:100px !important;}>Fake news detector!</p>', unsafe_allow_html=True)
 
#from PIL import Image
#img = Image.open("trump.png")
 
# display image using streamlit
# width is used to set the width of an image
#st.image(img, width=200)



model = load("fake_news_model_rfc.joblib")


desc = "This web app detects fake news written in English.\
        You can either enter the URL of a news article, or paste the text here(works better)."

st.subheader("Enter the text to find out if it is fake news")


def fakenewsdetection():
    user = st.text_area("Enter your headline here: ")
    if len(user) < 1:
        st.write("  ")
    else:
        return user

    

user_input = fakenewsdetection()

user_input = pd.Series(user_input)

true_prob, fake_prob = model.predict_proba(user_input)[0]


fig, ax = plt.subplots(figsize = (18,8))
plot = sns.barplot(x = ['True News Probability', 'Fake News Probability'], y = [true_prob, fake_prob], palette = ['green', 'red'], ax=ax)

ax.set_xticklabels(['True News Probability','Fake News Probability'], fontsize = 18)


for p in plot.patches:
    if p.get_height() == 0:
        pass
    else:
        plot.annotate(format(p.get_height() * 100, '.1f') + '%',
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha = 'center', va = 'center',
                       xytext = (3, 10), fontsize=20,
                       textcoords = 'offset points')
plt.margins(y = 0.1)

st.pyplot(fig)


#Results text

result = fake_prob - true_prob
if result > 0.5:
    st.write("This is very likely to be fake news")
elif result > 0.3 and result < 0.5:
    st.write("This might be fake news, double check your sources")
elif result < -0.5:
    st.write("This is likely to be true")

    




#if true_prob <= 0.4:
 #   st.write("This is unlikely to be true")
#elif true_prob >=0.5 and true_prob<=0.7:
 #   st.write("This is very likely true news")
#elif true_prob > 0.7:
 #   st.write("This is very likely true news")
    
    
#if fake_prob <= 0.4:
 #   st.write("This is unlikely to be fake news")
#elif fake_prob >=0.5 and fake_prob<=0.7:
 #   st.write("This is very likely fake news")
#elif fake_prob >= 0.7:
  #  st.write("This is definitely fake news")    
                    

st.write(true_prob, fake_prob)
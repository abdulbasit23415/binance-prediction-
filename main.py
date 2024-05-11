import streamlit as st
import requests,os,sys
from dotenv import load_dotenv

load_dotenv()
print(sys.path)
st.title("NewsApp using NewYork Times API")
news_api=os.getenv("new_api")
url=requests.get(f"https://api.nytimes.com/svc/mostpopular/v2/emailed/7.json?api-key={news_api}")
js=url.json()
rs=js['results']
for result in rs:
    st.write("----------------------------")
    # st.write(result['id'])
    st.write(result['title'])
    st.write(result['url'])
    st.image(result['media'][0]['media-metadata'][0]['url'])
    

    
    

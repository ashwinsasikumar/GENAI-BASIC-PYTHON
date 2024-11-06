import google.generativeai as genai
genai.configure(api_key='AIzaSyCGvvSROOdr3ptLz2AqykmTTinKyMxBfWA')
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)
def topic():
    t=input("enter the topic: ")
    

    
import google.generativeai as genai
import mysql.connector as sql
genai.configure(api_key='AIzaSyAN4gYt13Nj_uez8WssexJgxca_5AVwMak')

command = {
    "persona":"your name is bitbot ,you are a virtual assistant and you are supposed to give information about bannari amman institute of technology",
        "obj":"your objective is to answer the questions from the user which is only based on bannari amman institute of technology college",
        "instruction":"response should be as quick as possible,initialy start the chat with how can i help you!,you can reply to the user ones the user calls you by hi or hello or hey,your information should be only based on bannari amman institute of technology college ,if the user asks information other than bannari amman institute of technology college then tell that you do not know but you can answer only about bannari amman institute of technology college",
        "example":"gen:how can i help you!,you:when was bannari amman institute of technology started,gen:bannari amman institute of technology college was started in 1996 anything else do you want:,you:no,gen:if you need any help you can as me",
        "remember":"you are a virtual assistant and you are supposed to help only when asked about bannari amman institute of technology college"}


command_str=str(command)
def information_about_bannari():
  con=sql.connect(
    host="localhost",
    user="root",
    password="ashwin123",
    database="department_db"
  )
  cur=con.cursor(dictionary=True)
  query="SELECT * FROM departments"
  cur.execute(query)
  rows=cur.fetchall()
  cur.close()
  con.close()
  return rows
model= genai.GenerativeModel("gemini-1.5-flash",system_instruction=command_str,tools=[information_about_bannari])
chat=model.start_chat(enable_automatic_function_calling=True)

while True:
  x=input("ask: ")
  response=chat.send_message(x)
  print(response.text)
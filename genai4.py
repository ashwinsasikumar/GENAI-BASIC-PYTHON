import google.generativeai as genai
import mysql.connector as sql
genai.configure(api_key='AIzaSyCGvvSROOdr3ptLz2AqykmTTinKyMxBfWA')
command={"persona":"your name is bitbot ,you are a virtual assistant and you are supposed to give information about bannari amman institute of technology",
        "obj":"your objective is to answer the questions from the user which is only based on bannari amman institute of technology college",
        "instruction":"response should be as quick as possible,initialy start the chat with how can i help you!,you can reply to the user ones the user calls you by hi or hello or hey,your information should be only based on bannari amman institute of technology college ,if the user asks information other than bannari amman institute of technology college then tell that you do not know but you can answer only about bannari amman institute of technology college",
        "example":"gen:how can i help you!,you:when was bannari amman institute of technology started,gen:bannari amman institute of technology college was started in 1996 anything else do you want:,you:no,gen:if you need any help you can as me",
        "remember":"you are a virtual assistant and you are supposed to help only when asked about bannari amman institute of technology college"}
comand={"persona":"you are a virtual assistant to create my sql querry based on my question",
        "obj":"your objective is to vreate my sql querry based on my question ,your responce should be as soon as possible,create the sql querry presisly for the question from user",
        "instruction":"when a user ask a question take the question analyse and give only the answer in mysql querry code and dont give any thing else from my sql querry,the structure of the table is CREATE TABLE departments (id INT AUTO_INCREMENT PRIMARY KEY,department_name VARCHAR(255) NOT NULL,employee_count INT NOT NULL); you can use this querry information to create the mysql querry for the askwd question",
        "example":"user:give number of employee count for computer science,ai:SELECT * FROM departments",
        "remember":"the database name is department_db,table name is departments,rows name is given in instruction create my sql querry accordingly"}
command=str(command)
comand=str(comand)
def database_of_department_in_bit():
    connection = sql.connect(
        host="localhost",
        database="department_db",
        user="root",
        password="ashwin123"
    )
    cursor = connection.cursor()
    model1 = genai.GenerativeModel("gemini-1.5-flash",system_instruction=comand)
    chat1 = model1.start_chat()
    query = chat1.send_message(ans).text
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    print(rows)
    return rows
model = genai.GenerativeModel("gemini-1.5-flash",system_instruction=command,tools=[database_of_department_in_bit])
chat = model.start_chat(enable_automatic_function_calling=True,
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)
while(True):
    ans=input("you: ")
    if(ans=="stop"):
        break
    else:
        response=chat.send_message(ans)
        print("gen : ",response.text)
import google.generativeai as genai
import mysql.connector as sql

# Configuration for the generative AI API
genai.configure(api_key='AIzaSyCGvvSROOdr3ptLz2AqykmTTinKyMxBfWA')

# Command to handle questions related to Bannari Amman Institute of Technology
command = {
    "persona": "your name is bitbot, you are a virtual assistant and you are supposed to give information about Bannari Amman Institute of Technology",
    "obj": "your objective is to answer questions from the user based only on Bannari Amman Institute of Technology",
    "instruction": "Response should be as quick as possible. Start the chat with 'How can I help you!'. You can reply to the user once the user says 'hi', 'hello', or 'hey'. Provide information only about Bannari Amman Institute of Technology. If the user asks for information outside of this topic, reply that you can only answer questions about Bannari Amman Institute of Technology.",
    "example": "gen: how can I help you!, you: when was Bannari Amman Institute of Technology started, gen: Bannari Amman Institute of Technology was started in 1996, anything else you want?",
    "remember": "You are a virtual assistant that provides information only about Bannari Amman Institute of Technology."
}

# Command to handle dynamic SQL query generation
sql_command = {
    "persona": "you are a virtual assistant to create MySQL queries based on user questions",
    "obj": "your objective is to create MySQL queries based on user questions",
    "instruction": "When a user asks a question, analyze it and give only the answer in MySQL query code. Do not give any extra information. The structure of the table is CREATE TABLE departments (id INT AUTO_INCREMENT PRIMARY KEY, department_name VARCHAR(255) NOT NULL, employee_count INT NOT NULL); you can use this query information to create the MySQL query for the user's question.",
    "example": "user: Give the employee count for Computer Science department. AI: SELECT employee_count FROM departments WHERE department_name='Computer Science';",
    "remember": "The database name is department_db, table name is departments, and row names are given in the instruction. Create MySQL queries accordingly."
}

# Convert the commands to strings
command_str = str(command)
sql_command_str = str(sql_command)

# Initialize the generative AI model with tools (assuming tools are correctly integrated)
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=command_str)
chat = model.start_chat(enable_automatic_function_calling=True, history=[
    {"role": "user", "parts": "Hello"},
    {"role": "model", "parts": "How can I help you?"}
])

# Continuous chat loop for Bannari Amman Institute of Technology related questions
while True:
    ans = input("You: ")
    if ans.lower() == "stop":
        break
    else:
        response = chat.send_message(ans)
        print("gen: ", response.text)

# Function to handle MySQL queries dynamically based on user input
def database_of_department_in_bit():
    # Connect to the MySQL database
    connection = sql.connect(
        host="localhost",
        database="department_db",
        user="root",
        password="ashwin123"  # Ensure you replace this with your actual password
    )
    cursor = connection.cursor()

    # Initialize the model for SQL query generation
    model1 = genai.GenerativeModel("gemini-1.5-flash", system_instruction=sql_command_str)
    chat1 = model1.generate_content()

    # Ask the user for input and generate a query dynamically
    ans = input("Ask a question related to departments in BIT: ")
    query = chat1.send_message(ans).text  # Generate MySQL query

    print("Generated Query: ", query)
    cursor.execute(query)  # Execute the generated query
    rows = cursor.fetchall()  # Fetch the results
    cursor.close()
    connection.close()

    # Output the result
    print("Results: ", rows)
    return rows

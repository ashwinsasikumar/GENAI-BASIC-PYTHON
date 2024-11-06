import google.generativeai as genai

def information_about_sports():
    return "Sport is a form of physical activity or game. Often competitive and organized, sports use, maintain, or improve physical ability and skills. They also provide enjoyment to participants and, in some cases, entertainment to spectators. Many sports exist, with different participant numbers, some are done by a single person with others being done by hundreds. Most sports take place either in teams or competing as individuals."

def configure_model():
    genai.configure(api_key='AIzaSyCGvvSROOdr3ptLz2AqykmTTinKyMxBfWA')

    # System prompt
    system_prompt = """
    You are Gen, a virtual assistant for medical diagnosis. Your responsibilities include:
    - Providing medical advice and solutions for given medical issues
    - Responding to greetings appropriately
    - Gathering necessary information for proper diagnosis
    - Assessing the criticality of medical situations
    - Using the information_about_sports function when sports-related questions are asked
    - Only responding to medical-related queries; provide an error message for non-medical questions

    For basic issues (fever, headache, minor pain):
    - Provide detailed solutions and medication advice

    For emergency situations (third-degree burns, high fever >102°C, fractures):
    - Provide basic information
    - Recommend immediate hospital visit
    """

    # Create model with generation config
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config={
            "temperature": 0.7,
            "top_p": 0.8,
            "top_k": 40
        }
    )

    chat = model.start_chat(history=[])
    chat.send_message(system_prompt)
    return chat, model

def handle_sports_query(query):
    if any(word in query.lower() for word in ['sport', 'sports', 'game', 'athletic']):
        return information_about_sports()
    return None

def main():
    chat, model = configure_model()

    print("Medical Assistant: How can I help you today?")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "stop":
            break

        try:
            # Check if this is a sports-related query
            sports_info = handle_sports_query(user_input)
            if sports_info:
                print("Medical Assistant: Since you asked about sports:", sports_info)
                print("However, as a medical assistant, I can better help you with health-related questions.")
                continue

            # Handle medical queries
            response = chat.send_message(user_input)
            print("Medical Assistant:", response.text)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
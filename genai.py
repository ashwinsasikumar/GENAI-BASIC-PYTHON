import google.generativeai as genai
def information_about_sports():
    return "Sport is a form of physical activity or game. Often competitive and organized, sports use, maintain, or improve physical ability and skills. They also provide enjoyment to participants and, in some cases, entertainment to spectators. Many sports exist, with different participant numbers, some are done by a single person with others being done by hundreds. Most sports take place either in teams or competing as individuals."

def configure_model():
    genai.configure(api_key='AIzaSyCGvvSROOdr3ptLz2AqykmTTinKyMxBfWA')
    
    # Define the tools/functions that can be called
    tools = [{
        "name": "information_about_sports",
        "description": "Get information about sports in general",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }]
    
    # System prompt as a well-formatted string
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
    
    Remember to verify medical terminology and maintain focus on medical context.
    """
    
    # Create model with tools configuration
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        tools=tools,
        generation_config={
            "temperature": 0.7,
            "top_p": 0.8,
            "top_k": 40
        }
    )
    
    return model

def main():
    model = configure_model()
    conversation_history = []
    
    while True:
        user_input = input("How can I help you: ")
        if user_input.lower() == "stop":
            break
            
        conversation_history.append(user_input)
        
        try:
            response = model.generate_content(
                conversation_history,
                generation_config={"temperature": 0.7},
                tools=[information_about_sports]
            )
            
            # Handle function calling if present in response
            if hasattr(response, 'tool_calls') and response.tool_calls:
                for tool_call in response.tool_calls:
                    if tool_call.function.name == "information_about_sports":
                        sports_info = information_about_sports()
                        conversation_history.append(f"Function result: {sports_info}")
            
            print(response.text)
            conversation_history.append(response.text)
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
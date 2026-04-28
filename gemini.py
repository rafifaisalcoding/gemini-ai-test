from google import genai

print("starting...")
client = genai.Client(api_key="put token here") #import the API key of the AI

while True:
        userinput =input("Please input your response.") #Initialise and ask the user for input.
        try:
                    
            response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview", # AI model to proceed witpip install google-api-coreh.
            contents= userinput # Input
        )
            print(response.text) # the actual response so the user can receive
        except:
              print("too much traffic")
        

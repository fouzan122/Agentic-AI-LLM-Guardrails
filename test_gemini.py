
from gemini_service import generate_response

try:
    result = generate_response("Explain Python in one sentence.")
    print("Gemini API working!")
    print("Response:", result)

except Exception as e:
    print("Gemini API failed!")
    print("Error:", type(e).__name__, str(e))

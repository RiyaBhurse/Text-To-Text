import google.generativeai as genai
import os
import time

os.environ["API_KEY"]= "AIzaSyBUtpL2m21nHa28G0Lic54AiuqtEOy_9AY"
genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')
startTime = time.time()
response = model.generate_content("behave like a receptionist and greet the customer, receptionist of a resort, give info about the availablity rooms")
endTime = time.time()
timeTaken = endTime - startTime
print("Time taken: ", timeTaken)
print(response.text)

# subhash@mydukan.io
# 8097476656
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse  # For URL encoding

class Voice:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.ListenOnMic()

    def ListenOnMic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()
                    print(f"Command: {command}")

                if "search" in command:
                    search_query = command.split("search")[-1].strip()
                    print(f"Searching for: {search_query}")
                    
                    # URL encode the search query
                    encoded_query = urllib.parse.quote(search_query)
                    
                    # Initialize the ChromeDriver
                    service = Service(ChromeDriverManager().install())
                    driver = webdriver.Chrome(service=service)
                    
                    # Perform the Google search
                    search_url = f"https://www.google.com/search?q={encoded_query}"
                    driver.get(search_url)
                    
                    # Optionally, you can add a delay or close the driver after some time
                    # time.sleep(10)  # Wait 10 seconds before closing
                    # driver.quit()
                    
            except sr.UnknownValueError:
                print("Sorry, I didn't understand.")
            except sr.RequestError:
                print("Sorry, there was an error with the speech recognition service.")
            except Exception as e:
                print(f"An error occurred: {e}")

listener = Voice()

import paralleldots
# Setting your API key

class API:

    def __init__(self):
        paralleldots.set_api_key('8GwL0GsV8nsLJNEUyVvuxh85sLknLZYVnPGUnoC0NLM')

    def sentiment_analysis(self, text):
        response = paralleldots.sentiment(text)
        return response

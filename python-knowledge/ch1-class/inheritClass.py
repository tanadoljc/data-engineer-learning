from firstClass import llms

class chatbot(llms):

    def __init__(self, model, query): # must call query of Parent
        self.model = model
        self.query = query

    def showme(self):
        print(f"I am calling {self.model}")
        llms.openai()

obj_inherit = chatbot("openai", "Hey, I am 4most eiei")
obj_inherit.openai()
""""""
class AnonymousSurvey():
    """"""

    def __init__(self,question):
        """"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """"""
        return(f"Your's question is : {self.question}")
    
    def store_response(self,response):
        """"""
        self.responses.append(response)
    
    def show_result(self):
        """"""
        for response in self.responses:
            print(f"Response : {response}")

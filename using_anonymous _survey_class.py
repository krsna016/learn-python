from Anonymous_survey_class import AnonymousSurvey
q_1 = AnonymousSurvey(question="What's your favourite Language ?")
print(q_1.show_question())
q_1.store_response("Python")
q_1.show_result()
q_1.store_response("C")
q_1.show_result()


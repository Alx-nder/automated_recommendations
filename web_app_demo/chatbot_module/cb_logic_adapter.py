from chatterbot.logic import LogicAdapter
import sys
import random

sys.path.append("C:\\xampp\\htdocs\\virtualTourWebsite\\zoomapi\\")
import makemeeting


class agentlogicadapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words=['help','agent','somebody','talk','speak']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False
        
    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
    
        # Let's base the confidence value on if agent is available
        confidence = random.uniform(0, 1)

        
        response_statement = Statement(text=makemeeting.setup_meet)
        return confidence, response_statement
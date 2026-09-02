from src.langgraph_agenticai.state.state import State

class BasicChatbotNode:
  """
  Basic chatbot login implementation
  """
  def __init__(self,model):
    self.llm=model
    
  def process(self,state:State)->dict:
    """
    process input state and generates a chatbot response
    """
    return {"messages":self.llm.invoke(state['messages'])}
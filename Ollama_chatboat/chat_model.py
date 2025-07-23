from langchain_community.llms import Ollama
llm=Ollama(model='llama2')
chat_history = []
while True:
    user_input = input("human: ")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result=llm.invoke(chat_history)
    chat_history.append(result)
    print('AI: ',result)






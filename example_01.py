"""
Minimal example of a CLI chatbot using the GPT4All API only.
GPT4All must be installed locally!
"""

import gpt4all
from colorama import Fore, Style
import pprint
 
 
# Small model -> useful for testing as executes much faster
#model = gpt4all.GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# Large model -> much better chat quality but slow on local CPU
model = gpt4all.GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")


system_prompt =  """"You are a helpful pirate AI assistant. 
Please answer as if talking like a pirate!"""


# Enter the chat_session context. This context provides automatic in-memory
# chat history in the form of a list of dicts, with each dict entry containing 
# a content key and a role key, with the role values of either system, user, or 
# assistant.
#
# The chat session can be terminated by hitting enter without any input.
with model.chat_session(system_prompt=system_prompt):    
    while True:
        new_question = input(
            Fore.GREEN + Style.BRIGHT + "Question: " + Style.RESET_ALL
        )
        if new_question:
            response = model.generate(new_question)
            print(Fore.CYAN + Style.BRIGHT + "AI: " + Style.NORMAL + response)
        else:            
            break
    
    # Print the whole chat session at the end - helpful for understanding
    # the structure.
    pprint.pprint(model.current_chat_session)

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from chartie import ChatBot

def main():
    # Instantiate the chatbot object class
    chatbot = ChatBot()
    
    # greet user
    print("CooKGenie:", chatbot.greetings())

    name = None
    while name is None:
        # get user's name and greet user by name
        print("CooKGenie: " + chatbot.prompt_for_name())
        name = input("You: ")
    print("CooKGenie: Hello, " + name + "!")

    while True:
        #prompt user to enrol for cooking training
        print("CooKGenie:", chatbot.prompt_to_enroll())
        enroll_response = input(name + ": ").lower()
       
        # enrol user for cooking tranining if user chooses to and update the enrollment csv file
        if enroll_response in chatbot.enrol_affirmation():
            print("CooKGenie:", chatbot.enroll())
            if not chatbot.ask_for_more():
                break
                
        # prompt user to ask for more help if user chose not to enrol for cooking training
        elif enroll_response in chatbot.enroll_rejection():
            question = print("CooKGenie: " + chatbot.prompt_for_help())
            help_response = input(name + ": ").lower()
            
            # provide help tailored to user's request
            if help_response in chatbot.help_reply():
                print("CooKGenie: " + str(chatbot.ask_for_more()))
                continue
                
            # provide food recipe information via Open AI as per user's recipe request
            elif help_response in chatbot.recipe_reply():
                print("CooKGenie: " + chatbot.prompt_for_cuisine())
                cuisine_response = input(name + ": ").lower()
                print("CooKGenie:", chatbot.generate_recipe_response(cuisine_response))
                if not chatbot.ask_for_more():
                    break
                    
            # provide food technique information via Open AI as per user's recipe request 
            elif help_response in chatbot.technique_reply():
                print("CooKGenie: " + chatbot.prompt_for_cuisine())
                cuisine_response = input(name + ": ").lower()
                print("CooKGenie:", chatbot.generate_technique_response(cuisine_response))
                if not chatbot.ask_for_more():
                    break
                    
         # provide food recipe information via Open AI as per user's recipe request
        elif enroll_response in chatbot.recipe_reply():
            print("CooKGenie: " + chatbot.prompt_for_cuisine())
            cuisine_response = input(name + ": ").lower()
            print("CooKGenie:", chatbot.generate_recipe_response(cuisine_response))
            if not chatbot.ask_for_more():
                break
                
        # provide food technique information via Open AI as per user's recipe request 
        elif enroll_response in chatbot.technique_reply():
            print("CooKGenie: " + chatbot.prompt_for_cuisine())
            cuisine_response = input(name + ": ").lower()
            print("CooKGenie:", chatbot.generate_technique_response(cuisine_response))
            if not chatbot.ask_for_more():
                break
                
                # provide food technique information via Open AI as per user's recipe request 
        elif enroll_response in chatbot.technique_reply():
            print("CooKGenie: " + chatbot.prompt_for_cuisine())
            cuisine_response = input(name + ": ").lower()
            print("CooKGenie:", chatbot.generate_technique_response(cuisine_response))
            if not chatbot.ask_for_more():
                break        
                
                 # provide informatio about the chabot's identity        
        elif enroll_response in chatbot.cookgenie_query():
            chatbot.cookgenie_identity()
            if not chatbot.ask_for_more():
                break

        # provide information about the cookgenie developer    
        elif enroll_response in chatbot.origin_query():
            chatbot.cookgenie_creator()
            if not chatbot.ask_for_more():
                break

        # provide information about the chatbot's feature   
        elif enroll_response in chatbot.feature_query():
            chatbot.cookgenie_feature()   
            if not chatbot.ask_for_more():
                break        
                
        # terminate the program if user choose not to continue
        elif chatbot.check_exit(enroll_response):
            print("CooKGenie: Goodbye, " + name + "!")
            break
            
        #request for clarification if user's input deos not match any for bot's programmed keywords 
        else:
            print("CooKGenie: " +  chatbot.re_try())
            
if __name__ == '__main__':
    main()  


# In[ ]:





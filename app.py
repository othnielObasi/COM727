#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
from chartie import ChatBot
import os

app = Flask(__name__)

# Instantiate the chatbot object class
chatbot = ChatBot()

@app.route('/')
def index():
    return render_template(os.path.join('com272', 'index.html'))

@app.route('/chat', methods=['POST'])
def chat():
    # greet user
    response = {'message': 'CooKGenie: ' + chatbot.greetings()}
    return response

    name = None
    while name is None:
        try:
            # get user's name and greet user by name
            response = {'message': 'CooKGenie: ' + chatbot.prompt_for_name()}
            name = request.form['text']
        except KeyError:
            response = {'message': 'Please enter your first name.'}

    response = {'message': 'CooKGenie: Hello, ' + name + '!'}

    while True:
        # prompt user to enrol for cooking training
        response = {'message': 'CooKGenie: ' + chatbot.prompt_to_enroll()}
        
        enroll_response = request.form['text'].lower()
       
        # enrol user for cooking training if user chooses to and update the enrollment csv file
        if enroll_response in chatbot.enrol_affirmation():
            response = {'message': 'CooKGenie: ' + chatbot.enroll()}
            if not chatbot.ask_for_more():
                break
                
        # prompt user to ask for more help if user chose not to enrol for cooking training
        elif enroll_response in chatbot.enroll_rejection():
            question = {'message': 'CooKGenie: ' + chatbot.prompt_for_help()}
            help_response = request.form['text'].lower()
            
            # provide help tailored to user's request
            if help_response in chatbot.help_reply():
                response = {'message': 'CooKGenie: ' + str(chatbot.ask_for_more())}
                continue
                
            # provide food recipe information via Open AI as per user's recipe request
            elif help_response in chatbot.recipe_reply():
                response = {'message': 'CooKGenie: ' + chatbot.prompt_for_cuisine()}
                cuisine_response = request.form['text'].lower()
                response = {'message': 'CooKGenie: ' + chatbot.generate_recipe_response(cuisine_response)}
                if not chatbot.ask_for_more():
                    break
                    
            # provide food technique information via Open AI as per user's recipe request 
            elif help_response in chatbot.technique_reply():
                response = {'message': 'CooKGenie: ' + chatbot.prompt_for_cuisine()}
                cuisine_response = request.form['text'].lower()
                response = {'message': 'CooKGenie: ' + chatbot.generate_technique_response(cuisine_response)}
                if not chatbot.ask_for_more():
                    break
                    
         # provide food recipe information via Open AI as per user's recipe request
        elif enroll_response in chatbot.recipe_reply():
            response = {'message': 'CooKGenie: ' + chatbot.prompt_for_cuisine()}
            cuisine_response = request.form['text'].lower()
            response = {'message': 'CooKGenie: ' + chatbot.generate_recipe_response(cuisine_response)}
            if not chatbot.ask_for_more():
                break
                
                        
         # provide food technique information via Open AI as per user's recipe request 
        elif enroll_response in chatbot.technique_reply():
            response = {'message': 'CooKGenie: ' + chatbot.prompt_for_cuisine()}
            cuisine_response = request.form['text'].lower()
            response = { 'message':'CooKGenie: ' + chatbot.generate_technique_response(cuisine_response)}
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
                
               # provide information about the chatbot's features
        elif enroll_response in chatbot.feature_query():
            chatbot.cookgenie_feature()
            if not chatbot.ask_for_more():
                break

        # terminate the program if the user chooses not to continue
        elif chatbot.check_exit(enroll_response):
            response = {'message': 'CooKGenie: Goodbye, ' + name + '!'}
            break

        # request for clarification if the user's input does not match any of the bot's programmed keywords
        else:
            response = {'message': 'CooKGenie: ' + chatbot.re_try()}

    return response

if __name__ == '__main__':
    app.run(debug=True)
                 


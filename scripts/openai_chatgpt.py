import scripts.keys as key
import scripts.truLens as tru
from openai import OpenAI
client = OpenAI(api_key = key.openAI_key)




#Function to make submission to chat gpt API
def submit_recipe(ingredients):
    prompt = ("I have the following items in my kitchen, can you list me three different meals I can out together with the following? For now though, just state what the three meals are and explain to the user why they should make this meal. Only use the ingredients that are inputted. A minimum one is required. Assume basic kitchen spices are available. The steps for the meal are not needed till at a later point. An example of how I want the list to start is '1. Name of Meal: meal description' separate each option by a \n. This is a strict requirement. Even if the input of ingredients is null. The ingredients that follow this statement are separated by. ', ':" + ingredients )

    response = call_OpenAI(prompt)

    #Determining relevancy of of prompt
    tru.truLensMonitor(call_OpenAI, prompt)





    #Parses out my data
    dishNameAndDescription = response.split('\n')

    ##This gives me each item food choice and puts them in a set with descriptions, as well cleans up a ',' that appears
    dishNameAndDescription = [element for element in dishNameAndDescription if len(element) >5]
    ##This further cleans up the above, and will give me the name of each meal

    dishes = []
    for dishName in dishNameAndDescription:
        start_pos = dishName.find('.') +2
        end_pos = dishName.find(':')

        if start_pos != -1 and end_pos != -1:
            title = dishName[start_pos:end_pos].strip()
            dishes.append(title)

    return dishNameAndDescription, dishes




###API call to chatgpt
def call_OpenAI(prompt):


    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"user","content": prompt},
        ],
        max_tokens = 1024,
    )


    response_content = response.choices[0].message.content


    return response_content
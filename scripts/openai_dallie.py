import scripts.keys as key
from openai import OpenAI

import os
import requests
from PIL import Image
from io import BytesIO


client = OpenAI(api_key = key.openAI_key)


#Uncomment the following after testing complete
def generateImage(input, previousInput, filename, filepath):

    if previousInput == '':
        response = client.images.generate(
        model="dall-e-2",
        prompt=input,
        size="1024x1024",
        quality="standard",
        n=1,
        )
    else:
        response = client.images.generate(
        model="dall-e-2",
        prompt=f"Use the previous to help shape this image. The previous prompt was {previousInput}. The current prompt that uses thee previous prompt is {input}",
        size="1024x1024",
        quality="standard",
        n=1,
        )
    

    image_url = response.data[0].url

    #Download image with the following line:
    image_response = requests.get(image_url)

    #Check if reuqest was successful
    if image_response.status_code == 200:
        #open image with pillow
        image = Image.open(BytesIO(image_response.content))

        #save image
        x = os.path.join(filepath, filename)
        image.save(x)

    else:
        print(f"Failed to download image. Status code: {image_response.status_code}")

    return x



    
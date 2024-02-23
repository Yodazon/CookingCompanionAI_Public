#Below is importing Trulens for chatGPT evaluation
# Imports main tools:
from trulens_eval import Feedback, OpenAI as fOpenAI, Tru
from trulens_eval import TruBasicApp
import scripts.keys as key
from openai import OpenAI
client = OpenAI(api_key = key.openAI_key)


def truLensMonitor(openAIFunction, prompt_input):
    tru = Tru()
    tru.reset_database()
    # Initialize OpenAI-based feedback function collection class:
    fopenai = fOpenAI()

    # Define a relevance function from openai
    f_relevance = Feedback(fopenai.relevance).on_input_output()

    # Initialize OpenAI-based feedback function collection class:
    fopenai = fOpenAI()

    # Define a relevance function from openai
    f_relevance = Feedback(fopenai.relevance).on_input_output()

    tru_llm_standalone_recorder = TruBasicApp(openAIFunction, app_id="MealGenerate", feedbacks=[f_relevance])

    with tru_llm_standalone_recorder as recording:
        tru_llm_standalone_recorder.app(prompt_input)

    result = tru.get_records_and_feedback(app_ids=['MealGenerate'])[0]
    print((tru.get_records_and_feedback(app_ids=['MealGenerate'])[0])) # pass an empty list of app_ids to get all
    if 'relevance' in result.columns:
        relevance_column = result['relevance']
        print(relevance_column)
    else:
        print("The 'latency' column is not present in the result.")
import asyncio
from agents import Agent,Runner,OpenAIChatCompletionsModel,set_tracing_disabled
from dotenv import load_dotenv
load_dotenv()
from openai import AsyncOpenAI
import os
gemini_api_key = os.getenv('GEMINI_API_KEY')

user = input('How we can help you: ')
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)
set_tracing_disabled(disabled=True)


async def main():
    agent = Agent(
    name='Personal Agent',
    instructions='You are a my Personal Assitant Agent',
    model=OpenAIChatCompletionsModel(model='gemini-2.0-flash',openai_client=client)
    )

    result =  await Runner.run(
        agent,
        user
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
    


# Import necessary libraries
import os
from cryptoagent.main import OpenAIChat, CryptoAgent
from swarms import Agent
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Ensure API key is loaded
openai_api_key = os.getenv("OPENAI_API_KEY")

# Create an instance of OpenAIChat class for LLM integration
model = OpenAIChat(
    openai_api_key=openai_api_key, model_name="gpt-4o-mini", temperature=0.1
)

# Create the input agent
input_agent = Agent(
    agent_name="Crypto-Analysis-Agent",
    system_prompt="You are a financial analysis agent that provides crypto analysis with live data.",
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="crypto_agent.json",
    user_name="swarms_corp",
    retry_attempts=2,
    context_length=10000,
)

# Create CryptoAgent instance and pass the input agent
crypto_analyzer = CryptoAgent(agent=input_agent)

# Define the coins to be analyzed
coin_ids = ["bitcoin", "ethereum", "dogecoin", "xrp"]

# Fetch and summarize crypto data for multiple coins in parallel
summaries = crypto_analyzer.run(coin_ids)

# Print the summaries
for summary in summaries:
    print(summary)

from strands import Agent
from strands.models import BedrockModel
from strands_tools import image_reader

# configure the model
bedrock_model = BedrockModel(model_id='anthropic.claude-3-sonnet-20240229-v1:0') # mistral.mistral-large-3-675b-instruct amazon.nova-pro-v1:0

MULTIMODAL_SYSTEM_PROMPT = """ You are a helpful assistant that can process documents and images. 
All the images supplied are for players who play in the Canadian Football League.
Your task is to identify the team name and the player number from the image.
You should return the team name and the player number in a JSON format.
The JSON format should be like this:
{
    "team_name": "Team Name",
    "player_number": "Player Number"
}

If you are not able to identify the team name or the player number, you should return an empty JSON object.
If you are not able to identify the team name or the player number, you should return an empty JSON object.
"""

# create the agent with multimodal capabilities
agent = Agent(
    system_prompt=MULTIMODAL_SYSTEM_PROMPT,
    tools=[image_reader],
    model=bedrock_model
)

result = agent("Can you describe this image: `/Users/akshayranganath/Projects/aws-hackathon/player-identification/data/5.jpg`")
print(result)
from strands import Agent
from strands.models import BedrockModel
from strands_tools import image_reader
from prompt import get_prompt
import json

# configure the model
bedrock_model = BedrockModel(model_id='anthropic.claude-3-sonnet-20240229-v1:0') # mistral.mistral-large-3-675b-instruct amazon.nova-pro-v1:0
MULTIMODAL_SYSTEM_PROMPT = get_prompt()


def get_player_details(image_path: str) -> dict:
# create the agent with multimodal capabilities
    agent = Agent(
        system_prompt=MULTIMODAL_SYSTEM_PROMPT,
        tools=[image_reader],
        model=bedrock_model
    )

    result = agent(f"Can you describe this image: {image_path}")
    return json.loads(str(result))

if __name__=="__main__":
    result = get_player_details("/Users/akshayranganath/Projects/aws-hackathon/player-identification/data/5.jpg")
    print('**** Result ****')
    print(result)
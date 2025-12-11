# test_strands.py
import os
import boto3
from botocore.session import Session
from strands import Agent
from strands_tools import calculator

def main():
    # Debug: Show profile info
    print("AWS_PROFILE env:", os.getenv("AWS_PROFILE"))
    print("AWS_DEFAULT_PROFILE env:", os.getenv("AWS_DEFAULT_PROFILE"))

    session = Session()
    print("Boto3 using profile:", session.profile)

    try:
        sts = boto3.client("sts")
        print("AWS identity:", sts.get_caller_identity())
    except Exception as e:
        print("Unable to get caller identity:", e)

    # Create an agent with a simple tool (calculator)
    agent = Agent(tools=[calculator])

    # Test prompt
    result = agent("What is the square root of 144?")
    print("Agent response:", result)

if __name__ == "__main__":
    main()

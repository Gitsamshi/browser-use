"""
AWS Claude Example with Browser-Use

This example shows how to use AWS Bedrock Claude models with browser-use.
Make sure your AWS credentials are configured before running.
"""

import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from browser_use import Agent
from browser_use.llm import ChatAnthropicBedrock


async def main():
    """Simple example using AWS Claude via Bedrock."""
    
    print("🚀 Setting up AWS Claude agent...")
    
    # Initialize AWS Claude via Bedrock
    # This uses the ChatAnthropicBedrock convenience class
    llm = ChatAnthropicBedrock(
        # Available Claude models in AWS Bedrock (with us. prefix):
        model='us.anthropic.claude-3-7-sonnet-20250219-v1:0',  # Latest Claude 3.7 Sonnet
        # model='us.anthropic.claude-3-5-sonnet-20241022-v2:0',  # Claude 3.5 Sonnet
        # model='us.anthropic.claude-3-haiku-20240307-v1:0',     # Claude 3 Haiku (faster, cheaper)
        # model='us.anthropic.claude-3-opus-20240229-v1:0',      # Claude 3 Opus (most capable)
        
        aws_region='us-east-1',  # Change to your preferred region
        temperature=0.7,
        max_tokens=4096,
    )

    print(f"✅ Model: {llm.name}")
    print(f"✅ Provider: {llm.provider}")
    print(f"✅ Region: us-east-1")
    
    # Define a simple task
    task = "go to https://www.amazon.com/ and search for 'iphone 15' and tell me the first result"
    
    print(f"\n🎯 Task: {task}")
    
    # Create and run the agent
    agent = Agent(task=task, llm=llm)
    
    try:
        print("\n🤖 Starting agent...")
        result = await agent.run()
        print(f"\n✅ Task completed successfully!")
        print(f"📋 Result: {result}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Check your AWS credentials are correctly set")
        print("2. Ensure you have access to AWS Bedrock in your region")
        print("3. Verify the Claude model is available in your region")


if __name__ == '__main__':
    asyncio.run(main()) 
"""
AWS Claude Streamlit Demo for Browser-Use

Run with: python -m streamlit run aws_streamlit_demo.py

Make sure your AWS credentials are configured in .env or via AWS CLI.
"""

import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv

load_dotenv()

import streamlit as st  # type: ignore

from browser_use import Agent
from browser_use.browser import BrowserSession
from browser_use.controller.service import Controller
from browser_use.llm import ChatAnthropicBedrock

if os.name == 'nt':
	asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())


def get_aws_claude_llm(model: str, region: str, temperature: float):
	"""Get AWS Claude LLM instance."""
	try:
		return ChatAnthropicBedrock(
			model=model,
			aws_region=region,
			temperature=temperature,
			max_tokens=4096,
		)
	except Exception as e:
		st.error(f'Error initializing AWS Claude: {e}')
		st.error('Please check your AWS credentials and Bedrock access.')
		st.stop()


async def run_browser_agent(task: str, llm, max_steps: int):
	"""Run the browser agent with the given task."""
	try:
		# Initialize browser session
		browser_session = BrowserSession()
		controller = Controller()
		
		# Create agent
		agent = Agent(
			task=task,
			llm=llm,
			browser_session=browser_session,
			controller=controller
		)
		
		# Run agent
		result = await agent.run(max_steps=max_steps)
		return result, None
		
	except Exception as e:
		return None, str(e)


def main():
	"""Main Streamlit app."""
	st.set_page_config(
		page_title="Browser-Use with AWS Claude",
		page_icon="🤖",
		layout="wide"
	)
	
	st.title("🤖 Browser-Use with AWS Claude")
	st.markdown("**Automate web tasks using AI-powered browser automation!**")
	
	# Sidebar for configuration
	with st.sidebar:
		st.header("⚙️ Configuration")
		
		# Model selection
		model = st.selectbox(
			"🧠 Claude Model",
			[
				"us.anthropic.claude-3-7-sonnet-20250219-v1:0",  # Latest Claude 3.7 Sonnet
				"us.anthropic.claude-3-5-sonnet-20241022-v2:0",  # Claude 3.5 Sonnet
				"us.anthropic.claude-3-haiku-20240307-v1:0",     # Claude 3 Haiku (faster, cheaper)
				"us.anthropic.claude-3-opus-20240229-v1:0",      # Claude 3 Opus
			],
			index=0,
			help="Choose the Claude model for your task"
		)
		
		# Region selection
		region = st.selectbox(
			"🌍 AWS Region",
			["us-east-1", "us-west-2", "eu-west-1", "ap-southeast-1"],
			index=0,
			help="Select your AWS Bedrock region"
		)
		
		# Temperature
		temperature = st.slider(
			"🌡️ Temperature",
			min_value=0.0,
			max_value=1.0,
			value=0.7,
			step=0.1,
			help="Controls randomness in responses"
		)
		
		# Max steps
		max_steps = st.slider(
			"📊 Max Steps",
			min_value=1,
			max_value=20,
			value=5,
			step=1,
			help="Maximum number of steps the agent can take"
		)
		
		st.markdown("---")
		st.markdown("### 🔧 Setup")
		st.info("""
		**Requirements:**
		1. AWS credentials configured
		2. Access to AWS Bedrock
		3. Claude model access in your region
		""")
	
	# Main interface
	col1, col2 = st.columns([1, 1])
	
	with col1:
		st.header("📝 Task Input")
		
		# Task input
		task = st.text_area(
			"Describe what you want the agent to do:",
			value="Go to google.com and search for 'AWS Bedrock pricing'",
			height=100,
			help="Enter a detailed description of the web task you want to automate"
		)
		
		# Example tasks
		st.markdown("**💡 Example Tasks:**")
		example_tasks = [
			"Search Google for the latest AI news",
			"Go to GitHub and find the most popular Python repositories",
			"Navigate to weather.com and get the forecast for New York",
			"Visit Amazon and search for 'laptop' then show me the first result",
			"Go to Wikipedia and find information about machine learning"
		]
		
		for example in example_tasks:
			if st.button(f"Use: {example}", key=f"example_{hash(example)}"):
				task = example
				st.rerun()
	
	with col2:
		st.header("🚀 Execution")
		
		# Run button
		if st.button("▶️ Run Agent", type="primary", use_container_width=True):
			if not task.strip():
				st.error("Please enter a task!")
				return
			
			# Show configuration
			st.info(f"""
			**Configuration:**
			- Model: {model}
			- Region: {region}
			- Temperature: {temperature}
			- Max Steps: {max_steps}
			""")
			
			# Initialize LLM
			with st.spinner("Initializing AWS Claude..."):
				llm = get_aws_claude_llm(model, region, temperature)
			
			# Run agent
			with st.spinner(f"Running agent (max {max_steps} steps)..."):
				try:
					# Run the agent
					loop = asyncio.new_event_loop()
					asyncio.set_event_loop(loop)
					
					result, error = loop.run_until_complete(
						run_browser_agent(task, llm, max_steps)
					)
					
					loop.close()
					
					if error:
						st.error(f"❌ Error: {error}")
					else:
						st.success("✅ Task completed successfully!")
						st.markdown("### 📋 Result:")
						st.write(result)
						
				except Exception as e:
					st.error(f"❌ Unexpected error: {str(e)}")
					st.markdown("""
					**🔧 Troubleshooting:**
					- Check your AWS credentials are correctly configured
					- Ensure you have access to AWS Bedrock in your selected region
					- Verify the Claude model is available in your region
					""")
	
	# Footer
	st.markdown("---")
	st.markdown("""
	### 📚 About
	This demo uses **browser-use** with **AWS Claude** via Bedrock to automate web browser tasks.
	The AI agent can navigate websites, click elements, fill forms, and extract information.
	
	**🔗 Links:**
	- [Browser-Use GitHub](https://github.com/gregpr07/browser-use)
	- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
	""")


if __name__ == '__main__':
	main() 
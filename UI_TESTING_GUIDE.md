# 🎯 Browser-Use UI Testing Guide with AWS Claude

## 🔧 Prerequisites
1. **AWS credentials configured** in `.env` or via AWS CLI
2. **Access to AWS Bedrock** and Claude models in your region
3. **All dependencies installed** ✅

## 🌟 Available UI Options

### 🌐 Option 1: Gradio Web Interface (Recommended)
**Best for:** Interactive testing with real-time output

```bash
python aws_gradio_demo.py
```

**Features:**
- ✅ Real-time agent output streaming
- ✅ Model and region selection
- ✅ Temperature and step controls
- ✅ Copy-paste friendly results
- ✅ Access at: http://localhost:7860

### 📱 Option 2: Streamlit Web Interface  
**Best for:** Professional-looking interface with detailed configuration

```bash
python -m streamlit run aws_streamlit_demo.py
```

**Features:**
- ✅ Professional UI with sidebar configuration
- ✅ Example task buttons
- ✅ Detailed error messages and troubleshooting
- ✅ Configuration summary
- ✅ Access at: http://localhost:8501

### 💻 Option 3: Command Line Example
**Best for:** Quick testing and debugging

```bash
python aws_claude_example.py
```

**Features:**
- ✅ Simple terminal output
- ✅ Easy to modify for testing
- ✅ Good for debugging

## 🎮 How to Test

### Step 1: Configure AWS Credentials
Edit your `.env` file:
```bash
AWS_ACCESS_KEY_ID=your-aws-access-key-here
AWS_SECRET_ACCESS_KEY=your-aws-secret-key-here
AWS_DEFAULT_REGION=us-east-1
```

### Step 2: Choose Your Interface
Pick one of the UI options above and run it.

### Step 3: Try Example Tasks
**Simple tasks to start with:**
- "Go to google.com and search for 'AWS Bedrock pricing'"
- "Visit github.com and find the most popular Python repository"
- "Navigate to weather.com and get today's weather"

**More complex tasks:**
- "Search Google for 'best laptops 2024', visit the first result, and summarize the top 3 recommendations"
- "Go to Amazon, search for 'wireless headphones', and compare the prices of the first 3 results"

### Step 4: Monitor the Browser
- The agent will open a Chromium browser window
- You can watch it navigate and interact with websites
- Check the UI output for detailed step-by-step progress

## 🛠️ Available Configuration

### Claude Models
- `anthropic.claude-3-5-sonnet-20241022-v2:0` (Latest, recommended)
- `anthropic.claude-3-haiku-20240307-v1:0` (Faster, cheaper)
- `anthropic.claude-3-opus-20240229-v1:0` (Most capable)

### AWS Regions
- `us-east-1` (Virginia)
- `us-west-2` (Oregon)  
- `eu-west-1` (Ireland)
- `ap-southeast-1` (Singapore)

### Parameters
- **Temperature:** 0.0-1.0 (controls randomness)
- **Max Steps:** 1-20 (maximum actions agent can take)

## 🚨 Troubleshooting

### Common Issues:

**1. AWS Credentials Error**
```
Error: AWS credentials not found
```
**Solution:** Check your `.env` file or run `aws configure`

**2. Model Access Error**
```
Error: AccessDeniedException
```
**Solution:** Enable Claude model access in your AWS Bedrock console

**3. Region Error**  
```
Error: Model not available in region
```
**Solution:** Try a different region or check model availability

**4. Import Error**
```
ModuleNotFoundError: No module named 'gradio'
```
**Solution:** Run `uv add gradio streamlit` again

## 🎯 Success Indicators

You'll know it's working when:
- ✅ Browser window opens automatically
- ✅ Agent starts navigating to websites
- ✅ UI shows step-by-step progress
- ✅ You get meaningful results back

## 🔗 Quick Links

- **Gradio Demo:** `python aws_gradio_demo.py`
- **Streamlit Demo:** `python -m streamlit run aws_streamlit_demo.py`  
- **CLI Example:** `python aws_claude_example.py`

Choose the interface that works best for your testing needs! 🚀 
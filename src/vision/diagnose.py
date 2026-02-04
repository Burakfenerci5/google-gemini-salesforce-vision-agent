import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

# Configure the API with your key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_image_with_gemini3(image_path):
    """
    Uses Gemini 3 Pro (Preview) to perform deep visual reasoning.
    """
    try:
        # UPGRADE: Using 'gemini-3-pro-preview' (Released Nov 2025)
        # This model excels at "Agentic" tasks and complex instruction following.
        model = genai.GenerativeModel('gemini-3-pro-preview')
        
        if not os.path.exists(image_path):
            return {"error": "Image file not found."}

        img = Image.open(image_path)

        # Gemini 3 Pro Prompting: Be specific and demand structured JSON.
        prompt = """
        You are a Senior Field Service Engineer Agent.
        Analyze this image of industrial equipment.
        
        Return a strict JSON object with these fields:
        1. "part_name": The likely technical name of the equipment.
        2. "severity": "Low", "Medium", or "Critical".
        3. "damage_analysis": A deep reasoning explanation of the visual defects (rust, fractures, wear).
        4. "action": The recommended repair step (e.g., "Replace Seal", "Lubricate").

        Do not include markdown formatting, just the raw JSON.
        """

        print(f"🧠 [Gemini 3 Pro] Analyzing {image_path} with Deep Reasoning...")
        
        # Generate content
        response = model.generate_content([prompt, img])
        
        # Parse the JSON response (Gemini 3 is excellent at strict JSON)
        clean_json = response.text.strip().replace('```json', '').replace('```', '')
        return json.loads(clean_json)

    except Exception as e:
        print(f"❌ API Error: {e}")
        return {
            "part_name": "Unknown", 
            "severity": "Manual Review Required", 
            "action": "Escalate to Human"
        }
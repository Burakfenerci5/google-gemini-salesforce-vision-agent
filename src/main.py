import os
from src.salesforce.work_order import WorkOrderManager
from src.vision.diagnose import analyze_image_with_gemini3

def run_agentic_workflow():
    # 1. Setup
    sf = WorkOrderManager()
    wo_id = "WO-2026-885"
    
    # 2. Simulate fetching the image
    image_path = sf.get_image_attachment(wo_id)
    
    # Create a dummy image for the demo if it doesn't exist
    if not os.path.exists(image_path):
        from PIL import Image
        img = Image.new('RGB', (100, 100), color = 'red')
        img.save(image_path)
    
    # 3. Visual Reasoning (Gemini 3 Pro)
    if os.getenv("GOOGLE_API_KEY"):
        diagnosis = analyze_image_with_gemini3(image_path)
        
        # 4. Update Salesforce
        sf.update_work_order(wo_id, diagnosis)
    else:
        print("⚠️ GOOGLE_API_KEY not set. Skipping AI call.")
        print("   (Please export your key to run the live demo)")

    # Cleanup
    if os.path.exists(image_path):
        os.remove(image_path)

if __name__ == "__main__":
    run_agentic_workflow()
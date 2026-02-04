import time

class WorkOrderManager:
    """
    Simulates interactions with Salesforce Field Service (SFS).
    """
    def get_image_attachment(self, work_order_id):
        print(f"📸 [Salesforce] Fetching image attachment for Work Order {work_order_id}...")
        # In a real app, this would use simple-salesforce to get the ContentVersion
        return "equipment_damage.jpg"

    def update_work_order(self, work_order_id, diagnosis_json):
        """
        Updates the record with the structured AI output.
        """
        print(f"\n✅ [Salesforce] Updating Work Order {work_order_id}...")
        print(f"   -> Part Identified: {diagnosis_json.get('part_name')}")
        print(f"   -> Damage Severity: {diagnosis_json.get('severity')}")
        print(f"   -> Recommended Action: {diagnosis_json.get('action')}")
        time.sleep(0.5)
        print("   -> (Record Saved Successfully)")
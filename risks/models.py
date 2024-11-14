import uuid
import json
from datetime import datetime
from RiskManagement.settings import RISK_FILE_PATH


class Risk:
    def __init__(self, title, description, state):
        self.id = str(uuid.uuid4())
        self.state = state
        self.title = title
        self.description = description
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def to_dict(self):
        return {
            'id': self.id,
            'state': self.state,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


def load_risks():
    try:
        with open(RISK_FILE_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_risks(risks):
    with open(RISK_FILE_PATH, 'w') as f:
        json.dump(risks, f, indent=4)

def get_all_risks():
    return load_risks()

def get_risk_by_id(risk_id):
    risks = load_risks()
    for risk in risks:
        if risk['id'] == risk_id:
            return risk
    return None

def check_and_create_risk(title, description, state):
    risks = load_risks()
    
    for risk in risks:
        if risk['title'] == title and risk['description'] == description:
            if risk['state'] == state:
                return {"message":f"Risk state is same(no changes found)", "risk":risk}
            data = {"message":f"Risk updated successfully {risk['state']} --> {state}", "risk":risk}
            risk['state'] = state
            risk['updated_at'] = datetime.now().isoformat()
            save_risks(risks)
            return data
    
    try:
        new_risk = Risk(title, description, state)
        risks.append(new_risk.to_dict())
        save_risks(risks)
        return {"message":"Risk created successfully.", "risk":new_risk.to_dict()}
    except Exception as err:
        return {"error": str(err)}

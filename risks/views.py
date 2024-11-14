from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import get_all_risks, get_risk_by_id, check_and_create_risk

@api_view(['GET', 'POST'])
@csrf_exempt
def get_or_create_risk_view(request):
    if request.method == 'GET':
        risks = get_all_risks()
        return JsonResponse({'risks_count':len(risks), 'risks': risks})
    elif request.method == 'POST':
        try:
            RISK_STATES = ['open', 'closed', 'accepted', 'investigating']
            data = json.loads(request.body)
            title = data.get('title', None)
            description = data.get('description', None)
            state = data.get('state', None)
            if state not in RISK_STATES:
                return JsonResponse({"error":f"Invalid risk state {state}. Choose from: {', '.join(RISK_STATES)}"}, status=400)
            if title and description and state:
                risk = check_and_create_risk(title, description, state)
                if 'error' in risk:
                    return JsonResponse(risk, status=400)
                return JsonResponse(risk, status=201)
            else:
                return JsonResponse({'error': 'Title, description, and state are required'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

@api_view(['GET'])
def get_risk(request, id):
    risk = get_risk_by_id(id)
    if risk:
        return JsonResponse(risk)
    else:
        return JsonResponse({'error': 'Risk not found'}, status=404)


import os
import pandas as pd
import joblib
from django.shortcuts import render
from django.http import JsonResponse

# Define the path to the model
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'xgb_model.pkl')

# Load the model
model = joblib.load(MODEL_PATH)

# View for prediction
def index(request):
    if request.method == 'POST':
        # Collect form data
        inputs = {
            'FlgActCN_T12': int(request.POST.get('FlgActCN_T12', 0)),
            'FlgActCN_T11': int(request.POST.get('FlgActCN_T11', 0)),
            'FlgActCN_T10': int(request.POST.get('FlgActCN_T10', 0)),
            'FlgActCN_T09': int(request.POST.get('FlgActCN_T09', 0)),
            'FlgActCN_T08': int(request.POST.get('FlgActCN_T08', 0)),
            'FlgActCN_T07': int(request.POST.get('FlgActCN_T07', 0)),
            'FlgActCN_T06': int(request.POST.get('FlgActCN_T06', 0)),
            'FlgActCN_T05': int(request.POST.get('FlgActCN_T05', 0)),
            'FlgActCN_T04': int(request.POST.get('FlgActCN_T04', 0)),
            'FlgActCN_T03': int(request.POST.get('FlgActCN_T03', 0)),
            'FlgActCN_T02': int(request.POST.get('FlgActCN_T02', 0)),
            'FlgActCN_T01': int(request.POST.get('FlgActCN_T01', 0)),
        }

        # Create a DataFrame for prediction
        input_df = pd.DataFrame([inputs])

        # Predict using the model
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0, 1]

        # Return response
        return JsonResponse({
            'prediction': 'Realizará compras en cuotas' if prediction == 1 else 'No realizará compras en cuotas',
            'probability': f'{probability:.2f}'
        })

    return render(request, 'index.html')

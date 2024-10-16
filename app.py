import gradio as gr
import pandas as pd
import joblib

# Load the saved pipeline
model_pipeline = joblib.load('model_pipeline.pkl')

def predict_churn(credit_score, gender, tenure, balance, age, products_number, credit_card, active_member, estimated_salary, country):
    # Create a DataFrame from the inputs
    sample_data = pd.DataFrame({
        'credit_score': [credit_score],
        'gender': [gender],
        'tenure': [tenure],
        'balance': [balance],
        'age': [age],
        'products_number': [products_number],
        'credit_card': [credit_card],
        'active_member': [active_member],
        'estimated_salary': [estimated_salary],
        'country': [country]
    })

    # Make a prediction
    prediction = model_pipeline.predict(sample_data)

    # Return the prediction
    return f"The prediction for churn is: {prediction[0]}"

# Create the Gradio interface
iface = gr.Interface(
    fn=predict_churn,
    inputs=[
        gr.Slider(300, 850, value=502, label="Credit Score"),
        gr.Dropdown(["Male", "Female"], label="Gender"),
        gr.Slider(0, 100, value=42, label="Tenure"),
        gr.Number(label="Balance"),
        gr.Slider(18, 100, value=42, label="Age"),
        gr.Slider(1, 10, value=3, label="Number of Products"),
        gr.Dropdown(["Yes", "No"], label="Has Credit Card"),
        gr.Dropdown(["Yes", "No"], label="Is Active Member"),
        gr.Number(label="Estimated Salary"),
        gr.Dropdown(["France", "Spain", "Germany", "Italy", "Portugal"], label="Country"),
    ],
    outputs="text",
    title="Churn Prediction",
    description="Enter the customer's information to predict churn."
)

# Launch the Gradio app
iface.launch(share=True)

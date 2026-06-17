import openai

openai.api_key = "YOUR_API_KEY"

def summarize_alert(alert_text):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"Summarize this security alert in simple terms:\n\n{alert_text}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

alert = "Multiple failed login attempts detected from IP 192.168.1.100."
print(summarize_alert(alert))

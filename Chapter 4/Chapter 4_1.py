import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def analyze_siem_alert(alert_text):
    prompt = (
        "You are a cybersecurity analyst. Summarize the following SIEM alert "
        "with potential threat impact, suggested severity, and recommended actions:\n\n"
        f"Alert: {alert_text}\n\nSummary:"
    )
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150,
        temperature=0.3,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

# Sample SIEM alert text
alert = """
Multiple failed login attempts detected from IP 192.168.1.100 targeting admin accounts between 2am-3am.
"""

summary = analyze_siem_alert(alert)
print("AI-Generated Alert Summary:\n", summary)

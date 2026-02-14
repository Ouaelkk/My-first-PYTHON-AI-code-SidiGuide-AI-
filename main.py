import os
from groq import Groq

client = Groq(api_key="GROQ_API_KEY")

def calculate_weighted_average(gen_avg, math_grade, stream):
    """Calculates the 2026 style weighted average for Science/Tech branches."""
    if stream in ["Math", "Technique Math", "Sciences Exp"]:
        return (gen_avg * 2 + math_grade) / 3
    return gen_avg

def get_ai_advice(grades_data, preferences):
    prompt = f"""
    User Data:
    - BAC General Average: {grades_data['gen_avg']}
    - Math Grade: {grades_data['math']}
    - Physics Grade: {grades_data['phys']}
    - Weighted Average (Math/CS): {grades_data['weighted']:.2f}
    - Interests: {preferences}

    Instructions:
    1. Based on Algerian 2025/2026 thresholds (e.g., Medicine ~16.5+, ESI/CS ~17+, USTHB ~12-14), suggest 3 specific universities in Algeria.
    2. Explain if they should consider 'Campus France' or 'Erasmus' based on their {grades_data['gen_avg']} average.
    3. Respond in a mix of French and Algerian Darja. Be encouraging!
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are 'Sidi Guide', the expert on Algerian university orientation."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

# --- MAIN PROGRAM ---
print("--- 🎓 BIENVENUE TO SIDI GUIDE 2026 ---")

# 1. Gather Info
stream = input("Ton Filière (Math/Tech/Science): ")
moyenne = float(input("Ta Moyenne Générale: "))
math_note = float(input("Note de Math: "))
phys_note = float(input("Note de Physique: "))
aims = input("What do you love? (e.g., AI, Medicine, Civil Engineering): ")

# 2. Logic Step
weighted = calculate_weighted_average(moyenne, math_note, stream)

# 3. AI Step
print("\n🔄 Sidi Guide is analyzing your chances...")
advice = get_ai_advice({
    "gen_avg": moyenne, 
    "math": math_note, 
    "phys": phys_note, 
    "weighted": weighted
}, aims)

print("\n" + advice)

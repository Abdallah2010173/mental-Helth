from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import re

app = Flask(__name__)
CORS(app)  # تمكين الـ CORS لجميع النهايات

# قائمة الكلمات المفتاحية والردود
response_dict = {
    'stress': [
        "It sounds like you're feeling stressed. Here are a few tips: try deep breathing exercises, take regular breaks, and consider speaking to a mental health professional.",
        "Stress can be overwhelming. Have you tried mindfulness or relaxation techniques? Sometimes talking things out can also help."
    ],
    'anxiety': [
        "Anxiety can be tough. Practicing mindfulness and staying active might help. If it becomes overwhelming, talking to a therapist could be useful.",
        "Feeling anxious is challenging. Have you tried keeping a journal or practicing relaxation techniques? These can sometimes help manage anxiety."
    ],
    'depression': [
        "If you're feeling depressed, reaching out to a mental health professional can provide you with support and treatment options.",
        "Depression can be difficult to handle alone. Talking to a counselor or therapist might offer the help and guidance you need."
    ],
    'pulling': [
        "If you're struggling with hair-pulling or similar behaviors, consider reaching out to a mental health professional for support and strategies.",
        "Managing hair-pulling involves understanding its triggers. Speaking with a counselor can provide you with strategies to manage and reduce this behavior."
    ]
}

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()
    print(f"Received message: {user_message}")  # تسجيل الرسالة
    response = suggest_solution(user_message)
    return jsonify({'response': response})

def suggest_solution(user_message):
    # تحقق من الكلمات المفتاحية في رسالة المستخدم
    for keyword in response_dict:
        if re.search(r'\b' + re.escape(keyword) + r'\b', user_message):
            # إرجاع رد عشوائي من القائمة
            return random.choice(response_dict[keyword])
    
    # الرد الافتراضي إذا لم يفهم الرسالة
    return "Sorry, I didn't understand that. Could you please provide more details?"

if __name__ == '__main__':
    app.run(debug=True)

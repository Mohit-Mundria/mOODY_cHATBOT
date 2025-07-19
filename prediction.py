from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import joblib
import numpy as np
import random 
import requests
import json

emotion_dict={
    0:'sad',
    1:'joy',
    2:'love',
    3: 'anger',
    4:'fear',
    5:'surprise'
}


model=load_model(r'D:\End to end project\Moody_Chatbot\mOODY_cHATBOT\emotion_classifier.h5')
vectorizer=joblib.load(r'D:\End to end project\Moody_Chatbot\mOODY_cHATBOT\emotion_tokenizer.pkl')

    
    

emotion_prompts = {
    "sad": [
        "User feels sad. Write a response that validates their feelings and offers comfort.",
        "Respond like a friend who genuinely cares about their sadness. Ask gently how you can support.",
        "The user is feeling down. Share a soft and supportive message to help them feel less alone.",
        "User is heartbroken. Give an empathetic, warm reply, maybe share something positive.",
        "Acknowledge their pain, don't try to fix it. Just listen and be present.",
        "Offer virtual support, use kind and soft words. Help the user feel understood.",
        "Ask what triggered the sadness without being too direct. Let the user open up.",
        "Use comforting words and short relatable advice, like a friend.",
        "Share a short quote or story about hope during tough times.",
        "Use friendly and non-judgmental tone. Reassure that it’s okay to feel this way.",
        "Invite the user to share more about what’s making them sad.",
        "Tell them it’s okay to cry and offer to sit with them virtually.",
        "Use a gentle tone to check if the user needs someone to talk to.",
        "Send comforting thoughts and tell them they’re not alone.",
        "Validate their feelings without offering solutions immediately.",
        "Ask if they want to talk about it, or if they’d prefer a distraction.",
        "Say something uplifting, but not overly cheerful.",
        "Offer to talk or just be there for them in silence.",
        "Start with: 'Hey, I noticed you're feeling a bit low. Want to talk about it?'",
        "Let the user know that this feeling will pass, but you're here now."
    ],
    
    "joy": [
        "The user is feeling happy. Celebrate their joy and ask what’s making them smile.",
        "Respond excitedly and share their happiness. Be cheerful!",
        "Say something that adds to their happiness, like a funny or positive comment.",
        "Ask them what’s the best part of their day so far.",
        "Tell them it’s great to see them so happy and ask what's going well.",
        "Show genuine excitement. Use emojis or exclamation marks if appropriate.",
        "Ask if they want to share their good news!",
        "Cheer them on and tell them they deserve the joy.",
        "Say something like: 'That’s awesome! Tell me more!'",
        "Add to the positivity with a quick uplifting quote or fun fact.",
        "Ask what made them smile today.",
        "React like a friend who’s thrilled for them.",
        "Encourage them to spread the happiness by doing something kind.",
        "Say: 'That sounds amazing! What else has been going great lately?'",
        "Reflect their energy. Keep the tone light and bright.",
        "Ask if something special happened today.",
        "Invite them to tell you what’s making them feel so good.",
        "Compliment their vibe. Positivity is contagious.",
        "Celebrate their mood and suggest keeping the streak going.",
        "Encourage them to keep doing whatever made them feel so joyful."
    ],
    
    "love": [
        "User feels love. Respond with warmth and ask what sparked that feeling.",
        "Acknowledge their loving vibe and share a positive message back.",
        "Be romantic or poetic in tone — even playful — but keep it gentle.",
        "Say: 'Sounds like your heart is full! Tell me more about it.'",
        "Ask if they’re in love or just feeling the beauty of life today.",
        "Write in the tone of a supportive and affectionate friend.",
        "Say something like: 'Love makes the world better. What's bringing that out in you today?'",
        "Respond like someone who appreciates deep feelings.",
        "Be curious but kind: 'Who or what’s making your heart smile today?'",
        "Use words of admiration and emotional support.",
        "Compliment their sensitivity and openness.",
        "Suggest they share a story or memory about that love.",
        "Say: 'Wow, you sound so connected right now. That's beautiful.'",
        "Invite them to talk about what makes them feel loved or who they love.",
        "Encourage them to express this feeling outward to someone they care for.",
        "Be poetic: ‘Love is powerful. Let it flow.’",
        "Say something gentle like: 'Love suits you well today 🙂'",
        "Ask how you can celebrate this emotion with them.",
        "Support their feeling with curiosity, not judgment.",
        "Offer a moment of reflection or a prompt like: 'What does love mean to you right now?'"
    ],
    
    "anger": [
        "The user is feeling angry. Help them calm down, validate them, don’t escalate.",
        "Respond like a neutral friend. Let them vent safely.",
        "Acknowledge their frustration and ask what’s bothering them.",
        "Avoid judgment. Say something like: 'That sounds really upsetting. Want to talk more?'",
        "Stay calm in tone. Offer space to share more.",
        "Ask if they want to blow off steam or need help processing.",
        "Say: 'It’s okay to feel that way. You’re not alone.'",
        "Invite them to express their anger more — without consequences.",
        "Offer grounding questions like: 'What do you think triggered that?'",
        "Validate their anger, but steer away from blame.",
        "Say: 'Anger shows something matters to you. Want to explore it?'",
        "Help them explore what resolution might look like.",
        "Use gentle, slow-paced responses. Avoid being too chipper.",
        "Check if they want to be distracted or continue discussing the cause.",
        "Avoid solutions unless they ask. Just listen for now.",
        "Say: 'That must’ve been tough. I hear you.'",
        "Ask: 'Would sharing the whole story help you feel lighter?'",
        "Encourage safe emotional expression.",
        "Don’t dismiss their feelings. Reflect what they say in a calm tone.",
        "Let them know you’re not judging and you're here to listen."
    ],
    
    "fear": [
        "User feels scared or anxious. Be calm and comforting. Ask what’s making them afraid.",
        "Say: 'It’s okay to be scared. Want to talk about it?'",
        "Respond gently and help them ground themselves.",
        "Use calming words. Reassure them that they’re safe here.",
        "Invite them to breathe and talk through the fear.",
        "Offer to be a calm voice in the chaos. Just listen.",
        "Say: 'Would it help to talk about what’s worrying you?'",
        "Don’t push too hard. Let them open up slowly.",
        "Offer reassurance and emotional safety.",
        "Acknowledge their fear without trying to fix it immediately.",
        "Say: 'I’m here. You’re not alone in this.'",
        "Remind them they’re stronger than they think.",
        "Ask: 'What part of this is the hardest right now?'",
        "Offer a distraction if they seem overwhelmed.",
        "Use a grounded tone: 'Let’s take this one step at a time.'",
        "Say: 'Fear is normal. Let’s face it together.'",
        "Avoid shock or surprise. Stay steady.",
        "Use reassuring words like 'safe', 'okay', 'here for you'.",
        "Ask if they want to talk about a plan or just vent.",
        "Support them emotionally without questioning their fears."
    ],
    
    "surprise": [
        "User feels surprised. Respond with curiosity and ask what happened.",
        "Be playful or astonished — mirror their emotion.",
        "Say: 'No way! What just happened?'",
        "Ask if it’s a good surprise or a not-so-good one.",
        "Reflect their shock with emojis or exclamatory phrases.",
        "Be curious: 'Tell me more, I’m all ears!'",
        "Say: 'Whoa, didn’t see that coming, huh?'",
        "Encourage storytelling: 'Start from the beginning…'",
        "Use expressions like 'That’s wild!' or 'What a twist!'",
        "Ask how they’re feeling now after the surprise.",
        "Say: 'Was it unexpected in a good way?'",
        "Let them lead the conversation — surprises make great stories.",
        "Say: 'I love a good surprise. Want to tell me all about it?'",
        "Use excitement to keep the mood going.",
        "Offer your thoughts once they share more about the surprise.",
        "Use humor or wit depending on tone.",
        "Be lively: 'Okay now I’m really curious!'",
        "Ask: 'What was your reaction when it happened?'",
        "Say: 'That must’ve been a moment to remember!'",
        "React naturally: 'Wait, what? Really?'"
    ]
}

    
    
def predict(text):
    text_vectorized=vectorizer.texts_to_sequences([text])
    padded = pad_sequences(text_vectorized, maxlen=200)
    padded = np.array(padded)
    prediction=model.predict(padded)
    predicted_class=prediction.argmax(axis=1)[0]
    return predicted_class

input_text=input("You:   ")
emotion=predict(input_text)
emotion_pred=emotion_dict[emotion]
print(f"Predicted Emotion: {emotion_pred}")



def get_response(input_text,emotion_pred):
    
    prompt = random.choice(emotion_prompts[emotion_pred])
    response = requests.post(
         'http://localhost:11434/api/generate',
         json={
            'model': 'llama3.2:latest',
            'prompt': f"{prompt}\nUser said: '{input_text}'\nGenerate an empathetic, contextual response.",
            'stream': False
        }
    )
    return response.json()['response']


print(f"chatbot_response : {get_response(input_text, emotion_pred)}")
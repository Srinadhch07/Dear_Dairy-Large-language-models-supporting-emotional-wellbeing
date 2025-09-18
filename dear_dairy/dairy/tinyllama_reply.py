
# import ollama

# def generate_tinyllama_reply(text):

#     prompt = f"""
#     You are a mental and wellbeing support AI assistant. Your primary function is to first, analyze the emotion of the user's text and provide a single-word emotion label. Then, based on that emotion, provide a supportive and empathetic response that focuses on the user's mental health and betterment.

#     ### Rules:
#     1.  **Emotion Detection:** Immediately provide a single-word emotion label. This word must be the very first word of your response.
#     2.  **Emotional Analysis:** Briefly explain *why* that emotion was detected, referencing keywords from the user's text.
#     3.  **Supportive Response:** Based on the detected emotion, provide a helpful and empathetic reply.
#         * For positive emotions (e.g., Happy, Joyful), your response should reinforce the positive feelings, suggest ways to cherish the moment, and encourage a continued focus on wellbeing.
#         * For negative emotions (e.g., Sadness, Annoyance), your response should be empathetic, offer a sense of validation, and provide gentle, helpful suggestions or a listening ear.
#         * The entire response should be in a friendly, conversational tone and should not sound like a generic chatbot.

#     ### Example Interaction:

#     **User Text:** "Dear Dairy, Today I felt so much happy and enjoyed a lot with my friends"

#     **AI Response:** Happy. Your text conveys a clear sense of joy, especially with phrases like "felt so much happy" and "enjoyed a lot." It's wonderful that you had such a positive experience! Cherishing these moments is a great way to boost your spirits. Remember to hold onto this feeling and perhaps think about what made today so special. I'm here if you want to talk more about it.

#     ---

#     **Now, apply these rules to the following text:**

#     {text}
#     """

#     try:
#         response = ollama.chat(
#             model="gemma:2b",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         print(f'AI reply: ',response['message']['content'])
#         return response['message']['content']
#     except Exception as e:
#         return f"(Gemma Error: {str(e)})"
    
# text  = """
# Dear Diary,

# I'm not sure how to start this, but today was just one of those days. You know, the kind where nothing goes to plan. I woke up to my alarm not going off and immediately felt like I was playing catch-up. I rushed out the door without my coffee and got stuck in the worst traffic I've seen all year. It felt like every little thing was a roadblock, a sign that the universe was just not on my side.

# I spent most of the afternoon trying to fix a small problem at work that just kept getting bigger. I ended up staying late, even though I had plans to meet up with Sarah. I felt so bad canceling on her, but I was just exhausted. By the time I got home, all I wanted to do was curl up on the couch and watch something mindless.

# It's strange how a day can feel so heavy, like a weight you just can't shake. I'm trying to remember that tomorrow is a new day and maybe things will look different then. I just hope I can leave this feeling behind me tonight.

# Until tomorrow,
# SRINADH
# """

# text2 ="""
# Dear Diary,

# I'm sitting here with a cup of tea, and I finally have a moment to myself. Today felt like a whirlwind, but in the best way. My project at work finally launched, and the initial feedback has been incredible. I was so nervous about it, but seeing all the positive comments made all those late nights and stressful moments feel worth it.

# After work, I decided to take a spontaneous walk in the park. The sun was just starting to set, casting this beautiful golden light through the trees. I saw a group of kids playing soccer, their laughter echoing across the field. It was such a simple, perfect moment that made me feel so grateful for everything.

# I feel a sense of calm and accomplishment that I haven't felt in a while. It's a reminder that even when things are tough, there's always something beautiful just around the corner. I'm going to bed tonight with a full heart and a peaceful mind.

# All the best,
# srinadh
# """


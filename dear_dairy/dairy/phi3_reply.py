# # phi3_reply.py
# import ollama

# def generate_phi3_reply(text, emotion):
 
#     prompt = f"""
#     You are an empathetic assistant.
#     The user feels {emotion}.
#     Respond in a kind, concise, and understanding way.
#     User message: "{text}"
#     """

#     try:
#         response = ollama.chat(
#             model="phi3",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response['message']['content']
#     except Exception as e:
#         return f"(Phi-3 Error: {str(e)})"

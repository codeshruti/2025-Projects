import openai
import os
import pandas

# add OpenAI key
def generate_movie_scene(characters, setting, plot, genre):
    """
    Generates a movie script scene based on characters, setting, plot, and genre.
    """
    prompt = f"""
    You are a professional screenwriter. Write a dynamic and engaging movie scene.
    Characters: {characters}
    Setting: {setting}
    Plot: {plot}
    Genre: {genre}
    
    Begin with a descriptive opening. Include dialogue, actions, and emotions. Make it vivid and true to the genre.
    """
    
    try:
        response = openai.chats.completion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert scriptwriter."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.8
        )
        script = response['choices'][0]['message']['content']
        return script
    except Exception as e:
        return f"Error: {str(e)}"

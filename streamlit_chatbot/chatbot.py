import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configure Gemini API
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# Initialize chat history
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

# Gemini response with persona
def get_gemini_response(prompt):
    system_prompt = """
You are a friendly movie expert helping users find films that match their mood or genre.

When the user tells you how they’re feeling or what genre they like:

🎬 Recommend exactly 3 movies.  
Each should include:
- Movie title and year, followed by 2–3 fitting emojis.
- A short and compact description (max 2 sentences).
- One or two sentence vibe (e.g., “Dark and intense” or “Warm and feel-good”).

Keep it casual, fun, and concise — no more than 30 words per movie.  
Don't number the list — just break them with spacing.  
End your response with a fun follow-up question, to see if maybe you
 can recommend other movies, more suited to their liking. The question should
 be related to the previous genre chosen.
"""
    full_prompt = f"{system_prompt.strip()}\n\nUser: {prompt}\nAssistant:"
    response = model.generate_content(full_prompt)
    return response.text

# Main app
def main():
    st.title("🎬What to Watch?")


    initialize_session_state()

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Mood and Genre selectors
    col1, col2 = st.columns(2)

    with col1:
        mood = st.radio(
            "How are you feeling?",
            ["Happy", "Sad", "nostalgic", "Tired", "Bored", "Romantic"],
            key="mood"
        )

    with col2:
        genre = st.multiselect(
            "Pick your genre/s:",
            ["Any Genre", "Drama", "Adventure", "Thriller", "Fantasy", "Mystery", "Suspense", "Comedy", "Horror", "Sci-Fi", "Action", "Musical", "Documentary", "Romance", "Rom-com", "Slice of Life", "Coming-of-Age"],
            key="genre"
        )

    # Button to get initial recommendation
    if st.button("🎥 Get Recommendation"):
        genre_text = ", ".join(genre) if genre else "any genre"
        user_input = f"I'm feeling {mood} and want a {genre_text} movie."

        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        response = get_gemini_response(user_input)

        with st.chat_message("assistant"):
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

    # Text input for follow-up questions or replies to bot
    if prompt := st.chat_input("Anything else to add?"):
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = get_gemini_response(prompt)

        with st.chat_message("assistant"):
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})




# List of movie trivia/fun facts
movie_trivia = [
    "Did you know? The famous line 'Here's looking at you, kid' from Casablanca was improvised by Humphrey Bogart.",
    "Fun fact: The sound of a lightsaber in Star Wars was created by mixing the hum of a film projector and the sound of a broken television.",
    "The Lion King's opening scene was inspired by the views of the African savannah that the animators saw on a plane trip.",
    "In The Matrix, the green tint was added to the scenes that happened in the Matrix to give the film an otherworldly look.",
    "The Shining's iconic 'Here's Johnny!' scene was improvised by Jack Nicholson. It wasn’t in the original script!"
]








st.markdown(
    """
    <style>
    .stApp {
        background-color: #F5F5DC;
    }
    </style>
    """,
    unsafe_allow_html=True
)







if __name__ == "__main__":
    main()


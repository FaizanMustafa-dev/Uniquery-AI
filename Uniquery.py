import streamlit as st
import requests
import tkinter as tk
from tkinter import messagebox
import requests
import re
import json
# Streamlit Page Configuration
st.set_page_config(
    page_title="Uniquery AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API Details (replace with actual API key)
API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = "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"

# Custom CSS for Sidebar and Main Content
st.markdown("""
    <style>
    .sidebar {
        background-color: #000000;
        height: 100%;
        padding: 0;
        margin: 0;
    }

    .sidebar-option {
        font-size: 20px;
        color: #ffffff;
        padding: 20px;
        text-align: left;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .sidebar-option:hover {
        background-color: #1a1a1a;
        border-radius: 5px;
    }

    .sidebar-option:active {
        background-color: #333333;
    }

    .css-1d391kg, .css-1ixjh6v {
        border: none !important;
        outline: none !important;
    }

    .main-container {
        background-color: #181818;
        color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        margin: 20px;
    }

    .chat-input {
        display: flex;
        align-items: center;
        margin-top: 20px;
    }

    .chat-input input {
        flex: 1;
        padding: 10px;
        border: none;
        border-radius: 5px;
        margin-right: 10px;
        font-size: 16px;
    }

    .chat-input button {
        padding: 10px 20px;
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .chat-input button:hover {
        background-color: #0056b3;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("<div class='sidebar'>", unsafe_allow_html=True)
    if st.button("Home", key="Home"):
        st.session_state.page = "Home"
    if st.button("QueryBot", key="QueryBot"):
        st.session_state.page = "QueryBot"
    if st.button("StudyBuddy", key="StudyBuddy"):
        st.session_state.page = "StudyBuddy"
    if st.button("Trainify", key="Trainify"):
        st.session_state.page = "Trainify"
    if st.button("DomainGuru", key="DomainGuru"):
        st.session_state.page = "DomainGuru"
    if st.button("QuizMaster", key="QuizMaster"):
        st.session_state.page = "QuizMaster"
    if st.button("About Developers", key="About Developers"):
        st.session_state.page = "About Developers"
    st.markdown("</div>", unsafe_allow_html=True)

# Function to interact with the Groq API for quiz generation
def chat_with_groq(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "model": "llama3-8b-8192",  # Replace with the correct model
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code}, {response.text}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


def query_bot_chat(user_message):
    """Send a user query to the Groq API and get a response."""
    api_url = "https://api.groq.com/openai/v1/chat/completions"  # Replace with actual API URL
    api_key = "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"  # Replace with actual API key

    # Construct the prompt with conditional response
    user_message_with_instruction = (
        f"You are a QueryBot specialized in answering study-related queries. "
        f"Answer the following query if it is related to studies:\n\n"
        f"{user_message}\n\n"
        "Strict Instruction: If this query is not related to studies (like who is ---,where is --,how to---), "
        "respond only with the following text and nothing else:\n"
        "'I am a QueryBot designed to assist with study-related queries only. Kindly ask questions related to studies or learning.'"
    )

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": user_message_with_instruction}
        ]
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            response_data = json.loads(response.text)
            bot_message = response_data["choices"][0]["message"]["content"]
            return bot_message.strip()
        else:
            return f"Error: Unable to connect to API (Status code: {response.status_code})"
    except Exception as e:
        return f"Error: Failed to fetch response due to {e}"

   
# Default Page Setting
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Page Content Logic
if st.session_state.page == "Home":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Welcome to Uniquery AI! 🤖</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p class='subtitle'>
    Explore the world of AI-powered solutions. Our platform includes various tools designed to make learning, querying, and exploring domains easy and engaging. Use the navigation bar to access:
    </p>
    <ul style="line-height: 1.8; font-size: 18px; margin-left: 20px;">
        <li><strong>QueryBot:</strong> Your intelligent assistant for any question.</li>
        <li><strong>StudyBuddy:</strong> Generate study materials for any topic.</li>
        <li><strong>Trainify:</strong> Customize chatbot experiences to suit your preferences.</li>
        <li><strong>DomainGuru:</strong> Get in-depth insights on specialized topics.</li>
        <li><strong>QuizMaster:</strong> Create and attempt quizzes on any topic.</li>
        <li><strong>About Developers:</strong> Learn about the team behind Uniquery AI.</li>
    </ul>
    <p class='subtitle'>
    Begin by selecting a feature from the sidebar and let Uniquery AI assist you on your journey!
    </p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == "QueryBot":
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)
        st.markdown("<div class='title'>🤖 AI Chatbot</div>", unsafe_allow_html=True)
        st.markdown("<div class='subtitle'>Your personal assistant, powered by the Groq API.</div>", unsafe_allow_html=True)

        # Chat history
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Chat interface
        with st.form("chat_form"):
            user_message = st.text_input("Type your message here:", placeholder="Ask me anything...")
            submitted = st.form_submit_button("Send")

            if submitted and user_message:
                # Display user message
                st.session_state.chat_history.append(("user", user_message))

                # Get chatbot response
                bot_response = chat_with_groq(user_message)

                # Display bot response
                st.session_state.chat_history.append(("bot", bot_response))

        # Display chat history
        for role, message in st.session_state.chat_history:
            if role == "user":
                st.markdown(f"<div class='chat-bubble-user'>{message}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='chat-bubble-bot'>{message}</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
def fetch_questions_from_api(api_url, api_key, num_questions, topic):
    """Fetch questions from the API based on user input."""
    prompt = (
        f"Generate {num_questions} multiple-choice questions on the topic '{topic}'. "
        "Each question should include 4 options, specify the correct option, and return the data in JSON format. Format it as follows:\n"
        "[\n"
        "    {\n"
        '        "text": "Question text",\n'
        '        "options": ["Option1", "Option2", "Option3", "Option4"],\n'
        '        "correct_option": CorrectOptionIndex\n'
        "    }\n"
        "]"
    )

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            content = extract_questions_from_response(response.text)
            if content:
                return content
            else:
                st.error("Failed to extract valid questions from API response.")
        else:
            st.error(f"API Error: {response.status_code}")
    except Exception as e:
        st.error(f"Failed to fetch questions: {e}")

    return []


def extract_questions_from_response(response_text):
    """Extract valid questions from the API response."""
    try:
        response_data = json.loads(response_text)
        message_content = response_data["choices"][0]["message"]["content"]
        match = re.search(r'\[\s*(\{.*?\})\s*\]', message_content, re.DOTALL)

        if match:
            questions_data = match.group(0)
            questions = json.loads(questions_data)
            return questions
        else:
            return None
    except (json.JSONDecodeError, KeyError) as e:
        st.error(f"Error parsing JSON: {e}")
        return None


def quiz_master():
    st.write("Generate quizzes based on your chosen topic.")

    # Input fields for number of questions and topic
    num_questions = st.number_input(
        "How many questions do you want?", min_value=1, step=1, value=1
    )
    topic = st.text_input("Enter a topic for the quiz:")

    # API details
    api_url = "https://api.groq.com/openai/v1/chat/completions"  # Replace with correct API URL
    api_key = "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"  # Replace with your actual API key

    # State to manage questions and answers
    if "questions" not in st.session_state:
        st.session_state.questions = []
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    # Fetch questions from API
    if st.button("Make Quiz"):
        if not topic.strip():
            st.error("Please enter a valid topic.")
        else:
            questions = fetch_questions_from_api(api_url, api_key, num_questions, topic)
            if questions:
                st.session_state.questions = questions
                st.session_state.quiz_started = True
                st.session_state.answers = {}

    # Start the quiz if questions are available
    if st.session_state.quiz_started and st.session_state.questions:
        start_quiz()


def start_quiz():
    """Display the quiz questions and collect answers."""
    st.header("Quiz Time!")
    questions = st.session_state.questions
    answers = st.session_state.answers

    for idx, question in enumerate(questions):
        st.subheader(f"Question {idx + 1}: {question['text']}")
        selected_option = st.radio(
            "Choose an option:",
            question["options"],
            key=f"question_{idx}"
        )
        answers[idx] = selected_option

    if st.button("Submit Quiz"):
        calculate_score()


def calculate_score():
    """Calculate and display the final score."""
    questions = st.session_state.questions
    answers = st.session_state.answers

    score = 0
    total = len(questions)

    for idx, question in enumerate(questions):
        correct_option = question["options"][question["correct_option"]]
        if answers.get(idx) == correct_option:
            score += 1

    # Clear questions from UI
    st.session_state.quiz_started = False
    st.session_state.questions = []

    # Show final score
    st.subheader("Quiz Completed!")
    st.write(f"Your final score: {score} / {total}")
    st.success("Thank you for participating!")


# Initialize session state variables
if "page" not in st.session_state:
    st.session_state.page = "QuizMaster"
if "questions" not in st.session_state:
    st.session_state.questions = []
if "responses" not in st.session_state:
    st.session_state.responses = []

# Page logic for QuizMaster 
if st.session_state.page == "QuizMaster":
        quiz_master()
    
    

elif st.session_state.page == "DomainGuru":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("DomainGuru 🌐")
    st.write("Ask DomainGuru any question related to your domain of interest. It will provide expert-level insights!")

    # Input Form
    with st.form("domain_form"):
        domain_query = st.text_input("Enter your domain-related query:", placeholder="e.g., Explain quantum entanglement, What is the impact of AI in healthcare?")
        submitted = st.form_submit_button("Submit Query")

        if submitted and domain_query:
            with st.spinner("Processing your query..."):
                # Use the chat_with_groq function to get the response
                response = chat_with_groq(domain_query)
                if response.startswith("Error"):
                    st.error(response)
                else:
                    st.success("Here’s what I found:")
                    st.markdown(response)

    st.markdown("</div>", unsafe_allow_html=True)
    
elif st.session_state.page == "Trainify":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("Trainify 🛠️")
    st.write("Customize and fine-tune your chatbot experience using Trainify. Set parameters, and ask your query to see results tailored to your needs!")

    # User inputs for chatbot configuration
    st.subheader("Step 1: Configure Your Chatbot")

    # Input: Chatbot Tune
    chatbot_tune = st.selectbox(
        "Choose the chatbot's personality or tune:",
        ["Default", "Friendly", "Professional", "Concise", "Detailed", "Creative"]
    )

    # Input: Prompt Engineering
    prompt_engineering = st.selectbox(
        "Select a prompt engineering technique:",
        ["None", "Zero-shot", "Few-shot", "Instruction-based", "Chain-of-thought"]
    )

    # Input: Domain
    domain = st.selectbox(
        "Select a domain for your query:",
        ["General Knowledge", "Technology", "Science", "Health", "Business", "Education"]
    )

    # Input: Language
    language = st.selectbox(
        "Choose the response language:",
        ["English", "Spanish", "French", "German", "Chinese", "Arabic"]
    )

    # Divider
    st.markdown("<hr>", unsafe_allow_html=True)

    st.subheader("Step 2: Ask Your Query")

    # User query input
    user_query = st.text_input(
        "Enter your query:",
        placeholder="e.g., Explain the benefits of AI in education."
    )

    # Submit button
    submitted = st.button("Submit Query")

    # Process the query when submitted
    if submitted and user_query:
        with st.spinner("Processing your query based on your configurations..."):
            # Create the prompt dynamically
            prompt = f"""You are a chatbot with the following configurations:
            - Personality: {chatbot_tune}
            - Prompt Engineering: {prompt_engineering}
            - Domain: {domain}
            - Language: {language}

            Please respond to the user's query: {user_query}
            """
            
            # Fetch the response using the chat_with_groq function
            response = chat_with_groq(prompt)

            # Display the response
            if response.startswith("Error"):
                st.error(response)
            else:
                st.success("Here’s the response:")
                st.markdown(response)

    # Help section
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Need Help?")
    st.write("""
    - **Chatbot Tune**: Adjust the chatbot's tone and style of response.
    - **Prompt Engineering**: Optimize the AI's response generation approach.
    - **Domain**: Specify the area of knowledge for the query.
    - **Language**: Set the language in which you want the response.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    

elif st.session_state.page == "DomainGuru":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("DomainGuru 🌐")
    st.write("Ask DomainGuru any question related to your domain of interest. It will provide expert-level insights!")

    # Input Form
    with st.form("domain_form"):
        domain_query = st.text_input("Enter your domain-related query:", placeholder="e.g., Explain quantum entanglement, What is the impact of AI in healthcare?")
        submitted = st.form_submit_button("Submit Query")

        if submitted and domain_query:
            with st.spinner("Processing your query..."):
                # Use the chat_with_groq function to get the response
                response = chat_with_groq(domain_query)
                if response.startswith("Error"):
                    st.error(response)
                else:
                    st.success("Here’s what I found:")
                    st.markdown(response)

    st.markdown("</div>", unsafe_allow_html=True)

    
elif st.session_state.page == "StudyBuddy":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("StudyBuddy 📘")

    topic = st.text_input("Enter a topic to study:", placeholder="e.g., Quantum Physics, Python Programming")
    fetch_questions = st.button("Get Important Questions")

    if fetch_questions and topic.strip():
        with st.spinner("Fetching questions and answers..."):
            prompt = f"Provide a list of important questions and answers for studying the topic: {topic}. Format each as follows:\n\nQ: [Question]\nA: [Answer]\n"

            # Fetch data from API
            response = chat_with_groq(prompt)

            if response.startswith("Error"):
                st.error(response)
            else:
                # Parse and display questions
                st.session_state.study_content = response

    if "study_content" in st.session_state:
        st.subheader("Study Questions and Answers")
        st.markdown(st.session_state.study_content)

    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == "About Developers":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("About Developers 🛠️")
    st.write("""
    This project is built by the dedicated students of **COMSATS University Islamabad, Sahiwal Campus**, 
    FA22 Batch of Computer Science. The dashboard showcases innovative ideas, technical expertise, and 
    a collaborative spirit among these bright minds.
    """)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.subheader("Meet the Developers 👨‍💻👩‍💻")
    st.write("""
    This project is a result of the combined efforts of the following team members:
    
    - **Faizan Mustafa**: Lead Developer – Responsible for the architecture and core functionality of the application.
    - **Aina Zahid**: UI Designer – Designed and implemented the user interface, ensuring a smooth user experience.
    - **Muaaz Sajjid**: Chatbot Logic Developer – Developed and optimized the chatbot's logical operations and flow.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="text-align: center;">
            <img src="https://via.placeholder.com/200" alt="Faizan Mustafa" 
            style="border-radius: 50%; width: 200px; height: 200px;">
            <h3 style="margin-top: 10px;">Faizan Mustafa</h3>
            <p style="font-size: 16px; margin: 0;">FA22-BCS-027</p>
            <button onclick="window.location.href='https://github.com/FaizanMustafa';" 
            style="margin-top: 10px; padding: 10px 20px; font-size: 14px; border: none; 
            background-color: #0078d4; color: white; border-radius: 5px; cursor: pointer;">
            Contact Faizan
            </button>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <img src="https://via.placeholder.com/200" alt="Aina Zahid" 
            style="border-radius: 50%; width: 200px; height: 200px;">
            <h3 style="margin-top: 10px;">Aina Zahid</h3>
            <p style="font-size: 16px; margin: 0;">FA22-BCS-016</p>
            <button onclick="window.location.href='https://github.com/AinaZahid';" 
            style="margin-top: 10px; padding: 10px 20px; font-size: 14px; border: none; 
            background-color: #0078d4; color: white; border-radius: 5px; cursor: pointer;">
            Contact Aina
            </button>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="text-align: center;">
            <img src="https://via.placeholder.com/200" alt="Muaaz Sajjid" 
            style="border-radius: 50%; width: 200px; height: 200px;">
            <h3 style="margin-top: 10px;">Muaaz Sajjid</h3>
            <p style="font-size: 16px; margin: 0;">FA22-BCS-047</p>
            <button onclick="window.location.href='https://github.com/MuaazSajjid';" 
            style="margin-top: 10px; padding: 10px 20px; font-size: 14px; border: none; 
            background-color: #0078d4; color: white; border-radius: 5px; cursor: pointer;">
            Contact Muaaz
            </button>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("""
    The team has worked tirelessly to bring this vision to life. Thank you for checking out the **AI Dashboard**!
    """)
    st.markdown("</div>", unsafe_allow_html=True)

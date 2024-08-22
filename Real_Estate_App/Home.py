
import streamlit as st
import sqlite3

# Function to insert data into the database
def insert_into_db(name, email, message):
    conn = sqlite3.connect('contact_form.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_queries (name, email, message)
        VALUES (?, ?, ?)
    ''', (name, email, message))
    conn.commit()
    conn.close()

# Create database and table if not exists
def create_database():
    conn = sqlite3.connect('contact_form.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_queries (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database
create_database()

# Streamlit configuration
st.set_page_config(
    page_title="Gurgaon Real Estate Website",
    page_icon="🏡",
)

st.sidebar.success("Select one option to proceed with your query")

# Display the image
st.image(r"Real_Estate_App/real_estate_image.png", use_column_width=True)

# Welcome message and introduction
st.markdown(
    """
    <style>
    .welcome-text {
        text-align: center;
        padding: 20px;
        background-color: #2C3E50;
        border-radius: 10px;
    }
    .welcome-text h1 {
        font-size: 3em;
        color: #FFD700;
    }
    .welcome-text p {
        font-size: 1.5em;
        color: #ECF0F1;
    }
    .section {
        padding: 20px;
        background-color: #34495E;
        border-radius: 10px;
        margin-top: 30px;
    }
    .section h2 {
        font-size: 2.5em;
        color: #FFD700;
        text-align: center;
    }
    .feature {
        margin-top: 20px;
        padding: 20px;
        border: 2px solid #FFD700;
        border-radius: 10px;
        background-color: #2C3E50;
    }
    .feature h3 {
        color: #FFD700;
    }
    .feature p {
        font-size: 1.25em;
        color: #ECF0F1;
    }
    .contact-form {
        padding: 20px;
        background-color: #34495E;
        border-radius: 10px;
        margin-top: 30px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    }
    .contact-form h2 {
        font-size: 2.5em;
        color: #FFD700;
        text-align: center;
    }
    .contact-form input, .contact-form textarea {
        width: 100%;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
        border: 1px solid #BDC3C7;
        box-sizing: border-box;
    }
    .contact-form input[type="submit"] {
        background-color: #FFD700;
        color: #2C3E50;
        border: none;
        cursor: pointer;
        font-size: 1.2em;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
    .contact-form input[type="submit"]:hover {
        background-color: #FFC300;
    }
    </style>
    <div class="welcome-text">
        <h1>Welcome to Gurgaon Real Estate! 🏡</h1>
        <p>Your premier destination for discovering your dream property in Gurgaon.
        Whether you're looking for a luxurious apartment or a cozy house, we've got
        you covered with the best listings in town.</p>
    </div>
    <div class="section">
        <h2>Explore Our Features</h2>
        <div class="feature">
            <h3>Price Predictor</h3>
            <p>Accurately predict property prices based on real-time data and advanced algorithms. Whether you're buying or selling, our price predictor gives you the insights you need to make informed decisions.</p>
        </div>
        <div class="feature">
            <h3>Analytics Module</h3>
            <p>Dive deep into the data with our comprehensive analytics module. Understand market trends, property performance, and investment potential with intuitive visualizations and reports.</p>
        </div>
        <div class="feature">
            <h3>Recommender System</h3>
            <p>Get personalized property recommendations tailored to your preferences. Our AI-driven recommender system helps you find the perfect home that matches your criteria and budget.</p>
        </div>
    </div>
    <div class="contact-form">
        <h2>Contact Us</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Handle form submission
st.markdown(
    """
    <style>
    .stTextInput, .stTextArea {
        width: 100% !important;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
        border: 1px solid #BDC3C7;
        box-sizing: border-box;
    }
    .stButton {
        background-color: #FFD700 !important;
        color: #2C3E50 !important;
        border: none !important;
        cursor: pointer !important;
        font-size: 1.2em !important;
        padding: 10px !important;
        border-radius: 5px !important;
        margin-top: 10px !important;
    }
    .stButton:hover {
        background-color: #FFC300 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.form(key='contact_form'):
    name = st.text_input("Name", placeholder="Enter your name")
    email = st.text_input("Email", placeholder="Enter your email")
    message = st.text_area("Message", placeholder="Enter your message")

    submit_button = st.form_submit_button("Send")

    if submit_button:
        if name and email and message:
            insert_into_db(name, email, message)
            st.success("Your message has been recorded. Thank you!")
        else:
            st.error("Please fill in all fields.")

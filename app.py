import streamlit as st
from llm import Model

# Initialize the model
model = Model()

# Streamlit interface
st.title('Educational Assistant📖')

st.markdown("""
    <style>
    .justified-text {
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Section
st.sidebar.title("About")
st.sidebar.caption("""
        <div class="justified-text">
           This AI-powered educational assistant helps students by providing accurate answers to their questions, explaining complex concepts, summarizing textbook content, and generating personalized study plans. Powered by the Gemini API and built with Streamlit.
        </div>
        """, unsafe_allow_html=True)

for _ in range(3):
        st.sidebar.write("") 

# Menu options
menu = ["Ask a Question", "Explain a Concept", "Summarize Textbook", "Personalized Study Plan"]
choice = st.sidebar.selectbox("Choose an option", menu)

for _ in range(10):
        st.sidebar.write("") 
        
st.sidebar.subheader("Build By:")
st.sidebar.write("[Pachaiappan❤️](https://mr-vicky-01.github.io/Portfolio)")
st.sidebar.write("contact: [Email](mailto:pachaiappan1102@gamil.com)")

if choice == "Ask a Question":
    st.subheader("Ask a Question")
    question = st.text_input("Enter your question")
    if st.button("Get Answer"):
        prompt = f"You are a helpful Q&A assistant. Try to give an accurate answer. Question: {question}"
        with st.spinner("Analyzing your query..."):
            response = model.get_response(prompt)
        st.write("Answer:")
        st.write(response)

elif choice == "Explain a Concept":
    st.subheader("Explain a Concept")
    concept = st.text_input("Enter the concept to explain")
    if st.button("Get Explanation"):
        prompt = f"Explain the following concept in detail: {concept}"
        with st.spinner("Generating explanation..."):
            response = model.get_response(prompt)
        st.write("Explanation:")
        st.write(response)

elif choice == "Summarize Textbook":
    st.subheader("Summarize Textbook")
    uploaded_file = st.file_uploader("Upload a textbook image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        if st.button("Summarize"):
            prompt = "Summarize this textbook content"
            with st.spinner("Summarizing the content..."):
                response = model.get_response(prompt, uploaded_file)
            st.write("Summary:")
            st.write(response)

elif choice == "Personalized Study Plan":
    st.subheader("Personalized Study Plan")
    subjects = st.text_input("Enter the subjects you need help with (comma-separated)")
    study_time = st.slider("How many hours can you study per day?", 1, 8)
    if st.button("Get Study Plan"):
        prompt = f"Create a study plan for the following subjects: {subjects}. The student can study for {study_time} hours per day."
        with st.spinner("Creating your study plan..."):
            response = model.get_response(prompt)
        st.write("Study Plan:")
        st.write(response)
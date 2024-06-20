# Educational Assistant 📖

## Overview

Educational Assistant is an AI-powered application designed to help students by providing accurate answers to their questions, explaining complex concepts, summarizing textbook content, and generating personalized study plans. It uses the Gemini API for its powerful AI capabilities and is built with Streamlit for an intuitive user interface. This project showcases the use of AI in the educational field and can be a valuable addition to your portfolio.

## Features

- **Ask a Question**: Get accurate answers to any question.
- **Explain a Concept**: Receive detailed explanations of complex concepts.
- **Summarize Textbook**: Summarize the content of uploaded textbook images.
- **Personalized Study Plan**: Generate customized study plans based on user input.

## Demo
![image](https://github.com/Mr-Vicky-01/Legal-Doc-Analyzer/assets/143078285/4d72af99-037d-4797-8842-f0b021d1de87)

- Try this app: [Link](https://huggingface.co/spaces/Mr-Vicky-01/Educational-Assitant)

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit
- Required Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Mr-Vicky-01/Educational-Assitant.git
    cd Educational-Assitant
    ```

2. Install the required libraries:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Set up the Google API Key:

    Go to this site to generate API key [HERE](https://aistudio.google.com). Once you have the API key, locate the .env file in your project directory. Open it and paste your API key like this:
    ```bash
    GOOGLE_API_KEY = "paste the api key here"
    ```

### Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open the app in your browser and interact with the various features.

## File Structure

- `app.py`: Main application file containing the Streamlit interface.
- `llm.py`: Contains the definition of the `Model` class used for generating responses.
- `requirements.txt`: Lists the required Python packages for the application.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or feedback, feel free to reach out:

- **Email**: pachaiappan1102@gmail.com

## Acknowledgments

- Gemini API for their powerful content generation model.
- Streamlit for providing an easy-to-use web app framework.
- The open-source community for providing valuable resources and support.

# Personalized Interview Question Generator

## Project Overview

This is a web-based application built using **Streamlit** and **Hugging Face's Transformers** that generates technical interview questions based on the given tech stack. The app leverages pre-trained transformer models (like \`flan-t5-base\`) to generate interview questions dynamically for software engineering roles, with a focus on real-world, practical questions related to specific technologies like Python, JavaScript, Machine Learning, and more.

---

## Features

- **Generate Interview Questions**: Dynamically generates real-world technical questions based on the tech stack (e.g., Python, React, Java, etc.).
- **Streamlit-based UI**: Simple and interactive interface for candidates to input their tech stack and receive personalized questions.
- **Multiple Tech Stack Support**: Supports multiple tech stacks (e.g., Python, Flask, ML, C++) and generates relevant questions for each.
- **Pre-trained Transformer Model**: Uses Hugging Face's \`flan-t5-base\` transformer model to generate questions.

---

## Installation Instructions

To get started with this project, follow these steps:

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/your-username/talentscout.git
cd talentscout
\`\`\`

### 2. Install Dependencies

Make sure you have Python 3.7+ installed. You can install the required dependencies using \`pip\`:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

You will need to install **Streamlit**, **Hugging Face's Transformers**, and **Torch** for the app to run.

### 3. Install Hugging Face's Model

The model will be automatically downloaded the first time you run the application. However, make sure you have access to Hugging Face API tokens if you plan to use their models directly.

To set up Hugging Face's API token:

1. Create an account on [Hugging Face](https://huggingface.co).
2. Go to your [account settings](https://huggingface.co/settings/tokens) and generate an API token.
3. Use the following environment variable to set your token:

\`\`\`bash
export HF_AUTH_TOKEN="your-token-here"
\`\`\`

Alternatively, you can use a **tokenized approach** for secure access.

---

## How to Run

Once everything is set up, you can run the app with the following command:

\`\`\`bash
streamlit run app.py
\`\`\`

This will launch the app in your web browser.

---

## Usage

### Tech Stack Input

1. Enter the **candidate's name** and **tech stack** (comma-separated, e.g., \`Python, Flask, Machine Learning\`).
2. The app will generate **1 technical interview question** based on the entered tech stack.

### Example:

- **Tech Stack**: Python, Flask
- **Generated Question**: "How do you securely store and validate JWT tokens in a Flask application?"

---

## Project Structure

\`\`\`
talentscout/
│
├── app.py               # Main Streamlit app
├── requirements.txt     # List of required Python packages
└── README.md            # Project overview and instructions
\`\`\`

---

## Dependencies

- **Streamlit**: For creating the interactive web application.
- **Transformers**: For accessing pre-trained language models like \`flan-t5-base\` from Hugging Face.
- **Torch**: For running the model and processing inputs.
- **Hugging Face API**: For accessing the pre-trained models.

To install the necessary packages, run:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

## Contributing

Feel free to contribute to this project. You can improve or add new features such as:

- Support for more tech stacks
- Ability to generate multiple questions at once
- Exporting generated questions to text/PDF files
- Optimizing model usage or adding more powerful models

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

### Example Workflow:

1. **Start the app**: You’ll be prompted for the candidate’s name and tech stack (e.g., \`Python, Flask, Machine Learning\`).
2. **Question Generation**: After inputting the tech stack, the app generates one technical interview question based on the entered tech stack.
3. **Question Display**: The generated question is displayed in the app for the interviewer to ask.

---

### 📝 Future Enhancements:

- **Multi-question generation**: Add the ability to generate multiple questions in a batch.
- **Multiple Role-Specific Question Templates**: Introduce question templates based on job roles (e.g., backend, frontend, data science).
- **PDF Export**: Allow users to export the questions to a downloadable format (e.g., PDF, TXT).
- **MCQ Generator**: Add a mode to generate multiple-choice questions for interviews.

---

## Contact

For any issues or feature requests, feel free to open an issue on the [GitHub repository](https://Ankita780/Personalized-Interview-Questions-Generator/issues).



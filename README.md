<img width="492" height="626" alt="Tech_Chatbot" src="https://github.com/user-attachments/assets/ca08aefc-45dd-4203-b7c8-65829164de82" />

# 🤖 Technology Chatbot

A semantic AI-powered Technology Chatbot built with **Python**, **Tkinter**, and **Sentence Transformers**. Instead of relying on simple keyword matching, the chatbot uses **sentence embeddings** and **cosine similarity** to understand user intent and provide relevant technology-related responses.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![AI](https://img.shields.io/badge/AI-SentenceTransformers-orange.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)

---

## 📖 Overview

This project demonstrates how modern Natural Language Processing (NLP) techniques can be used to create an intelligent chatbot capable of understanding technology-related questions.

The chatbot covers topics such as:

* 💻 Computers & PC Hardware
* 📱 Smartphones & Tablets
* 🌐 Networking & WiFi
* 👨‍💻 Programming & Software Development
* 🔒 Cybersecurity & Privacy
* 🎮 Gaming & Performance Optimization
* ☁️ Cloud Services & Storage
* 🤖 Artificial Intelligence
* 🖥️ Operating Systems (Windows, Linux, macOS)

Unlike traditional rule-based chatbots, this implementation uses **semantic similarity matching**, allowing users to ask questions in different ways while still receiving meaningful responses.

---

## ✨ Features

* 🔍 Semantic understanding using Sentence Transformers
* 🧠 AI-based intent matching
* 📊 Confidence score display
* 🎨 Modern dark-themed GUI
* ⚡ Fast response generation
* 🖱️ Easy-to-use Tkinter interface
* 🧹 Chat history clearing functionality
* 📚 Expandable knowledge base

---

## 🏗️ Technologies Used

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| Python                | Core programming language |
| Tkinter               | Graphical User Interface  |
| Sentence Transformers | Semantic embeddings       |
| all-MiniLM-L6-v2      | Lightweight NLP model     |
| PyTorch               | Tensor computations       |
| Cosine Similarity     | Intent matching           |

---

## 🧠 How It Works

1. The chatbot loads predefined question-response pairs.

2. Each question pattern is converted into an embedding vector using:

   ```python
   SentenceTransformer('all-MiniLM-L6-v2')
   ```

3. User input is transformed into an embedding.

4. Cosine similarity compares the input with all stored patterns.

5. The most similar pattern is selected.

6. If similarity exceeds the threshold (`0.3`), the corresponding answer is returned.

7. Otherwise, the chatbot responds that it doesn't understand the query.

---

## 📂 Project Structure

```text
technology-chatbot/
│
├── chatbot.py
├── README.md
├── requirements.txt
└── screenshots/
    └── chatbot-ui.png
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/technology-chatbot.git

cd technology-chatbot
```

### 2️⃣ Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install sentence-transformers torch
```

---

## ▶️ Running the Application

```bash
python chatbot.py
```

The graphical chatbot window will open automatically.

---

## 💬 Example Conversations

### Example 1

**User:**

```text
My WiFi is very slow
```

**Bot:**

```text
Try restarting your router, moving closer,
or changing the WiFi channel.
```

---

### Example 2

**User:**

```text
I want to learn Python programming
```

**Bot:**

```text
Learning to code? I can help with concepts,
bugs, or projects.
```

---

### Example 3

**User:**

```text
Recommend a laptop
```

**Bot:**

```text
Tell me your budget and use,
and I’ll suggest a good laptop.
```

---

## 🎯 Future Improvements

* OpenAI API integration
* Voice input/output
* Database-backed knowledge base
* Context-aware conversations
* Multi-language support
* Dynamic learning from conversations
* Better UI with CustomTkinter

---

## 📸 Screenshots

Add screenshots here:

```markdown
![Chatbot UI](screenshots/chatbot-ui.png)
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request


---

## 👨‍💻 Author

Created by JP using Python and NLP technologies.

If you found this project useful, consider giving it a ⭐ on GitHub!



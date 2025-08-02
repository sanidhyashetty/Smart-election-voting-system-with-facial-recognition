Smart Election Voting System with Facial Recognition

A secure, AI-powered voting system built with Python that uses facial recognition to authenticate voters and ensure a transparent and tamper-proof election process. This project combines computer vision, machine learning, and voice assistance to provide a modern alternative to traditional voting systems.

🔍 Project Overview

This system captures a voter's facial data and links it to their Aadhar number. During the voting process, a webcam is used to identify the voter in real time. If authenticated, the voter is allowed to cast a single vote. The system prevents duplicate votes and announces the winning party based on vote count.

📁 Files and Structure
add_faces.py – Registers a new voter by capturing and saving 50 face images.

give_vote.py – Recognizes the voter's face, records the vote, and announces the winner.

background.png – Background UI image for the voting screen.

requirements.txt – List of required Python libraries.

Votes.csv – Stores all vote records with voter ID, selected party, date, and time.

data/

faces_data.pkl – Encoded face data used for classification.

names.pkl – Voter IDs (Aadhar numbers) corresponding to the facial data.

🚀 How to Run (Using VS Code)

Open the Project in VS Code

Launch Visual Studio Code.

Open the folder that contains your project files (add_faces.py, give_vote.py, etc.).

Install the Required Libraries

In VS Code, go to the terminal (press Ctrl + ~ or use Terminal > New Terminal from the top menu).

Run the following command to install all necessary packages:

pip install -r requirements.txt


Register a Voter

In the Explorer (left panel), open the file add_faces.py.

Right-click anywhere in the editor and select “Run Python File in Terminal”.

Enter the voter's Aadhar number when prompted.

The webcam will open and capture facial images automatically.

Cast a Vote

Open give_vote.py in the editor.

Right-click inside the file and select “Run Python File in Terminal”.

The webcam will recognize the voter.

Once recognized, press the corresponding number key:

1 for BJP

2 for Congress

3 for AAP

4 for NOTA

The vote will be recorded in Votes.csv.

View Results

After the voting session ends, the system will automatically calculate and announce the winning party based on the votes.

🧠 Technologies Used

Python

OpenCV – Face detection and image processing

scikit-learn – K-Nearest Neighbors (KNN) classifier

pywin32 – Voice feedback (Windows-only)

CSV – Vote logging

✅ Features

Real-time face detection and recognition

One-vote-per-person validation

Speech feedback for better accessibility

Dynamic vote logging with timestamp

Automated result announcement

Simple and intuitive UI using OpenCV display


💡 Notes
Make sure your webcam is connected and functioning properly.

Votes.csv will be created automatically in the main project directory after the first vote is cast.

Voice feedback works only on Windows (via pywin32).

This setup assumes you're running everything from VS Code directly, without command-line navigation or external editors.


💡 Future Improvements

Cross-platform voice support

Admin login and dashboard for managing elections

GUI-based interface using Tkinter or PyQt

Real-time vote analytics

Cloud integration for scalable deployment

🙌 Contributions

Contributions, suggestions, and forks are welcome. You can improve this project by adding more features, enhancing the UI, or improving face recognition accuracy.

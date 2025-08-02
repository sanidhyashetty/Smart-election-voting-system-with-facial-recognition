# from sklearn.neighbors import KNeighborsClassifier

# import cv2
# import pickle
# import numpy as np
# import os
# import csv
# import time
# from datetime import datetime
# from win32com.client import Dispatch


# def speak(str1):
#     speak = Dispatch(("SAPI.SpVoice"))
#     speak.Speak(str1)


# video = cv2.VideoCapture(0)
# facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# if not os.path.exists('data/'):
#     os.makedirs('data/')

# with open('data/names.pkl', 'rb') as f:
#     LABELS = pickle.load(f)

# with open('data/faces_data.pkl', 'rb') as f:
#     FACES = pickle.load(f)

# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(FACES, LABELS)
# imgBackground = cv2.imread("background.png")

# COL_NAMES = ['NAME', 'VOTE', 'DATE', 'TIME']

# def check_if_exists(value):
#     try:
#         with open("Votes.csv", "r") as csvfile:
#             reader = csv.reader(csvfile)
#             for row in reader:
#                 if row and row[0] == value:
#                     return True
#     except FileNotFoundError:
#         print("File not found or unable to open the CSV file.")
#     return False

# while True:
#     ret, frame = video.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
#     output = None  # Initialize output to a default value
#     for (x, y, w, h) in faces:
#         crop_img = frame[y:y+h, x:x+w]
#         resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
#         output = knn.predict(resized_img)
#         ts = time.time()
#         date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
#         timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")
#         exist = os.path.isfile("Votes.csv")
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
#         cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
#         cv2.putText(frame, str(output[0]), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
#         attendance = [output[0], timestamp]
        
#     imgBackground[370:370 + 480, 225:225 + 640] = frame
#     cv2.imshow('frame', imgBackground)
#     k = cv2.waitKey(1)
    
#     if output is not None:
#         voter_exist = check_if_exists(output[0])
#         if voter_exist:
#             speak("YOU HAVE ALREADY VOTED")
#             break

#         if k == ord('1'):
#             speak("YOUR VOTE HAS BEEN RECORDED")
#             time.sleep(5)
#             if exist:
#                 with open("Votes.csv", "a") as csvfile:
#                     writer = csv.writer(csvfile)
#                     attendance = [output[0], "BJP", date, timestamp]
#                     writer.writerow(attendance)
#             else:
#                 with open("Votes.csv", "a") as csvfile:
#                     writer = csv.writer(csvfile)
#                     writer.writerow(COL_NAMES)
#                     attendance = [output[0], "BJP", date, timestamp]
#                     writer.writerow(attendance)
#             speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
#             break

#         if k == ord('2'):
#             speak("YOUR VOTE HAS BEEN RECORDED")
#             time.sleep(5)
#             if exist:
#                 with open("Votes.csv", "a") as csvfile:
#                     writer = csv.writer(csvfile)
#                     attendance = [output[0], "CONGRESS", date, timestamp]
#                     writer.writerow(attendance)
#             else:
#                 with open("Votes.csv", "a") as csvfile:
#                     writer = csv.writer(csvfile)
#                     writer.writerow(COL_NAMES)
#                     attendance = [output[0], "CONGRESS", date, timestamp]
#                     writer.writerow(attendance)
#             speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
#             break

#         if k == ord('3'):
#             speak("YOUR VOTE HAS BEEN RECORDED")
#             time.sleep(5)
#             if exist:
#                 with open("Votes.csv", "a") as csvfile:
#                     writer = csv.writer(csvfile)
#                     attendance = [output[0], "AAP", date, timestamp]
#                     writer.writerow(attendance)
#             else:
#                 with open("Votes.csv", "a") as csvfile:
#                     writer = csv.writer(csvfile)
#                     writer.writerow(COL_NAMES)
#                     attendance = [output[0], "AAP", date, timestamp]
#                     writer.writerow(attendance)
#             speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
#             break

#         if k == ord('4'):
#             speak("YOUR VOTE HAS BEEN RECORDED")
#             time.sleep(5)
#             if exist:
#                 with open("Votes.csv", "a") as csvfile:
#                     writer = csv.writer(csvfile)
#                     attendance = [output[0], "NOTA", date, timestamp]
#                     writer.writerow(attendance)
#             else:
#                 with open("Votes.csv", "a") as csvfile:
#                     writer = csv.writer(csvfile)
#                     writer.writerow(COL_NAMES)
#                     attendance = [output[0], "NOTA", date, timestamp]
#                     writer.writerow(attendance)
#             speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
#             break

# video.release()
# cv2.destroyAllWindows()

from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch
from collections import Counter

def speak(str1):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)

def check_if_exists(value):
    try:
        with open("Votes.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row and row[0] == value:
                    return True
    except FileNotFoundError:
        print("File not found or unable to open the CSV file.")
    return False

# Function to count votes and declare the winner
def declare_winner(votes_file):
    try:
        with open(votes_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            votes = []

            # Iterate over rows and ensure there are at least 2 columns: name and vote
            for row in reader:
                if len(row) >= 2:  # Ensure there are enough columns
                    votes.append(row[1])  # Extract the party names (column 1)

        # Count votes for each party
        vote_counts = Counter(votes)
        
        # Determine the party with the most votes
        winner = vote_counts.most_common(1)[0]  # Get the most common party
        print(f"The winner of the election is: {winner[0]} with {winner[1]} votes.")
        speak(f"The winner of the election is: {winner[0]} with {winner[1]} votes.")
        return winner
    except FileNotFoundError:
        print("Votes file not found.")
        return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Main voting system
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if not os.path.exists('data/'):
    os.makedirs('data/')

with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)

with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)
imgBackground = cv2.imread("background.png")

COL_NAMES = ['NAME', 'VOTE', 'DATE', 'TIME']

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    output = None  # Initialize output to a default value
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        exist = os.path.isfile("Votes.csv")
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(output[0]), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        attendance = [output[0], timestamp]
        
    imgBackground[370:370 + 480, 225:225 + 640] = frame
    cv2.imshow('frame', imgBackground)
    k = cv2.waitKey(1)
    
    if output is not None:
        voter_exist = check_if_exists(output[0])
        if voter_exist:
            speak("YOU HAVE ALREADY VOTED")
            break

        if k == ord('1'):
            speak("YOUR VOTE HAS BEEN RECORDED")
            time.sleep(5)
            if exist:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    attendance = [output[0], "BJP", date, timestamp]
                    writer.writerow(attendance)
            else:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    attendance = [output[0], "BJP", date, timestamp]
                    writer.writerow(attendance)
            speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
            break

        if k == ord('2'):
            speak("YOUR VOTE HAS BEEN RECORDED")
            time.sleep(5)
            if exist:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    attendance = [output[0], "CONGRESS", date, timestamp]
                    writer.writerow(attendance)
            else:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    attendance = [output[0], "CONGRESS", date, timestamp]
                    writer.writerow(attendance)
            speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
            break

        if k == ord('3'):
            speak("YOUR VOTE HAS BEEN RECORDED")
            time.sleep(5)
            if exist:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    attendance = [output[0], "AAP", date, timestamp]
                    writer.writerow(attendance)
            else:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    attendance = [output[0], "AAP", date, timestamp]
                    writer.writerow(attendance)
            speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
            break

        if k == ord('4'):
            speak("YOUR VOTE HAS BEEN RECORDED")
            time.sleep(5)
            if exist:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    attendance = [output[0], "NOTA", date, timestamp]
                    writer.writerow(attendance)
            else:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    attendance = [output[0], "NOTA", date, timestamp]
                    writer.writerow(attendance)
            speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
            break

# Close video and window
video.release()
cv2.destroyAllWindows()

# Declare the winner after voting ends
declare_winner("Votes.csv")

import streamlit as st
import random
import csv
import time
from triviaAI import TriviaAI

class TriviaQA:
    qaList = []
    triviaAI = TriviaAI()

    def __init__(self, question, answer):
        """
        Initialize a TriviaQA object.

        Parameters:
        - question (str): The trivia question.
        - answer (str): The correct answer to the trivia question.
        """
        self.question = question
        self.answer = answer

    @classmethod
    def load_questions(cls):
        """
        Load trivia questions from a CSV file into qaList if it's empty.

        This method reads questions from a CSV file and populates the qaList class attribute if it's empty.
        """
        if not cls.qaList:
            with open("questionsDatabase.csv", 'r') as file:
                csvReader = csv.reader(file)
                for row in csvReader:
                    qa = TriviaQA(row[0], row[1])
                    cls.qaList.append(qa)
    
    @classmethod
    def randomize(cls):
        """
        Randomly select a trivia question from qaList.

        Returns:
        - chosenQ (TriviaQA): A randomly chosen trivia question.
        """
        if st.session_state.use_AI:
            num = random.randint(1,2)
            if num == 1:
                cls.triviaAI.write_new()
                cls.load_questions()
                chosenQ = random.choice(cls.qaList)
                return chosenQ
            else:
                raw = cls.triviaAI.generate_new()
                qa = TriviaQA(raw[0], raw[1])
                return qa
        else:
            cls.load_questions()
            chosenQ = random.choice(cls.qaList)
            return chosenQ

class Trivia:
    def __init__(self, x=5, inTrivia=False, success=False):
        """
        Initialize a Trivia game instance.

        Parameters:
        - x (int): The number of attempts allowed in the trivia game.
        - inTrivia (bool): Flag indicating whether the user is currently in a trivia game.
        - success (bool): Flag indicating whether the user successfully answered the trivia question.
        """
        self.x = x
        self.inTrivia = inTrivia
        self.success = success

    def trivia_action(self):
        """
        Perform actions based on the user's interaction with the trivia game.

        This method handles the logic of displaying questions, accepting user answers, and determining outcomes.
        """
        if self.inTrivia:
            if 'current_question' not in st.session_state or not self.inTrivia:
                st.session_state.current_question = TriviaQA.randomize()
                st.session_state.attempts_left = self.x
                self.inTrivia = True

            current_question = st.session_state.current_question
            attempts_left = st.session_state.attempts_left

            if isinstance(current_question, TriviaQA):
                st.write(current_question.question)
                trivia_options = st.radio(
                    "Select an answer 👇",
                    ["A", "B", "C"],
                    key="trivia_options",
                    index=None
                )

                if st.button("Submit"):
                    if trivia_options == current_question.answer:
                        st.toast("✅ Correct! You climbed out of the pit!")
                        self.success = True
                        self.inTrivia = False
                        with st.spinner("You are being transported to a new room..."):
                            time.sleep(2)
                            st.session_state.gameLocs.userRoom = random.randint(1, 30)                    
                        st.session_state.current_question = TriviaQA.randomize()
                        st.switch_page("pages/main.py")
                    else:
                        attempts_left -= 1
                        st.session_state.attempts_left = attempts_left
                        if attempts_left > 0:
                            st.toast(f"❌ Incorrect! You have {attempts_left} attempts left.")
                            with st.spinner("Generating new question..."):
                                time.sleep(1)
                            st.session_state.current_question = TriviaQA.randomize()
                            st.rerun()
                        else:
                            st.toast("💀 Out of attempts! Better luck next time.")
                            self.inTrivia = False
                            time.sleep(1)
                            st.session_state.gameLocs.userRoom = random.randint(1, 30)  
                            st.switch_page("pages/lose.py")
            else:
                st.error("Error loading question. Please try again.")
                self.inTrivia = False

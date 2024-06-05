import json
import streamlit as st
from collections import defaultdict

class Scoring:
    def __init__(self, name, score):
        """
        Initialize the Scoring class.

        Parameters:
        - name (str): The name of the player.
        - score (int): The score of the player.
        """
        self.name = name
        self.score = score

    @classmethod
    def read_scores(cls):
        """
        Reads the JSON scores file.

        Returns:
        - scores (list): List of scores read from the JSON file.
        """
        try:
            with open('scores.json', 'r') as file:
                scores = json.load(file)
                return scores
        except FileNotFoundError:
            return []

    @classmethod
    def write_score(cls, name, score):
        """
        Writes a new score to the JSON scores file.

        Parameters:
        - name (str): The name of the player.
        - score (int): The score of the player.
        """
        scores_data = Scoring.read_scores()
        new_entry = {"name": name, "score": score}
        scores_data.append(new_entry)
        with open('scores.json', 'w') as file:
            json.dump(scores_data, file, indent=4)

    @classmethod
    def return_high_scores(cls):
        """
        Returns the top individual scores and the top average scores for players.

        Returns:
        - top_individual_scores (list): List of top 5 individual scores.
        - top_average_scores (list): List of top 5 players with the highest average scores.
        """
        scores = Scoring.read_scores()
        
        # Top 5 individual scores
        top_individual_scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:5]

        # Calculate average scores for each player
        player_scores = defaultdict(list)
        for entry in scores:
            player_scores[entry["name"]].append(entry["score"])
        
        average_scores = {player: sum(scores) / len(scores) for player, scores in player_scores.items()}
        top_average_scores = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)[:5]

        return top_individual_scores, top_average_scores

    @classmethod
    def calculate_score(cls):
        """
        Calculate the final score for the current game session.

        The score is calculated based on various factors including win status, number of arrows, number of rooms, etc.

        Returns:
        - score (int): The calculated score for the current session.
        """
        minus = 0
        for i in range(4):
            if st.session_state.seenList[i + 1]:
                minus += 100
        if st.session_state.map_opened == 0:
            st.session_state.map_opened = 100
        score = (st.session_state.win_status + 1000 + 100 * st.session_state.arrows -
                 10 * st.session_state.num_rooms - minus + st.session_state.map_opened +
                 20 * st.session_state.attack - st.session_state.wumpus_health)
        return score

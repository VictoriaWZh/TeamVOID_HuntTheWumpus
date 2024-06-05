import plotly.graph_objects as go

class Map:
    def __init__(self, occRoomList, seenList):
        """
        Initialize the Map class.

        Parameters:
        - occRoomList (list): List of occupied rooms.
        - seenList (list): List indicating whether a room has been seen or not.
        """
        self.occRoomList = occRoomList
        self.seenList = seenList

    def create_hexagon_grid(self, statuses):
        """
        Create a hexagonal grid representing the map with different room statuses.

        Parameters:
        - statuses (list): List of room statuses.

        Returns:
        - fig (plotly.graph_objs.Figure): Plotly figure representing the hexagonal grid.
        """
        fig = go.Figure()

        # Positions of hexagons on map
        hexagons = [
            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
            (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
            (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
            (0, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1),
            (0, -2), (1, -2), (2, -2), (3, -2), (4, -2), (5, -2)
        ]
        
        # Looping through map to graph hexagons
        for i, (x, y) in enumerate(hexagons):
            status = statuses[i]
            color = 'white' if status == 'default' else status
            fig.add_trace(go.Scatter(
                x=[x + 0.5 * (y % 2)], y=[y * (3 / 4)],
                mode='markers+text',
                marker=dict(size=90, symbol='hexagon', color=color, line=dict(width=2, color='black')),
                text=str(i + 1),  # Add the number to the hexagon
                textposition='middle center',  # Position the text in the center
                textfont=dict(color='black'),  # Change the text color to black
                showlegend=False  # Hide the legend for each trace
            ))

        # Configure the hexagon map
        fig.update_layout(
            xaxis=dict(showgrid=False, zeroline=False, visible=False),
            yaxis=dict(showgrid=False, zeroline=False, visible=False),
            height=600,
            width=600,
            margin=dict(l=10, r=10, t=10, b=10),
            showlegend=False  # Ensure the legend is hidden
        )
        return fig

    @staticmethod
    def ascii_grid(currentRoomsList, seenList):
        """
        Create an ASCII representation of the map.

        Parameters:
        - currentRoomsList (list): List of currently occupied rooms.
        - seenList (list): List indicating whether a room has been seen or not.

        Returns:
        - map_str (str): String representation of the ASCII map.
        """
        playerSymbol = "x"
        wumpusSymbol = "w"
        batSymbol = "^"
        pitSymbol = "U"

        map_str = ""

        i = 1
        j = 1
        for _ in range(5):
            for _ in range(6):
                map_str += " ___ "
            map_str += "\n"
            for _ in range(6):
                if i < 10:
                    map_str += "/ " + str(i) + " \\"
                else:
                    map_str += "/" + str(i) + " \\"
                i += 1
            map_str += "\n"
            for _ in range(6):
                if j in currentRoomsList:
                    index = currentRoomsList.index(j)
                    if index == 0:
                        map_str += "\\_" + playerSymbol + "_/"
                    elif index == 1 and seenList[index]:
                        map_str += "\\_" + wumpusSymbol + "_/"
                    elif (index == 2 or index == 3) and seenList[index]:
                        map_str += "\\_" + batSymbol + "_/"
                    elif (index == 4 or index == 5) and seenList[index]:
                        map_str += "\\_" + pitSymbol + "_/"
                    else:
                        map_str += "\\___/"
                else:
                    map_str += "\\___/"
                j += 1
            map_str += "\n"
        return map_str
    
    @staticmethod
    def text_map(occRoomsList, seenList):
        """
        Create a textual map indicating visited bat and pit rooms.

        Parameters:
        - occRoomsList (list): List of occupied rooms.
        - seenList (list): List indicating whether a room has been seen or not.

        Returns:
        - visited_bats (list): List of rooms with visited bats.
        - visited_pits (list): List of rooms with visited pits.
        """
        visited_bats = []
        visited_pits = []
        for i in range(len(seenList)):
            if seenList[i]:
                if i == 1 or i == 2:
                    visited_bats.append(occRoomsList[i])
                if i == 3 or i == 4:
                    visited_pits.append(occRoomsList[i])
        
        return visited_bats, visited_pits

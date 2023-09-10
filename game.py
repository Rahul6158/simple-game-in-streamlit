import streamlit as st

# Define the story as a dictionary where each key represents a story node.
story = {
    'start': {
        'text': "You wake up in a mysterious forest. Do you want to 'go left' or 'go right'?",
        'choices': ['go left', 'go right'],
        'outcomes': ['left_path', 'right_path']
    },
    'left_path': {
        'text': "You find an abandoned cabin. Do you 'enter' or 'keep walking'?",
        'choices': ['enter', 'keep walking'],
        'outcomes': ['cabin', 'continue']
    },
    'right_path': {
        'text': "You encounter a pack of wolves. Do you 'run' or 'stand still'?",
        'choices': ['run', 'stand still'],
        'outcomes': ['game_over', 'game_over']
    },
    'cabin': {
        'text': "Inside the cabin, you find a treasure chest. Do you 'open' it or 'ignore' it?",
        'choices': ['open', 'ignore'],
        'outcomes': ['win', 'continue']
    },
    'game_over': {
        'text': "Game over! You didn't survive the adventure.",
        'choices': [],
        'outcomes': []
    },
    'win': {
        'text': "Congratulations! You found the treasure and won the game.",
        'choices': [],
        'outcomes': []
    }
}

# Function to display a story node and get user input for choices.
def display_story_node(node):
    st.write(story[node]['text'])
    choice = st.selectbox("Your choice:", story[node]['choices'])
    next_node = story[node]['outcomes'][story[node]['choices'].index(choice)]
    return next_node

# Streamlit app
st.title("Choose Your Adventure Game")

current_node = 'start'
while current_node not in ['game_over', 'win']:
    current_node = display_story_node(current_node)

if current_node == 'game_over':
    st.error("Game over! You didn't survive the adventure.")
else:
    st.success("Congratulations! You found the treasure and won the game.")

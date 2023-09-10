import streamlit as st

# Define the story as a dictionary where each key represents a story node.
story = {
    'start': {
        'text': "Jangirii wakes up in a mysterious forest. Should he 'go left' or 'go right'?",
        'choices': ['go left', 'go right'],
        'outcomes': ['left_path', 'right_path'],
        'image': 'https://example.com/forest.jpg'  # Image URL for this step
    },
    'left_path': {
        'text': "Jangirii finds an abandoned cabin. Should he 'enter' or 'keep walking'?",
        'choices': ['enter', 'keep walking'],
        'outcomes': ['cabin', 'continue'],
        'image': 'https://example.com/cabin.jpg'  # Image URL for this step
    },
    'right_path': {
        'text': "Jangirii encounters a pack of wolves. Should he 'run' or 'climb a tree'?",
        'choices': ['run', 'climb a tree'],
        'outcomes': ['game_over', 'tree_top'],
        'image': 'https://example.com/wolves.jpg'  # Image URL for this step
    },
    'cabin': {
        'text': "Inside the cabin, Jangirii finds a treasure chest. Should he 'open' it or 'ignore' it?",
        'choices': ['open', 'ignore'],
        'outcomes': ['win', 'continue'],
        'image': 'https://example.com/treasure.jpg'  # Image URL for this step
    },
    'tree_top': {
        'text': "Jangirii reaches the tree's top and is safe from the wolves. Should he 'wait' or 'climb down'?",
        'choices': ['wait', 'climb down'],
        'outcomes': ['win', 'game_over'],
        'image': 'https://example.com/safe_tree.jpg'  # Image URL for this step
    },
    # Add more nodes with text, choices, outcomes, and image URLs...
    'win': {
        'text': "Congratulations! Jangirii found the treasure and won the game.",
        'choices': [],
        'outcomes': [],
        'image': 'https://example.com/winning_image.jpg'  # Image URL for the win scenario
    },
    'game_over': {
        'text': "Game over! Jangirii didn't survive the adventure.",
        'choices': [],
        'outcomes': [],
        'image': 'https://example.com/game_over.jpg'  # Image URL for the game over scenario
    }
}

# Function to display a story node and get user input for choices.
def display_story_node(node):
    st.write(story[node]['text'])
    if 'image' in story[node]:
        st.image(story[node]['image'], use_container_width=True)  # Display the image
    if story[node]['choices']:
        choice = st.selectbox("Jangirii's choice:", story[node]['choices'])
        next_node = story[node]['outcomes'][story[node]['choices'].index(choice)]
        return next_node
    else:
        if node == 'win':
            st.success("Congratulations! Jangirii found the treasure and won the game.")
        else:
            st.error("Game over! Jangirii didn't survive the adventure.")
        return node  # No choices, the game is over

# Streamlit app
st.title("Jangirii's Choose Your Adventure Game")

current_node = 'start'
while current_node not in ['win', 'game_over']:
    current_node = display_story_node(current_node)

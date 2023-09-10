import streamlit as st

# Define the story as a dictionary where each key represents a story node.
story = {
    'start': {
        'text': "Jangirii wakes up in a mysterious forest. Should he 'go left' or 'go right'?",
        'choices': ['go left', 'go right'],
        'outcomes': ['left_path', 'right_path']
    },
    'left_path': {
        'text': "Jangirii finds an abandoned cabin. Should he 'enter' or 'keep walking'?",
        'choices': ['enter', 'keep walking'],
        'outcomes': ['cabin', 'continue']
    },
    'right_path': {
        'text': "Jangirii encounters a pack of wolves. Should he 'run' or 'stand still'?",
        'choices': ['run', 'stand still'],
        'outcomes': ['continue', 'continue']
    },
    'cabin': {
        'text': "Inside the cabin, Jangirii finds a treasure chest. Should he 'open' it or 'ignore' it?",
        'choices': ['open', 'ignore'],
        'outcomes': ['win', 'continue']
    },
    'continue': {
        'text': "Jangirii continues his journey deeper into the forest.",
        'choices': [],
        'outcomes': ['decision_5', 'decision_6', 'decision_7', 'decision_8', 'decision_9', 'decision_10', 'decision_11', 'decision_12', 'decision_13', 'decision_14']
    },
    'decision_5': {
        'text': "Jangirii follows the riverbank and discovers a hidden path behind a waterfall. Should he 'venture behind the waterfall' or 'climb to higher ground'?",
        'choices': ['venture behind the waterfall', 'climb to higher ground'],
        'outcomes': ['win', 'win']
    },
    'decision_6': {
        'text': "Jangirii decides to camp for the night to rest. In the morning, he continues his journey.",
        'choices': [],
        'outcomes': ['win']
    },
    'decision_7': {
        'text': "Jangirii keeps wandering through the forest, but he finds a friendly hermit who offers him food and shelter. Should he 'accept the hermit's help' or 'decline and keep walking'?",
        'choices': ['accept the hermit\'s help', 'decline and keep walking'],
        'outcomes': ['win', 'win']
    },
    'decision_8': {
        'text': "Jangirii accepts the creature's help and follows it deeper into the forest. Eventually, he reaches the heart of the Enchanted Forest.",
        'choices': [],
        'outcomes': ['win']
    },
    'decision_9': {
        'text': "Jangirii declines the hermit's offer and continues walking. Eventually, he finds his way out of the forest.",
        'choices': [],
        'outcomes': ['win']
    },
    # Add more pages and decisions here...
    'win': {
        'text': "Congratulations! Jangirii found the treasure and won the game.",
        'choices': [],
        'outcomes': []
    }
}

# Function to display a story node and get user input for choices.
def display_story_node(node):
    st.write(story[node]['text'])
    if story[node]['choices']:
        choice = st.selectbox("Jangirii's choice:", story[node]['choices'])
        next_node = story[node]['outcomes'][story[node]['choices'].index(choice)]
        return next_node
    else:
        return node

# Streamlit app
st.title("Jangirii's Choose Your Adventure Game")

current_node = 'start'
while current_node not in ['win']:
    current_node = display_story_node(current_node)

st.success("Congratulations! Jangirii found the treasure and won the game.")

import streamlit as st
import random
from constants import random_questions


def init_values(key, value=None):
    """
    set a key in st.session_state to a given value if it does not already exist
    session_states: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
    """
    if key not in st.session_state:
        st.session_state[key] = value


def random_question():
    question = random.choice(random_questions)
    st.session_state.question = question
    st.markdown(question)
    return question


def validate_question(question):
    if not question:
        st.warning("Please write a question, or submit a random question.")
        return False
    return True

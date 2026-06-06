import streamlit as st


def show_error_card(title, message):

    st.markdown(
        f"""
        <div class="error-card">
            <strong>{title}</strong><br>
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )


def show_success_card(title, message):

    st.markdown(
        f"""
        <div class="success-card">
            <strong>{title}</strong><br>
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )


def show_custom_card(title, content):

    st.markdown(
        f"""
        <div class="custom-card">
            <h4>{title}</h4>
            <p>{content}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def validate_input(text):

    words = len(text.split())
    characters = len(text)

    if not text.strip():

        return False, "Please enter some text."

    if words > 1000:

        return False, (
            "Maximum limit is 1000 words."
        )

    if characters > 7000:

        return False, (
            "Maximum limit is 7000 characters."
        )

    return True, ""


def initialize_session_state():

    defaults = {

        "analyzed": False,

        "corrected_text": "",

        "grammar_errors": [],

        "spelling_errors": [],

        "punctuation_errors": [],

        "sentiment_result": None,

        "statistics_result": None,

        "readability_result": None,

        "suggestions_result": None,

        "paraphrased_text": "",

        "summary_text": ""
    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value
import streamlit as st

from utils.corrections import TextCorrector
from utils.sentiment import SentimentAnalyzer
from utils.statistics import TextStatistics
from utils.readability import ReadabilityAnalyzer
from utils.suggestions import WritingSuggestions
from utils.paraphrase import Paraphraser
from utils.summarize import Summarizer
from utils.config import HF_API_KEY, MAX_WORDS, MAX_CHARACTERS

# ------------------------------
# OBJECTS
# ------------------------------

corrector = TextCorrector()
sentiment_analyzer = SentimentAnalyzer()
statistics_analyzer = TextStatistics()
readability_analyzer = ReadabilityAnalyzer()
suggestion_analyzer = WritingSuggestions()
paraphraser = Paraphraser(HF_API_KEY)
summarizer = Summarizer(HF_API_KEY)

# ------------------------------
# PAGE CONFIG
# ------------------------------

st.set_page_config(page_title="WriteWise", page_icon="📝", layout="wide")

# ------------------------------
# SESSION STATE
# ------------------------------

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "corrected_text" not in st.session_state:
    st.session_state.corrected_text = ""

if "errors" not in st.session_state:
    st.session_state.errors = {}

if "sentiment" not in st.session_state:
    st.session_state.sentiment = {}

if "statistics" not in st.session_state:
    st.session_state.statistics = {}

if "readability" not in st.session_state:
    st.session_state.readability = {}

if "suggestions" not in st.session_state:
    st.session_state.suggestions = []

if "paraphrased_text" not in st.session_state:
    st.session_state.paraphrased_text = ""

if "summary_text" not in st.session_state:
    st.session_state.summary_text = ""

# ------------------------------
# CUSTOM CSS
# ------------------------------


def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()

# ------------------------------
# SIDEBAR
# ------------------------------

with st.sidebar:

    st.markdown("# WriteWise")

    st.markdown("---")

    st.markdown("### Features")

    st.markdown("""
✅ Grammar Correction

✅ Spelling Correction

✅ Punctuation Correction

✅ Sentiment Analysis

✅ Readability Analysis

✅ Writing Suggestions

✅ Paraphrasing

✅ Summarization
""")

    st.markdown("---")

    st.markdown("### Limits")

    st.info("""
Maximum Input

• 1000 Words

• 7000 Characters
""")

# ------------------------------
# HEADER
# ------------------------------

st.markdown(
    """
<div class="hero">
<h1>WriteWise</h1>
<p>Correct • Analyze • Improve</p>
</div>
""",
    unsafe_allow_html=True,
)

# ------------------------------
# INPUT SECTION
# ------------------------------

st.markdown("## Enter Your Text")

user_text = st.text_area(
    "", height=250, placeholder="Paste or type your content here..."
)

word_count = len(user_text.split())
char_count = len(user_text)

col1, col2 = st.columns(2)

with col1:
    st.caption(f"Words: {word_count}/{MAX_WORDS}")

with col2:
    st.caption(f"Characters: {char_count}/{MAX_CHARACTERS}")

# ------------------------------
# ANALYZE BUTTON
# ------------------------------

analyze = st.button("✨ Let's Go!", use_container_width=True)

if analyze:

    if not user_text.strip():

        st.warning("Please enter some text.")

        st.stop()

    if word_count > MAX_WORDS:

        st.error("Word limit exceeded.")

        st.stop()

    if char_count > MAX_CHARACTERS:

        st.error("Character limit exceeded.")

        st.stop()

    with st.spinner("Analyzing your writing..."):

        st.session_state.errors = corrector.get_all_errors(user_text)

        st.session_state.corrected_text = corrector.get_corrected_text(user_text)

        st.session_state.sentiment = sentiment_analyzer.analyze(user_text)

        st.session_state.statistics = statistics_analyzer.get_statistics(user_text)

        st.session_state.readability = readability_analyzer.analyze(user_text)

        st.session_state.suggestions = suggestion_analyzer.analyze(user_text)

        st.session_state.analysis_done = True

# --------------------------------------------------
# RESULTS SECTION
# --------------------------------------------------

if st.session_state.analysis_done:

    # ------------------------------------------
    # GRAMMAR & WRITING CORRECTIONS
    # ------------------------------------------

    st.markdown("---")
    st.markdown("# Grammar & Writing Corrections")

    tab1, tab2, tab3 = st.tabs(["Grammar", "Spelling", "Punctuation"])

    # ---------- Grammar ----------

    with tab1:

        grammar_errors = st.session_state.errors.get("grammar", [])

        if grammar_errors:

            for error in grammar_errors:

                st.error(f"Error: {error['error']}")

                if error.get("suggestion"):

                    st.success(f"Suggestion: {error['suggestion']}")

        else:

            st.success("No grammar issues found.")

    # ---------- Spelling ----------

    with tab2:

        spelling_errors = st.session_state.errors.get("spelling", [])

        if spelling_errors:

            for error in spelling_errors:

                st.error(f"Error: {error['error']}")

                if error.get("suggestion"):

                    st.success(f"Suggestion: {error['suggestion']}")

        else:

            st.success("No spelling issues found.")

    # ---------- Punctuation ----------

    with tab3:

        punctuation_errors = st.session_state.errors.get("punctuation", [])

        if punctuation_errors:

            for error in punctuation_errors:

                st.error(f"Error: {error['error']}")

                if error.get("suggestion"):

                    st.success(f"Suggestion: {error['suggestion']}")

        else:

            st.success("No punctuation issues found.")

    # ------------------------------------------
    # CORRECTED TEXT
    # ------------------------------------------

    st.markdown("### Corrected Text")

    st.text_area("Corrected Version", value=st.session_state.corrected_text, height=200, key="corrected_output")

    # ------------------------------------------
    # SENTIMENT ANALYSIS
    # ------------------------------------------

    st.markdown("---")
    st.markdown("# Sentiment Analysis")

    sentiment = st.session_state.sentiment

    col1, col2 = st.columns(2)

    with col1:

        st.metric("Sentiment", sentiment.get("sentiment", "Unknown"))

    with col2:

        st.metric("Confidence", f"{sentiment.get('confidence',0)}%")

    st.info(sentiment.get("reason", "No explanation available."))

    # ------------------------------------------
    # READABILITY INSIGHTS
    # ------------------------------------------

    st.markdown("---")
    st.markdown("# Readability Insights")

    stats = st.session_state.statistics

    readability = st.session_state.readability

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:

        st.metric("Score", readability.get("score", "-"))

    with c2:

        st.metric("Level", readability.get("level", "-"))

    with c3:

        st.metric("Reading Time", stats.get("reading_time", "-"))

    with c4:

        st.metric("Words", stats.get("word_count", 0))

    with c5:

        st.metric("Characters", stats.get("character_count", 0))

    st.info(readability.get("description", ""))

    # ------------------------------------------
    # WRITING SUGGESTIONS
    # ------------------------------------------

    st.markdown("---")
    st.markdown("# Writing Suggestions")

    suggestions = st.session_state.suggestions

    if suggestions:

        for item in suggestions:

            st.warning(f"{item['type']} : " f"{item['message']}")

    else:

        st.success("No major writing issues detected.")
    # ------------------------------------------
    # AI TOOLS
    # ------------------------------------------

    st.markdown("---")
    st.markdown("# AI Tools")

    p_col, s_col = st.columns(2)

    # ==========================================
    # PARAPHRASE
    # ==========================================

    with p_col:

        st.markdown("### ✨ Paraphrase")

        st.text_area(
            "Paraphrased Text",
            value=st.session_state.paraphrased_text,
            height=220,
            key="paraphrase_output",
        )

        if st.button("Generate Paraphrased Version", use_container_width=True, key="paraphrase_btn"):

            with st.spinner("Generating paraphrased text..."):

                st.session_state.paraphrased_text = paraphraser.paraphrase(user_text)


    # ==========================================
    # SUMMARIZATION
    # ==========================================

    with s_col:

        st.markdown("### 📝 Summarize")

        st.text_area(
            "Summary",
            value=st.session_state.summary_text,
            height=220,
            key="summary_output",
        )

        if st.button("Generate Summary", use_container_width=True,key="summary_btn"):

            with st.spinner("Generating summary..."):

                st.session_state.summary_text = summarizer.summarize(user_text)



# ------------------------------------------------
# FOOTER
# ------------------------------------------------

st.markdown("---")

st.caption("WriteWise • AI Writing Assistant • Built with Streamlit and Hugging Face")

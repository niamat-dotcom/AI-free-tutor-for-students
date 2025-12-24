

# import streamlit as st
# from collections import Counter
# from fpdf import FPDF

# # ---------------- CONFIG ----------------
# st.set_page_config(
#     page_title="🌟 World-Class AI Tutor",
#     page_icon="🎓",
#     layout="wide"
# )

# SUBJECTS = {
#     "SAT English": ["Reading", "Writing", "Vocabulary"],
#     "SAT Math": ["Algebra", "Problem Solving", "Geometry"],
#     "Duolingo English Test": ["Writing", "Speaking"],
#     "Python Programming": ["Basics", "OOP"]
# }

# # ---------------- SESSION ----------------
# st.session_state.setdefault("chat", [])
# st.session_state.setdefault("analytics", [])

# # ---------------- UTIL ----------------
# def clean_text(text):
#     return text.encode("latin-1", "ignore").decode("latin-1")

# # ---------------- OFFLINE KNOWLEDGE BASE ----------------
# OFFLINE_KNOWLEDGE = {
#     "verb": (
#         "**Verb (Clear & Exam-Focused Explanation)**\n\n"
#         "A **verb** is a word that shows:\n"
#         "• an **action** → run, eat, study\n"
#         "• a **state** → is, am, are\n"
#         "• a **condition** → seem, become\n\n"
#         "**Examples:**\n"
#         "• I **study** every day.\n"
#         "• She **is** happy.\n"
#         "• They **run** fast.\n\n"
#         "**SAT / Duolingo Tip:**\n"
#         "Always check **tense** and **subject-verb agreement**."
#     ),

#     "noun": (
#         "**Noun** names a person, place, thing, or idea.\n\n"
#         "Examples: student, city, book, freedom."
#     ),

#     "adjective": (
#         "**Adjective** describes a noun.\n\n"
#         "Examples: big house, fast car, intelligent student."
#     ),

#     "python variable": (
#         "**Python Variable**\n\n"
#         "A variable stores data in memory.\n\n"
#         "Example:\n"
#         "`x = 10`"
#     ),

#     "oop": (
#         "**Object-Oriented Programming (OOP)**\n\n"
#         "OOP organizes code using **classes** and **objects**.\n\n"
#         "Main concepts:\n"
#         "• Class\n"
#         "• Object\n"
#         "• Inheritance\n"
#         "• Encapsulation"
#     )
# }

# # ---------------- OFFLINE TUTOR ----------------
# def ask_ai(user_question, topic):
#     q = user_question.lower()

#     for key in OFFLINE_KNOWLEDGE:
#         if key in q:
#             return OFFLINE_KNOWLEDGE[key]

#     return (
#         "**Offline Tutor Mode** 🧠\n\n"
#         "This tutor works **without external APIs** to ensure reliability.\n\n"
#         "Try asking:\n"
#         "• explain verb\n"
#         "• explain noun\n"
#         "• python variable\n"
#         "• oop concepts\n\n"
#         "This design is intentional and admission-ready."
#     )

# # ---------------- PDF ----------------
# def save_pdf(filename, content):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Helvetica", size=12)
#     pdf.multi_cell(0, 8, clean_text(content))
#     pdf.output(filename)

# # ---------------- UI ----------------
# st.title("🌟 World-Class AI Tutor")
# st.caption("Free • Offline-First • Exam-Focused • Admission-Ready")

# tab1, tab2, tab3 = st.tabs(["💬 Tutor", "📝 Practice", "📊 Analytics"])

# # ================= TAB 1 =================
# with tab1:
#     c1, c2, c3 = st.columns(3)
#     subject = c1.selectbox("Subject", SUBJECTS)
#     topic = c2.selectbox("Topic", SUBJECTS[subject])
#     level = c3.selectbox("Difficulty", ["easy", "medium", "hard"])

#     user_msg = st.chat_input("Ask your question...")

#     if user_msg:
#         reply = ask_ai(user_msg, topic)
#         st.session_state.chat.append(("user", user_msg))
#         st.session_state.chat.append(("ai", reply))
#         st.session_state.analytics.append(topic)

#     for role, msg in st.session_state.chat:
#         with st.chat_message("user" if role == "user" else "assistant"):
#             st.markdown(msg)

#     if st.session_state.chat:
#         if st.button("📄 Save Last Answer as PDF"):
#             save_pdf("lesson.pdf", st.session_state.chat[-1][1])
#             st.success("Saved lesson.pdf")
# with tab2:
#     st.info("Practice engine can be expanded without APIs.")
#     st.write("Example practice coming soon.")


# with tab3:
#     if st.session_state.analytics:
#         counts = Counter(st.session_state.analytics)
#         for k, v in counts.items():
#             st.write(f"📌 {k}: {v} times")
#         st.metric("Total Interactions", len(st.session_state.chat) // 2)
#     else:
#         st.info("No activity yet")

# st.divider()
# st.caption(" • made by nimatullah samadi • for students • Free ai tutor")
import streamlit as st
from collections import Counter
from fpdf import FPDF

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title=" World-Class Offline AI Tutor",
    page_icon="🎓",
    layout="wide"
)

SUBJECTS = {
    "SAT English": ["Reading", "Writing", "Vocabulary"],
    "SAT Math": ["Algebra", "Problem Solving", "Geometry"],
    "Duolingo English Test": ["Writing", "Speaking"],
    "Python Programming": ["Basics", "OOP"]
}

# ---------------- SESSION ----------------
st.session_state.setdefault("chat", [])
st.session_state.setdefault("analytics", [])

# ---------------- UTIL ----------------
def clean_text(text):
    return text.encode("latin-1", "ignore").decode("latin-1")

# ---------------- OFFLINE KNOWLEDGE BASE ----------------
OFFLINE_KNOWLEDGE = {
    "verb": "**Verb**: Shows an action, state, or condition.\nExamples: run, eat, is, am\nTip: Check tense and subject-verb agreement.",
    "noun": "**Noun**: Names a person, place, thing, or idea.\nExamples: student, city, book, freedom.",
    "adjective": "**Adjective**: Describes a noun.\nExamples: big house, fast car.",
    "python variable": "**Python Variable**: Stores data.\nExample: x = 10",
    "oop": "**OOP**: Organizes code with classes & objects.\nConcepts: Class, Object, Inheritance, Encapsulation",
    "algebra": "**Algebra**: Deals with symbols & rules.\nExample: Solve 2x + 5 = 13 → x = 4",
    "geometry": "**Geometry**: Studies shapes & space.\nExample: Area of rectangle = width × height",
    "problem solving": "**Problem Solving**: Approach word problems step by step.\nTip: Identify variables, write equations, solve systematically.",
    "reading": "**Reading**: Focus on comprehension & main ideas.\nTip: Highlight key points and eliminate wrong answers.",
    "writing": "**Writing**: Focus on grammar, punctuation, and sentence structure.\nTip: Check subject-verb agreement, tense, and clarity.",
    "vocabulary": "**Vocabulary**: Learn high-frequency words.\nTip: Use flashcards and practice in context.",
    "speaking": "**Speaking**: Practice pronunciation, fluency, and clarity.\nTip: Record yourself and compare with native speakers.",
    "basics": "**Python Basics**: Variables, data types, operators, loops, functions.\nExample: x = 5; print(x)"
}

# ---------------- OFFLINE TUTOR ----------------
def ask_ai(user_question, topic):
    q = user_question.lower()
    # Check knowledge base
    for key in OFFLINE_KNOWLEDGE:
        if key in q or key in topic.lower():
            answer = OFFLINE_KNOWLEDGE[key]
            return f"{answer}\n\n**Step-by-step guidance:**\n1. Understand the concept.\n2. Look at examples.\n3. Practice exercises.\n4. Check your answer."

    # Generic fallback
    return (
        f"**Tutor (Offline Mode)** 🧠\n"
        f"You asked about '{topic}'.\n"
        "Step-by-step approach:\n"
        "1. Break the question into parts.\n"
        "2. Identify key concepts.\n"
        "3. Solve step by step.\n"
        "4. Review and check your reasoning.\n\n"
        "Even offline, this ensures learning continues."
    )

# ---------------- PDF ----------------
def save_pdf(filename, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 8, clean_text(content))
    pdf.output(filename)

# ---------------- UI ----------------
st.title("🌟 World-Class AI Tutor")
st.caption("Free • Offline-First • Exam-Focused ")

tab1, tab2, tab3 = st.tabs(["💬 Tutor", "📝 Practice", "📊 Analytics"])

# ================= TAB 1: CHAT =================
with tab1:
    c1, c2, c3 = st.columns(3)
    subject = c1.selectbox("Subject", SUBJECTS)
    topic = c2.selectbox("Topic", SUBJECTS[subject])
    level = c3.selectbox("Difficulty", ["easy", "medium", "hard"])

    user_msg = st.chat_input("Ask your question...")

    if user_msg:
        # Add context for chat
        conversation_context = "\n".join([f"{role}: {msg}" for role, msg in st.session_state.chat])
        reply = ask_ai(user_msg, topic)
        st.session_state.chat.append(("user", user_msg))
        st.session_state.chat.append(("ai", reply))
        st.session_state.analytics.append(topic)

    # Display chat
    for role, msg in st.session_state.chat:
        with st.chat_message("user" if role == "user" else "assistant"):
            st.markdown(msg)

    # Save last answer as PDF
    if st.session_state.chat:
        if st.button("📄 Save Last Answer as PDF"):
            save_pdf("lesson.pdf", st.session_state.chat[-1][1])
            st.success("Saved lesson.pdf")

# ================= TAB 2: PRACTICE =================
with tab2:
    st.info("Practice engine coming soon. Offline tutor can generate questions manually or via templates.")

# ================= TAB 3: ANALYTICS =================
with tab3:
    if st.session_state.analytics:
        counts = Counter(st.session_state.analytics)
        for k, v in counts.items():
            st.write(f"📌 {k}: {v} times")
        st.metric("Total Interactions", len(st.session_state.chat) // 2)
    else:
        st.info("No activity yet")

st.divider()
st.caption("• Made by Nimatullah Samadi •  World-Class Offline AI Tutor")

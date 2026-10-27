import streamlit as st

st.title("🔥 HOW COOKED AM I?")

st.write("Welcome to the most scientifically accurate university survival test.")

sleep = st.slider("How many hours do you sleep?", 0, 12, 6)

assignments = st.slider(
    "How many assignments do you have unfinished?",
    0, 10, 2
)

procrastination = st.slider(
    "How much do you procrastinate?",
    0, 100, 50
)

coffee = st.slider(
    "How many coffees do you drink per day?",
    0, 10, 2
)

if st.button("CALCULATE 🔥"):

    cooked = assignments * 10
    cooked = cooked + procrastination / 2

    if sleep < 5:
        cooked = cooked + 20

    if coffee >= 5:
        cooked = cooked + 10

    if cooked > 100:
        cooked = 100

    st.write("## Your Cooked Score:")

    st.write(str(int(cooked)) + "%")

    if cooked < 30:
        st.success("🟢 You're fine. Somehow.")
        
    elif cooked < 60:
        st.warning("🟡 You're getting toasted.")
        
    elif cooked < 80:
        st.error("🟠 You're pretty cooked.")
        
    else:
        st.error("💀 YOU ARE ABSOLUTELY COOKED.")

        st.write("Academic comeback status: questionable.")
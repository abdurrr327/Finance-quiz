import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="💰 Personal Finance Quiz", layout="wide")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stProgress > div > div > div > div {
            background-color: #f39c12 !important;
        }
        .floating-quote {
            position: fixed;
            top: 50%;
            right: 20px;
            width: 250px;
            padding: 10px;
            background-color: #f8f9fa;
            color: #rtb4tjnt;
            font-size: 16px;
            font-weight: bold;
            border-left: 5px solid #f39c12;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# 🖼️ Add a finance knowledge image at the start
st.image("money.jpg", use_container_width=round)

st.title("💰 Personal Finance Quiz")
st.write("📢 *Test your financial literacy with this engaging quiz!* 🧠")
st.markdown("""
    <div class="floating-quote">
        FREE PALESTINE!
    </div>
""", unsafe_allow_html=True)

quiz_data = [
    {"question": "What is the primary purpose of a budget?", "options": ["To track expenses", "To save for retirement", "To invest in stocks", "To pay taxes"], "answer": "To track expenses"},
    {"question": "What does APR stand for?", "options": ["Annual Percentage Rate", "Annual Payment Rate", "Average Payment Rate", "Annual Profit Rate"], "answer": "Annual Percentage Rate"},
    {"question": "Which of the following is a good practice for saving money?", "options": ["Spending all your income", "Saving a portion of your income", "Borrowing money for luxury items", "Ignoring savings"], "answer": "Saving a portion of your income"},
    {"question": "What is an emergency fund?", "options": ["A fund for vacations", "A fund for unexpected expenses", "A fund for investments", "A fund for daily expenses"], "answer": "A fund for unexpected expenses"},
    {"question": "What is the benefit of compound interest?", "options": ["Interest on the principal only", "Interest on both the principal and accumulated interest", "No interest", "Fixed interest rate"], "answer": "Interest on both the principal and accumulated interest"},
    {"question": "What is the primary function of a financial market?", "options": ["To facilitate the exchange of goods", "To provide a platform for buying and selling financial instruments", "To regulate interest rates", "To manage government debt"], "answer": "To provide a platform for buying and selling financial instruments"},
    {"question": "Which of the following is a characteristic of a bond?", "options": ["Ownership in a company", "Fixed interest payments", "Unlimited liability", "High volatility"], "answer": "Fixed interest payments"},
    {"question": "What does diversification in investment mean?", "options": ["Investing in a single asset", "Spreading investments across various assets to reduce risk", "Investing only in high-risk assets", "Timing the market for maximum returns"], "answer": "Spreading investments across various assets to reduce risk"},
    {"question": "What is the purpose of a credit score?", "options": ["To determine an individual's income", "To assess the creditworthiness of a borrower", "To calculate tax liabilities", "To evaluate investment performance"], "answer": "To assess the creditworthiness of a borrower"},
    {"question": "Which financial instrument represents ownership in a company?", "options": ["Bond", "Stock", "Mutual Fund", "Derivative"], "answer": "Stock"},
    {"question": "What is the time value of money?", "options": ["Money loses value over time due to inflation", "Money available now is worth more than the same amount in the future", "Money can only be invested for a fixed period", "Money has no intrinsic value"], "answer": "Money available now is worth more than the same amount in the future"},
    {"question": "What is a mutual fund?", "options": ["A type of insurance policy", "A pool of funds collected from many investors to invest in securities", "A loan provided by a bank", "A government bond"], "answer": "A pool of funds collected from many investors to invest in securities"},
    {"question": "What is the primary risk associated with investing in stocks?", "options": ["Inflation risk", "Market risk", "Interest rate risk", "Credit risk"], "answer": "Market risk"},
    {"question": "What does the term 'liquidity' refer to in finance?", "options": ["The ability to convert an asset into cash quickly", "The amount of debt a company has", "The profitability of an investment", "The risk associated with an investment"], "answer": "The ability to convert an asset into cash quickly"},
    {"question": "Which of the following is a common method for valuing a company?", "options": ["Price-to-earnings ratio (P/E)", "Dividend yield", "Market capitalization", "All of the above"], "answer": "All of the above"},
]
total_questions = len(quiz_data)

# Personal Details
st.header("👤 Personal Details")
name = st.text_input("**FULL NAME:**")
institute = st.text_input("**INSTITUTE:**")
mail = st.text_input("**EMAIL:**")

score = 0
answers = {}

# Quiz Questions
st.header("📝 Take the Quiz")
for i, q in enumerate(quiz_data):
    st.subheader(f"Question {i + 1}: {q['question']}")
    user_answer = st.radio("Select your answer:", q["options"], index=None, key=f"q_{i}")
    
    answers[q["question"]] = user_answer
    if user_answer == q["answer"]:
        score += 1

# Progress Bar
progress = (len(answers) / total_questions) * 100
st.progress(progress / 100)

if st.button("📊 Submit Quiz"):
    st.header("✅ Your Quiz Results")
    st.success(f"🎯 You scored {score} out of {total_questions}!")
    
    score_percentage = (score / total_questions) * 100
    st.info(f"📊 **Score Percentage:** {score_percentage:.2f}%")

    # Show detailed answer review
    for i, q in enumerate(quiz_data):
        st.write(f"**Q{i + 1}: {q['question']}**")
        st.write(f"📝 **Your Answer:** {answers[q['question']] if answers[q['question']] else 'Not answered'}")
        st.write(f"✅ **Correct Answer:** {q['answer']}")
        st.write("---")

    st.subheader("📊 Your Score Overview")
    fig, ax = plt.subplots(figsize=(4, 3))  # Reduced size
    ax.bar(["Correct", "Incorrect"], [score, total_questions - score], color=["#2ecc71", "#e74c3c"])
    ax.set_ylabel("Number of Questions")
    ax.set_title("Quiz Performance")
    st.pyplot(fig)
    

    user_data = {"Name": name, "Institute": institute, "Email": mail, "Score": score, "Total Questions": total_questions, "Score Percentage": f"{score_percentage:.2f}%"}
    df = pd.DataFrame([user_data])
    csv_data = df.to_csv(index=False)
    st.download_button(label="⬇️ Download Results", data=csv_data, file_name="quiz_results.csv", mime="text/csv")

st.write("🚀 *Keep learning and improving your financial knowledge!* 💡")

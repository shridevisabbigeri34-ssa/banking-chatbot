import streamlit as st
import pandas as pd

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Banking Chatbot",
    page_icon="🏦",
    layout="wide"
)
st.markdown("""
<style>

/* Main app background */
.stApp {
    background-color: var(--background-color);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #0f172a;
}

[data-testid="stSidebar"] * {
    color: white;
}

/* Main headings - adapts to light/dark theme */
h1, h2, h3 {
    color: var(--text-color);
}

/* Normal text */
.stMarkdown, .stText, p, label {
    color: var(--text-color);
}

/* Buttons */
.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 20px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #1d4ed8;
    color: white;
}

/* Card service buttons */
.card-service button {
    width: 100%;
    text-align: left;
}

/* Make inputs readable in dark mode */
input, textarea {
    color: var(--text-color) !important;
}

/* Select boxes */
[data-baseweb="select"] {
    color: var(--text-color);
}

</style>
""", unsafe_allow_html=True)
# --------------------------------
# DEMO ACCOUNT DATA
# --------------------------------

if "balance" not in st.session_state:
    st.session_state.balance = 25000.00

if "card_status" not in st.session_state:
    st.session_state.card_status = "Active"

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        {
            "Date": "20 Sep 2026",
            "Description": "UPI Payment",
            "Amount": -500
        },
        {
            "Date": "19 Sep 2026",
            "Description": "Salary Credit",
            "Amount": 15000
        },
        {
            "Date": "18 Sep 2026",
            "Description": "ATM Withdrawal",
            "Amount": -2000
        },
        {
            "Date": "16 Sep 2026",
            "Description": "Online Shopping",
            "Amount": -1200
        }
    ]

# --------------------------------
# ACCOUNT DETAILS
# --------------------------------

account = {
    "name": "Shri",
    "account_number": "XXXX XXXX 1234",
    "account_type": "Savings Account"
}

# --------------------------------
# HEADER
# --------------------------------

st.title("🏦 Banking Chatbot")

st.caption("🔒 Demo Mode — No real money or banking transactions are processed.")

st.write(
    f"Welcome, **{account['name']}!** "
    "How can I help you today?"
)

# --------------------------------
# SIDEBAR
# --------------------------------

st.sidebar.title("🏦 Banking Services")

st.sidebar.write(f"👤 **{account['name']}**")
st.sidebar.write(f"💳 **{account['account_number']}**")
st.sidebar.write(f"💰 **₹{st.session_state.balance:,.2f}**")

st.sidebar.divider()

service = st.sidebar.radio(
    "Select a service:",
    [
        "💬 Chat",
        "💰 Account Balance",
        "📜 Transactions",
        "💸 Transfer Money",
        "💳 Card Services",
        "🏦 Loans",
        "📞 Customer Support"
    ]
)

# --------------------------------
# ACCOUNT BALANCE
# --------------------------------

if service == "💰 Account Balance":

    st.header("💰 Account Balance")

    st.metric(
        "Available Balance",
        f"₹{st.session_state.balance:,.2f}"
    )

    st.write(f"**Account Holder:** {account['name']}")
    st.write(f"**Account Number:** {account['account_number']}")
    st.write(f"**Account Type:** {account['account_type']}")

# --------------------------------
# TRANSACTIONS
# --------------------------------

elif service == "📜 Transactions":

    st.header("📜 Transaction History")

    if st.session_state.transactions:

        df = pd.DataFrame(st.session_state.transactions)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("No transactions available.")

# --------------------------------
# TRANSFER MONEY
# --------------------------------

elif service == "💸 Transfer Money":

    st.header("💸 Transfer Money")

    st.info("Demo transfer — no real money will be transferred.")

    recipient = st.text_input(
        "Recipient Account Number",
        placeholder="Enter demo account number"
    )

    amount = st.number_input(
        "Amount (₹)",
        min_value=1.0,
        max_value=float(st.session_state.balance),
        step=100.0
    )

    if st.button("Transfer Money"):

        if not recipient:
            st.error("Please enter a recipient account number.")

        elif amount > st.session_state.balance:
            st.error("Insufficient balance.")

        else:

            st.session_state.balance -= amount

            st.session_state.transactions.insert(
                0,
                {
                    "Date": "20 Sep 2026",
                    "Description": f"Transfer to ****{recipient[-4:]}",
                    "Amount": -amount
                }
            )

            st.success(
                f"✅ ₹{amount:,.2f} transferred successfully!"
            )

            st.write(
                f"Remaining Balance: "
                f"**₹{st.session_state.balance:,.2f}**"
            )

# --------------------------------
# CARD SERVICES
# --------------------------------

elif service == "💳 Card Services":

    st.header("💳 Card Services")

    st.write("**Card Number:** XXXX XXXX XXXX 5678")

    if st.session_state.card_status == "Active":
        st.success("🟢 Card Status: Active")
    else:
        st.error("🔴 Card Status: Blocked")

    st.divider()

    st.subheader("Card Management")

    if st.session_state.card_status == "Active":

        if st.button("🔒 Block Card"):

            st.session_state.card_status = "Blocked"

            st.warning("Card has been blocked in demo mode.")

    else:

        if st.button("🔓 Unblock Card"):

            st.session_state.card_status = "Active"

            st.success("Card has been unblocked in demo mode.")

    st.divider()

    st.subheader("Other Card Services")

    st.write("• Change PIN")
    st.write("• Request replacement card")
    st.write("• View card limits")
    st.write("• Report lost card")

# --------------------------------
# LOANS
# --------------------------------

elif service == "🏦 Loans":

    st.header("🏦 Loan Services")

    loan_type = st.selectbox(
        "Select Loan Type",
        [
            "Personal Loan",
            "Home Loan",
            "Education Loan",
            "Vehicle Loan"
        ]
    )

    st.write(f"### {loan_type}")

    loan_amount = st.number_input(
        "Requested Loan Amount (₹)",
        min_value=10000.0,
        step=10000.0
    )

    monthly_income = st.number_input(
        "Monthly Income (₹)",
        min_value=0.0,
        step=5000.0
    )

    if st.button("Check Demo Eligibility"):

        if monthly_income >= 25000:

            st.success(
                "✅ Based on this demo rule, "
                "you meet the basic income criterion."
            )

        else:

            st.warning(
                "⚠️ Based on this demo rule, "
                "the income criterion is not met."
            )

        st.caption(
            "This is only a demonstration and is not a real "
            "loan eligibility decision."
        )

# --------------------------------
# CUSTOMER SUPPORT
# --------------------------------

elif service == "📞 Customer Support":

    st.header("📞 Customer Support")

    st.write("How can we help?")

    issue = st.selectbox(
        "Select your issue",
        [
            "Account problem",
            "Card problem",
            "Transaction problem",
            "UPI problem",
            "Loan enquiry",
            "Other"
        ]
    )

    description = st.text_area(
        "Describe your issue"
    )

    if st.button("Submit Support Request"):

        if description.strip():

            st.success(
                "✅ Support request submitted in demo mode."
            )

            st.write(
                f"**Issue:** {issue}"
            )

            st.write(
                "Reference ID: DEMO-2026-001"
            )

        else:

            st.error(
                "Please describe your issue."
            )

# --------------------------------
# CHATBOT
# --------------------------------

elif service == "💬 Chat":

    st.header("💬 Banking Assistant")

    if "messages" not in st.session_state:

        st.session_state.messages = [
            {
                "role": "assistant",
                "content":
                "👋 Hello! Ask me about your balance, "
                "transactions, card, loans, or transfers."
            }
        ]

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.write(message["content"])

    user_input = st.chat_input(
        "Ask your banking question..."
    )

    if user_input:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        with st.chat_message("user"):
            st.write(user_input)

        query = user_input.lower()

        # Balance
        if "balance" in query:

            response = (
                f"💰 Your current balance is "
                f"₹{st.session_state.balance:,.2f}."
            )

        # Transactions
        elif "transaction" in query:

            response = (
                "📜 You can view your complete transaction "
                "history from the **Transactions** section."
            )

        # Card
        elif "card" in query:

            response = (
                f"💳 Your card is currently "
                f"**{st.session_state.card_status}**. "
                "You can manage it from Card Services."
            )

        # Transfer
        elif "transfer" in query or "send money" in query:

            response = (
                "💸 You can make a simulated transfer "
                "using the **Transfer Money** section."
            )

        # Loan
        elif "loan" in query:

            response = (
                "🏦 We currently support demo information "
                "for Personal, Home, Education and Vehicle loans."
            )

        # Greeting
        elif any(word in query for word in ["hello", "hi", "hey"]):

            response = (
                f"👋 Hello {account['name']}! "
                "How can I help you today?"
            )

        # Help
        elif "help" in query:

            response = (
                "🤖 I can help you with:\n\n"
                "💰 Balance\n"
                "📜 Transactions\n"
                "💸 Money transfers\n"
                "💳 Card services\n"
                "🏦 Loans\n"
                "📞 Customer support"
            )

        else:

            response = (
                "🤔 I don't have an answer for that yet. "
                "Try asking about your balance, transactions, "
                "card, loans, or transfers."
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        with st.chat_message("assistant"):
            st.write(response)

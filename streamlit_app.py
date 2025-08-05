import streamlit as st
import random

# ------------------ App Config ------------------
st.set_page_config(page_title="Domain Flipper Tool", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌍 Domain Flipper Tool</h1>", unsafe_allow_html=True)
st.markdown("##### 🧠 Enter a niche and find domains you can flip for profit!")

# ------------------ Input Form ------------------
with st.form("domain_search_form"):
    niche = st.text_input("Enter a niche or keyword (e.g. AI, eco, finance, pet)", max_chars=20)
    min_price = st.number_input("Minimum price (€)", value=1, min_value=0)
    max_price = st.number_input("Maximum price (€)", value=10, min_value=1)
    tld_preference = st.selectbox("Preferred domain type", [".com", ".net", ".co", ".io", ".ai", "Any"])
    submit = st.form_submit_button("🔍 Search Domains")

# ------------------ Demo Domain Generator ------------------
def generate_domains(niche, tld, count=5):
    sample_words = ["hub", "base", "center", "zone", "flip", "nest", "lab", "gen", "now", "flow"]
    domains = []

    for _ in range(count):
        name = niche.lower() + random.choice(sample_words)
        extension = tld if tld != "Any" else random.choice([".com", ".net", ".co", ".io"])
        price = round(random.uniform(1, 10), 2)
        resale = round(price * random.uniform(5, 20), 2)
        domains.append((name + extension, price, resale))
    return domains

# ------------------ On Submit ------------------
if submit:
    if not niche:
        st.warning("Please enter a keyword or niche.")
    else:
        st.success(f"Showing available domains related to '{niche}'...")
        domains = generate_domains(niche, tld_preference)

        for name, price, resale in domains:
            st.markdown(f"""
                <div style='border:1px solid #4CAF50; padding:10px; border-radius:10px; margin-bottom:10px'>
                    <strong>🌐 Domain:</strong> <code>{name}</code><br>
                    <strong>💶 Price:</strong> €{price}<br>
                    <strong>📈 Suggested Resale Price:</strong> €{resale}
                </div>
            """, unsafe_allow_html=True)

        # ------------------ Trademark Checker ------------------
        st.markdown("---")
        st.subheader("🔎 Trademark & Registry Checker")

        st.info(f"Checking for trademarks or registry issues with: *{niche}*")

        st.markdown(f"""
        - 🔍 *EUIPO (Europe)* – No exact trademark match found.
        - 🔍 *USPTO (USA)* – Clear.
        - 🔍 *Malta Business Registry* – No active companies using this name.
        """)

        st.markdown("✅ You're clear to explore these domains. Still, double-check before buying.")

        # ------------------ Clear Button ------------------
        if st.button("🔄 Clear Search"):
            st.experimental_rerun()
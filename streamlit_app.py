import streamlit as st
import requests

st.set_page_config(page_title="Domain Flipper Tool", layout="wide")

st.title("🌐 Domain Flipper Tool")
st.markdown("Find cheap, available domains with resale potential.")

with st.form("domain_search"):
    niche = st.text_input("Enter a niche or keyword (e.g. tech, pets, crypto):")
    letters = st.text_input("Preferred length or letters (e.g. 4-letter, short, trendy):")
    min_price = st.number_input("Minimum Price (€)", min_value=0.0, value=1.0)
    max_price = st.number_input("Maximum Price (€)", min_value=0.0, value=10.0)
    submitted = st.form_submit_button("🔍 Search")

if submitted:
    with st.spinner("Searching domains..."):
        # Simulated results – in real version this would query GoDaddy or similar
        st.success("Here are some domain suggestions:")
        sample_domains = [
            {"domain": "zexo.com", "price": 7.50, "valuation": 2500},
            {"domain": "pynkz.com", "price": 5.99, "valuation": 1800},
            {"domain": "cyvoa.com", "price": 6.49, "valuation": 2200},
        ]

        for d in sample_domains:
            st.write(f"🟢 *{d['domain']}* - €{d['price']} - Est. Resale: €{d['valuation']}")

        st.info("Trademark checks and international registries coming soon!")
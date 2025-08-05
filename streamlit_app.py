import streamlit as st

# --- Title ---
st.title("Domain Flipper AI Tool")

# --- Description ---
st.markdown("""
Use this tool to search for affordable and trendy domain names.  
You can filter by niche, number of letters, and price range in Euros.
""")

# --- Inputs ---
niche = st.text_input("Enter niche or keyword (optional)")

col1, col2 = st.columns(2)
with col1:
    min_letters = st.number_input("Min letters", min_value=1, max_value=20, value=4)
with col2:
    max_letters = st.number_input("Max letters", min_value=1, max_value=20, value=4)

col3, col4 = st.columns(2)
with col3:
    min_price = st.number_input("Min price (€)", min_value=1, value=1)
with col4:
    max_price = st.number_input("Max price (€)", min_value=1, value=10)

# --- Buttons ---
col5, col6 = st.columns([1, 1])
search_trigger = col5.button("🔍 Search")
clear_trigger = col6.button("🧹 Clear")

# --- Sample domain data (fake sample for testing) ---
sample_domains = [
    {"name": "ziloq.com", "price": 6.5, "registrar": "Dynadot", "valuation": 1400},
    {"name": "clipzy.com", "price": 9.49, "registrar": "GoDaddy", "valuation": 1150},
    {"name": "quipiq.com", "price": 9.95, "registrar": "NameSilo", "valuation": 890},
    {"name": "trendyhub.com", "price": 8.99, "registrar": "GoDaddy", "valuation": 1200},
    {"name": "snaploop.com", "price": 7.99, "registrar": "Namecheap", "valuation": 950},
]

# --- Filter Logic ---
def filter_domains(niche, min_l, max_l, min_p, max_p):
    results = []
    for domain in sample_domains:
        name = domain["name"]
        base = name.replace(".com", "")
        if (
            (not niche or niche.lower() in name.lower())
            and min_l <= len(base) <= max_l
            and min_p <= domain["price"] <= max_p
        ):
            results.append(domain)
    return results

# --- Display Results ---
if search_trigger:
    matches = filter_domains(niche, min_letters, max_letters, min_price, max_price)
    if matches:
        for domain in matches:
            st.subheader(domain["name"])
            st.write(f"💶 Price: €{domain['price']} at {domain['registrar']}")
            st.write(f"📈 Estimated resale value: €{domain['valuation']}")
            st.markdown("---")
    else:
        st.warning("😕 No matching domains found.")

# --- Clear Search ---
if clear_trigger:
    st.experimental_rerun()

# --- Footer ---
st.info("🛡 Trademark and registry checks coming soon.")
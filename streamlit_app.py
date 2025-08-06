import streamlit as st

# --- App Title ---
st.title("Domain Flipper AI Tool")

# --- Description ---
st.markdown("""
This tool helps you find potentially resellable domains based on your preferences.  
Search by niche, keywords, number of letters, and price range.  
""")

# --- Search Input Fields ---
niche = st.text_input("Enter niche or keyword (optional)")
min_letters = st.number_input("Min letters in domain", min_value=1, max_value=20, value=4)
max_letters = st.number_input("Max letters in domain", min_value=1, max_value=20, value=4)
min_price = st.number_input("Minimum price in EUR", min_value=1, value=1)
max_price = st.number_input("Maximum price in EUR", min_value=10, value=10)

# --- Buttons ---
col1, col2 = st.columns([1, 1])
search_trigger = col1.button("🔍 Search")
clear_trigger = col2.button("🧹 Clear Search")

# --- Function to simulate search ---
def find_domains(niche, min_l, max_l, min_p, max_p):
    import random
    all_domains = [
        ("trendyhub.com", 8.99, "GoDaddy", 1200),
        ("snaploop.com", 7.99, "Namecheap", 950),
        ("ziloq.com", 6.50, "Dynadot", 1400),
        ("clipzy.com", 9.49, "GoDaddy", 1150),
        ("quipiq.com", 9.95, "NameSilo", 890),
    ]

    results = []
    for name, price, registrar, valuation in all_domains:
        if (
            (not niche or niche.lower() in name.lower())
            and min_l <= len(name.replace(".com", "")) <= max_l
            and min_p <= price <= max_p
        ):
            results.append((name, price, registrar, valuation))
    return results

# --- Results Output ---
if search_trigger:
    results = find_domains(niche, min_letters, max_letters, min_price, max_price)
    
    if results:
        for name, price, registrar, valuation in results:
            st.write(f"{name}")
            st.write(f"💶 Price: €{price} from {registrar}")
            st.write(f"📈 Estimated resale value: €{valuation}")
            st.markdown("---")
    else:
        st.warning("😕 No matching domains found.")

if clear_trigger:
    st.experimental_rerun()

# --- Footer ---
st.info("✅ Trademark & International Registry checks coming soon!")





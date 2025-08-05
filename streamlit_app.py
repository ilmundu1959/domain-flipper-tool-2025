import streamlit as st
import random
import pandas as pd

# --- UI Setup ---
st.set_page_config(page_title="Domain Hunter AI", layout="centered")
st.title("🔍 Domain Hunter AI")
st.markdown("Find low-cost, brandable domains based on your niche and filters.")

# --- Session State for Clearing ---
if "clear" not in st.session_state:
    st.session_state.clear = False

# --- User Inputs ---
with st.form("search_form"):
    niche = st.text_input("Enter a niche or keyword (for inspiration only):", value="tech")
    min_price = st.number_input("Minimum Price (€):", min_value=0, value=1)
    max_price = st.number_input("Maximum Price (€):", min_value=1, value=10)
    min_len, max_len = st.slider("Number of letters in domain name:", 2, 20, (4, 8))
    selected_extensions = st.multiselect(
        "Choose allowed extensions:",
        options=[".com", ".net", ".io", ".co", ".ai", ".org"],
        default=[".com"]
    )
    submitted = st.form_submit_button("🔎 Search")
    if st.form_submit_button("❌ Clear Search"):
        st.session_state.clear = True

# --- Reset inputs if cleared ---
if st.session_state.clear:
    st.session_state.clear = False
    st.experimental_rerun()

# --- Domain Generator ---
def generate_brandable_names(niche, min_len, max_len, extensions, count=30):
    word_parts = ["zen", "ly", "hub", "base", "flip", "snap", "gen", "pulse", "loop", "deck", "boost"]
    domains = []

    for _ in range(count * len(extensions)):
        part1 = random.choice(word_parts)
        part2 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(min_len-2, max_len-2)))
        domain = part1 + part2
        domain = domain[:max_len]
        full_domain = domain + random.choice(extensions)
        domains.append(full_domain)
    
    return list(set(domains))

# --- Simulate domain availability ---
def check_availability(domains):
    results = []
    for domain in domains:
        price = round(random.uniform(1, 1500), 2)
        registrar = random.choice(['GoDaddy', 'Namecheap', 'Google Domains', 'IONOS', 'Hover'])
        resale_est = round(price * random.uniform(1.4, 3.2), 2)
        results.append({
            "Domain": domain,
            "Price (€)": price,
            "Registrar": registrar,
            "Estimated Resale (€)": resale_est
        })
    return results

# --- Run Search ---
if submitted:
    if not selected_extensions:
        st.error("Please select at least one domain extension.")
    else:
        generated_domains = generate_brandable_names(niche, min_len, max_len, selected_extensions)
        results = check_availability(generated_domains)
        filtered = [r for r in results if min_price <= r["Price (€)"] <= max_price]

        if filtered:
            st.success(f"Found {len(filtered)} domain(s) matching your criteria.")
            df = pd.DataFrame(filtered)
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("No domains found with your filters. Try adjusting the extension, price, or name length.")

# --- Footer ---
st.markdown("---")
st.markdown("🔐 Trademark checks & international registries coming soon.")

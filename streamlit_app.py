import streamlit as st import random import pandas as pd

--- UI Setup ---

st.set_page_config(page_title="Domain Hunter AI", layout="centered") st.title("🔍 Domain Hunter AI") st.markdown("Find resellable, low-cost domains based on niche, length, and price range.")

--- User Inputs ---

niche = st.text_input("Enter niche or keyword:", "tech") min_price = st.number_input("Min price (EUR):", min_value=1, value=1) max_price = st.number_input("Max price (EUR):", min_value=1, value=10) min_length, max_length = st.slider("Domain name length (min to max characters):", 2, 20, (4, 8))

if st.button("Clear Search"): st.experimental_rerun()

--- Domain Generator ---

def generate_domain_names(niche, min_len, max_len, count=20): extensions = ['.com', '.net', '.io'] domains = [] for _ in range(count): name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(min_len, max_len))) domain = f"{name}{random.choice(extensions)}" domains.append(domain) return list(set(domains))

--- Simulated Domain Availability & Pricing ---

def check_availability(domains): results = [] for domain in domains: price = round(random.uniform(1, 1500), 2) registrar = random.choice(['GoDaddy', 'Namecheap', 'Google Domains']) retail_price = round(price * random.uniform(1.5, 2.5), 2) results.append({ "Domain": domain, "Price (EUR)": price, "Registrar": registrar, "Estimated Resale (EUR)": retail_price }) return results

--- Main Search Logic ---

if niche: domains = generate_domain_names(niche, min_length, max_length) checked = check_availability(domains) filtered = [d for d in checked if min_price <= d['Price (EUR)'] <= max_price]

if filtered:
    st.success(f"Found {len(filtered)} matching domains:")
    df = pd.DataFrame(filtered)
    st.dataframe(df, use_container_width=True)
else:
    st.warning("No domains found in that price range. Try adjusting your filters.")

--- Coming Soon Message ---

st.markdown("""

🔐 Trademark check & International registry alerts coming soon. """)
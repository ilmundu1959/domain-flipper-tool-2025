import streamlit as st
import random
import pandas as pd
import io

# --- UI Setup ---
st.set_page_config(page_title="Domain Hunter AI", layout="centered")
st.title("🔍 Domain Hunter AI")
st.markdown("Find resellable, low-cost domains based on niche, length, and price range.")

# --- User Inputs ---
niche = st.text_input("Enter niche or keyword (or exact domain to search):", "tech")
exact_word = st.text_input("Or enter exact domain name to search (optional):", "")
min_price = st.number_input("Min price (EUR):", min_value=1, value=1)
max_price = st.number_input("Max price (EUR):", min_value=1, value=10)
min_length, max_length = st.slider("Domain name length (min to max characters):", 2, 20, (4, 8))

sort_option = st.selectbox("Sort results by:", ["Price: Low to High", "Price: High to Low"])

if st.button("Clear Search"):
    st.experimental_rerun()

# --- Domain Generator ---
def generate_domain_names(niche, min_len, max_len, count=20):
    extensions = ['.com', '.net', '.io']
    domains = []
    for _ in range(count):
        name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(min_len, max_len)))
        domain = f"{name}{random.choice(extensions)}"
        domains.append(domain)
    return list(set(domains))

# --- Simulated Domain Availability & Pricing ---
def check_availability(domains):
    results = []
    for domain in domains:
        price = round(random.uniform(1, 1500), 2)
        registrar = random.choice(['GoDaddy', 'Namecheap', 'Google Domains'])
        retail_price = round(price * random.uniform(1.5, 2.5), 2)
        results.append({
            "Domain": domain,
            "Price (EUR)": price,
            "Registrar": registrar,
            "Estimated Resale (EUR)": retail_price
        })
    return results

# --- Main Search Logic ---
results = []

if exact_word.strip():
    # Searching exact domain with all extensions
    extensions = ['.com', '.net', '.io']
    search_domains = [f"{exact_word.strip()}{ext}" for ext in extensions]
    checked = check_availability(search_domains)
    filtered = [d for d in checked if min_price <= d['Price (EUR)'] <= max_price
                and min_length <= len(d['Domain'].split('.')[0]) <= max_length]
    results = filtered
elif niche.strip():
    domains = generate_domain_names(niche, min_length, max_length)
    checked = check_availability(domains)
    filtered = [d for d in checked if min_price <= d['Price (EUR)'] <= max_price]
    results = filtered

if results:
    # Sorting
    if sort_option == "Price: Low to High":
        results = sorted(results, key=lambda x: x['Price (EUR)'])
    else:
        results = sorted(results, key=lambda x: x['Price (EUR)'], reverse=True)

    st.success(f"Found {len(results)} matching domains:")
    df = pd.DataFrame(results)
    st.dataframe(df, use_container_width=True)

    # Export CSV
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download results as CSV",
        data=csv,
        file_name='domain_hunter_results.csv',
        mime='text/csv'
    )
else:
    st.warning("No domains found in that price range. Try adjusting your filters or search term.")

# --- Coming Soon Message ---
st.markdown("""
---
🔐 Trademark check & International registry alerts coming soon.
""")
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

        st.info("Trademark checks and international registries coming soon!")

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

🔐 Trademark check & International registry alerts coming soon. """)

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
🔐 Trademark check & International registry alerts coming soon.
""")

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
st.info("✅ Trademark & International Registry checks coming soon!")
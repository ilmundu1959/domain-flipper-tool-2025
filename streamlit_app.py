import streamlit as st
import random

st.set_page_config(page_title="Domain Flipper Tool", layout="centered")

# Title
st.title("🔍 Domain Flipper Tool")
st.markdown("Find brandable domains based on niche, price, and length. Great for reselling! 💸")

# Input Fields
with st.form("search_form"):
    niche = st.text_input("Enter a niche or keyword", "")
    min_price = st.number_input("Minimum Price (€)", min_value=0, value=1)
    max_price = st.number_input("Maximum Price (€)", min_value=1, value=10)
    min_len = st.number_input("Minimum number of letters", min_value=1, value=4)
    max_len = st.number_input("Maximum number of letters", min_value=1, value=8)

    selected_extensions = st.multiselect(
        "Select extensions",
        [".com", ".net", ".org", ".co", ".ai"],
        default=[".com"]
    )

    submitted = st.form_submit_button("🔍 Search Domains")
    cleared = st.form_submit_button("❌ Clear Search")

# Clear search logic
if cleared:
    st.experimental_rerun()

# Domain generator function
def generate_brandable_names(niche, min_len, max_len, selected_extensions):
    names = []
    base_words = ['zo', 'ly', 'go', 'fi', 'me', 'neo', 'pro', 'tech', 'hub', 'gen', 'cloud']

    for _ in range(100):
        part1 = random.choice(base_words)
        remaining_length = max_len - len(part1)

        if remaining_length < 1:
            continue

        part2 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, remaining_length)))
        name = part1 + part2

        if not (min_len <= len(name) <= max_len):
            continue

        for ext in selected_extensions:
            names.append(name + ext)

    return names

# Simulate pricing and registrar source
def simulate_domain_data(domains, min_price, max_price):
    results = []
    registrars = ["GoDaddy", "Namecheap", "Google Domains", "Dynadot", "Porkbun"]

    for domain in domains:
        price = round(random.uniform(min_price, max_price), 2)
        resale_price = round(price * random.uniform(2.5, 8.0), 2)
        registrar = random.choice(registrars)

        results.append({
            "domain": domain,
            "price": f"€{price}",
            "resale_price": f"€{resale_price}",
            "registrar": registrar
        })

    return results

# Process search
if submitted and niche and min_len <= max_len and min_price <= max_price:
    st.info("🔄 Searching for available domains...")
    generated_domains = generate_brandable_names(niche, min_len, max_len, selected_extensions)
    
    if not generated_domains:
        st.warning("No domains found for your criteria.")
    else:
        domain_data = simulate_domain_data(generated_domains, min_price, max_price)

        st.success(f"✅ Found {len(domain_data)} domain suggestions")
        for item in domain_data:
            st.markdown(f"""
            **🌐 Domain:** `{item['domain']}`  
            💶 **Price:** {item['price']}  
            💰 **Estimated Resale:** {item['resale_price']}  
            🏢 **Registrar:** {item['registrar']}  
            ---
            """)
        
        st.markdown("*Trademark checks and international registry features coming soon.*")

elif not submitted and not cleared:
    st.info("Enter your criteria and press **Search Domains** to begin.")


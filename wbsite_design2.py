import streamlit as st

# Page config
st.set_page_config(
    page_title="Your Company Name",
    page_icon="🧭",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        h1, h2, h3 {
            color: #004aad;
        }
        .btn-primary {
            background-color: #004aad;
            color: white;
            padding: 0.6em 1.2em;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            display: inline-block;
            margin-top: 1em;
        }
        .socials a {
            margin-right: 1rem;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
# st.image("logo.png", width=150)  # Uncomment if logo is available
st.title("Welcome to Your Company Name")
st.subheader("Innovative Solutions. Trusted Results.")

st.markdown('<a href="#contact-us" class="btn-primary">Contact Us</a>', unsafe_allow_html=True)

# --- About Us ---
st.header("About Us")
st.write("""
**Your Company Name** is a leading provider of [products/services] tailored for businesses and individuals who seek excellence, innovation, and measurable results. 
We specialize in providing customized solutions that align with your goals, values, and growth trajectory.

Founded in [Year], we’ve worked with clients across multiple industries including healthcare, finance, technology, and education. 
Our mission is simple: to empower organizations through intelligent design, cutting-edge technology, and transparent collaboration.

Whether you are a startup looking for scalable services or an enterprise in need of transformation, we’re here to help you thrive.
""")

# --- Services ---
st.header("Our Services")
services = {
    "🔹 Service One": "Comprehensive [describe what it is and how it helps the client].",
    "🔹 Service Two": "Designed for clients who need [brief benefit or feature].",
    "🔹 Service Three": "Our premium solution includes [key features or outcomes]."
}

for title, desc in services.items():
    st.subheader(title)
    st.write(desc)

# --- Project/Company Description ---
st.header("What We Do")
st.write("""
We bring together creativity, strategy, and technology to help your business scale. 
Our solutions are data-driven and focused on results. We don’t just offer services—we build partnerships that create value.

**Why Choose Us?**

- ✅ Client-first approach
- ✅ Transparent processes and communication
- ✅ Scalable and customizable solutions
- ✅ Dedicated support and consultation

**Industries We Serve:**

- Technology & SaaS
- Healthcare & Pharma
- Finance & Insurance
- Retail & E-commerce
- Education & Non-Profits

Our clients trust us because we deliver measurable results with integrity and innovation.
""")

# --- Website & Social Media ---
st.header("Connect With Us")
st.markdown("""
- 🌐 **Website**: [www.yourcompany.com](https://www.yourcompany.com)
- 📸 **Instagram**: [@yourcompany](https://www.instagram.com/yourcompany)
- 💼 **LinkedIn**: [Your Company LinkedIn](https://www.linkedin.com/company/yourcompany)
- 👍 **Facebook**: [facebook.com/yourcompany](https://www.facebook.com/yourcompany)
- 🐦 **Twitter/X**: [@yourcompany](https://twitter.com/yourcompany)
""")

# --- Contact Section ---
st.markdown('<h2 id="contact-us">Contact Us</h2>', unsafe_allow_html=True)
st.write("📧 Email: contact@yourcompany.com")
st.write("📞 Phone: +91-12345-67890")

with st.form("contact_form"):
    st.subheader("Send us a message")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Submit")

    if submit:
        st.success("Thank you for your message! We'll get back to you soon.")




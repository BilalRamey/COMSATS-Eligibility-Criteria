import streamlit as st
import requests
from bs4 import BeautifulSoup

#Web Scraping Function to Get Eligibility Criteria (if needed for other campuses
def get_eligibility_criteria():
    url = "https://ww2.comsats.edu.pk/internationalstudents/eligibility-criteria.aspx"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find relevant section
        eligibility_section = soup.find('div', class_='eligibility-criteria')  # Adjust as per HTML structure
        
        if eligibility_section:
            criteria_text = eligibility_section.get_text(separator='\n').strip()
            return criteria_text
        else:
            return "Eligibility criteria section not found."

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

#Function to Check Eligibility
def check_eligibility(intermediate_marks, nts_score):
    # Displaying the extracted criteria
    st.subheader("Eligibility Criteria:")
    st.write("1. Minimum 50% marks in Intermediate or equivalent.")
    st.write("2. Minimum 50% marks in the NTS-NAT test.")

    # Compare the user input with eligibility criteria
    if intermediate_marks >= 50 and nts_score >= 50:
        st.success("Congratulations! You are eligible for admission based on your marks.")
    else:
        st.error("Unfortunately, you do not meet the eligibility criteria for admission.")

#Step 3: Streamlit App Structure
def main():
    st.title("COMSATS Admission Eligibility Checker")

    st.write("""
    This application compares your academic marks with the eligibility criteria for BS programs at COMSATS.
    """)
    
    # Input for intermediate marks and NTS score
    intermediate_marks = st.number_input("Enter your Intermediate percentage (e.g., 75.5):", min_value=0.0, max_value=100.0, step=0.1)
    nts_score = st.number_input("Enter your NTS-NAT test score (e.g., 55.0):", min_value=0.0, max_value=100.0, step=0.1)

    if st.button("Check Eligibility"):
        check_eligibility(intermediate_marks, nts_score)

#Run the app
if __name__ == "__main__":
    main()

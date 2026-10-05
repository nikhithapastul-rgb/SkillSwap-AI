import streamlit as st
from services.matching import find_matches

# Page configuration
st.set_page_config(
    page_title="SkillSwap AI",
    page_icon="🤝",
    layout="wide"
)

# Application title
st.title("🤝 SkillSwap AI")
st.subheader(
    "An Intelligent Platform for Skill Exchange and Collaborative Learning"
)

st.write(
    "Learn new skills by connecting with people who have the knowledge "
    "you want and sharing the skills you already know."
)

st.divider()

# User information
st.header("👤 Create Your Skill Profile")

name = st.text_input("Your Name")
email = st.text_input("Your Email")

st.subheader("🎯 Skills You Can Teach")

teach_skills = st.multiselect(
    "Select the skills you can teach",
    [
        "Python",
        "Java",
        "Web Development",
        "SQL",
        "Machine Learning",
        "Communication",
        "Excel"
    ]
)

st.subheader("📚 Skills You Want to Learn")

learn_skills = st.multiselect(
    "Select the skills you want to learn",
    [
        "Python",
        "Java",
        "Web Development",
        "SQL",
        "Machine Learning",
        "Communication",
        "Excel"
    ]
)

# Create profile
if st.button("Create My Profile"):

    if not name.strip() or not email.strip():
        st.warning("Please enter your name and email.")

    elif not teach_skills and not learn_skills:
        st.warning("Please select at least one skill.")

    else:
        st.success(f"Welcome to SkillSwap AI, {name}!")

        st.write("### Your Profile Summary")

        st.write("**Name:**", name)
        st.write("**Email:**", email)

        st.write(
            "**Skills you can teach:**",
            ", ".join(teach_skills)
            if teach_skills
            else "None selected"
        )

        st.write(
            "**Skills you want to learn:**",
            ", ".join(learn_skills)
            if learn_skills
            else "None selected"
        )


# Sample users for testing
users = [
    {
        "name": "Rahul",
        "teaches": ["Java", "SQL"],
        "learns": ["Python"]
    },
    {
        "name": "Ananya",
        "teaches": ["Python", "Machine Learning"],
        "learns": ["Java"]
    },
    {
        "name": "Priya",
        "teaches": ["Excel", "Communication"],
        "learns": ["Python"]
    },
    {
        "name": "Arjun",
        "teaches": ["Web Development", "Java"],
        "learns": ["SQL"]
    },
    {
        "name": "Sneha",
        "teaches": ["SQL", "Python"],
        "learns": ["Web Development"]
    }
]


# Find skill matches
if st.button("🔍 Find Skill Matches"):

    matches = find_matches(
        teach_skills,
        learn_skills,
        users
    )

    if matches:

        st.header("🤝 Your Skill Matches")

        for match in matches:

            st.success(
                f"Match found with {match['name']}! "
                f"Match Score: {match['match_score']}%"
            )

            st.write(
                "**They can teach:**",
                ", ".join(match["teaches"])
            )

            st.write(
                "**They want to learn:**",
                ", ".join(match["learns"])
            )

    else:
        st.info("No matching users found yet.")
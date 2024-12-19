from create_quiz import creat_quiz
from get_questions_v2 import get_questions
from add_questions import add_questions
import pandas as pd
from publish import publish_quiz

query = "solving right triangle"

# create quiz
# insert the query as subtopic and fetch questions
# add questions to quiz
# publish quiz

df = pd.read_csv("low_ssr_queries_jan_march_2023.csv")

for idx, row in df.iterrows():
    query = row['query']
    domain = row['Domain']
    topic = row['Topic']
    skill = row['Skill']
    subSkill = row['Sub-skill']

    create_quiz_data = creat_quiz(title = query, grade = [] , subject = ["Mathematics"])
    print(create_quiz_data)

    questions = get_questions(subtopic = query, topic = topic, language = "English", subject = "Mathematics")

    add_questions(create_quiz_data['quiz_id'], create_quiz_data['draft_id'], questions['data']['questions'])

    publish_quiz(create_quiz_data['quiz_id'], create_quiz_data['draft_id'])

    print(f"Quiz created successfully and published {create_quiz_data['quiz_id']}")

    break





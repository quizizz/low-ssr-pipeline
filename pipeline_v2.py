from create_quiz import create_quiz
from get_questions_v2 import get_questions
from add_questions import add_questions
import pandas as pd
from publish import publish_quiz
from relevance import get_relevance
from similar_questions import get_similar_question
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

    create_quiz_data = create_quiz(title = query, grade = [] , subject = ["Mathematics"])
    print(create_quiz_data)

    x = get_questions(subtopic = query, topic = query, language = "English", subject = "Mathematics")
    print(x['data']['questions'])

    # create a mapping where question_id is the key and the value is the question object
    question_object_mapping = {question['_id']: question for question in x['data']['questions']}

    question_ids = [x['data']['questions'][i]['_id'] for i in range(len(x['data']['questions']))]
    result = get_relevance(question_ids, query)
    print(result)

    result_list = list(result.keys())

    questions_to_keep = set()
    for question_id in result_list:
        try:
            if result[question_id]['relevancyScore'] >= 7:
                print(question_id)
                questions_to_keep.add(question_id)
        except:
            pass

    similar_questions = set()
    for question_id in questions_to_keep:
        for i in range(2):
            try:
                similar_q_result = get_similar_question(question_object_mapping[question_id], create_quiz_data['quiz_id'], create_quiz_data['draft_id'])
                new_question_id = similar_q_result['data']['questions'][0]['_id']
                similar_questions.add(new_question_id)
                question_object_mapping[new_question_id] = similar_q_result['data']['questions'][0]
            except:
                pass

    print(similar_questions)

    # run relevance on the similar questions
    similar_questions_relevance_result = get_relevance(list(similar_questions), query)
    print(similar_questions_relevance_result)

    # add all the questions to the quiz
    similar_question_objects = [question_object_mapping[question_id] for question_id in list(similar_questions)]
    add_questions(create_quiz_data['quiz_id'], create_quiz_data['draft_id'], similar_question_objects)

    questions_to_keep_objects = [question_object_mapping[question_id] for question_id in list(questions_to_keep)]
    add_questions(create_quiz_data['quiz_id'], create_quiz_data['draft_id'], questions_to_keep_objects)

    publish_quiz(create_quiz_data['quiz_id'], create_quiz_data['draft_id'])

    break





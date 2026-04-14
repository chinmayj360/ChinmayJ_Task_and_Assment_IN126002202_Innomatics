from langchain_core.runnables import RunnableLambda
import json

def match(inputs):
    candidate = json.loads(inputs["candidate"])
    jd = inputs["jd"].lower()

    matched_skills = []

    for skill in candidate["skills"]:
        if skill.lower() in jd:
            matched_skills.append(skill)

    score = len(matched_skills) * 25  # simple scoring

    return type("Obj", (), {
        "content": json.dumps({
            "match_score": score,
            "matched_skills": matched_skills
        })
    })()

match_chain = RunnableLambda(match)
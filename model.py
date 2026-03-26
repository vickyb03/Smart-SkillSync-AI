from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_skills(resume, job_desc):
    documents = [resume, job_desc]

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return round(float(similarity[0][0]) * 100, 2)

from math import sqrt

ratings = {
    'User1': {'Movie1': 5, 'Movie2': 3, 'Movie4': 1},
    'User2': {'Movie1': 4, 'Movie4': 1},
    'User3': {'Movie1': 1, 'Movie2': 1, 'Movie4': 5},
    'User4': {'Movie3': 5, 'Movie4': 4}
}

def similarity(user1, user2):
    common = set(ratings[user1]) & set(ratings[user2])
    if not common:
        return 0
    
    sum_sq = sum((ratings[user1][item] - ratings[user2][item])**2 for item in common)
    return 1 / (1 + sqrt(sum_sq))


def recommend(user):
    scores = {}
    
    for other in ratings:
        if other == user:
            continue
        
        sim = similarity(user, other)
        
        for movie in ratings[other]:
            if movie not in ratings[user]:
                scores.setdefault(movie, 0)
                scores[movie] += sim * ratings[other][movie]
    
    
    return sorted(scores, key=scores.get, reverse=True)

print("Recommended for User1:", recommend('User1'))
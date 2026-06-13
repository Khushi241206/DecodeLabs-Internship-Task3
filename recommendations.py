from data import items

def recommend(user_interests):
    recommendations = []

    for item in items:
        score = len(
            set(user_interests).intersection(
                set(item["tags"])
            )
        )

        recommendations.append({
            "name": item["name"],
            "score": score
        })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations
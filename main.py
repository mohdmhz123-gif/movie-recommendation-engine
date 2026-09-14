from movies import movies

genre = input("Enter your favourite genre: ")
minimum_rating = float(input("Enter minimum rating: "))

print("\nRecommended Movies:\n")

recommendations = []

# Find movies that match the user's preferences
for movie in movies:
    if movie["genre"].lower() == genre.lower() and movie["rating"] >= minimum_rating:
        recommendations.append(movie)

# Sort recommendations from highest rating to lowest
recommendations = sorted(
    recommendations,
    key=lambda movie: movie["rating"],
    reverse=True
)

# Display recommendations
for movie in recommendations:
    print(movie["title"])

# Handle no matches
if not recommendations:
    print("No highly-rated movies found.")
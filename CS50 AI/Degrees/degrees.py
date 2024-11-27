import csv
import sys

from util import Node, StackFrontier, QueueFrontier
from collections import deque


# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Add person details to the 'people' dictionary
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set() # Initialize an empty set to hold movie_ids
            }
             # Add to 'names' dictionary: mapping the lowercase name to a set of person_ids
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Add movie details to the 'movies' dictionary
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                # Link the movie to the person in the 'people' dictionary
                people[row["person_id"]]["movies"].add(row["movie_id"])
                 # Link the person to the movie in the 'movies' dictionary
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                  # Ignore entries with invalid person_id or movie_id
                pass


def main():
    """
    Main function to execute when running the program.
    Prompts user for input and finds the degrees of separation
    between two actors.
    """
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]") # Ensures correct command-line usage
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"  # Default to 'large' directory if none is provided

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

     # Prompt user for the source actor's name and retrieve their ID
    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")

    # Prompt user for the target actor's name and retrieve their ID
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    # Find the shortest path between the source and target actors
    path = shortest_path(source, target)

    # Print the result
    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
         # Include the starting person in the path for printing purposes
        path = [(None, source)] + path
        # Loop through and display each step in the path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.
    If no possible path, returns None.
    """
    # Check if source is the same as target
    if source == target:
        return []

    # Initialize the frontier with the starting point
    frontier = deque([[(None, source)]])  # Each element in frontier is a path (a list of (movie_id, person_id) pairs)
    visited = set()  # To keep track of visited nodes to avoid cycles

    while frontier:
        # Get the next path to explore
        path = frontier.popleft()
        _, current_person = path[-1]  # The last person in the current path
        
        # Mark the current person as visited
        if current_person not in visited:
            visited.add(current_person)

            # Explore neighbors (people who starred with this person in a movie)
            for movie_id, neighbor in neighbors_for_person(current_person):
                # If neighbor is the target, we've found the path
                if neighbor == target:
                    return path[1:] + [(movie_id, neighbor)]
                
                # If the neighbor hasn't been visited, add the new path to the frontier
                if neighbor not in visited:
                    new_path = path + [(movie_id, neighbor)]
                    frontier.append(new_path)

    # If we exhaust the frontier and never find the target, return None
    return None


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()  # Run the main function if this script is executed directly

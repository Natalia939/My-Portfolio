import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]: .4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]: .4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.
    """
    probs = {key: 0 for key in corpus}
    n = len(corpus)

    # If the page has no outgoing links, treat it as linking to all pages
    links = corpus[page] if corpus[page] else corpus.keys()

    for p in probs:
        probs[p] = (1 - damping_factor) / n
        if p in links:
            probs[p] += damping_factor / len(links)

    return probs


def sample_pagerank(corpus, damping_factor, num_samples):
    """
    Return PageRank values for each page by sampling `num_samples` pages.
    """
    sampled_counts = {page: 0 for page in corpus}
    current_page = random.choice(list(corpus.keys()))  # Start with a random page

    for _ in range(num_samples):
        sampled_counts[current_page] += 1  # Count visits to each page
        transition_probs = transition_model(corpus, current_page, damping_factor)
        pages = list(transition_probs.keys())
        probabilities = list(transition_probs.values())
        current_page = random.choices(pages, probabilities)[0]

    # Normalize to ensure the total is 1
    total_visits = sum(sampled_counts.values())
    pagerank = {page: count / total_visits for page, count in sampled_counts.items()}

    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating.
    """
    num_pages = len(corpus)
    pagerank = {page: 1 / num_pages for page in corpus}  # Initialize PR values
    threshold = 0.001

    while True:
        new_pagerank = {}
        for page in corpus:
            # Start with the random jump factor
            page_score = (1 - damping_factor) / num_pages

            # Add contributions from all incoming links
            for p in corpus:
                if page in corpus[p]:
                    page_score += damping_factor * (pagerank[p] / len(corpus[p]))
                elif not corpus[p]:  # Handle pages with no links
                    page_score += damping_factor * (pagerank[p] / num_pages)

            new_pagerank[page] = page_score

        # Check for convergence
        converged = all(
            abs(new_pagerank[page] - pagerank[page]) < threshold
            for page in pagerank
        )

        if converged:
            break
        pagerank = new_pagerank.copy()

    # Normalize to ensure the total is 1
    total_score = sum(pagerank.values())
    pagerank = {page: value / total_score for page, value in pagerank.items()}

    return pagerank


if __name__ == "__main__":
    main()

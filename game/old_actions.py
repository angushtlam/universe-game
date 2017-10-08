import time
from queue import Queue

from util import wikipedia as util_wikipedia


def generate_article_adjacency_map(article_id, max_depth=2):
    depth = 0
    result = {}
    new_articles = Queue()

    result[article_id] = depth
    new_articles.put(article_id)
    new_articles.put(None)

    while not new_articles.empty():
        article = new_articles.get()

        if article is None:
            depth += 1

            if depth == max_depth:
                break

            continue

        result[article] = depth

        articles = util_wikipedia.get_article_links_on_article_by_id(article)
        time.sleep(0.5)

        for article in articles:
            # Ignore non-article links
            if not isinstance(int(article), int) or int(article) < 0:
                continue

            if article not in result:
                new_articles.put(article)

        new_articles.put(None)
        print(str(new_articles.qsize()) + ', ' + str(depth))

    return result

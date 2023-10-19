import json
import os
import pandas as pd
import requests
from apikey import CORE_API_KEY as API_KEY

API_ENDPOINT = "https://api.core.ac.uk/v3/"

def query_api(url_fragment, query, limit=100, is_scroll=False, scroll_id=None):

    headers = {"Authorization": "Bearer " + API_KEY}
    query = {"q": query, "limit": limit}

    if is_scroll:
        if scroll_id:
            query["scroll_id"] = scroll_id
        else:
            query["scroll"] = True

    response = requests.post(f"{API_ENDPOINT}{url_fragment}", data=json.dumps(query), headers=headers)

    if response.status_code == 200:
        return response.json(), response.elapsed.total_seconds()
    else:
        print(f"Error code {response.status_code}, {response.content}")

def scroll(search_url, query, extract_info=lambda x: x):
    results = []
    count = 0
    scroll_id = None
    
    while True:
        result, elapsed = query_api(search_url, query, is_scroll=True, scroll_id=scroll_id)
        scroll_id = result["scrollId"]
        hits = result["totalHits"]
        size = len(result["results"])
        if size == 0:
            break
        for hit in result["results"]:
            results.append(extract_info(hit))
        count += size
        print(f"{count}/{hits} {round(elapsed, 2)}s")

    return results

def extract_info(hit):
    # Documentation for all returned fields can be found here: https://api.core.ac.uk/docs/v3#tag/Search/null.
    # Included here are the features we may want to use as features as well as the data we'll need for training (i.e., abstract and text).
    return {
        "id": hit["id"],
        "title": hit["title"],
        "type": hit["documentType"],
        "citations": hit["citationCount"],
        "published_date": hit["publishedDate"],
        "updated_date": hit["updatedDate"],
        # "abstract": hit["abstract"],    # currently not using abstracts
        "text": hit["fullText"],
        "url": hit["downloadUrl"]
    }

if __name__ == '__main__':
    # create dataset per year
    start_year = 2013
    end_year = 2023
    for year in range(start_year, end_year + 1):
        print(f"\n{year}\n")
        if os.path.isfile(f"data/{year}.parquet"):
            continue
        query = f"metabolomics AND language:English AND yearPublished:{year}"
        raw = scroll("search/works", query, extract_info)
        df = pd.DataFrame(raw).set_index("id")
        df.to_parquet(f"data/{year}.parquet")

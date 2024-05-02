from scrapegraphai.graphs import SmartScraperGraph

def task(key:str, url:str, prompt:str, model:str):
    """
    Task that execute the scraping:
        Arguments:
        - url (str): url to scrape
        - prompt (str): prompt
        - model (str): name of the model
        Return:
        - results_df["output"] (dict): result as a dictionary
        - results_df (pd.Dataframe()): result as padnas df
    """

    graph_config = {
        "llm": {
            "model": "ollama/llama3",
            "temperature": 0,
            "format": "json",  # Ollama needs the format to be specified explicitly
            "base_url": "http://localhost:11434",  # set Ollama URL
        },
        "embeddings": {
            "model": "ollama/nomic-embed-text",
            "base_url": "http://localhost:11434",  # set Ollama URL
        },
    }

    # ************************************************
    # Create the SmartScraperGraph instance and run it
    # ************************************************

    smart_scraper_graph = SmartScraperGraph(
        prompt=prompt,
        # also accepts a string with the already downloaded HTML code
        source=url,
        config=graph_config
    )

    result = smart_scraper_graph.run()
    return result

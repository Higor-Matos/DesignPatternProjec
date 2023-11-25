import wikipediaapi


class WikipediaAPI:
    _instance = None  # Atributo privado para armazenar a única instância.

    def __new__(cls):
        # Verifica se a instância já existe, se não, cria uma nova.
        if cls._instance is None:
            cls._instance = super(WikipediaAPI, cls).__new__(cls)
            # Configura a instância com a API da Wikipedia e um user agent específico.
            user_agent = "MyWikiSearchApp/1.0 (meuemail@example.com)"
            cls._instance.wiki = wikipediaapi.Wikipedia(
                language='pt', user_agent=user_agent)

        return cls._instance

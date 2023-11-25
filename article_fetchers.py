
from abc import ABC, abstractmethod
from wikipedia_api import WikipediaAPI

import wikipediaapi

# Padrão Factory Method: Define uma interface comum para criar objetos, mas
# permite que as subclasses decidam qual classe instanciar.


class ArticleFetcher(ABC):
    @abstractmethod
    def fetch(self, query):
        pass

# Subclasse que implementa o método 'fetch' para buscar artigos por título.


class ArticleByTitleFetcher(ArticleFetcher):
    def fetch(self, title):
        title = title.strip()
        if not title:
            return "Por favor, insira um título válido."

        wiki = WikipediaAPI().wiki  # Usa a instância Singleton da API.
        page = wiki.page(title)
        return page.text if page.exists() else "Artigo não encontrado."

# Subclasse que implementa o método 'fetch' para buscar artigos por categoria.


class ArticleByCategoryFetcher(ArticleFetcher):
    def fetch(self, category):
        category = category.strip()
        if not category:
            return "Por favor, insira uma categoria válida."

        wiki = WikipediaAPI().wiki  # Usa a instância Singleton da API.
        cat = wiki.page("Category:" + category)
        if not cat.exists():
            return "Categoria não encontrada."

        return [page.title for page in cat.categorymembers.values()] if cat.categorymembers else "Nenhum artigo encontrado nesta categoria."

# Factory para criar o tipo apropriado de buscador com base no tipo especificado.


class FetcherFactory:
    def get_fetcher(self, fetcher_type):
        if fetcher_type == "title":
            return ArticleByTitleFetcher()
        elif fetcher_type == "category":
            return ArticleByCategoryFetcher()

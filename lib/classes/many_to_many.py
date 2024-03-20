from itertools import count


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be string")
        elif not 5 <= len(title) <= 50:
            raise ValueError("Title must be within 2 and 16 characters")
        elif hasattr(self, "Title"):
            raise AttributeError("Title cannot be reset")
        else:
            self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("author must be author")
        else:
            self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be magazine")
        else:
            self._magazine = magazine


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be string")
        elif len(name) == 0:
            raise ValueError("Please enter name")
        elif hasattr(self, "name"):
            raise AttributeError("Name cannot be reset")
        else:
            self._name = name

    def articles(self):
        return [articles for articles in Article.all if articles.author is self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = list({article.magazine.category for article in self.articles()})
        return topics if topics else None


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be string")
        elif not 2 <= len(name) <= 16:
            raise ValueError("Name must be within 2 and 16 characters")
        else:
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Please enter category")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = list([article.title for article in self.articles()])
        return titles if titles else None

    def contributing_authors(self):
        author_article_count = {}

        for article in self.articles():
            author = article.author
            if author in author_article_count:
                author_article_count[author] += 1
            else:
                author_article_count[author] = 1

        authors_contributions = [
            author for author, count in author_article_count.items() if count > 2
        ]
        return authors_contributions if authors_contributions else None

    @classmethod
    def top_publisher(cls):
        return (
            max(cls.all, key=lambda magazine: len(magazine.articles()))
            if Article.all
            else None
        )

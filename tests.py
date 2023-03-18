import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_twice(self, collector):
        collector.add_new_book('Пикачу')
        collector.add_new_book('Пикачу')

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_book_not_exist(self, collector):
        name, rating = "Спящая красавица", 10
        collector.set_book_rating(name, rating)
        assert collector.get_book_rating(name) is None

    @pytest.mark.parametrize("name, rating", [['Золушка', 6], ['Белоснежка', 8]])
    def test_set_book_rating_true(self, collector, name, rating):
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)
        assert collector.get_book_rating(name) == rating

    @pytest.mark.parametrize("name, rating", [['Золушка', 0], ['Белоснежка', 11]])
    def test_set_book_rating_out_of_range(self, collector, name, rating):
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)
        assert collector.get_book_rating(name) == 1

    def test_get_book_rating_book_not_exist(self, collector):
        name = "Спящая красавица"
        assert collector.get_book_rating(name) is None

    def test_get_books_with_specific_rating_true(self, collector):
        books = {'Золушка': 10, 'Белоснежка': 7}
        for name, rating in books.items():
            collector.add_new_book(name)
            collector.set_book_rating(name, rating)
        assert len(collector.get_books_with_specific_rating(7)) == 1

    def test_add_book_in_favorites_add_one_book(self, collector):
        name = "Красавица и Чудовище"
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)

        assert name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_add_book_twice(self, collector):
        name = "Красавица и Чудовище"
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_book_not_exist(self, collector):
        name = "Красавица и Чудовище"
        collector.add_book_in_favorites(name)

        assert name not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_true(self, collector):
        name = "Холодное сердце"
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)

        assert name not in collector.get_list_of_favorites_books()

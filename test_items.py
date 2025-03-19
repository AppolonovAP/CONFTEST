import time
import pytest

@pytest.mark.parametrize('language', ['es', 'fr'])
def test_add_to_cart_button(browser, language):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # Визуальная проверка, чтобы убедиться, что страница загружена

    # Проверяем наличие кнопки "Добавить в корзину"
    button = browser.find_element("css selector", ".btn-add-to-basket")
    assert button is not None, f"Кнопка добавления в корзину не найдена для языка {language}"
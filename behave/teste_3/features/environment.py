from selenium import webdriver

elementos = {'busca': 'id-search-field'}


def before_all(context):
    context.ff = webdriver.Firefox()
    context.e = elementos


def after_all(context):
    context.ff.quit()

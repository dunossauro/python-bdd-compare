from radish import before
from selenium import webdriver

elementos = {'busca': 'id-search-field'}


@before.each_scenario
def context(scenario):
    scenario.context.e = elementos
    scenario.context.ff = webdriver.Firefox()

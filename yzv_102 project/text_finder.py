import requests
from bs4 import BeautifulSoup
import random


def easy_text_finder():
    '''
    easy text finder finds texts from the internet. In easy texts the user will not be bothered with uppercase letters
    and the words will be more casual. Also the user will not be bothered with some hard punctuations.
    :return:
    '''

    # this is the website for finding texts
    website = requests.get("https://agilefingers.com/texts/burnett-carolyn-judson-the-blue-grass-seminary-girls-on-the-water-en")

    soup = BeautifulSoup(website.content, "html.parser")

    all_text = soup.find("div", {"id": "textForTypingContent"})

    # some manupulation in the text for accesing the paragraphs
    paragraphs = all_text.text.split("\n\n")

    # filtering the length of the paragraphs
    easy_paragraphs = list(filter(lambda x: 125 < len(x) < 225, paragraphs))

    # getting a random text and filtering the text for getting an easier text.
    text = list(filter(lambda ch: ch not in ('''"''', "'"), random.choice(easy_paragraphs)))
    str_text = "".join(text).lower()
    line_text = " ".join(str_text.split("\n"))

    line_text = " " + line_text    # this will help us when we print the sentences one by one in the tests.

    # filtering some specific words
    if "mr." in line_text or "mrs." in line_text:
        line_text = line_text.replace("mr.", "mr").replace("mrs.", "mr")

    # finding sentences without regex
    sentence_check = line_text[:]
    sentences = sentence_check.replace("!", ".").replace("?", ".").split(".")

    # this is a bug since we split the sentences with dot.
    # after splitting the text, the last item in the list will be an empty element, so we remove it.
    if "" in sentences:
        sentences.remove("")

    # to see how many texts are there
    # print(len(easy_paragraphs))

    return str_text, sentences

# easy_text_finder()


def medium_text_finder():
    '''
    medium text finder finds texts from the internet. In medium texts the user needs to type uppercase letters and the
    words are a bit more complicated. Also the user will not be bothered with some hard punctuations.
    :return:
    '''

    # this is the website for finding texts
    website = requests.get("https://agilefingers.com/texts/dickens-charles-oliwer-twist-en")

    soup = BeautifulSoup(website.content, "html.parser")

    all_text = soup.find("div", {"id": "textForTypingContent"})

    # some manupulation in the text for accesing the paragraphs
    paragraphs = all_text.text.split("\n\n")

    # filtering the length of the paragraphs
    medium_paragraphs = list(filter(lambda x: 80 < len(x) < 250, paragraphs))

    # getting a random text and filtering the text for getting a medium difficulty text.
    text = list(filter(lambda ch: ch not in ('''"''', "'"), random.choice(medium_paragraphs)))
    str_text = "".join(text)
    line_text = " ".join(str_text.split("\n"))

    line_text = " " + line_text  # this will help us when we print the sentences one by one in the tests.

    # filtering some specific words
    if "Mr." in line_text or "Mrs." in line_text:
        line_text = line_text.replace("Mr.", "Mr").replace("Mrs.", "Mrs")

    # finding sentences without regex
    sentence_check = line_text[:]
    sentences = sentence_check.replace("!", ".").replace("?", ".").split(".")

    # this is a bug since we split the sentences with dot.
    # after splitting the text, the last item in the list will be an empty element, so we remove it.
    if "" in sentences:
        sentences.remove("")

    # to see how many texts are there
    # print(len(medium_paragraphs))

    return str_text, sentences

# medium_text_finder()


def hard_text_finder():
    '''
        hard text finder finds texts from the internet. In hard texts there is not filtering in the text.
        The user needs to type the exact same text. Also the word are a bit more complicated.
        :return:
    '''

    # this is the website for finding texts
    website = requests.get("https://agilefingers.com/texts/schmidt-ferdinand-gudrun-en")

    soup = BeautifulSoup(website.content, "html.parser")

    all_text = soup.find("div", {"id": "textForTypingContent"})

    # some manupulation in the text for accesing the paragraphs
    paragraphs = all_text.text.split("\n\n")

    # filtering the length of the paragraphs
    hard_paragraphs = list(filter(lambda x: 80 < len(x) < 225, paragraphs))

    # since we dont filter the text, we dont need to convert to string again, therefore theres no str_text variable
    # like the other functions above

    # getting a random text.
    text = random.choice(hard_paragraphs)
    line_text = " ".join(text.split("\n"))

    line_text = " " + line_text  # this will help us when we print the sentences one by one in the tests.

    # filtering some specific words
    if "Mr." in line_text or "Mrs." in line_text:
        line_text = line_text.replace("Mr.", "Mr").replace("Mrs.", "Mrs")

    # finding sentences without regex
    sentence_check = line_text[:]
    sentences = sentence_check.replace("!", ".").replace("?", ".").split(".")

    # this is a bug since we split the sentences with dot.
    # after splitting the text, the last item in the list will be an empty element, so we remove it.
    if "" in sentences:
        sentences.remove("")

    # this is a also a bug fix.
    # after splitting the text, in such cases the list item can be ", so we remove it.
    if '"' in sentences:
        sentences.remove('"')

    # to see how many texts are there
    # print(len(medium_paragraphs))

    return text, sentences

# hard_text_finder()


def tongue_twister_finder():

    # this is the website for finding tongue twisters
    website = requests.get("https://www.mondly.com/blog/2019/08/23/71-best-tongue-twisters-to-perfect-your-english-pronunciation/")

    soup = BeautifulSoup(website.content, "html.parser")

    twisters_data = soup.find_all("ul")

    # gathering tongue twisters
    twisters = [item.text for item in twisters_data[4]]

    # chosing and manipulating the text
    chosen = random.choice(twisters)
    chosen = " " + chosen.replace("’", "'")

    # finding sentences without regex
    sentences = chosen.replace(";", ".").replace("!", ".").replace("?", ".").split(".")

    # this is a bug since we split the sentences with dot.
    # after splitting the text, the last item in the list will be an empty element, so we remove it.
    if "" in sentences:
        sentences.remove("")

    return chosen, sentences

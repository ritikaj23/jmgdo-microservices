import connexion
import six

from swagger_server import util

    # hello_in_different_languages_controller.py

hellos = {
    "English": "hello",
    "Hindi": "namastey",
    "Spanish": "hola",
    "French": "bonjour",
    "German": "guten tag",
    "Italian": "salve",
    "Chinese": "nǐn hǎo",
    "Portuguese": "olá",
    "Arabic": "asalaam alaikum",
    "Japanese": "konnichiwa",
    "Korean": "anyoung haseyo",
    "Russian": "Zdravstvuyte"
}


def greetings_get():  # noqa: E501
    return hellos
    """Returns a list of Greetings

    Returns greetings in different languages # noqa: E501


    :rtype: None
    """






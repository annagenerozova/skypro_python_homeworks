import pytest
from string_utils import StringUtils

utils = StringUtils()

@pytest.mark.parametrize("string, result",
    #Позитивные 
    [("skypro", "Skypro"),
     ("тест", "Тест"),
     ("сочетание слов", "Сочетание слов"),
     #Негативные
     ("123слово", "123слово"),
     ("",""),
     (" "," "),
     ("123654", "123654")
     ] )
def test_capitilize (string , result):
    res = utils.capitilize (string)
    assert res == result

@pytest.mark.parametrize("string, result" ,
    [(" skypro", "skypro"),
    ("skypro", "skypro"),
    ("   skypro", "skypro"),
    ("", ""),
    ("   ", ""),
    (" 123", "123")
    ])
def test_trim(string, result):
    res = utils.trim (string)
    assert res == result
                         
@pytest.mark.parametrize("string, delimeter, result" ,
    [("1,2,3,4", "," , ["1","2","3","4"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("apple;banana;cherry", ";", ["apple", "banana", "cherry"]),
    ("", ",", []),
    ("a,,b", ",", ["a", "", "b"]),
   # ("   ", ",", ["   "])
    ]) 
def test_to_list(string, delimeter, result):
    res = utils.to_list (string, delimeter)
    assert res == result                         

@pytest.mark.parametrize("string, symbol, result" ,
    [("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "a", False),
    ("hello", "o", True),
    ("test", "t", True),
    ("apple", "p", True),
    ("", "", True)
    ])
def test_contains(string, symbol, result):
    res = utils.contains (string, symbol)
    assert res == result 

@pytest.mark.parametrize("string, symbol, result" ,
    [("SkyPro", "S", "kyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("123456", "3", "12456"),
    ("", "", ""),
    ("hello world", "o", "hell wrld"),
    ("test", "t", "es"),
    ("apple pie", "pie", "apple "),
    ("banana", "a", "bnn"),
    ("", "a", "")
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol (string, symbol)
    assert res == result 

@pytest.mark.parametrize("string, symbol, result" ,
    [("SkyPro", "S", True),
    ("SkyPro", "P", False),
    ("сочетание слов", "с", True),
    ("test", "t", True),
    ("banana", "b", True),
    ("banana", "n", False),
    ("", "a", False),
    ("no match", "no", True),
    ("no match", "m", False),
    ("","",True)
    ])
def test_starts_with(string, symbol, result):
    res = utils.starts_with (string, symbol)
    assert res == result 

@pytest.mark.parametrize("string, symbol, result" ,
    [("SkyPro", "o", True),
    ("SkyPro", "P", False),
    ("сочетание слов", "в", True),
    ("test", "t", True),
    ("banana", "a", True),
    ("banana", "n", False),
    ("", "a", False),
    ("no match", "ch", True),
    ("no match", "m", False),
    ("","",True)
    ])
def test_end_with(string, symbol, result):
    res = utils.end_with (string, symbol)
    assert res == result

@pytest.mark.parametrize("string, result",
    [ ("",True),
    ("   ",True),
    ("SkyPro", False),
    ("12345", False)
    ])
def test_is_empty(string, result):
    res = utils.is_empty (string )
    assert res == result

@pytest.mark.parametrize("lst,joiner, result",
    [([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    ([1, 2, 3, 4], "-", "1-2-3-4"),
    ([1], ", ", "1"),
    ([], ", ", ""),
    #(["мопс", "йорк", "чухуа"], "; ", "мопс; йорк; чихуа")
    (["apple", "banana", "cherry"], "; ", "apple; banana; cherry")
    ])
def test_list_to_string(lst,joiner, result):
    res = utils.list_to_string (lst, joiner)
    assert res == result
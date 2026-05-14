from contactbook import ContactBook
def test_search_existing():
    cb=ContactBook()
    cb.add_contact('lokesh','9989370804','lokesh@gmail.com')
    assert cb.search_contact('lokesh') is True

def test_search_non_existing():
    cb=ContactBook()
    assert cb.search_contact('ajay') is False

def test_remove_existing():
    cb=ContactBook()
    cb.add_contact('ajay','9550929777','ajay@gmail.com')
    cb.del_contact('ajay')
    assert cb.search_contact('ajay') is False

def test_remove_non_existing():
    cb=ContactBook()
    assert cb.del_contact('ajay') is False

def test_del_from_empty_list():
    cb = ContactBook()
    cb.contacts.clear()
    result = cb.del_contact('santhosh')
    assert result is False
    assert len(cb.contacts) == 0

def test_search_case_insensitivity():
    cb=ContactBook()
    cb.add_contact('Santhosh',123455677,'santhosh@gmail.com')
    assert cb.search_contact('santhosh') is True
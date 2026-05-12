from tax_calculator import calculate_tax

def test_normal_case():
    assert calculate_tax(1000,18.0)==180.0

def test_default_case():
    assert calculate_tax(1000)==180.0

def test_zero_amount():
    assert calculate_tax(0,18.0)==0.0

def test_zero_tax():
    assert calculate_tax(1000,0)==0.0

def test_negative_amount():
    try:
        calculate_tax(-1000,18.0)
        assert False,"should be raise value error"

    except ValueError:
        pass

def test_invalid_amount():
    try:
        calculate_tax(1000,150.0)
        assert False,"should be raise value error"

    except ValueError:
        pass
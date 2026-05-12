def calculate_tax(amount: float,tax_rate: float=18.0)->float:
    if amount<0:
        raise ValueError(f"Amount should not be in negative {amount}")
    if tax_rate<0 or tax_rate>100:
        raise ValueError(f"Tax rate amount set wrong{tax_rate}")
    else:
        tax=amount*(tax_rate/100)
    return round(tax,2)

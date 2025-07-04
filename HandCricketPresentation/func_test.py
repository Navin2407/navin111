def fuction_test(ui, enemy, curren_score):
    """the main method """
    if ui < 0 or ui >= 7:
        return "invalid value!"
    elif ui == enemy:
        return curren_score, "you are out!"
    else:
        return curren_score + ui, "continue"
def test_out_case():
    """the test for negative result"""
    assert fuction_test(6, 6, 30) == (30, "you are out!")

def test_continue_case():
    """the test for positive result"""
    assert fuction_test(4, 5, 23) == (27, "continue")

def test_invalid_case():
    """the test for invalid result"""
    assert fuction_test(-11, 4, 34) == "invalid value!"

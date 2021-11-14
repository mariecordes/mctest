from mctest.emotions import make_heart2


def test_heart_width():
    heart_string = make_heart2(2)
    assert len(heart_string) == 13

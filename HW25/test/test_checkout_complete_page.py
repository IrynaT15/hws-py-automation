def test_complete_header_text(complete):
    assert complete.is_complete_header_text_correct()


def test_back_home(complete):
    assert complete.back_home()

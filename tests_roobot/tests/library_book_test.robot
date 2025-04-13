*** Settings ***
Library    ../source/BookLibrary.py
Library    Collections

*** Variables ***
${reader1}=    Reader1
${reader2}=    Reader2

*** Test Cases ***

Book Creation
    ${book}=    Create Book    Book Tile    Author Name    1234567890    1234567890
    Should Be Equal    ${book.book_info['book_name']}    Book Tile
    Should Be Equal    ${book.book_info['author']}    Author Name
    Should Be Equal    ${book.book_info['num_pages']}    1234567890
    Should Be Equal    ${book.book_info['isbn']}    1234567890

    Should Be Equal    ${book.status['is_reserved']}    ${False}
    Should Be Equal    ${book.status['is_given']}    ${False}
    Should Be Equal    ${book.status['reserved_by']}    ${None}
    Should Be Equal    ${book.status['given_to']}    ${None}
    Log    Book Status After Creation: ${book.status}

Book Reservation
    # Reservation Success
    ${book}=    Create Hobbit Book
    ${reserve}=    Reserve Book    ${book}    ${reader1}
    Should Be Equal    ${reserve}    ${True}
    Should Be Equal    ${book.status['is_reserved']}    ${True}
    Should Be Equal    ${book.status['reserved_by']}    ${reader1}
    Log    Book Status After Reservation: ${book.status}

    # Reservation Fails For Already Reserved Book
    ${reserve_already_reserved_book}=   Reserve Book    ${book}    ${reader2}
    Should Be Equal    ${reserve_already_reserved_book}    ${False}
    Should Be Equal    ${book.status['reserved_by']}    ${reader1}
    Log    Book Status After Failed Reservation: ${book.status}

Cancel Book Reservation
    ${book}=    Create Hobbit Book

    # Cancellation Fails For Not Reserved Book
    ${cancel_not_reserved_book}=    Cancel Reserve    ${book}    ${reader1}
    Should Be Equal    ${cancel_not_reserved_book}    ${False}
    Log    Book Status After Failed Cancelation: ${book.status}

    ${reserve}=    Reserve Book    ${book}    ${reader1}

    # Cancellation Fails For Wrong Reader
    ${cancel_by_wrong_reader}=    Cancel Reserve    ${book}    ${reader2}
    Should Be Equal    ${cancel_by_wrong_reader}    ${False}
    Log    Book Status After Failed Cancelation: ${book.status}

    # Cancellation Success
    ${cancel}=    Cancel Reserve    ${book}    ${reader1}
    Should Be Equal    ${cancel}    ${True}
    Should Be Equal    ${book.status['is_reserved']}    ${False}
    Should Be Equal    ${book.status['reserved_by']}    ${None}
    Log    Book Status After Cancelation: ${book.status}

Get A Reserved Book Success
    ${book}=    Create Hobbit Book
    ${reservation}=    Reserve Book    ${book}    ${reader1}
    ${get_book}=    Get Book    ${book}    ${reader1}
    Should Be Equal    ${get_book}    ${True}
    Should Be Equal    ${book.status['is_given']}    ${True}
    Should Be Equal    ${book.status['is_reserved']}    ${False}
    Should Be Equal    ${book.status['given_to']}    ${reader1}
    Log    Book Status After Issue: ${book.status}

Get A Non-Reserved Book Success
    ${book}=    Create Hobbit Book
    ${get_book}=    Get Book    ${book}    ${reader1}
    Should Be Equal    ${get_book}    ${True}
    Should Be Equal    ${book.status['is_given']}    ${True}
    Should Be Equal    ${book.status['is_reserved']}    ${False}
    Should Be Equal    ${book.status['given_to']}    ${reader1}
    Log    Book Status After Issue: ${book.status}

Get Book Fails
    ${book}=    Create Hobbit Book
    ${reserve}=    Reserve Book    ${book}    ${reader1}

    # Wrong Reader Cannot Get A Reserved Book
    ${get_book_wrong_reader}=    Get Book    ${book}    ${reader2}
    Should Be Equal    ${get_book_wrong_reader}    ${False}
    Should Be Equal    ${book.status['is_given']}    ${False}
    Log    Book Status After Failed Issue: ${book.status}

    # Reader Cannot Get An Issued Book
    ${get_book}=    Get Book    ${book}    ${reader1}
    ${get_the_same_book}=    Get Book    ${book}    ${reader2}
    Should Be Equal    ${get_the_same_book}    ${False}
    Should Be Equal    ${book.status['given_to']}    ${reader1}
    Log    Book Status After Failed Issue: ${book.status}

Return Book
    ${book}=    Create Hobbit Book

    # Return Book Fails For Non-Given Book
    ${return_non_given_book}=    Return Book    ${book}    ${reader1}
    Should Be Equal    ${return_non_given_book}    ${False}
    Log    Book Status After Failed Return: ${book.status}

    ${get_book}=    Get Book    ${book}    ${reader1}

    # Return Book Fails For Wrong Reader
    ${return_by_wrong_reader}=    Return Book    ${book}    ${reader2}
    Should Be Equal    ${return_by_wrong_reader}    ${False}
    Log    Book Status After Failed Return: ${book.status}

    # Return Book Success
    ${return}=    Return Book    ${book}    ${reader1}
    Should Be Equal    ${return}    ${True}
    Should Be Equal    ${book.status['is_given']}    ${False}
    Should Be Equal    ${book.status['given_to']}    ${None}
    Log    Book Status After Return: ${book.status}

*** Keywords ***
Create Hobbit Book
    ${book}=    Create Book    The Hobbit    J.R.R. Tolkien    400    001
    RETURN    ${book}

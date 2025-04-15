*** Settings ***
Library    ../source/ReaderLibrary.py
Library    ../source/BookLibrary.py
Library    Collections

*** Test Cases ***

Reader Creation
    ${reader}=    Create Reader    Reader 1
    Should Be Equal    ${reader.name}    Reader 1
    Should Be Equal    ${reader.reserved_book}    ${None}
    Should Be Equal    ${reader.given_book}    ${None}

Reserve Book
    ${book}=    Create Hobbit Book
    ${reader}=    Create Reader    Reader 1

    # Reserve Book Success
    ${reserve}=    Reader Reserve Book    ${reader}    ${book}
    ${expected_message}=    Set Variable
    ...    ${book.book_info['isbn']}: Success! Reservation for ${reader.name} is completed
    Should Be Equal    ${reserve}    ${expected_message}

    # Reserve Book Again By The Same Reader Fails
    ${reserve_book_again_by_the_same_reader}=    Reader Reserve Book    ${reader}    ${book}
    ${expected_message}=    Set Variable
    ...    ${book.book_info['isbn']}: Warning! ${reader.name} already has a reserved book
    Should Be Equal    ${reserve_book_again_by_the_same_reader}    ${expected_message}

    # Reserve Already Reserved By Another Reader Fails
    ${reader2}=    Create Reader    Reader 2
    ${reserve_the_same_book_by_another_reader}=    Reader Reserve Book    ${reader2}    ${book}
    ${expected_message}=    Set Variable
    ...    ${book.book_info['isbn']}: Warning! The book is already reserved by ${reader.name}
    Should Be Equal    ${reserve_the_same_book_by_another_reader}    ${expected_message}

Cancel Book Reservation
    ${book}=    Create Hobbit Book
    ${reader}=    Create Reader    Reader 1

    # Cancel Reservation Fails For Non-Reserved Book
    ${cancel_non_reserved_book}=    Reader Cancel Reserve    ${reader}    ${book}
    ${expected_message}=    Set Variable
    ...    ${book.book_info['isbn']}: Warning! ${reader.name} has no reservation for the book
    Should Be Equal    ${cancel_non_reserved_book}    ${expected_message}

    ${reserve}=    Reader Reserve Book    ${reader}    ${book}

    # Cancel Book Reservation Success
    ${cancel}=    Reader Cancel Reserve    ${reader}    ${book}
    ${expected_message}=    Set Variable
    ...    ${book.book_info['isbn']}: Success! Reservation for ${reader.name} is cancelled
    Should Be Equal    ${cancel}    ${expected_message}
    Should Be Equal    ${reader.reserved_book}    ${None}

Get Book
    ${book}=    Create Hobbit Book
    ${reader}=    Create Reader    Reader 1

    # Get Book Success
    ${get_book}=    Reader Get Book    ${reader}    ${book}
    ${expected_message}=    Set Variable
    ...    ${book.book_info['isbn']}: Success! The book can be given to ${reader.name}
    Should Be Equal    ${get_book}    ${expected_message}
    Should Be Equal    ${reader.given_book}    ${book}

    # Get Already Issued Book Fail
    ${get_already_issued_book}=    Reader Get Book    ${reader}    ${book}
    ${expected_message}=    Set Variable
    ...    ${book.book_info['isbn']}: Warning! The book cannot be given to ${reader.name}
    Should Be Equal    ${get_already_issued_book}    ${expected_message}

Return Book
    ${book}=    Create Hobbit Book
    ${reader1}=    Create Reader    Reader 1
    ${reader2}=    Create Reader    Reader 2

    # Return Not Issued Book Fails
    ${return}=    Reader Return Book    ${reader1}    ${book}
    ${expected_message}=    Set Variable
    ...    ${book.book_info['isbn']}: Warning! The book could not be returned by ${reader1.name}
    Should Be Equal    ${return}    ${expected_message}

    ${get_book}=    Reader Get Book    ${reader1}    ${book}

    # Return Book By Wrong Reader Fails
    ${return_by_wrong_reader}=    Reader Return Book    ${reader2}    ${book}
    ${expected_message}=    Set Variable
    ...    ${book.book_info['isbn']}: Warning! The book could not be returned by ${reader2.name}
    Should Be Equal    ${return_by_wrong_reader}    ${expected_message}

    # Return Book Success
    ${return}=    Reader Return Book    ${reader1}    ${book}
    ${expected_message}=    Set Variable
    ...    ${book.book_info['isbn']}: Success! The book is returned by ${reader1.name}
    Should Be Equal    ${return}    ${expected_message}
    Should Be Equal    ${reader1.given_book}    ${None}

*** Keywords ***
Create Hobbit Book
    ${book}=    Create Book    The Hobbit    J.R.R. Tolkien    400    001
    RETURN    ${book}

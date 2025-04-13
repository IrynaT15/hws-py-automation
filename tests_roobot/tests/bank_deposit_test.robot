*** Settings ***
Library    ../source/BankLibrary.py
Library    Collections

*** Test Cases ***

Create Bank Record
    ${bank_record}=    Create Bank Record
    Should Be Equal    ${bank_record.client_id}    ${None}
    Should Be Equal    ${bank_record.client_name}    ${None}
    Should Be Equal    ${bank_record.is_deposit_open}    ${False}
    Should Be Equal    ${bank_record.start_balance}    ${None}
    Should Be Equal    ${bank_record.years}    ${None}
    Should Be Equal    ${bank_record.interest_frequency}    ${None}
    Should Be Equal    ${bank_record.interest_rate}    ${0.1}
    ${empty_list}    Create List
    Should Be Equal    ${bank_record.client_ids}    ${empty_list}

Register Client
    # Register Client Success
    ${bank_record}=    Create Bank Record
    ${register_client}=    Register Client    ${bank_record}    001    Client
    Should Be Equal    ${register_client}    001: Success! New client is registered
    Should Be Equal    ${bank_record.client_id}    001
    Should Be Equal    ${bank_record.client_name}    Client
    List Should Contain Value    ${bank_record.client_ids}    ${bank_record.client_id}

    # Register Fails For Already Registered Client
    ${register_existing_client}=    Register Client    ${bank_record}    001    Client
    Should Be Equal    ${register_existing_client}    001: Warning! Client is already registered
    List Should Not Contain Duplicates    ${bank_record.client_ids}

Open Deposit Account
    ${bank_record}=    Create Bank Record
    ${register_client}=    Register Client    ${bank_record}    001    Client

    # Open Deposit Account Fails For Start Balance = 0
    ${open_account_with_zero_balance}=    Open Deposit Account    ${bank_record}    001     0    5    12
    Should Be Equal    ${open_account_with_zero_balance}    Warning! Invalid start balance.

    # Open Deposit Account Fails For Negative Start Balance
    ${open_account_with_negative_balance}=    Open Deposit Account    ${bank_record}    001     -100    5    12
    Should Be Equal    ${open_account_with_negative_balance}    Warning! Invalid start balance.

    # Open Deposit Account Success
    ${open_account}=    Open Deposit Account    ${bank_record}    001     1000    5    12
    ${expected_message}=    Set Variable
    ...    001: Success! Deposit account is opened. 1000 BYN for 5 years.
    Should Be Equal    ${open_account}    ${expected_message}
    Should Be Equal As Numbers    ${bank_record.start_balance}    1000
    Should Be Equal As Numbers    ${bank_record.years}    5
    Should Be Equal As Numbers    ${bank_record.interest_frequency}    12
    Should Be Equal    ${bank_record.is_deposit_open}    ${True}

    # Open New Deposit Account For The Same Client Fails
    ${open_new_account_for_the_same_client}=    Open Deposit Account    ${bank_record}    001     1000    5    12
    Should Be Equal    ${open_new_account_for_the_same_client}    001: Warning! Client has an open deposit.

    # Open Deposit Account Fails For Not Registered Clien ID
    ${open_account_for_not_registered_client}=    Open Deposit Account    ${bank_record}    01     1000    5    12
    Should Be Equal    ${open_account_for_not_registered_client}    Warning! Client not registered.
    List Should Not Contain Value    ${bank_record.client_ids}    01

Calculate Deposit Interest Rate
    ${bank_record}=    Create Bank Record

    # Calculation Fails For Not Registered Client
    ${calculate_for_not_registered_client}=    Calc Deposit Interest Rate    ${bank_record}    001
    Should Be Equal    ${calculate_for_not_registered_client}    Warning! Client not registered.

    ${register_client}=    Register Client    ${bank_record}    001    Client

    # Calculation Fails For Client Without Opened Account
    ${calculate_for_client_without_account}=    Calc Deposit Interest Rate    ${bank_record}    001
    Should Be Equal    ${calculate_for_client_without_account}    001: Warning! No open deposit account.

    # Calculation Success
    ${open_account}=    Open Deposit Account    ${bank_record}    001     1000    1    12
    ${calculate}=    Calc Deposit Interest Rate    ${bank_record}    001
    Should Be Equal As Numbers    ${calculate}    1104.71

Close Deposit
    ${bank_record}=    Create Bank Record

    # Close Deposit Fails For Not Registered Client
    ${close_deposit_for_not_registered_client}=    Close Deposit    ${bank_record}    001
    Should Be Equal    ${close_deposit_for_not_registered_client}    Warning! Client not registered.

    # Close Deposit Fails For Without Opened Account (1)
    ${register_client}=    Register Client    ${bank_record}    001    Client
    ${close_deposit_for_client_without_account}=    Close Deposit    ${bank_record}    001
    Should Be Equal    ${close_deposit_for_client_without_account}    Warning! Client has no open deposit account.

    # Close Deposit Success
    ${open_account}=    Open Deposit Account    ${bank_record}    001     1000    1    12
    ${close_deposit}=    Close Deposit    ${bank_record}    001
    Should Be Equal    ${close_deposit}    001: Success! Deposit account is closed

    # Close Deposit Fails For Without Opened Account (2)
    ${close_deposit_for_client_without_account}=    Close Deposit    ${bank_record}    001
    Should Be Equal    ${close_deposit_for_client_without_account}    Warning! Client has no open deposit account.

from math import log
from math import ceil

CHOICE_MSG = 'What do you want to calculate? \ntype "n" - for monthly payments,\
\ntype "a" - for annuity monthly payment amount,\ntype "p" - for loan principal:'
PRINCIPAL_MSG = 'Enter the loan principal:'
PERIODS_MSG = 'Enter the number of periods:'
ANNUITY_MSG = 'Enter the annuity payment:'
PAYMENT_MSG = 'Enter the monthly payment:'
INTEREST_MSG = 'Enter the loan interest:'
MON_PAY_RESULT1 = 'It will take '
MON_PAY_RESULT2 = 'to repay this loan!'
ANNUITY_RESULT = 'Your monthly payment ='
PRINCIPAL_RESULT = 'Your loan principal ='

MONTHS_NUM = 12
PERCENT_ALL = 100

choice = input(CHOICE_MSG)
# input all other things needed
if choice != 'p':
    principal = int(input(PRINCIPAL_MSG))
if choice == 'p':
    annuity = float(input(ANNUITY_MSG))
if choice != 'n':
    periods = int(input(PERIODS_MSG))
else:
    month_pay = int(input(PAYMENT_MSG))


interest = float(input(INTEREST_MSG))

# process
output_msg = ""
nom_int_rt = interest / (MONTHS_NUM * PERCENT_ALL)
int_rt_modified = (1 + nom_int_rt)
if choice == 'n':
    mon_num = log(month_pay/(month_pay - nom_int_rt * principal), int_rt_modified)
    mon_num = ceil(mon_num)
    output_msg += MON_PAY_RESULT1
    years = mon_num // MONTHS_NUM
    mon_num = mon_num % MONTHS_NUM
    if years != 0:
        output_msg += (' ' + str(years) + 'year')
        if years != 1:
            output_msg += 's'
    if mon_num != 0:
        output_msg += (' ' + str(mon_num) + 'month')
        if mon_num != 1:
            output_msg += 's'
    output_msg += ' ' + MON_PAY_RESULT2
elif choice == 'a':
    output_msg += ANNUITY_RESULT
    int_rt_modified = pow(int_rt_modified, periods)
    annuity = ceil(principal * nom_int_rt * int_rt_modified / (int_rt_modified - 1))
    output_msg += (' ' + str(annuity) + '!')
else:  # choice == 'p'
    output_msg += PRINCIPAL_RESULT
    int_rt_modified = pow(int_rt_modified, periods)
    principal = annuity * (int_rt_modified - 1) / (nom_int_rt * int_rt_modified)
    output_msg += (' ' + str(principal) + '!')

print(output_msg)  # printing the result

total_sum = 0

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
one_digits_sum = sum([len(x) for x in digits])

two_digit_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
two_digit_tys = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
tys_sum = sum([len(x) for x in two_digit_tys])
two_digits_sum = sum([len(x) for x in two_digit_teens]) + tys_sum + tys_sum + one_digits_sum * len(two_digit_tys)

three_digits_sum = sum([len(x) + two_digits_sum for x in digits])
three_digits_sum += len('one hundred')
three_digits_sum = three_digits_sum + (999-100) * 3 - 9 * 3 # and

print sum([one_digits_sum, two_digits_sum, three_digits_sum, len('one thousand')])

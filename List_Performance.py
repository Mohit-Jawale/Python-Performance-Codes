import time

# code to check list performance

# code 1
start_time = time.time()

cube_numbers = []
for n in range(0, 100000000):
    if n % 2 == 1:
        cube_numbers.append(n ** 3)

end_time = time.time()
final_time_code_1 = end_time - start_time
print("This is time for code 1-:{final_time}".format(final_time=final_time_code_1))

# code 2

start_time = time.time()

cube_numbers = [n ** 3 for n in range(1, 100000000) if n % 2 == 1]

end_time = time.time()

final_time_code_2 = end_time - start_time
print("This is time for code 2-:{final_time}".format(final_time=final_time_code_2))


if final_time_code_2 < final_time_code_1:
    print("Code 2 is {percent}% faster than Code 1"
          .format(percent=abs((final_time_code_2-final_time_code_1)/final_time_code_2)*100))
else:
    print("Code 1 is {percent}% faster than Code 2"
          .format(percent=abs((final_time_code_2 - final_time_code_1) / final_time_code_2) * 100))

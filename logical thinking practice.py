#word_frequency_counter
text = input("Enter a sentence: ")
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word Frequency:", freq)

#student_grade_calculator.py
marks = [75, 80, 68, 90, 56]
average = sum(marks) / len(marks)
if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
else:
    grade = "C"
print("Average Marks:", average)
print("Grade:", grade)

#contact_book.py
contacts = {}
while True:
    name = input("Enter name (or 'exit'): ")
    if name == 'exit':
        break
    phone = input("Enter phone: ")
    contacts[name] = phone
print("\nContact Book:")
for name, phone in contacts.items():
    print(name, ":", phone)

#temperature_converter.py
c = float(input("Enter Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit:", f)

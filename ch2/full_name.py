first_name = 'ada'
last_name = "lovelace"
full_name = f"{first_name} {last_name}"  # f字符串, python3.6引入

print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)


# output:
# ada lovelace
# Hello, Ada Lovelace!
# Hello, Ada Lovelace!

# python 3.5以前
full_name = "{} {}".format(first_name, last_name)

print(full_name) # ada lovelace


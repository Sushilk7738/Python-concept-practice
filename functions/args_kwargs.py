
# def peoples(*args):
#     for i in args:
#         print(i)

# peoples("Sushil", "Yash", "Shailesh")



# def add(*sums):
#     total = 0
#     for i in sums:
#         total += i
#     return total

# result = add(11, 22, 33, 44)
# print(result)


# def info(**desc):
#     for i, j in desc.items():
#         print(f"{i} : {j}")

# info(name = "Sushil", role = "Backend Developer", salary = "₹100000")
# print()
# info(name = "Laxmi", role = "Frontend Developer", salary = "₹120000")



# def myDecorator(func):
#     def wrapper(*args, **kwargs):
#         print("function started...")
#         func(*args, **kwargs)
#         print("function ended.")
#     return wrapper

# @myDecorator
# def myInfo(*args, **kwargs):
#     print(args, kwargs)

# result = myInfo(11, 12, 32, 42, name = "Sushil", age = 24)


#* Employee salary calculator:-

# def calulate_salary(base, *bonus, **deductions):
#     total_bonus = sum(bonus)
#     total_deductions = sum(deductions.values())

#     inhand_salary = base + total_bonus - total_deductions
#     return inhand_salary

# result = calulate_salary(
#     100000, 
#     3000, 1200,
#     tax = 4500,
#     insurance = 2400
# )

# print(f"Final salary : ₹{result}")




# Dynamic blog creator: 

# def create_blog(**blog):
#     for i, j in blog.items():
#         print(f"{i} : {j}")

# create_blog(
#     title = "Sushil's Blogs",
#     author = "Sushil Kamble",
#     category = "Python Programming",
#     views = 15000
# )



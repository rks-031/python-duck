from user import User
from post import Post

# object creation of User class
app_user_one = User("rks@gmail.com", "Rohit", "1234", "Software Engineer")
app_user_one.get_user_info()

app_user_one.change_password("5678")
app_user_one.change_job_title("Senior Software Engineer")
app_user_one.get_user_info()

    
app_user_two = User("user@example.com", "Alice", "abcd", "Data Scientist")
app_user_two.get_user_info()

print("\n")

# object creation of Post class
app_post_one = Post("Hello, world!", app_user_two.name)

app_post_one.get_post_info()

app_post_two = Post("Learning OOP in Python!", app_user_one.name)
app_post_two.get_post_info()
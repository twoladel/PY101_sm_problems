def greetings(lst, job_dict):
    return (
        f"Hello, {' '.join(lst)}! Nice to have a "
        f"{job_dict['title']} {job_dict['occupation']} around.")

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
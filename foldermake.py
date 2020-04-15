import os

k="stud"
# If folder doesn't exist, then create it.
if not os.path.isdir(k):
    os.makedirs("stud")
    print("created folder : ", k)

else:
    print(k, "folder already exists.")
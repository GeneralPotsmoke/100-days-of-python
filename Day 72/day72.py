import matplotlib.pyplot as plt

languages = ['Python', 'JavaScript', 'Java', 'C++', 'C#']
popularity = [85, 80, 75, 60, 50]

plt.bar(languages, popularity)
plt.xlabel('Programming Languages')
plt.ylabel('Popularity')
plt.title('Popularity of Programming Languages')
plt.show()

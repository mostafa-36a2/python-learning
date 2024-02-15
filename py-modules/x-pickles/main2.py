import pickle

# Create a generator
def generate_data():
    for i in range(10):
        yield i

# Serialize the generator
pickle.dump(generate_data(), open('data.pkl', 'wb'))

# De-serialize the generator
generator = pickle.load(open('data.pkl', 'rb'))

# Use the generator
for i in generator:
    print(i)
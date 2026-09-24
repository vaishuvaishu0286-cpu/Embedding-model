from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentence1 = input("Enter sentence 1: ")
sentence2 = input("Enter sentence 2: ")

embedding1 = model.encode(sentence1)
embedding2 = model.encode(sentence2)

print("\n========== EMBEDDINGS ==========\n")

print("Sentence:", sentence1)
print("Embedding:", embedding1)

print("\nSentence:", sentence2)
print("Embedding:", embedding2)
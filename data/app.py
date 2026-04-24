from graph import app

print("RAG BOT STARTED")

while True:
    q = input("\nAsk: ")

    if q.lower() == "exit":
        break

    result = app.invoke({"query": q})

    print("\nANSWER:\n", result["answer"])
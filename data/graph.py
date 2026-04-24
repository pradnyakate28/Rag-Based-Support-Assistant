from langgraph.graph import StateGraph
from retriever import retrieve

#Retrieve Node
def retrieve_node(state):
    query = state["query"]
    docs = retrieve(query)

    return {
        "query": query,
        "docs": docs
    }


#Generate Node
def generate_node(state):
    docs = state.get("docs", [])

    if not docs:
        return {"answer": "No relevant data found."}

    query = state["query"].lower()
    text = docs[0].page_content

    lines = [l.strip() for l in text.split("\n") if l.strip()]

    #exact match
    for i in range(len(lines)):
        if query in lines[i].lower():
            for j in range(i + 1, len(lines)):
                if not lines[j].endswith(":"):
                    return {"answer": lines[j]}

    #keyword fallback
    for i in range(len(lines)):
        if "service" in lines[i].lower():
            for j in range(i + 1, len(lines)):
                if not lines[j].endswith(":"):
                    return {"answer": lines[j]}

    #final fallback
    return {"answer": lines[0]}


#  Graph setup
workflow = StateGraph(dict)

workflow.add_node("retrieve", retrieve_node)
workflow.add_node("generate", generate_node)

workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "generate")
workflow.set_finish_point("generate")

app = workflow.compile()
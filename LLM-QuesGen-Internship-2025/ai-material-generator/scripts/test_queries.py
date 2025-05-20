from backend.app.core.vectorstore import get_relevant_chunks

def test_query():
     grade = "Grade 1"
     chapter = " "
     chunks = get_relevant_chunks(grade, chapter)
     print("Relevant Chunks: ", chunks)

if __name__ == "__main__":
     test_query()
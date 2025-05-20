def build_prompt(context_chunks, request):
     with open(f"models/prompt_templates/{'worksheet' if request.type == 'Worksheet' else 'question_paper'}.txt", 'r') as f:
          template = f.read()
     context = "\n".join(context_chunks)
     prompt = template.format(
          grade = request.grade,
          chapter = request.chapter,
          difficulty = request.difficulty,
          context = context
     )

     return prompt
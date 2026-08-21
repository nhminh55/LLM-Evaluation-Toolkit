def evaluate_answer(answer, expected_answer):
  """
  Compare and LLM answer with an expected answer.
  """
  if answer.strip().lower() == expected_answer.strip().lower():
    return 1.0
    
  return 0.0

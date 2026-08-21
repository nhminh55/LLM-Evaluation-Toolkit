from src.evaluator import evaluate_answer

def test_correct_answer():
  answer = "Python is a programming language."
  expected = "Python is a programming language."
  score = evaluation_answer(answer, expected)
  assert score == 1.0

def test_wrong_answer():
   answer = "Python is a type of database."
   expected = "Python is a programming language."

   score = evaluate_answer(answer, expected)

   assert score == 0.0

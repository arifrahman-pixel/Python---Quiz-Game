from questions import Question

Question_prompts = [
    "Whats the color of apple\n(1) Red\n(2) Blue\n(3) Yellow\n",
    "Whats the color of banana\n(1) Silver\n(2) Pink\n(3) Yellow\n",
    "Whats the color of Oranges\n(1) Orange\n(2) Red\n(3) Pink\n",
    "Whats the color of Strawberry\n(1) Orange\n(2) Red\n(3) Pink\n",
]
Questions = [
    Question(Question_prompts[0],"1"),
    Question(Question_prompts[1],"3"),
    Question(Question_prompts[2],"1"),
    Question(Question_prompts[3],"2"),
]
def run_test(Questions):
    score = 0
    for Q in Questions:
        answer = input(Q.prompt)
        if answer == Q.answer:
         score += 1
    print("You got " + str(score)+" out of "+ str(len(Questions)))

run_test(Questions)


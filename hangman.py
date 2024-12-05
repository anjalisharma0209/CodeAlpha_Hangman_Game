import random
import hangman_stages
word_list=['apple','mango','orange']
selected=random.choice(word_list)
# print(selected)
display=[]
lives=6
for j in range(len(selected)):
    display+='_'
print(display)

game_over=False     

while not game_over:
    input1=input('enter guess letter\n')
    for j in range(len(selected)):#Mango j=0
        letter=selected[j]  
        if input1==letter:
           display[j]=input1
    print(display)
    
    if input1 not in selected:
        lives-=1
        if lives==0:
            game_over=True
            print('You lose!!')
            
    if '_' not in display:
        game_over=True
        print('you win')
    print(hangman_stages.stages[lives])
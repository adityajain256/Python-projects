print("It is a really tough game if you give every answer without failing you will win \"7crores\"\n")

name = input("Enter your name: ");

print("So",name,"give your ans in term of a,b,c,d.\n");
q=0
def asking( q):
    print(QL[q])
    print(opt[q])
    answer = input("Anser: ")

    while(q<15):
        if(answer==ans[q] ):
            print("your answer is correct.You won",prize[q])
            q = q+1
            asking(q)
          
        return 0;
       
    if(answer!=ans[q]):    
        print("your answer is incorrect\n So, you are going to your home with",prize[q-1])

    if(q ==15):
        if(answer==ans[15]):
            print("GAME OVER: you win it.RUPEES",prize[15])
    

    
QL = ["1. In what year did the Great October Socialist Revolution take place?", "2. What is the largest lake in the world?", "3. Which planet in the solar system is known as the “Red Planet”?", "4. Who wrote the novel “War and Peace”?", "5. What is the capital of Japan?", "6. Which river is the longest in the world?", "7. What gas is used to extinguish fires?", "8. What animal is the national symbol of Australia?", "9. Which of the following planets is not a gas giant?", "10. What is the name of the process by which plants convert sunlight into energy?", "11. What chemical element is designated as “Hg”?", "12. In what year was the first international modern Olympiad held?", "13. For which of these disciplines Nobel Prize is awarded?", "14. Entomology is the science that studies:", "15. Hitler's party is known as:", "16. For which Galileo is famous?"];

ans = ["a", "b", "c", "c","b","c","b","a","a","b","d","a","d","b","b","d" ];

opt = ["a. 1917 \nb. 1923 \nc. 1914 \nd.1920","a. Caspian Sea\n b. Baikal \n c. Lake Superior\n d. Ontario", "a. venus\n b. Earth\n c. Mars\n d. Jupiter","a. Anton Chekhov\n b. Fyodo Dostoevsky\n c. Leo Tolstoy\n d. Ivan Turgenev", "a. Beijing\n b. Tokyo\n c. Seoul\n d. Bangkok","a. Amazon\n b. Mississippi\n c. Nile\n d. Yangtaz","a. Oxygen\n b. Nitrogen\n c. Carbon dioxide\n d. Hydrogen","a. Kangaroo\n b. Koala\n c. Emu\n d. Crocodile","a. Mars\n b. Jupiter\n c. saturn\n d. Uranus","a. Respiration\n b. Photosynthesis\n c. Ocidation\n d. Evolution","a. Silver\n b. Tin\n c. copper\n d. Mercury","a. 1896\n b. 1900\n c. 1912\n d. 1924"," a. Pysics,Chemistry\n b. Physiology\n c. Medicine\n d. All of the above","a. Behavior of human beings \nb. Insects\n c. The origin and history of technical and scientific terms \nd. The formation of rocks","a. Labour Party\n b. Nazi Party\n c. Ku-Klux-Klan\n d. Democratic Party","a. Developed the telescope\nb. Discovered four satellites of Jupiter\nc.Found that the swinging motion of the pendulum results in consistent time measurement.\nd. All of the above"]

prize = ["1000","2000","3000","5000","10,000","20,000","40,000","80,000","1,60,000","3,20,000","6,40,000","12,50,000","25,50,000","50,00,000","1 crore","7 crore"]

asking(q)


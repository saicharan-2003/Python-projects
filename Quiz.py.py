import time
login_details=('admin','user')
admin_Id = 'SAI'
admin_password='123'
user_details={
        'Name':'sai',
        'Phone no':'9704085518'
    }
Questions = {
    'python': {
        '1': {
            'question': 'Which of the following is a correct variable name in Python?',
            'options': {'a':'1value','b':'value_1','c':'value-1','d':'value 1'},
            'answer': 'b'
        },
        '2': {
            'question': 'What is the output of print(2 ** 3)?',
            'options': {'a':'6', 'b':'8','c':'9','d':'5'},
            'answer': 'b'
        },
        '3': {
            'question':'What is the correct file extension for Python files?',
            'options':{'a':'.pyth','b':'.pt','c':'.py','d':'.pyt'},
            'answer':'c'
        },
        '4': {
            'question':'Which keyword is used to define a function in Python?',
            'options':{'a':'func','b':'define','c':'def','d':'function'},
            'answer':'c'
        },
        '5': {
            'question':'What does the input() function do?',
            'options':{'a':'Outputs a string','b':'Takes user input','c':'Declares a variable','d':'Returns a Boolean'},
            'answer':'b'
        }

    },
    'mysql': {
         '1': {
            'question': 'Which SQL command is used to update data in a table?',
            'options': {'a':'MODIFY','b':'UPDATE','c':'ALTER','d':'SET'},
            'answer': 'b'
        },
        '2': {
            'question': 'What does SQL stand for?',
            'options': {'a':'Simple Query Language', 'b':'Structured Question Language','c':'Structured Query Language','d':'Simplified Query Language'},
            'answer': 'c'
        },
        '3': {
            'question':'Which of the following is used to prevent duplicate values in a column?',
            'options':{'a':'PRIMARY KEY','b':'UNIQUE','c':'NOT NULL','d':'CHECK'},
            'answer':'b'
        },
        '4': {
            'question':'Which clause is used to sort the result in SQL?',
            'options':{'a':'ORDER BY','b':'SORT BY','c':'GROUP BY','d':'ARRANGE BY'},
            'answer':'a'
        },
        '5': {
            'question':' Which data type is used for textual data in MySQL?',
            'options':{'a':'VARCHAR','b':' INT','c':'BOOLEAN','d':'DECIMAL'},
            'answer':'a'
        }
    },
     'c': {
        '1': {
            'question': 'Which of the following is a valid keyword in C?',
            'options': {'a':'function','b':'integer','c':'return','d':'define'},
            'answer': 'c'
        },
        '2': {
            'question': ' Which header file is used for input and output functions?',
            'options': {'a':'stdlib.h', 'b':'io.h','c':'stdio.h','d':'conio.h'},
            'answer': 'c'
        },
        '3': {
            'question':' What symbol is used to end a statement in C?',
            'options':{'a':'-.','b':'- ,','c':'- :','d':'- ;'},
            'answer':'d'
        },
        '4': {
            'question':' What is the output of printf("%d", 10/4);?',
            'options':{'a':'2.5','b':'2','c':'2.0','d':'2.50'},
            'answer':'b'
        },
        '5': {
            'question':'What is the size of int in most systems?',
            'options':{'a':'2 bytes','b':'4 bytes','c':'8 bytes','d':'1 byte'},
            'answer':'b'
        }

    },
     'java': {
        '1': {
            'question': 'Which of the following is not a Java keyword?',
            'options': {'a':'static','b':'boolean','c':'void','d':'class'},
            'answer': 'b'
        },
        '2': {
            'question': 'Java is a ____ programming language?',
            'options': {'a':'compiled', 'b':'interpreted','c':'both compiled and interpreted','d':'script-based'},
            'answer': 'c'
        },
        '3': {
            'question':'Which method is the entry point of any Java program?',
            'options':{'a':'run()','b':'start()','c':'begin()','d':'main()'},
            'answer':'d'
        },
        '4': {
            'question':'Which operator is used to compare two values in Java?',
            'options':{'a':'=','b':':=','c':'==','d':'equals'},
            'answer':'c'
        },
        '5': {
            'question':'Which package contains the Scanner class?',
            'options':{'a':'java.io','b':'java.util','c':'java.lang','d':'java.input'},
            'answer':'b'
        }

    }
}
score={'python':{},'mysql':{},'c':{},'java':{}}
while True:
    login = input('Enter the (admin/user): ').lower()
    if login == login_details[0]:
            Id=input('Enter the admin Id : ').upper()
            print('*'*50)
            if Id == admin_Id:
                password=input('Enter the password : ')
                if admin_password == password: 
                    print('*'*15,'Login successfully','*'*15)
                    while True:
                        print('1.Add questions')
                        print('2.Modify questions')
                        print('3.Delete questions')
                        print('4.View all questions')
                        print('5.View all users details')
                        print('6.Exit')
                        print('*'*50)
                        print()
                        ch =input('Choose the option:')
                        print()
                        if ch >= '1' and ch <= '6':
                            ch = int(ch)
                        else:
                            print('Please enter a number only (1 to 6).')
                            continue
                        if ch == 1:
                            print('*'*10,'Adding the questions','*'*10)
                            print()
                            print('*'*5,'The subjects in the data','*'*5)
                            for subjects in Questions:
                                print(subjects)
                            print()
                            tech = input('Enter the subject : ').lower()
                            if tech in Questions:
                                    for que_no ,que in Questions[tech].items():
                                        print('Q.',que_no,que['question'])
                                        print()
                            while True:
                                if tech in Questions:
                                    break
                                else:
                                    Questions[tech]={}
                                    break
                            if tech in Questions:
                                q_no = input('Enter question ID : ')
                                if q_no not in Questions[tech]:  
                                    question_text = input('Enter the question: ')
                                    options = {}
                                    num_options = int(input('Enter number of options: '))
                                    if num_options<=4:
                                        for _ in range(num_options):
                                            key = input('Enter option key (e.g., a, b, c): ')
                                            value = input('Enter option text for '+key+':')
                                            options[key] = value
                                        correct_ans = input('Enter the correct answer: ')
                                        Questions[tech][q_no] = {
                                                        'question': question_text,
                                                        'options': options,
                                                        'answer': correct_ans
                                                        }
                                        print()
                                        print('Question:-',q_no,'is added',tech+'.')
                                        print()
                                        if q_no in Questions[tech]:
                                            for que,no in Questions[tech].items():
                                                if que==q_no:
                                                    print('Question:',que,'.',no['question'])
                                                    for option_no,option in no['options'].items():
                                                        print(option_no,'.',option)
                                                    print('Answer:',no['answer'])
                                                    print()
                                    else:
                                        print('-'*10,'The options should be less than or equal to 4','-'*10)
                                else:
                                    print('Already the question number is exist go and do modify the question')
                            else:
                                
                                print()
                        elif ch == 2:
                            print('*'*10,'Modify the questions','*'*10)
                            print()
                            print('*'*5,'The subjects in the data','*'*5)
                            for subjects in Questions:
                                print(subjects)
                            print()
                            tech = input('Enter the subject : ').lower()
                            if tech in Questions:
                                    for que_no ,que in Questions[tech].items():
                                        print('Q.',que_no,que['question'])
                                        print()
                            if tech in Questions:
                                q_no = input('Enter question ID : ')
                                if q_no in Questions[tech]:
                                    for que,no in Questions[tech].items():
                                        if que==q_no:
                                            print('Question:',que,'.',no['question'])
                                            for option_no,option in no['options'].items():
                                                print(option_no,'.',option)
                                            print('Answer:',no['answer'])
                                            print()
                                    question_text = input('Enter the question: ')
                                    options = {}
                                    num_options = int(input('Enter number of options: '))
                                    if num_options<=4:
                                        for _ in range(num_options):
                                            key = input('Enter option key (e.g., a, b, c): ')
                                            value = input('Enter option text for '+key+':')
                                            options[key] = value
                                        correct_ans = input('Enter the correct answer: ')
                                        Questions[tech][q_no] = {
                                                        'question': question_text,
                                                        'options': options,
                                                        'answer': correct_ans
                                                        }
                                        print()
                                        print('Question:-',q_no,'is modified.')
                                        print()
                                        if q_no in Questions[tech]:
                                            for que,no in Questions[tech].items():
                                                if que==q_no:
                                                    print('Question:',que,'.',no['question'])
                                                    for option_no,option in no['options'].items():
                                                        print(option_no,'.',option)
                                                    print('Answer:',no['answer'])
                                                    print()
                                    else:
                                        print('-'*10,'The options should be less than or equal to 4','-'*10)
                                else:
                                    print('Question no is not there in the data')
                            else:
                                print('Enter the correct tech')
                            print()
                        elif ch == 3:
                            print('*'*10,'Delete the question','*'*10)
                            print()
                            print('*'*5,'The subjects in the data','*'*5)
                            for subjects in Questions:
                                print(subjects)
                            print()
                            tech = input('Enter the subject : ').lower()
                            if tech in Questions:
                                for que_no ,que in Questions[tech].items():
                                        print('Q',que_no,que['question'])
                                        print()
                                q_no = input('Enter question ID : ')
                                if q_no in Questions[tech]:
                                    for que,no in Questions[tech].items():
                                        if que==q_no:
                                            print('Question:',q_no,'.',no['question'])
                                            for option_no,option in no['options'].items():
                                                print(option_no,'.',option)
                                            print('Answer:',no['answer'])
                                            print('*'*10,'Question is deleted','*'*10)
                                            print()
                                    Questions[tech].pop(q_no)
                                else:
                                    print('Enter the valid question to delete')
                            else:
                                print('The tech is worng')
                            print()
                        elif ch == 4:
                            print('*'*5,'View all the questions','*'*5)
                            print()
                            print('*'*5,'The subjects in the data','*'*5)
                            for subjects in Questions:
                                print(subjects)
                            print()
                            tech = input('Enter the subject : ')
                            print()
                            if tech in Questions:
                                for que_no ,que in Questions[tech].items():
                                        print('Q',que_no,que['question'])
                                        for option_no,option in que['options'].items():
                                            print(option_no,'.',option)
                                        print('Answer:',que['answer'])
                                        print()
                            else:
                                print('Wrong tech')
                            print()
                        elif ch == 5:
                            print('1.User_details')
                            print('2.User_score')
                            ch=int(input('Enter to see the (1.user_detalis/2.user_score):'))
                            if ch==1:
                                for user_name,password in user_details.items():
                                    print(user_name,'-',password)
                                print()
                            elif ch==2:
                                print()
                                print('*'*5,'The subjects in the data','*'*5)
                                for subjects in Questions:               
                                    print(subjects)
                                print()
                                tech=input('Enter the subject :').lower()
                                for user_name,user_score in score[tech].items():
                                    print(user_name,'-',user_score)
                                print()
                        elif ch == 6:
                            print('Exiting from admin login')
                            print()
                            break
                else:
                    print('Enter the correct password')
            else:
                print('Admin id is wrong Enter correct id')
    elif login == login_details[1]:
        while True:
                user=input('Enter the (User_Id) to take the test or enter the (exit) test: ')
                if user == 'exit':
                    print('Exit from the user_login')
                    break
                letter_count = 0
                total_count = 0
                for ch in user:
                    total_count = total_count + 1
                    if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
                        letter_count = letter_count + 1

                if letter_count != total_count:
                    print('Username must contain only letters. Try again.')
                    print()
                    continue
                password=input('Enter the user phone number :')
                digit_count = 0
                for ch in password:
                    if ch >= '0' and ch <= '9':
                        digit_count = digit_count + 1

                if digit_count != 10 or (password[0] not in '987'):
                    print('Phone number must be 10 digits and start with 9, 8, or 7.')
                    print()
                    continue
                if user not in user_details['Name']:
                    user_details={
                        'Name':user,
                        'Phone no':password
                        }
                print('*'*10,'Login successfully','*'*10)
                print()
                count=0
                print('*'*10,'Quiz types','*'*10)
                for subjects in Questions:               
                    print(subjects)
                print()
                start = time.time()
                tech = input('Enter the subject  : ').lower()
                if tech in Questions:
                    for q_id, q_data in Questions[tech].items():
                        print()
                        print('Question No -',q_id)
                        print('Question : ',q_data['question'])
                        for option_no,option in q_data['options'].items():
                            print(option_no,'.',option)
                        print()
                        user_answer=input('enter the answer : ')
                        if user_answer == q_data['answer']:
                            print('Correct answer')
                            print()
                            count+=1
                        else:
                            print()
                            print('Wrong answer! skipping the question')
                            print()
                    end=time.time()
                    print(user,'scored in',tech,'quiz is :',count)
                    print('Time taken by',user,'in',tech,'is :',round(end-start,2))
                    print('*'*50)
                    print()
                    while True:
                        if tech in score:
                            break
                        else:
                            score[tech]={}
                            break
                    score[tech][user]=count
                    for user_name,phone_no in user_details.items():
                        print(user_name,'-',phone_no)
                    print()
                else:
                    print('*'*10,'Wrong Tech','*'*10)
                    print()
        print()
        print('All users have completed the quiz.')
        print('Final Leaderboard:')
        print()
        for tech_name in score:
            if tech_name==tech:
                print('Leaderboard for', tech_name)
                print()
                tech_scores = score[tech_name]

       
                score_list = []
                for participated_user in tech_scores:
                    score_list.append((participated_user, tech_scores[participated_user]))

       
                for i in range(len(score_list)):
                    for j in range(i + 1, len(score_list)):
                        if score_list[i][1] < score_list[j][1]:
                            score_list[i], score_list[j] = score_list[j], score_list[i]

       
                rank = 1
                i=0
                while i<len(score_list)and rank<=3:
                    username = score_list[i][0]
                    user_score = score_list[i][1]
                    print(str(rank),'. ',username,' - ',str(user_score),' points')
                    rank =rank+1
                    i=i+1
                print()

    else:
        print('*'*10,'Wrong login_details','*'*10)
        break

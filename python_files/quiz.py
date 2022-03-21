import time
print("\n\n\n***********BRANCORE QUIZ***********\n")
print("\tby Brandon N. Sangma\n\n")


qstns = ["Q1. Who is the President of India?",
         "Q2. Who is the First President of India?",
         "Q3. Who is the Prime Minister of India?",
         "Q4. Who is the First Prime Minister of India?",
         'Q5. Who is the Vice president of India?',
         "Q6. Who is the First Vice president of India?",
         "Q7. Who is the Governor of India?",
         "Q8. Who is the First Governor of India?",
         "Q9. Who is the Governor of Meghalaya?",
         "Q10. Who is the First Governor of Meghalaya?",
         "Q11. Who is the Chief Justice of India?",
         "Q12. Who is the Chief Justice of Meghalaya?",
         "Q13. Who is the Chief Minister of Meghalaya?",
         "Q14. Who is the first Chief Minister of Meghalaya?",
         "Q15. Who is the Deputy Commissioner of West Garo Hills?",
         "Q16. Who is the Deputy Commissioner of North Garo Hills?",
         "Q17. Who is the Deputy Commissioner of East Garo Hills?",
         "Q18. Who is the Deputy Commissioner of South Garo Hills?",
         "Q19. Who is the Deputy Commissioner of South West Garo Hills?",
         "Q20. Who is the Chairman of Disaster Management?",
         "Q21. Who is the Chief Executive Officer of Disaster Management?",
         "Q22. Who is the District Disaster Management Officer?",
         "Q23. Who is the First man from meghalaya in Lok sabha?",
         "Q24. Who is the Minister of External Affairs of India?",
         "Q25. Who is the Minister of Home Affairs of India?",
         "Q26. Who is the Minister of Defence in India?",
         "Q27. Who is the Minister of Finance and Corporate Affairs?",
         "Q28. How many sub division in Garo hills?",
         "Q29. How many blocks in West Garo Hills?",
         "Q30. How many blocks in East Garo Hills?",
         "Q31. How many blocks in South West Garo Hills?",
         "Q32. How many Council of Ministers in Meghalaya?",
         "Q33. How many Districts in Meghalaya?",
         "Q34. How many Lok Sabha seats are there in Meghalaya?",
         "Q35. How many MLAs are there in Meghalaya?",
         "Q36. How many seats are there in Rajya Sabha?",
         "Q37. How many seats are there in Lok Sabha?",
         "Q38. How many MLAs are there in India?",
         "Q39. How many National Parks in Meghalaya?",
         "Q40. Who is the Power Minister of Meghalaya?",
         "Q41. Who is the Minister of Information Technology in Meghalaya?",
         "Q42. Who is the Education Minister of Meghalaya?",
         "Q43. Who is the Health Minister of Meghalaya?"]

result = 0

while Exception:
    try:
        name = input("\nPlease type your name...\n> ")
        if len(name) == 0:
            raise Exception
        print(f"Hello there {name}, Welcome to the game\n\t")

        q0 = input(f"{qstns[0]}\n\n> ")
        if q0.lower() == "ram nath kovind":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q1 = input(f"{qstns[1]}\n\n> ")
        if q1.lower() == "rajendra prasad":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q2 = input(f"{qstns[2]}\n\n> ")
        if q2.lower() == "narendra modi":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q3 = input(f"{qstns[3]}\n\n> ")
        if q3.lower() == "pandit jawaharlal nehru":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q4 = input(f"{qstns[4]}\n\n> ")
        if q4.lower() == "venkaiah naidu":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q5 = input(f"{qstns[5]}\n\n> ")
        if q5.lower() == "sarvepalli radahkrishnan":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q6 = input(f"{qstns[6]}\n\n> ")
        if q6.lower() == "shaktikanta das":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q7 = input(f"{qstns[7]}\n\n> ")
        if q7.lower() == "lord william bentinck":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q8 = input(f"{qstns[8]}\n\n> ")
        if q8.lower() == "satya pal malik":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q9 = input(f"{qstns[9]}\n\n> ")
        if q9.lower() == "braj kumar nehru":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q10 = input(f"{qstns[10]}\n\n> ")
        if q10.lower() == "sharad arvind bobde":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q11 = input(f"{qstns[11]}\n\n> ")
        if q11.lower() == "biswanath somadder":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q12 = input(f"{qstns[12]}\n\n> ")
        if q12.lower() == "conrad k sangma":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q13 = input(f"{qstns[13]}\n\n> ")
        if q13.lower() == "williamson a sangma":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q14 = input(f"{qstns[14]}\n\n> ")
        if q14.lower() == "ram singh":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q15 = input(f"{qstns[15]}\n\n> ")
        if q15.lower() == "r p marak":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q16 = input(f"{qstns[16]}\n\n> ")
        if q16.lower() == "swapnil tembe":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q17 = input(f"{qstns[17]}\n\n> ")
        if q17.lower() == "h b marak":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q18 = input(f"{qstns[18]}\n\n> ")
        if q18.lower() == "ramakrishna chitturi":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q19 = input(f"{qstns[19]}\n\n> ")
        if q19.lower() == "ram singh":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q20 = input(f"{qstns[20]}\n\n> ")
        if q20.lower() == "mary t sangma":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q21 = input(f"{qstns[21]}\n\n> ")
        if q21.lower() == "james d sangma":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q22 = input(f"{qstns[22]}\n\n> ")
        if q22.lower() == "purno a sangma":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q23 = input(f"{qstns[23]}\n\n> ")
        if q23.lower() == "subrahmanyam jaishankar":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q24 = input(f"{qstns[24]}\n\n> ")
        if q24.lower() == "g. kishan reddy":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q25 = input(f"{qstns[25]}\n\n> ")
        if q25.lower() == "rajnath singh":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q26 = input(f"{qstns[26]}\n\n> ")
        if q26.lower() == "nirmala sitharaman":
            print("\tCorrect Answer!\n")
            result += 1
        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q27 = input(f"{qstns[27]}\n\n> ")
        if q27 == "3":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q28 = input(f"{qstns[28]}\n\n> ")
        if q28 == "7":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q29 = input(f"{qstns[29]}\n\n> ")
        if q29 == "5":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q30 = input(f"{qstns[30]}\n\n> ")
        if q30 == "3":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q31 = input(f"{qstns[31]}\n\n> ")
        if q31 == "12":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q32 = input(f"{qstns[32]}\n\n> ")
        if q32 == "11":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q33 = input(f"{qstns[33]}\n\n> ")
        if q33 == "2":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q34 = input(f"{qstns[34]}\n\n> ")
        if q34 == "60":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q35 = input(f"{qstns[35]}\n\n> ")
        if q35 == "245":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q36 = input(f"{qstns[36]}\n\n> ")
        if q36 == "545":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q37 = input(f"{qstns[37]}\n\n> ")
        if q37 == "4120":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q38 = input(f"{qstns[38]}\n\n> ")
        if q38 == "2":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q39 = input(f"{qstns[39]}\n\n> ")
        if q39 == "james k sangma":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q40 = input(f"{qstns[40]}\n\n> ")
        if q40 == "hamletson dohling":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q41 = input(f"{qstns[41]}\n\n> ")
        if q41 == "lahkmen rymbui":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        q42 = input(f"{qstns[42]}\n\n> ")
        if q42 == "alexander laloo hek":
            print("\tCorrect Answer!\n")
            result += 1

        else:
            print(f"Hey  wrong answer\nAlso check your spellings!\n")

        print("Game is over\n")
        print("Collecting all your scores\nPlease Wait...\n")
        time.sleep(5)

        print(
            f"\t#####  {name} your total score is : {result} out of {len(qstns)}  #####\n\t")

        if result <= 10:
            print(f"\tYou need more hard work!!! You only got: {result}\n")
        if result >= 20:
            print(f"\tYou can do better than {result}\n")
        if result >= 30:
            print("\tGood job but aim for more marks\n")
        if result >= 40:
            print("\tWell done keep it up\n")

        print(f"\n\t***** {name} press ctrl+z to exit *****\n")

    except:
        pass

import random
from operator import itemgetter

class CovidGame:
    isOver = False
    round = 1
    increasedInfection = 0
    curedPatient = 0
    curedCountry = []

    def __init__(self, vac_list, cou_list):
        self.vac_list = vac_list[:]
        self.cou_list = cou_list[:]
    
    def roundStart(self, vac, cou):
            print("★", self.round , "번째 시도 ★\n")
            print("선택된 백신 :", self.vac_list[vac][0] + ",", "치료율 :", self.vac_list[vac][1] * 100, "%")
            print("선택된 나라 :", self.cou_list[cou][0]+ "," , "인구수 :", str(self.cou_list[cou][1])+ ",", "감염자수 :", self.cou_list[cou][2])
            self.curedPatient += int(self.cou_list[cou][2] * (1 - self.vac_list[vac][1]))
            self.cou_list[cou][2] = int(self.cou_list[cou][2] * (1 - self.vac_list[vac][1]))

            print("=================================================")
            if self.cou_list[cou][2] == 0:
                print("완치 된 국가:", self.cou_list[cou][0])
                self.curedCountry.append(self.cou_list.pop(cou))         


    def isGameOver(self):
        for i in range(len(self.cou_list)):
            if self.cou_list[i][2] >= self.cou_list[i][1]:
                self.isOver = True
        if self.round >= 6:
            self.isOver = True
    
    def roundEnd(self):
        for i in range(len(self.cou_list)):
            self.cou_list[i][2] += int(self.cou_list[i][1] * 0.15)
            self.increasedInfection += int(self.cou_list[i][1] * 0.15)
        if len(self.cou_list) == 0:
            print("모든 국가가 완치되었습니다 !!!")
        random.shuffle(self.vac_list)
        random.shuffle(self.cou_list)
        self.round += 1

    def printResult(self):
        print(str(self.round) + "차 백신 투여 후 감염된 나라에 대한 정보")
        print("=================================================")
        for country in self.cou_list:
            print("감염 국가 :", country[0])
            print("인구수 :", country[1])
            print("감염 인구수 :", country[2])
            print("")
    
    def GameOver(self):
        print("=================================================")
        print("                     최종결과                    ")
        print("=================================================")
        print("라운드마다 추가로 감염된 감염자 수:", str(self.increasedInfection)+"명")
        print("백신으로 치료된 감염자 수:", str(self.curedPatient)+"명")
        print("백신으로 완치된 국가:", end = " ")
        for cured in self.curedCountry:
            print(cured[0], end = " ")
        print("(", len(self.curedCountry), "개)")

        country = self.curedCountry[:] + self.cou_list[:]
        country = sorted(country , key = itemgetter(2))

        for i in range(5):
            print(str(i + 1) + "위")
            print("감염 국가 :", country[4 - i][0])
            print("인구수 :", country[4 - i][1])
            print("감염 인구수 :", country[4 - i][2])
            print("")
        print("게임 종료!")







termination = False

choose = 0

vac_list = [["백신1", 0.25], ["백신2", 0.5], ["백신3", 1]]
cou_list = [["한국", 1500, 300], ["중국", 3000, 800],["일본", 2000, 500], ["미국", 2500, 750],["독일", 2200, 1000]]



while not termination:
    print("--------------------------")
    print("     코로나 종식 게임     ")
    print("--------------------------")
    print("1. 백신 정보")
    print("2. 감염된 국가 정보")
    print("3. 게임 시작")
    print("4. 게임 종료")
    try:
        choose = int(input())
    except ValueError:
        print("오류가 발생했습니다. 숫자를 입력해주세요.")
        choose = 0

    if choose == 1:
        for vaccine in vac_list:
            print("백신 이름 : " + vaccine[0])
            print("백신 치료율 : "+ str(vaccine[1]*100) + "%")
            print("")

    elif choose == 2:
        for country in cou_list:
            print("감염 국가 :", country[0])
            print("인구수 :", country[1])
            print("감염 인구수 :", country[2])
            print("")

    elif choose == 3:
        game = CovidGame(vac_list, cou_list)
        print("사용할 백신(1~3)과 백신을 적용할 국가(1~5)의 번호를 차례대로 입력하세요")
        while True:
            try:
                vac, cou = input().split()
                vac = int(vac)
                cou = int(cou)
                break
            except ValueError:
                print("오류가 발생했습니다. 숫자를 입력해주세요.")

        while not game.isOver:
            if game.round == 1:
                game.roundStart(vac, cou)
            else :
                game.roundStart(random.randint(0,2), random.randint(0,len(game.cou_list) - 1))
            game.printResult()
            game.roundEnd()
            game.isGameOver()
       
        game.GameOver()

    elif choose == 4:
        termination = True
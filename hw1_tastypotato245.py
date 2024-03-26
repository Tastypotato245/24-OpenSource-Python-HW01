import random
import time

def NewNumberBaseball():
    isGoodDab = False

    while isGoodDab == False:
        isGoodDab = True
        dab_0 = random.randint(1, 9)
        dab_1 = random.randint(1, 9)
        dab_2 = random.randint(1, 9)
        if dab_0 == dab_1:
            isGoodDab = False
        if dab_0 == dab_2:
            isGoodDab = False
        if dab_1 == dab_2:
            isGoodDab = False
    life = 9

    isAlreadyWon = False

    def pitch(choice_0, choice_1, choice_2):
        nonlocal life
        nonlocal isAlreadyWon

        if isAlreadyWon:
            return True

        if choice_0 < 1:
            life = 0
        if choice_1 < 1:
            life = 0
        if choice_2 < 1:
            life = 0
        if choice_0 > 9:
            life = 0
        if choice_1 > 9:
            life = 0
        if choice_2 > 9:
            life = 0
        if choice_0 == choice_1:
            life = 0
        if choice_0 == choice_2:
            life = 0
        if choice_1 == choice_2:
            life = 0

        if life <= 0:
            return False

        life = life - 1

        strikes = 0

        if dab_0 == choice_0:
            strikes = strikes + 1
        if dab_1 == choice_1:
            strikes = strikes + 1
        if dab_2 == choice_2:
            strikes = strikes + 1

        if strikes == 3:
            isAlreadyWon = True
            return True

        balls = 0
        if dab_0 == choice_1:
            balls = balls + 1
        if dab_0 == choice_2:
            balls = balls + 1
        if dab_1 == choice_0:
            balls = balls + 1
        if dab_1 == choice_2:
            balls = balls + 1
        if dab_2 == choice_0:
            balls = balls + 1
        if dab_2 == choice_1:
            balls = balls + 1

        return strikes * 10 + balls

    # 세팅이 끝난 숫자 야구 게임용 함수를 return
    return pitch

# 새 보물 찾기 게임용 함수를 준비해 return하는 함수예요
def NewTreasureBox():
    # 보물 찾기 게임용 Data 준비

    # 답 좌표 고르기
    dab_x = random.uniform(0.0, 16.0) # [0.0, 16.0] 범위의 균등분포를 만족하는 임의의 float 값을 얻을 수 있어요
    dab_y = random.uniform(0.0, 16.0) # 이거 말고도 정규분포 등등 다른 버전도 많아요

    # 이번에 고른 좌표와 답 좌표 사이의 직선거리가 1.0 이하면 보물 찾기 성공
    dab_radius = 1.0

    # 기회는 열 번
    life = 10

    # 이미 이겼을 때만 True, 이미 졌거나 아직 게임이 끝나지 않은 경우 False
    isAlreadyWon = False

    # 보물 찾기 게임용 함수에 대한 함수 정의
    def pick(x, y):
        nonlocal life
        nonlocal isAlreadyWon

        if isAlreadyWon:
            return True        

        if life <= 0:
            return False

        life = life - 1

        # 직선거리 계산
        # Python에서는 ** 연산자를 써서 'a의 b제곱'을 a ** b와 같이 적을 수 있어요.
        distance = ( (dab_x - x) ** 2 + (dab_y - y) ** 2 ) ** 0.5

        # 직선거리가 미리 정한 값 이하인 경우 bool 형식 True를 return
        if distance <= dab_radius:
            return True

        # 아직도 return하지 않은 경우 계산해 둔 직선거리 값(아마도 float 형식)을 return
        return distance

    # 세팅이 끝난 보물 찾기 게임용 함수를 return
    return pick







# ---------------------------------------------------------------------
# 여기서부터 여러분이 코드 적을 만한 부분이 나와요




# 목표 2: (프로그래머가 아닌) 사용자가, 우리가 준비해 둔 prompt 등을 확인하면서 생각을 진행하여
# 게임 한 판을 키보드로 직접 플레이할 수 있도록,
# 함수 Game()에 대한 함수 정의 구성하기
def Game():
    # 아래에 있는 return문은 임시로 적어 두었어요. 코드 적기 시작할 때 지우면 돼요
    return








# ☆ 목표 3(안 해도 돼요): 스스로 계산을 진행하며 게임 한 판을 자동으로 플레이할 수 있도록 두 함수에 대한 함수 정의 구성하기

def ChooseTheGameToSolve():
    # 숫자 야구 게임을 자동으로 플레이하도록 만든다면 0을,
    # 보물 상자 게임을 자동으로 플레이하도록 만든다면 1을 return하도록 구성하면 돼요.
    #
    # 아래에 있는 return문에 적힌 수식을, 자신이 원하는 게임에 맞게 고쳐 적으면 끝나요
    return 1
    

def Solve(g):
    # 목표 1에서와 같이, 이름 g를 가지고 함수 호출식을 적어 둠으로써 게임을 진행시킬 수 있어요.
    # 열심히 게임 한 판을 진행한 다음, 게임용 함수가 True 또는 False를 return한다면 그대로 함수 내용물 실행을 끝내면 돼요.
    # - 아직 게임이 끝나지 않았는데도 Solve() 내용물 실행을 끝내버리면 패배로 간주해요
    ret = 0

    while type(ret) != bool:
        ret = g(0, 0)






# ---------------------------------------------------------------------

def Solve100000Pan():
    count_played = 0
    count_won = 0
    count_error = 0

    choice = ChooseTheGameToSolve()

    start_time = time.perf_counter_ns()
    
    if choice == 0:
        while count_played < 100000:
            g = NewNumberBaseball()
            Solve(g)

            if g(0, 0, 0):
                count_won = count_won + 1
                
            count_played = count_played + 1

    if choice == 1:
        while count_played < 100000:
            g = NewTreasureBox()
            Solve(g)

            if g(256, 256):
                count_won = count_won + 1
                
            count_played = count_played + 1

    end_time = time.perf_counter_ns()

    if count_played == 0:
        print('음? 함수 ChooseTheGameToSolve()에 대한 함수 정의 내용이 이상한 것 같아요. 다시 한 번 확인해 주세요.')
        return

    print('    Win rate: ' + str(count_won / count_played * 100) + '%')
    print('  Error rate: ' + str(count_error / count_played * 100) + '%')
    print('Elapsed time: ' + str(end_time - start_time) + ' ns')

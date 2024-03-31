# hw1_base_mk3.py
#
# 과제#1을 진행하기 위해 여러분이 직접 고쳐볼 파일이에요.
# 
# 과제를 수행할 때는 과제 설명서랑 수업 영상을 열어 두고 같이 보면서 진행해 주세요.


import random
import time


# ---------------------------------------------------------------------
# 강사가 미리 적어 둔 Code들이 있는 부분이에요.
# 이 부분 내용을 읽지 않아도, 목표 1을 해 두었다면 전혀 지장 없이 과제를 수행할 수 있어요.
#
# 주의: 여기 있는 글자들은 절대 고치면 안 돼요! 만약 본다면 눈으로만 예뻐해주세요
#
# 스크롤 주욱 내리면 여러분이 코드 적을 만한 부분이 있어요. 주석으로 표시해 둠


# 새 숫자 야구 게임용 함수를 준비해 return하는 함수예요
def NewNumberBaseball():
    # 숫자 야구 게임용 Data 준비

    # 답 고르기([1, 9] 범위 내의 겹치지 않는 숫자 세 개)
    isGoodDab = False

    while isGoodDab == False:
        # 여기서 '가정'을 하고...
        isGoodDab = True
        
        dab_0 = random.randint(1, 9)
        dab_1 = random.randint(1, 9)
        dab_2 = random.randint(1, 9)

        # 여기서 '검증'을 하고 있어요. 이 반복 실행 흐름을(특히 isGoodDab에 담겨 있을 값을 예상하면서) 슬쩍 확인해 봐요
        if dab_0 == dab_1:
            isGoodDab = False

        if dab_0 == dab_2:
            isGoodDab = False

        if dab_1 == dab_2:
            isGoodDab = False
        
    # 기회는 아홉 번
    life = 9

    # 이미 이겼을 때만 True, 이미 졌거나 아직 게임이 끝나지 않은 경우 False
    isAlreadyWon = False

    # 숫자 야구 게임용 함수에 대한 함수 정의
    def pitch(choice_0, choice_1, choice_2):
        # ☆ 'nonlocal문'은 지금은 몰라도 돼요
        #    일단 지금은 '이 위 할당문을 통해 도입해 둔 이름 life, isAlreadyWon을 그냥 쓰겠다'
        #    ...고 미리 적어두었다고 보면 적당해요.
        #
        #    당연히 되는걸 굳이 왜 이런걸 적냐 싶은 게 정상이긴 해요. 아무튼 지금은 몰라도 됨
        nonlocal life
        nonlocal isAlreadyWon

        # 이미 이겼다면 바로 bool 형식 True를 return
        if isAlreadyWon:
            return True

        # 고른 수가 적절한지 확인 --> 적절하지 않은 경우 life를 0으로 만듦(반칙패)
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

        # 이미 기회를 모두 소모한 경우 bool 형식 False를 return
        if life <= 0:
            return False


        # 기회 소모
        life = life - 1


        # Strike 수 계산
        strikes = 0

        if dab_0 == choice_0:
            strikes = strikes + 1

        if dab_1 == choice_1:
            strikes = strikes + 1

        if dab_2 == choice_2:
            strikes = strikes + 1

        # 3 strikes인 경우 이긴 것이므로 이를 기록해 둔 다음 bool 형식 True를 return
        if strikes == 3:
            isAlreadyWon = True
            return True


        # 아직도 return하지 않은 경우 ball 수도 계산
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
        

        # Strike 수와 ball 수를 조합하여 return
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
        # ☆ 'nonlocal문'은 지금은 몰라도 돼요
        #    일단 지금은 '이 위 할당문을 통해 도입해 둔 이름 life, isAlreadyWon을 그냥 쓰겠다'
        #    ...고 미리 적어두었다고 보면 적당해요.
        #
        #    당연히 되는걸 굳이 왜 이런걸 적냐 싶은 게 정상이긴 해요. 아무튼 지금은 몰라도 됨
        nonlocal life
        nonlocal isAlreadyWon

        # 이미 이겼다면 바로 bool 형식 True를 return
        if isAlreadyWon:
            return True        

        # 이미 기회를 모두 소모한 경우 bool 형식 False를 return
        if life <= 0:
            return False

        # 기회 소모
        life = life - 1

        # 직선거리 계산
        # Python에서는 ** 연산자를 써서 'a의 b제곱'을 a ** b와 같이 적을 수 있어요.
        distance = ( (dab_x - x) ** 2 + (dab_y - y) ** 2 ) ** 0.5

        # 직선거리가 미리 정한 값 이하인 경우 이를 기록해 둔 다음 bool 형식 True를 return
        if distance <= dab_radius:
            isAlreadyWon = True
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
    # 숫자 야구 게임을 자동으로 플레이하도록 만든다면 문장 return 0 엔터 를,
    # 보물 상자 게임을 자동으로 플레이하도록 만든다면 문장 return 1 엔터 를 적어 주세요.
    #
    # 우리가 수업시간에 적었던 return문과 달리 단어 return 뒤에 수식을 하나 적고 있는데,
    # 그 의미는 지금은 몰라도 괜찮아요.
    # -> 함수 정의 적는 여러분이 0을 골랐는지, 1을 골랐는지를 표시해 둔다고 생각해 주세요.
    #
    # 아무튼 아래에 있는 return문에 적힌 수식을, 자신이 원하는 게임에 맞게 고쳐 적으면
    # 이 함수에 대한 함수 정의 구성이 끝나요
    return 1
    

def Solve(g):
    # 목표 1에서와 같이, 이름 g를 가지고 함수 호출식을 적어 둠으로써 게임을 진행시킬 수 있어요.
    # 열심히 게임 한 판을 진행한 다음, 게임용 함수가 True 또는 False를 return한다면 그대로 함수 내용물 실행을 끝내면 돼요.
    # - 아직 게임이 끝나지 않았는데도 Solve() 내용물 실행을 끝내버리면 패배로 간주해요


    # 1. 첫 반복 준비
    #
    # 게임용 함수는 이름 g에 담겨 있어요.
    # 이 이름 자체는 이 함수 정의 첫 줄 괄호 안에 적어 둔 이름과 같아요.
    # (저렇게 함수 정의 첫 줄 괄호 안에다가, 이 함수의 '인수'가 뭐뭐 있는지를 정해 둘 수 있어요)
    # 잘은 모르겠지만 아무튼 그 g에 게임용 함수가 잘 담겨 있을 거예요
    # -> 여러분이 함수 ChooseTheGameToSolve()에 대한 함수 정의 적을 때 정한 그 게임에 대한 함수가 담겨 있음
    #
    # 따라서 여기서는 아무튼 첫 반복을 시작하기 위해,
    # 새 이름 ret에 적당히 bool 형식이 아닌 값을 담아 두도록 할당문을 적어 두었어요
    #
    # - 여러분의 Code를 반복 실행하는 도중에 필요한 Data가 있다면 여기서 미리 준비해 주세요
    ret = 0

    # 2. 언제 반복을 그만둘 것인지 지정
    # 게임용 함수가 bool 형식 값을 return할 때까지 계속 반복하고 있어요 
    while type(ret) != bool:
        # 3. (이번 반복 진행 +) 다음 반복 준비
        #
        # 이번 반복은, 일단 기본적으로는, 이름 g를 사용하여 함수 호출식을 적어 두면 돼요.
        # 물론, '이번에는 무슨무슨 숫자들을 사용해서 함수 내용물을 실행할 것인지'를 재기 위한,
        # 여러분만의 무언가 복잡한 코드들을 같이 적어 두어야 할 거예요.
        # - 아무튼 매 반복마다 게임용 함수에 대한 함수 호출식이 한 번씩 계산되도록 만들어 주세요
        #   (꼭 그럴 필요는 없긴 해요)
        #
        # - 현재 이 반복 흐름은 ret에 담겨 있는 값에 따라 언제까지 반복할 것인지 결정되므로,
        #   게임용 함수의 return값을 ret에 담아 둔 채로 이번 반복을 끝내도록 구성해 주세요

        # 예시용 코드는 항상 (0, 0)을 고르고 있기 때문에,
        # 이번 게임에서 보물이 그 주변에 묻혀 있었다면 반드시 성공, 그렇지 않다면 반드시 패배하고 있어요
        # 그렇다 보니 승률이 대충 0.3%에 머무르고 있어요(기하학적으로 봤을 때 이게 정상임)
        ret = g(0, 0)





# ---------------------------------------------------------------------
# 이 아래는 다시, 강사가 미리 적어 둔 Code들이 있는 부분이에요.
# 이 부분 내용을 읽지 않아도 전혀 지장 없이 목표 3에 도전할 수 있어요.
# (대신 과제 설명서 내용을 잘 읽어 주세요)
#
# 주의: 여기 있는 글자들은 절대 고치면 안 돼요! 눈으로만 예뻐해주세요

def Solve100000Pan():
    # 게임 100,000 판에 대한 통계를 내기 위한 Data를 준비하는 부분
    count_played = 0
    count_won = 0
    count_error = 0

    choice = ChooseTheGameToSolve()

    # ☆ 조금 더 정밀하게 현재시'각' 과 관련 있는 숫자를 얻고 싶을 때
    #    time.perf_counter() 또는 time.perf_counter_ns()를 사용할 수 있어요
    #    뭐 이건 몰라도 돼요
    start_time = time.perf_counter_ns()
    
    if choice == 0:
        while count_played < 100000:
            g = NewNumberBaseball()
            Solve(g)

            # 게임이 아직 안 끝났었다면 반칙패로 False를 return하게 됨. 게임이 이미 끝났다면 그 게임 결과를 return하게 됨
            if g(0, 0, 0):
                count_won = count_won + 1
                
            count_played = count_played + 1

    if choice == 1:
        while count_played < 100000:
            g = NewTreasureBox()
            Solve(g)

            # 게임이 아직 안 끝났었다면 반칙패로 False를 return하게 됨. 게임이 이미 끝났다면 그 게임 결과를 return하게 됨
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

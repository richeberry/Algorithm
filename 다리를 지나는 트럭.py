# Programmers LV.2 _ 다리를 지나는 트럭

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length # bridge_length 만큼 공간 할당

    while bridge: # bridge가 존재하는 동안
        time += 1 # 시간 +1
        bridge.pop(0) # truck_weights 들어가는 bridge 공간 삭제
        print(bridge)
        if truck_weights: # truck_weights가 남아있을 때까지
            if weight >= truck_weights[0] + sum(bridge): # 제일 앞의 트럭 무게와 bridge에 있는 무게 합이 최대 무게보다 작거나 같으면
                outtruck = truck_weights.pop(0) # truck_weights의 제일 앞의 트럭을 대기 트럭에서 
                print('outtruck',outtruck)
                bridge.append(outtruck) # 다리로 이동 
            else:
                bridge.append(0) # 최대 무게보다 크면 다시 bridge length 만큼 0 채움
    return time


print(solution(bridge_length, weight, truck_weights))

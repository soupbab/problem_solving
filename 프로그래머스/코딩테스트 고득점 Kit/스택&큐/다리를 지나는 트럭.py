def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = []
    onBridge = 0
    arrived = []
    
    while len(truck_weights) + len(queue) != 0:
        if len(queue) > 0:
            for truck in queue:
                truck[1] += 1
                
            if queue[0][1] > bridge_length:
                onBridge -= queue[0][0]
                arrived.append(queue.pop(0)[0])
        
        if len(truck_weights) > 0 and onBridge + truck_weights[0] <= weight:
            onBridge += truck_weights[0]
            queue.append([truck_weights.pop(0), 1])
            
        time += 1
        
    return time

def throttle_notifications(notifiy, K, W):
    result = []
    
    for i in range(len(notifiy)):
        user = notifiy[i]
        count = 0
        for j in range(max(0, len(result) - W), len(result)):
            if result[j] == user:
                count += 1

        if count < K:
            result.append(user)
    
    return result

notifiy = ["u1","u2","u1","u1","u2","u1"]
K = 2
W = 3

print(throttle_notifications(notifiy, K, W))
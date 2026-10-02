def detect_anomalies(arr, k):
    anomalies = []
    window_sum = sum(arr[:k])
    
    for i in range(k, len(arr)):
        moving_avg = window_sum / k
        if arr[i] > 2 * moving_avg:
            anomalies.append(i)
        
        # slide window
        window_sum += arr[i] - arr[i-k]
    
    return anomalies


# Dry Run
# arr=[10,12,15,50,18,20,100], k=3
# window_sum=37
# i=3 → avg=12.33, arr[3]=50 → anomaly
# i=4 → avg=25.67, arr[4]=18 → normal
# i=5 → avg=27.67, arr[5]=20 → normal
# i=6 → avg=29.33, arr[6]=100 → anomaly
# Output=[3,6]

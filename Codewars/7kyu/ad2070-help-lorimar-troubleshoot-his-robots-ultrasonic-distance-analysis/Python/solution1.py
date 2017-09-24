# Python - 3.4.3

def sensor_analysis(sensorData):
    # 取出距離的資料
    distanceData = [d[1] for d in sensorData]
    
    # 計算平均值
    mean = sum(distanceData) / len(distanceData)
    
    # 計算樣本標準差
    sd = (sum((d - mean) ** 2 for d in distanceData) / (len(distanceData) - 1)) ** 0.5
    
    # 結果四捨五入到小數第四位
    return (round(mean, 4), round(sd, 4))
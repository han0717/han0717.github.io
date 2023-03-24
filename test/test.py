#始化分鐘數
minutee_to_convert= 123
#算出整數的小時數
hour_decimal=minutee_to_convert/60
hours_part=int(hour_decimal)
#箅出整數的分鐘數
minutes_part=minutee_to_convert-hours_part*60
#輸出幾小時幾分鐘
print ("Hours")
print (hours_part)
print ("Minutes")
print (minutes_part)
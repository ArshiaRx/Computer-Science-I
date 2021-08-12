#9 - Taxi Zum Zum
def taxi_zum_zum(moves):
       
        xy_coordinate = [[0, 1], [1, 0], [0, -1] ,[-1, 0]]
        #^  xy_coordinate =[(x, y)]
        x, y, current_origin = 0, 0, 0
        
        for i in moves:
                if i =='R':
                        current_origin = (current_origin + 1) % 4
                elif i =='L':
                        current_origin = (current_origin - 1) % 4
                else:
                        x += xy_coordinate[current_origin][0]
                        y += xy_coordinate[current_origin][1]
#if none 'R' and 'L' add xy_coordinate position with origin to x and y 
            
        return (x, y)
    
#SUCCESSFUL 
# ====================================================================

print(taxi_zum_zum('RFRL'))
print(taxi_zum_zum('LFFLF'))
print(taxi_zum_zum('LLFLFLRLFR'))
print(taxi_zum_zum('FR' * 1000))
print(taxi_zum_zum('FFLLLFRLFLRFRLRRL'))

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Sort position and speed concatenately based on the position in reverse
        # After the sort, the car with a larger index cannot bypass the former one
        # The time to the target for each cars can be calculated by (target - position[i]) / speed[i] (= time[i])
        # With i < j, if time[i] < time[j]: these two are the fleet.
        # O(nlogn)

        position, speed = zip(*sorted(zip(position, speed), reverse=True))
        times = [(target - position[i]) / speed[i] for i in range(len(position))]
        print(position)
        print(speed)
        print(times)


        # fleet = 1
        # for i in range(1, len(position)):
        #     if times[i - 1] >= times[i]:
        #         # car[i - 1] and car[i] are at the same fleet, arriving with the time[i - 1]
        #         times[i] = times[i - 1]
        #     else:
        #         fleet += 1
        # return fleet
    
        stack = [] # store only the first car of each fleet
        for i in range(len(position)):
            if not stack or stack[-1] < times[i]:
                stack.append(times[i])
        return len(stack)
        
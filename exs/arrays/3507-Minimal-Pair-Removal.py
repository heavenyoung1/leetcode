from typing import  List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        print(f'ИСХОДНЫЙ МАССИВ {nums}')
        while self.decline(nums):
            count += 1
            self.sum_neighbor(nums)
        #print(f'COUNT {count}')
        print(f'КОНЕЧНЫЙ NUMS {nums}')
        return count

    # Проверка на убываемость
    def decline(self, nums: List[int]):
        flag = True
        for i in range(1, len(nums)):
            prev = nums[i - 1]
            act = nums[i]
            print(f'{prev} - {act}')
            if prev == act:
                print('РАВНО')
                continue
            elif prev < act:
                print('НЕУБЫВАЮЩИЙ')
                continue
                #return  False
            elif prev > act:
                print('УБЫВАЮЩИЙ')
                return True

        return False

    # Сложение соседей
    def sum_neighbor(self, nums: List[int]):
        general_min = 10000000
        pos_1 = None
        pos_2 = None
        for i in range(1, len(nums)):
            prev = nums[i - 1]
            act = nums[i]
            min_value = prev + act
            if min_value < general_min:
                general_min = min_value
                pos_1 = i - 1
                pos_2 = i

        #print(f'[sum_neighbor] POS1 {pos_1} POS2 {pos_2}')
        nums.pop(pos_2)
        nums[pos_1] = general_min
        #print(f'[sum_neighbor] Массив nums = {nums}')
        return nums




# print(not_decline([5,2,3,1]))
# print(not_decline([1,2,3,4,5]))
# print(sum_neighbor([5,2,3,1]))
# print(sum_neighbor([1,2,3,4,5]))


sol = Solution()
#print(sol.minimumPairRemoval([5,2,3,1]))
#(sol.minimumPairRemoval([2,2,1,1,1,0,-1]))
print(sol.minimumPairRemoval([-2,1,2,-1,-1,-2,-1,-1,1]))
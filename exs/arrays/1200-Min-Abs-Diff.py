from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sorted_arr = sorted(arr)
        out_arr = []
        global_min = 9999999
        for i in range(1, len(sorted_arr)):
            # ==========
            prev = i - 1
            act = i
            act_value = sorted_arr[act]
            prev_value = sorted_arr[prev]
            print(f'prev {prev}; act {act}')
            # ==========

            current_min = act_value - prev_value

            if current_min < global_min:
                print(f'CURRENT_MIN {current_min}')
                out_arr.clear()
                global_min = current_min

            if act_value - prev_value == global_min:
                local_arr = [sorted_arr[prev], sorted_arr[act]]
                out_arr.append(local_arr)

        # print(out_arr)
        return out_arr
"""
Time complexity: Beat 6.75%
Memory complexity: Beat 99%
2025/02/11
"""

def maxArea(height) -> int:
    # Dict的最大限制是没有order，index不能重复
    # 通过key查找很快，但是通过value查找很慢
    height_sort = height
    height_reverse = height[::-1]
    length = len(height)
    # height_sort.sort(reverse = True)
    max_square = 0
    index_left = 0
    index_right = 0
    # Special Case
    if len(height) == 1:
        return 0
    elif len(height) == 2:
        return min(height[0], height[1])*1
    
    s_hight = (min(height[index_left], height_reverse[index_right]))
    s_width = (length- index_right - 1) - index_left
    new_max_square = s_hight * s_width
    if max_square < new_max_square:
        max_square = new_max_square

    while index_left + index_right < length - 1:
        if height[index_left] <= height_reverse[index_right]:
            if height[index_left] > height[index_left + 1]:
                s_hight = (min(height[index_left], height_reverse[index_right]))
                s_width = (length- index_right - 1) - index_left
                new_max_square = s_hight * s_width
                if max_square < new_max_square:
                    max_square = new_max_square
                index_left += 1
                continue
            else:
                s_hight = (min(height[index_left], height_reverse[index_right]))
                s_width = (length- index_right - 1) - index_left
                new_max_square = s_hight * s_width
                if max_square < new_max_square:
                    max_square = new_max_square
                index_left += 1
        else:
            if height_reverse[index_right] > height_reverse[index_right + 1]:
                s_hight = (min(height[index_left], height_reverse[index_right]))
                s_width = (length- index_right - 1) - index_left
                new_max_square = s_hight * s_width
                if max_square < new_max_square:
                    max_square = new_max_square
                index_right += 1
                continue
            else:
                s_hight = (min(height[index_left], height_reverse[index_right]))
                s_width = (length- index_right - 1) - index_left
                new_max_square = s_hight * s_width
                if max_square < new_max_square:
                    max_square = new_max_square
                index_right += 1
    print(max_square)


maxArea([1,8,6,2,5,4,8,3,7])

# maxArea([1,2])

maxArea([1,2,4,3])
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Name        : Experiment_1.py
Author      : WiZ
Created     : 13th March 2019
Version     : 1.1
Modified    : 14th March 2019 - add comparision of sorting alogrithms：10000 integers， 100times
Description : Sorting algorithms

"""
import time
import random

# 1.Bubble Sort
def bubble_sort(list):
    length = len(list)
    for index in range(length):# 第一级遍历
        flag = True
        for j in range(1, length - index):# 第二级遍历
            if list[j - 1] > list[j]:# 前面的数大于后面的，交换（python特性可实现直接交换）
                list[j - 1], list[j] = list[j], list[j -1]
                flag = False
        if flag:
            return list# 如果没有发生交换，直接返回list
    return list

# 2.Selection Sort

def selection_sort(list):
    length = len(list)
    for i in range(0, length):
        min = i
        for j in range(i + 1, length):# 在未排序的元素中，寻找最小（大）的，放到起始位置
            if list[j] < list[min]:# 再从剩余元素中找最小的，放在排序队列的末尾
                # min = j
                list[min], list[j] = list[j], list[min]# 交换
    return list

# 3.Insertion Sort
def insertion_sort(list):
    length = len(list)
    for i in range(1, length):
        if list[i] < list[i - 1]:# 如果后面元素小于前面
            temp = list[i]# 取出
            index = i# 保存下标
            for j in range(i - 1, -1, -1):# 从后往前比较元素
                if list[j] > temp:# 如果有元素大于它
                    list[j + 1] = list[j]# 交换
                    index = j
                else:
                    break
            list[index] = temp# 交换完成
    return list

# 4.Shell Sort
def shell_sort(list):
    length = len(list)
    gap = length // 2# 向下取整
    while gap > 0:
        for i in range(gap, length):# 对每个步长的元素进行插入排序
            temp = list[i]
            j = i
            while j >= gap and list[j - gap] > temp:# 插入排序
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        gap = gap // 2# 缩小步长
    return list

# 5.Merge Sort
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(list):
    if len(list) <= 1:
        return list
    middle = int(len(list) / 2)
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    return merge(left, right)

# 6.Quick Sort

def quick_sort_1(L, left, right):
    if left <= right:
        key = L[left]
        i = left
        j = right
        while i < j:
            while i < j and key <= L[j]:
                j -= 1
            L[i] = L[j]
            while i < j and L[i] <= key:
                i += 1
            L[j] = L[i]
        L[i] = key
        quick_sort_1(L, left, i - 1)
        quick_sort_1(L, i + 1, right)
    return list

def quick_sort_11(list):
    less = []
    pivotList = []
    more = []
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        for i in list:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quick_sort_11(less)
        more = quick_sort_11(more)
    return less + pivotList + more
def quick_sort_2(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        return quick_sort_2([x for x in list[1 : ] if x < pivot] + [pivot] + quick_sort_2([x for x in list[1 : ] if x >= pivot]))
qs = lambda xs : ( (len(xs) <= 1 and [xs]) or [ qs( [x for x in xs[1:] if x < xs[0]] ) + [xs[0]] + qs( [x for x in xs[1:] if x >= xs[0]] ) ] )[0]

# 7.Heap Sort
def heap_sort(list):
    for start in range((len(list) - 2) // 2, -1, -1):
        sift_down(list, start, len(list) - 1)

    for end in range(len(list) - 1, 0, -1):
        list[0], list[end] = list[end], list[0]
        sift_down(list, 0, end - 1)
    return list
def sift_down(list, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and list[child] < list[child + 1]:
            child += 1
        if list[root] < list[child]:
            list[root], list[child] = list[child], list[root]
            root = child
        else:
            break

# 8.Count Sort
def count_sort(list):
    min = 10000000000
    max = -100
    for x in list:
        if x < min:
            min = x
        if x > max:
            max = x
    count = [0] * (max - min + 1)
    for index in list:
        count[index - min] += 1
    index = 0
    for a in range(max - min + 1):
        for c in range(count[a]):
            list[index] = a + min
            index += 1
    return list

# 9.Radix Sort
def radix_sort(nums):
    mod = 10
    div = 1
    mostBit = len(str(max(nums)))  # 最大数的位数决定了外循环多少次
    buckets = [[] for row in range(mod)] # 构造 mod 个空桶
    while mostBit:
        for num in nums:  # 将数据放入对应的桶中
            buckets[num // div % mod].append(num)
        i = 0  # nums 的索引
        for bucket in buckets:  # 将数据收集起来
            while bucket:
                nums[i] = bucket.pop(0) # 依次取出
                i += 1
        div *= 10
        mostBit -= 1
    return nums

# 10.Gnome Sort
def gnome_sort(l):
    i = 0
    while i < len(l):
        if i == 0 or l[i - 1] <= l[i]: #i=0或者正序不需交换，i+1
            i += 1
        else:  #否则，交换两数，i回退
            l[i - 1], l[i] = l[i], l[i - 1]
            i -= 1
        # print(l)
    return l

# 11.Cooktall Sort
def cooktall_sort(num_array):
    flag=True
    for i in range(len(num_array)//2):
        if flag:
            flag=False
            #将最大值排到队尾
            for j in range(i,len(num_array)-i-1):
                if num_array[j]>num_array[j+1]:
                    num_array[j],num_array[j+1]=num_array[j+1],num_array[j]
                    flag=True
            #将最小值排到队首
            for j in range(len(num_array)-1-i,i,-1):
                if num_array[j]<num_array[j-1]:
                    num_array[j],num_array[j-1]=num_array[j-1],num_array[j]
                    flag=True
        else:
            break
    return num_array
# 12.Monkey Sort
def monkey_sort(num_list):
# '''猴子排序，思想是：每次都随机打乱数组，直到有序为止'''
    result_list=sorted(num_list)
    if num_list==result_list:
        pass

    else:
        while num_list!=result_list:
            random.shuffle(num_list)
    return num_list

# 13.Bucket Sort
def bucket_sort(nums):
    # 选择一个最大的数
    max_num = max(nums)
    # 创建一个元素全是0的列表, 当做桶
    bucket = [0]*(max_num+1)
    # 把所有元素放入桶中, 即把对应元素个数加一
    for i in nums:
        bucket[i] += 1

    # 存储排序好的元素
    sort_nums = []
    # 取出桶中的元素
    for j in range(len(bucket)):
        if bucket[j] != 0:
            for y in range(bucket[j]):
                sort_nums.append(j)

    return sort_nums


def sort_compare():
    final_ranks = []
    for i in range(100):#running times
        print("执行第%d次..."%(i+1))

        List_sort = []
        Inter_num = 10000
        for i in range(Inter_num):
            List_sort.append(random.randint(1, 1000000))
            # if i == 10000:
            #     break

        orginal_sorts = []
        # print(List_sort)
        for i in range(50):
            orginal_sorts.append(list(List_sort))

        List_sort = orginal_sorts
        sorts_time = []
        # # 计算运行时间
        # print(List_sort[0])

        start = time.time();
        bubble_sort(List_sort[0]);
        end = time.time();  # print("Bubble    Sort:", end - start)
        sorts_time.append(['bubble', end - start])

        start = time.time();
        selection_sort(List_sort[1]);
        end = time.time();  # print("Selection Sort:", end - start)
        sorts_time.append(['selection', end - start])

        start = time.time();
        insertion_sort(List_sort[2]);
        end = time.time();  # print("Insertion Sort:", end - start)
        sorts_time.append(['insertion', end - start])

        start = time.time();
        shell_sort(List_sort[3]);
        end = time.time();  # print("Shell     Sort:", end - start)
        sorts_time.append(['shell', end - start])

        start = time.time();
        merge_sort(List_sort[4]);
        end = time.time();  # print("Merge     Sort:", end - start)
        sorts_time.append(['merge', end - start])

        start = time.time();
        quick_sort_1(List_sort[5], 0, len(List_sort[5]) - 1);
        end = time.time();  # print("Quick     Sort1:", end - start)
        start = time.time();
        quick_sort_11(List_sort[6]);
        end = time.time();  # print("Quick     Sort2:", end - start)
        sorts_time.append(['quick', end - start])

        start = time.time();
        heap_sort(List_sort[7]);
        end = time.time();  # print("Heap      Sort:", end - start)
        sorts_time.append(['heap', end - start])

        start = time.time();
        count_sort(List_sort[8]);
        end = time.time();  # print("Count     Sort:", end - start)
        sorts_time.append(['count', end - start])

        start = time.time();
        count_sort(List_sort[11]);
        end = time.time();  # print("Count     Sort:", end - start);
        sorts_time.append(['radix', end - start])

        start = time.time();
        gnome_sort(List_sort[12]);
        end = time.time();  # print("     Sort:", end - start)
        sorts_time.append(['gnome', end - start])

        start = time.time();
        cooktall_sort(List_sort[13]);
        end = time.time();  # print("     Sort:", end - start)
        sorts_time.append(['cooktall', end - start])

        # start = time.time();monkey_sort(List_sort[14]);end = time.time();  # print("     Sort:", end - start)
        # sorts_time.append(['monkey', end - start])

        start = time.time();
        bucket_sort(List_sort[30])
        end = time.time();  # print("     Sort:", end - start)
        sorts_time.append(['bucket', end - start])

        start = time.time();
        List_sort[9].sort();
        end = time.time();  # print("     Sort:", end - start)
        sorts_time.append(['sort', end - start])

        start = time.time();
        sorted(List_sort[15]);
        end = time.time();  # print("     Sort:", end - start)
        sorts_time.append(['sorted', end - start])

        sorts_time.sort(key=lambda x: x[1], reverse=False)
        j = 1
        final_rank = []
        for i in sorts_time:
            final_rank.append([i[0], j])
            j += 1
        temp_rank = []

        for i in final_rank:
            if i[0] == "sort":
                temp_rank.append(i[1])
        for i in final_rank:
            if i[0] == "sorted":
                temp_rank.append(i[1])
        for i in final_rank:
            if i[0] == "quick":
                temp_rank.append(i[1])
        for i in final_rank:
            if i[0] == "shell":
                temp_rank.append(i[1])
        for i in final_rank:
            if i[0] == "merge":
                temp_rank.append(i[1])
        for i in final_rank:
            if i[0] == "heap":
                temp_rank.append(i[1])
        for i in final_rank:
            if i[0] == "insertion":
                temp_rank.append(i[1])
        for i in final_rank:
            if i[0] == "cooktall":
                temp_rank.append(i[1])
        for i in final_rank:
            if i[0] == "selection":
                temp_rank.append(i[1])
        for i in final_rank:
            if i[0] == "bubble":
                temp_rank.append(i[1])
        for i in final_rank:
            if i[0] == "bucket":
                temp_rank.append(i[1])
        for i in final_rank:
            if i[0] == "gnome":
                temp_rank.append(i[1])
        for i in final_rank:
            if i[0] == "radix":
                temp_rank.append(i[1])
        for i in final_rank:
            if i[0] == "count":
                temp_rank.append(i[1])

        final_ranks.append(temp_rank)
        print(temp_rank)
    return(final_ranks)



if __name__ == "__main__":

    sort_compare()

# The following is a video link that explains the subset-sum problem clearly
# https://www.google.com/search?q=subset+sum+problem+bottom+up+&sca_esv=580877352&rlz=1C1JZAP_enCA969CA969&biw=2133&bih=1012&tbm=vid&sxsrf=AM9HkKkvkL_l7-jz3d7WrBiNCB2ip9pJLg%3A1699545723982&ei=ewJNZZ3QO7WrptQP79GAeA&ved=0ahUKEwjd-aCZpbeCAxW1lYkEHe8oAA8Q4dUDCA0&uact=5&oq=subset+sum+problem+bottom+up+&gs_lp=Eg1nd3Mtd2l6LXZpZGVvIh1zdWJzZXQgc3VtIHByb2JsZW0gYm90dG9tIHVwIDIFECEYoAEyBRAhGKABMgUQIRigATIFECEYoAEyBRAhGKABSPA3UIsMWKUncAB4AJABAJgBcqAB-AiqAQM3LjW4AQPIAQD4AQHCAgQQIxgnwgIHEAAYigUYQ8ICBRAAGIAEwgIKEAAYgAQYFBiHAsICBhAAGBYYHsICCBAAGBYYHhgPwgIIEAAYigUYhgPCAgcQIRigARgKwgIIECEYFhgeGB2IBgE&sclient=gws-wiz-video#fpstate=ive&vld=cid:5a583403,vid:s6FhG--P7z0,st:0

#************ Recursive Solution ************

def subset_sum_rec(numbers, target):
    if target == 0:
        return True
    if target < 0:
        return False
    if numbers == []:
        return False
    return subset_sum(numbers[:-1], target, d) or subset_sum(numbers[:-1], target - numbers[-1])


#************ Bottom Up Solution ************

def subset_sum_bottom_up(numbers, target):
    #initialize all elements of matrix sp to be False
    sp = [[False for j in range(target + 1)] for i in range(len(numbers) + 1)]
    # set first column of matrix to be True, because there will always be a subset that makes up 0
    for i in range(len(numbers) + 1):
        sp[i][0] = True
    for i in range(1, len(numbers) + 1):
        for j in range(1, target + 1):
            #copy the above row till i and j are equal
            if numbers[i - 1] > j:
                sp[i][j] = sp[i - 1][j]
            else:
                # if value directly above is True, then sp[i][j] is also True, otherwise go 1 row up and j columns back to copy the value (again, video above explains very well)
                sp[i][j] = sp[i - 1][j] or sp[i - 1][j - numbers[i - 1]]
    # returns bool values: if True, subset exists, if False, subset does not exist
    return sp[len(numbers)][target]


#************ Top Down Solution ************

def subset_sum_top_down(numbers, target):
    sp = {} # dictionary
    for i in range(len(numbers) + 1):
        sp[(i,0)] = True
    for i in range(target + 1):
        sp[(0,i)] = i == 0
    top_down_aux(numbers, len(numbers), target, sp)
    return sp[(len(numbers),target)]


def top_down_aux(numbers, i, j, sp):
    if numbers[i - 1] > j:
        if not (i - 1, j) in sp:
            top_down_aux(numbers, i - 1, j, sp)
        sp[(i, j)] = sp[(i - 1, j)]
    else:
        if not (i - 1, j) in sp:
            top_down_aux(numbers, i - 1, j, sp)
        if not (i - 1, j - numbers[i - 1]) in sp:
            top_down_aux(numbers, i - 1, j - numbers[i - 1], sp)
        sp[(i, j)] = sp[(i - 1, j)] or sp[(i - 1, j - numbers[i - 1])]
    
# def top_down_aux(items, i, j, td):
#     if i == 0 or j == 0:
#         td[(i, j)] = 0
#     else:
#         if items[i - 1][0] > j:
#             if not (i - 1, j) in td:
#                 td[(i, j)] = top_down_aux(items, i - 1, j, td)
#         else:
#             td[(i, j)] = max(top_down_aux(items, i - 1, j, td), top_down_aux(items, i - 1, j - items[i - 1][0], td) + items[i - 1][1])
#     return td[(i, j)]

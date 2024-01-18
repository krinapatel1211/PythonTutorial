
def findMinimumPlatformsRequired(n,arr,dep):
    platform = 1
    for i in range(n-1):
        if dep[i] >= arr[i+1]:
            platform += 1
            if dep[i+1] <= dep[i]:
                print(platform)
        return platform


n = 6
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
p = findMinimumPlatformsRequired(n, arr, dep)

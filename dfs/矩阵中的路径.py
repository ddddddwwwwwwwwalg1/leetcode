def func(nums,word):

    def dfs(i,j,k):

        if nums[i][j] != word[k] or (i,j) in visited:
            return False
        if k==len(word)-1:
            return True
        visited.add((i,j))
        return dfs(i+1,j,k+1) or dfs(i,j+1,k+1) or dfs(i-1,j,k+1) or dfs(i,j-1,k+1)

    for m in range(len(nums)):
        for n in range(len(nums[0])):
            visited = set()
            if dfs(m,n,0):
                return True

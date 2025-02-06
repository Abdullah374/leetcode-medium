class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()
       
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j,0))
                else:
                    mat[i][j] = -1

        while q:
            i, j, step = q.popleft()
            for sr, sc in directions:
                nr, nc = i+sr, j+sc
                if 0<=nr<m and 0<=nc<n and mat[nr][nc] == -1:
                    mat[nr][nc] = step+1
                    q.append((nr,nc,step+1))
                       
                    
        return mat
            

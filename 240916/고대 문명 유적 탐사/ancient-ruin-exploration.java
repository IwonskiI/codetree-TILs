import java.io.*;
import java.util.*;

public class Main {
    
    // CodeTree - 고대 문명 유적 탐사
    public static int K, M, max_score, fill_idx, stack_idx, wall_idx, rrr, ccc;
    public static int[] wall;
    public static int[][] board, d = new int[][] {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    public static int[][] fill, stack;
    
    // td : 0 - 90도 / 1 - 180도 / 2 - 270도
    public static int[][] turn(int r, int c, int td) {
        int[][] t_board = new int[3][3];
        t_board[0][0] = board[r-1][c-1];
    	t_board[0][1] = board[r-1][c];
    	t_board[0][2] = board[r-1][c+1];
    	t_board[1][0] = board[r][c-1];
    	t_board[1][1] = board[r][c];
    	t_board[1][2] = board[r][c+1];
    	t_board[2][0] = board[r+1][c-1];
    	t_board[2][1] = board[r+1][c];
    	t_board[2][2] = board[r+1][c+1];
        for(int tdd = 0; tdd <= td; tdd++) {
            int tmp = t_board[0][2];
            t_board[0][2] = t_board[0][0];
            t_board[0][0] = t_board[2][0];
            t_board[2][0] = t_board[2][2];
            t_board[2][2] = tmp;
            tmp = t_board[1][2];
            t_board[1][2] = t_board[0][1];
            t_board[0][1] = t_board[1][0];
            t_board[1][0] = t_board[2][1];
            t_board[2][1] = tmp;
        }
//        for(int rr = 0; rr < 3; rr++) {
//            for(int cc = 0; cc < 3; cc++) {
//                switch(td) {
//                case 0:
//                    t_board[rr][cc] = board[2-cc+(r-1)][rr+(c-1)];
//                    break;
//                case 1:
//                    t_board[rr][cc] = board[2-cc+(r-1)][2-rr+(c-1)];
//                    break;
//                case 2:
//                    t_board[rr][cc] = board[cc+(r-1)][2-rr+(c-1)];
//                    break;
//                }
//            }
//        }
        
        return t_board;
    }
    
    public static int calc() {
        int score = 0;
        stack_idx = 0;
        stack = new int[25][2];
        for(int i = 0; i < 25; i++) {
            stack[i][0] = -1;
            stack[i][1] = 26;
        }
        boolean[][] visited = new boolean[5][5];
        for(int sr = 0; sr < 5; sr++) {
            for(int sc = 0; sc < 5; sc++) {
                if(visited[sr][sc]) continue;
                visited[sr][sc] = true;
                int base = board[sr][sc];
                int c_score = 1;
                Deque<int[]> dq = new ArrayDeque<>();
                stack[stack_idx][0] = sr;
                stack[stack_idx][1] = sc;
                stack_idx++;
                dq.offer(new int[] {sr, sc});
                while(!dq.isEmpty()) {
                    int[] cur = dq.poll();
                    int cr = cur[0], cc = cur[1];
                    for(int dd = 0; dd < 4; dd++) {
                        int nr = cr + d[dd][0], nc = cc + d[dd][1];
                        boolean in_range = (0 <= nr && nr < 5) && (0 <= nc && nc < 5);
                        if(in_range && board[nr][nc] == base && !visited[nr][nc]) {
                            dq.offer(new int[] {nr, nc});
                            stack[stack_idx][0] = nr;
                            stack[stack_idx][1] = nc;
                            stack_idx++;
                            visited[nr][nc] = true;
                            c_score++;
                        }
                    }
                }
                if(c_score >= 3) score += c_score;
                else stack_idx -= c_score;
            }
        }
        return score;
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // 초기 입력
        K = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[5][5];
        wall = new int[M];
        wall_idx = 0;
        int[][] board_origin = new int[5][5];
        int[][] board_copy = new int[5][5];
        // 유적 판 입력
        for(int r = 0; r < 5; r++) {
            st = new StringTokenizer(br.readLine());
            for(int c = 0; c < 5; c++) {
                board[r][c] = Integer.parseInt(st.nextToken());
            }
        }
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < M; i++) {
            wall[i] = Integer.parseInt(st.nextToken());
        }
        
        for(int k = 0; k < K; k++) {
            max_score = 0;
            // 최대 가치 찾기
            fill = new int[25][2];
            for(int r = 0; r < 5; r++) {
                for(int c = 0; c < 5; c++) {
                    board_origin[r][c] = board[r][c];
                }
            }
            for(int td = 0; td < 3; td++) {
                for(int c = 1; c < 4; c++) {
                    for(int r = 1; r < 4; r++) {
                        int[][] t_board = turn(r, c, td);
                        for(int rr = 0; rr < 3; rr++) {
                            for(int cc = 0; cc < 3; cc++) {
                                board[rr+(r-1)][cc+(c-1)] = t_board[rr][cc];
                            }
                        }
                        int score = calc();
                        // 현재 가치가 더 높으면 최대값 갱신 및 현재 상태 저장
                        if(max_score < score) {
                            max_score = score;
                            fill = stack;
                            fill_idx = stack_idx;
                            rrr = r; ccc = c;
                            for(int sr = 0; sr < 5; sr++) {
                                for(int sc = 0; sc < 5; sc++) {
                                    board_copy[sr][sc] = board[sr][sc];
                                }
                            }
                        }
                        // 탐색 후 배열 초기화
                        for(int sr = r-1; sr <= r+1; sr++) {
                            for(int sc = c-1; sc <= c+1; sc++) {
                                board[sr][sc] = board_origin[sr][sc];
                            }
                        }
                    }
                }
            }
            
            if(max_score == 0) break;
            int[][] fill_fin = new int[fill_idx][2];
            for(int i = 0; i < fill_idx; i++) {
                fill_fin[i] = fill[i];
            }
            //유물 채워넣기
            Arrays.sort(fill_fin, (a, b) -> {
                if(a[1] == b[1]) return b[0] - a[0];
                return a[1] - b[1];
            });
            
            for(int sr = rrr-1; sr <= rrr+1; sr++) {
                for(int sc = ccc-1; sc <= ccc+1; sc++) {
                    board[sr][sc] = board_copy[sr][sc];
                }
            }
            
            while(fill_idx > 0) {
                for(int idx = 0; idx < fill_idx; idx++) {
                    int r = fill_fin[idx][0], c = fill_fin[idx][1];
                    board[r][c] = wall[wall_idx++];
                }
                
                int add_score = calc();
                if(add_score == 0) break;
                max_score += add_score;
                fill = stack;
                fill_idx = stack_idx;
                
                fill_fin = new int[fill_idx][2];
                for(int i = 0; i < fill_idx; i++) {
                    fill_fin[i] = fill[i];
                }
                
                Arrays.sort(fill_fin, (a, b) -> {
                    if(a[1] == b[1]) return b[0] - a[0];
                    return a[1] - b[1];
                });
            }
            
            sb.append(max_score).append(" ");
        }
        
        
        
        // 최종 결과 출력
        System.out.println(sb.toString());
    }

}
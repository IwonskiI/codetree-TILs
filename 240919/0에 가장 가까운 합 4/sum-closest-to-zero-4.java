import java.io.*;
import java.util.*;

public class Main {
    
	// CodeTree - 0에 가장 가까운 합 4
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        
        int N = Integer.parseInt(br.readLine()), min = Integer.MAX_VALUE;
        int[] lst = new int[N], ans = new int[3];
        st = new StringTokenizer(br.readLine());
        
        // 초기 입력
        for(int i = 0; i < N; i++) {
        	lst[i] = Integer.parseInt(st.nextToken());
        }
        // 오름차순 출력을 위한 정렬
        Arrays.sort(lst);
        
		// 0~N-2까지 각 숫자를 첫 숫자로 기준점을 잡고 최솟갑 계산
        for(int i = 0; i < N-2; i++) {
			// 시작점은 i+1, 끝점은 가장 끝(N-1)
        	int sp = i + 1, ep = N - 1;
			// 시작점이 끝점보다 작을때까지 반복
			// (시작점과 끝점이 교차하기 전까지)
            while(sp < ep) {
				// 현재 포인터의 세 정수 합과 절댓값 계산
            	int sum = lst[i] + lst[sp] + lst[ep];
				int abs = Math.abs(sum);
            	
				// 현재 합의 절댓값이 기존 최소 절댓갑보다 작다면
            	if(abs < min) {
					// 최솟값 갱신
            		min = abs;
					// 현재 자리에 저장된 수 저장
            		ans[0] = lst[i];
            		ans[1] = lst[sp];
            		ans[2] = lst[ep];
            	}
				
				// 합이 0보다 크다면 끝점을 앞으로 이동
            	if(sum > 0) ep--;
				// 합이 0보다 작다면 시작점을 뒤로 이동
            	else if(sum < 0) sp++;
				// 합이 0이라면
            	else {
					// 현재 위치에 저장된 숫자들을 출력후 종료
            		sb.append(lst[i]).append(" ").append(lst[sp]).append(" ").append(lst[ep]);
            		System.out.println(sb.toString());
            		return;
            	}
            }
        }
        
		// 탐색 종료 후 저장된 최소 합을 이루는 값 저장
		for(int i = 0; i < 3; i++){
			sb.append(ans[i]).append(" ");
		}

        // 최종 결과 출력
        System.out.println(sb.toString());

		return;
    }
}